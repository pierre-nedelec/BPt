"""
_Plotting.py
====================================
Main class extension file for the some plotting functionality.
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import math
import shap
import os
from IPython.display import display, HTML
from matplotlib.animation import FuncAnimation

from ..helpers.Data_Helpers import get_original_cat_names


def _plot(self, save_name, show=True):

    if show:
        if self.log_dr is not None:

            save_name = save_name.replace(' ', '_')
            save_name = save_name.replace('/', '')

            save_spot = os.path.join(self.exp_log_dr,
                                     save_name.replace(' ', '_') + '.png')
            plt.savefig(save_spot, dpi=100, bbox_inches='tight')

        if self.notebook:
            plt.show()


def _proc_subjects(self, data, subjects):

    if subjects == 'train':

        try:
            return data.loc[self.train_subjects]
        except KeyError:
            raise RuntimeError('No train subjects defined!')

    elif subjects == 'test':

        try:
            return data.loc[self.test_subjects]
        except KeyError:
            raise RuntimeError('No test subjects defined!')

    else:

        try:
            return data.loc[subjects]
        except KeyError:
            raise RuntimeError('Invalid subjects passed!')


def Show_Data_Dist(self, num_feats=20, frame_interval=500,
                   plot_type='bar', show_only_overlap=True,
                   subjects=None, save=True, save_name='data distribution'):

    '''This method displays some summary statistics about
    the loaded targets, as well as plots the distibution if possible.

    Parameters
    ----------
    num_feats: int, optional
        The number of random features's distributions in which to view.
        Note: If too many are selected it may take a long time to render
        and/or consume a lot of memory!

        (default = 20)

    frame_interval: int, optional
        The number of milliseconds between each frame.

        (default = 500)

    plot_type : {'bar', 'hist'}
        The type of base seaborn plot to generate for each datapoint.
        Either 'bar' for barplot, or 'hist' or seaborns dist plot.

        (default = 'bar')

    show_only_overlap : bool, optional
        If True, then displays only the distributions for valid overlapping
        subjects across data, covars, ect... otherwise, if False,
        shows the current loaded distribution as is.

        If subjects is set (anything but None), this param will be ignored.

        (default = True)

    subjects : None, 'train', 'test' or array-like, optional
        If not None, then plot only the subjects loaded as train_subjects,
        or as test subjects, of you can pass a custom list or array-like of
        subjects.

        (default = None)

    save : bool, optional
        If the animation should be saved as a gif, True or False.

        (default = True)

    save_name : str, optional
        The name in which the gif should be saved under.

        (default = 'data distribution')
    '''

    if subjects is None:
        data = self._set_overlap(self.data, show_only_overlap).copy()
    else:
        data = self._proc_subjects(self.data, subjects).copy()

    self._print('Loaded data top columns by skew:')
    self._print(self.data.skew().sort_values())

    fig, ax = plt.subplots()

    def update(i):
        fig.clear()

        col = data[list(data)[i]]
        non_nan_col = col[~pd.isnull(col)]

        if plot_type == 'hist':
            sns.distplot(non_nan_col)
        else:
            sns.boxplot(non_nan_col)

    np.random.seed(1)
    frames = np.random.randint(0, data.shape[1], size=num_feats)
    anim = FuncAnimation(fig, update, frames=frames, interval=500)
    html = HTML(anim.to_html5_video())

    if self.log_dr is not None:

        save_name = os.path.join(self.exp_log_dr,
                                 save_name.replace(' ', '_') + '.gif')
        anim.save(save_name, dpi=80, writer='imagemagick')
        plt.close()

    if self.notebook:
        return html

    return None


def Show_Targets_Dist(self, targets='SHOW_ALL', cat_show_original_name=True,
                      show_only_overlap=True, subjects=None, show=True):
    '''This method displays some summary statistics about
    the loaded targets, as well as plots the distibution if possible.

    Parameters
    ----------
    targets : str, int or list, optional
        The single (str) or multiple targets (list),
        in which to display the distributions of. The str input
        'SHOW_ALL' is reserved, and set to default, for showing
        the distributions of loaded targets.

        You can also pass the int index of the loaded target to show!

        (default = 'SHOW_ALL')

    cat_show_original_name : bool, optional
        If True, then when showing a categorical distribution (or binary)
        make the distr plot using the original names. Otherwise,
        use the internally used names.

        (default = True)

    show_only_overlap : bool, optional
        If True, then displays only the distributions for valid overlapping
        subjects across data, covars, ect... otherwise, if False,
        shows the current loaded distribution as is.

        (default = True)

    subjects : None, 'train', 'test' or array-like, optional
        If not None, then plot only the subjects loaded as train_subjects,
        or as test subjects, of you can pass a custom list or array-like of
        subjects.

        (default = None)

    show : bool, optional
        If True, then plt.show(), the matplotlib command will be called,
        and the figure displayed. On the other hand, if set to False,
        then the user can customize the plot as they desire.
        You can think of plt.show() as clearing all of the loaded settings,
        so in order to make changes, you can't call this until you are done.

        (default = True)
    '''

    if subjects is None:
        targets_df = self._set_overlap(self.targets, show_only_overlap).copy()
    else:
        targets_df = self._proc_subjects(self.targets, subjects).copy()

    if targets == 'SHOW_ALL':
        targets = self._get_base_targets_names()

    if not isinstance(targets, list):
        targets = [targets]

    for target in targets:

        target = self._get_targets_key(target)
        self._show_single_dist(target, targets_df, self.targets_encoders,
                               cat_show_original_name, show)
        self._print()


def Show_Covars_Dist(self, covars='SHOW_ALL', cat_show_original_name=True,
                     show_only_overlap=True, subjects=None, show=True):
    '''Plot a single or multiple covar distributions, along with
    outputting useful summary statistics.

    Parameters
    ----------
    covars : str or list, optional
        The single covar (str) or multiple covars (list),
        in which to display the distributions of. The str input
        'SHOW_ALL' is reserved, and set to default, for showing
        the distributions of all loaded covars.

        (default = 'SHOW_ALL')

    cat_show_original_name : bool, optional
        If True, then when showing a categorical distribution (or binary)
        make the distr plot using the original names. Otherwise,
        use the internally used names.

        (default = True)

    show_only_overlap : bool, optional
        If True, then displays only the distributions for valid overlapping
        subjects across data, covars, ect... otherwise, shows the current
        loaded distribution as is.

        (default = True)

    subjects : None, 'train', 'test' or array-like, optional
        If not None, then plot only the subjects loaded as train_subjects,
        or as test subjects, of you can pass a custom list or array-like of
        subjects.

        (default = None)

    show : bool, optional
        If True, then plt.show(), the matplotlib command will be called,
        and the figure displayed. On the other hand, if set to False,
        then the user can customize the plot as they desire.
        You can think of plt.show() as clearing all of the loaded settings,
        so in order to make changes, you can't call this until you are done.

        (default = True)
    '''

    if subjects is None:
        covars_df = self._set_overlap(self.covars, show_only_overlap).copy()
    else:
        covars_df = self._proc_subjects(self.covars, subjects).copy()

    if covars == 'SHOW_ALL':
        covars = list(self.covars_encoders)

    if not isinstance(covars, list):
        covars = [covars]

    for covar in covars:
        self._show_single_dist(covar, covars_df, self.covars_encoders,
                               cat_show_original_name, show)
        self._print()


def Show_Strat_Dist(self, strat='SHOW_ALL', cat_show_original_name=True,
                    show_only_overlap=True, subjects=None, show=True):
    '''Plot a single or multiple strat distributions, along with
    outputting useful summary statistics.

    Parameters
    ----------
    strat : str or list, optional
        The single strat (str) or multiple strats (list),
        in which to display the distributions of. The str input
        'SHOW_ALL' is reserved, and set to default, for showing
        the distributions of all loaded strat cols.

        (default = 'SHOW_ALL')

    cat_show_original_name : bool, optional
        If True, then make the distr. plot using the original names.
        Otherwise, use the internally used names.

        (default = True)

    show_only_overlap : bool, optional
        If True, then displays only the distributions for valid overlapping
        subjects across data, covars, ect... otherwise, shows the current
        loaded distribution as is.

        (default = True)

    subjects : None, 'train', 'test' or array-like, optional
        If not None, then plot only the subjects loaded as train_subjects,
        or as test subjects, of you can pass a custom list or array-like of
        subjects.

        (default = None)

    show : bool, optional
        If True, then plt.show(), the matplotlib command will be called,
        and the figure displayed. On the other hand, if set to False,
        then the user can customize the plot as they desire.
        You can think of plt.show() as clearing all of the loaded settings,
        so in order to make changes, you can't call this until you are done.

        (default = True)
    '''

    if subjects is None:
        strat_df = self._set_overlap(self.strat, show_only_overlap).copy()
    else:
        strat_df = self._proc_subjects(self.strat, subjects).copy()

    if strat == 'SHOW_ALL':
        strat = list(self.strat_encoders)

    if not isinstance(strat, list):
        strat = [strat]

    for s in strat:
        self._show_single_dist(s, strat_df, self.strat_encoders,
                               cat_show_original_name, show)
        self._print()


def _show_single_dist(self, name, df, all_encoders, cat_show_original_name,
                      show=True):

    try:
        encoder = all_encoders[name]
    except KeyError:
        raise KeyError('No col named', name, 'found!')

    # list = multilabel
    # 3-tuple = one-hot or dummy
    # OrdinalEncoder = ordinal categorical
    # None = regression
    # dict = Binary conv'ed from regression

    # Regression
    if encoder is None:

        single_df = df[[name]].copy()
        self._show_dist(single_df, plot_key=name,
                        cat_show_original_name=cat_show_original_name,
                        encoder=encoder, original_key=name, show=show)

    # Multilabel
    elif isinstance(encoder, list):
        single_df = df[encoder].copy()
        self._show_dist(single_df, plot_key=name,
                        cat_show_original_name=cat_show_original_name,
                        encoder=encoder, original_key=name, show=show)

    # Binary/ordinal or one-hot/dummy
    else:

        dropped_name = None

        # One-hot / dummy
        if isinstance(encoder, tuple):
            categories = encoder[1].categories_[0]
            categories = sorted(categories)

            df_names = [name + '_' + str(cat) for cat in categories]
            valid_df_names = [name for name in df_names if name in df]

            single_df = df[valid_df_names].copy()

            # Recover dropped column if dummy coded
            dropped_name = set(df_names).difference(set(valid_df_names))

            if len(dropped_name) > 0:
                dropped_name = list(dropped_name)[0]

                nans = single_df[single_df.isna().any(axis=1)].index

                single_df[dropped_name] =\
                    np.where(single_df.sum(axis=1) == 1, 0, 1)

                single_df.loc[nans] = np.nan

                single_df[dropped_name] =\
                    single_df[dropped_name].astype('category')

            # Back into order
            single_df = single_df[df_names]

        # Binary / ordinal
        else:
            single_df = df[[name]].copy()

        self._show_dist(single_df, name, cat_show_original_name,
                        encoder=encoder, original_key=name,
                        dropped_name=dropped_name, show=show)


def _show_dist(
 self, data, plot_key, cat_show_original_name, encoder=None, original_key=None,
 dropped_name=None, show=True):

    # Ensure works with NaN data loaded
    no_nan_subjects = data[~data.isna().any(axis=1)].index
    nan_subjects = data[data.isna().any(axis=1)].index
    no_nan_data = data.loc[no_nan_subjects]

    self._print('--', plot_key, '--')

    # Regression
    if encoder is None:

        summary = no_nan_data.describe()

        self._display_df(summary)

        vals = no_nan_data[original_key]
        self._print('Num. of unique vals:', len(np.unique(vals)))
        self._print()

        sns.distplot(no_nan_data)

    # Binary/ordinal or one-hot
    else:

        # One-hot
        if isinstance(encoder, tuple):
            encoder = encoder[0]
            sums = no_nan_data.sum()

        # Multilabel
        elif isinstance(encoder, list):
            cat_show_original_name = False
            sums = no_nan_data.sum()

        # Binary/ordinal
        else:
            unique, counts = np.unique(no_nan_data, return_counts=True)
            sums = pd.Series(counts, unique)

        display_df = pd.DataFrame(sums, columns=['Counts'])
        display_df.index.name = 'Internal Name'
        display_df['Frequency'] = sums / len(no_nan_data)

        if cat_show_original_name:

            original_names = get_original_cat_names(sums.index,
                                                    encoder,
                                                    original_key)

            display_df['Original Name'] = original_names
            display_df = display_df[['Original Name', 'Counts', 'Frequency']]

        else:
            display_df = display_df[['Counts', 'Frequency']]

        self._display_df(display_df)

        if dropped_name is not None:
            if len(dropped_name) > 0:
                self._print('Note:', dropped_name, 'was dropped due to dummy',
                            'coding but is still shown.')

        display_names = sums.index
        if cat_show_original_name:
            display_names = pd.Index(original_names)
            display_names.name = 'Original Name'

        sns.barplot(x=sums.values, y=display_names, orient='h')
        plt.xlabel('Counts')

    # If any NaN
    if len(nan_subjects) > 0:
        self._print('Note:', len(nan_subjects), 'subject(s) with NaN',
                    'not included/shown!')

    title = plot_key + ' distributions'
    plt.title(title)
    self._plot(title, show)


def _display_df(self, display_df):

    if self.notebook:
        display(display_df)

    self._print(display_df, dont_print=self.notebook)
    self._print(dont_print=self.notebook)


def _get_top_global(self, df, top_n, get_abs):

    if get_abs:
        imps = np.mean(np.abs(df))
    else:
        imps = np.mean(df)

    imps.sort_values(ascending=False, inplace=True)

    to_get = list(range(top_n))
    if not get_abs:
        to_get += [-i for i in range(top_n)]

    top = imps[to_get]
    feats = imps[to_get].index

    top_df = df[feats]

    if get_abs:
        top_df = top_df.abs()

    wide = top_df.melt()
    wide['mean'] = wide['variable'].copy()
    wide['mean'] = wide['mean'].replace(top.to_dict())

    return wide


def Plot_Global_Feat_Importances(
 self, feat_importances='most recent', top_n=10, show_abs=False,
 multiclass=False, ci=95, palette='default', figsize=(10, 10),
 title='default', titles='default', xlabel='default', n_cols=1, ax=None,
 show=True):
    '''Plots any global feature importance, e.g. base or shap, values per
    feature not per prediction.

    Parameters
    ----------
    feat_importances : 'most recent' or Feat_Importances object
        Input should be either a Feat_Importances object as output from a
        call to Evaluate, or Test, or if left as default 'most recent',
        the passed params will be used to plot any valid calculated feature
        importances from the last call to Evaluate or Test.

        Note, if there exist multiple valid feature importances in the
        last call, passing custom ax will most likely break things.

        (default = 'most recent')

    top_n : int, optional
        The number of top features to display. In the case where
        show_abs is set to True, or the feature importance being plotted
        is only positive, then top_n features will be shown. On the other
        hand, when show_abs is set to False and the feature importances being
        plotted contain negative numbers, then the top_n highest and top_n
        lowest features will be shown.

        (default = 10)

    show_abs : bool, optional
        In the case where the underlying feature importances contain
        negative numbers, you can either plot the top_n by absolute value,
        with show_abs set to True, or plot the top_n highest and lowest
        with show_abs set to False.

        (default = False)

    multiclass : bool, optional
        If multiclass is set to True, and the underlying feature importances
        were derived from a categorical or multilabel problem type, then
        a seperate feature importance plot will be made for each class.
        Alternatively, if multiclass is set to False, then feature importances
        will be averaged over all classes.

        (default = False)

    ci : float, 'sd' or None, optional
        Size of confidence intervals to draw around estimated values.
        If 'sd', skip bootstrapping and draw the standard deviation
        of the feat importances. If None, no bootstrapping will be performed,
        and error bars will not be drawn.

        (default = 95)

    palette : Seaborn palette name, optional
        Color scheme to use. Search seaborn palettes for more information.
        Default for absolute is 'Reds', and default for both pos
        and neg is 'coolwarm'.

        (default = 'default')

    title : str, optional
        The title used during plotting, and also used
        to save a version of the figure
        (with spaces in title replaced by _, and as a png).

        When multiclass is True, this is the full figure title.

        (default = 'default')

    titles: list, optional
        This parameter is only used when multiclass is True.
        titles should be a list with the name for each classes plot.
        If left as default, it will just be named the original loaded name
        for that class.

        (default = 'default')

    xlabel : str, optional
        The xlabel, descriping the measure of feature importance.
        If left as 'default' it will change depend on what feature importance
        is being plotted.

        (default = 'default')

    n_cols: int, optional
        If multiclass, then the number of class plots to
        plot on each row.

        (default = 1)

    ax: matplotlib axis, or axes, optional
        A custom ax to plot to for an individual plot, or if using
        multiclass, then a list of axes can be passed here.

        (default = None)

    show : bool, optional
        If True, then plt.show(), the matplotlib command will be called,
        and the figure displayed. On the other hand, if set to False,
        then the user can customize the plot as they desire.
        You can think of plt.show() as clearing all of the loaded settings,
        so in order to make changes, you can't call this until you are done.

        (default = True)
    '''

    if feat_importances == 'most recent':
        for fis in self.Model_Pipeline:
            if 'global' in fis.scope:
                self.Plot_Global_Feat_Importances(
                 fis, top_n, show_abs, multiclass, ci, palette, figsize, title,
                 titles, xlabel, n_cols, ax, show)

        return

    # Initial check to make sure valid feat importances passed
    if feat_importances.global_df is None:
        raise AttributeError('You must pass a feature importances object with',
                             'global_df, try plot local feat importance.')
        return

    # If multiclass
    if isinstance(feat_importances.global_df, list):
        if multiclass:

            dfs = feat_importances.global_df

            return self._plot_multiclass_global_feat_importances(
                        dfs, feat_importances, top_n=top_n, show_abs=show_abs,
                        ci=ci, palette=palette, figsize=figsize, title=title,
                        titles=titles, xlabel=xlabel, n_cols=n_cols, ax=ax,
                        show=show)

        else:
            df = pd.concat(feat_importances.global_df)
    else:
        df = feat_importances.global_df

    # Non-multi-class case
    ax = self._plot_global_feat_importances(df, feat_importances,
                                            top_n=top_n, show_abs=show_abs,
                                            ci=ci, palette=palette,
                                            title=title, xlabel=xlabel,
                                            ax=ax, show=show)
    return ax


def _plot_multiclass_global_feat_importances(self, dfs, feat_importances,
                                             top_n=10, show_abs=False,
                                             ci=95, palette='default',
                                             figsize=(10, 10), title='default',
                                             titles='default',
                                             xlabel='default', n_cols=2,
                                             ax=None, show=True):

    # Grab the right classes
    target = feat_importances.target
    target_key = self._get_targets_key(target)
    classes = self.targets_encoders[target_key].classes_

    # Set default titles
    if titles == 'default':
        titles = classes

    if title == 'default':
        name = feat_importances.get_name()
        title = name + ' Top Features by Class'

    # If an ax is passed, then use that instead of making subplots
    n_rows = math.ceil(len(classes) / n_cols)
    if ax is not None:
        axes = ax
    else:
        fig, axes = plt.subplots(n_rows, n_cols, figsize=figsize)

    # In the case where only 1 row or 1 col.
    single = False
    if n_rows == 1 or n_cols == 1:
        single = True

    for i in range(len(dfs)):

        row = i // n_cols
        col = i % n_cols
        rc = (row, col)

        if single:
            rc = i

        # Create the subplot
        axes[rc] = self._plot_global_feat_importances(
            dfs[i], feat_importances, top_n=top_n,
            show_abs=show_abs, ci=ci, palette=palette,
            title=titles[i], xlabel='default', ax=axes[rc])

    # Set any remaining subplots to nothing
    for i in range(len(dfs), n_rows * n_cols):

        row = i // n_cols
        col = i % n_cols
        rc = (row, col)

        if single:
            rc = i

        axes[rc].set_axis_off()

    # Set the title and layout if no custom ax passed
    if ax is None:
        fig.tight_layout()
        fig.subplots_adjust(top=.9, hspace=.25)
        fig.suptitle(title, fontsize="x-large")
        self._plot(title, show)

    else:
        return axes


def _plot_global_feat_importances(self, df, feat_importances, top_n=10,
                                  show_abs=False, ci=95,
                                  palette='default', title='default',
                                  xlabel='default', ax=None, show=True):

    # Distinguish between feat importances that have been set to abs
    min_val = np.min(np.min(df))
    add_abs_sign = True

    if min_val >= 0:
        show_abs = True
    else:
        add_abs_sign = False

    # Get df, with only top_n, in wide form for plotting
    top_df = self._get_top_global(df, top_n, show_abs)

    # Abs / all pos values
    if show_abs:
        if palette == 'default':
            palette = 'Reds'

        if title == 'default':
            name = feat_importances.get_name()
            title = name + ' Top ' + str(top_n) + ' Features'

        if xlabel == 'default':
            xlabel = feat_importances.get_global_label()

        sns.barplot(x='value', y='variable', hue='mean',
                    data=top_df, orient='h', ci=ci,
                    palette=palette, errwidth=2, ax=ax, dodge=False)

    # Pos + neg values
    else:
        if palette == 'default':
            palette = 'coolwarm'

        if title == 'default':
            name = feat_importances.get_name()
            title = name + ' Top ' + str(top_n) + ' +/- Features'

        if xlabel == 'default':
            xlabel = feat_importances.get_global_label()

            if add_abs_sign:
                xlabel = '|' + xlabel + '|'

        sns.barplot(x='value', y='variable', hue='mean',
                    data=top_df, orient='h', ci=ci,
                    palette=palette, errwidth=2, ax=ax,
                    dodge=False)

        # Add an extra line down the center
        if ax is None:
            current_ax = plt.gca()
            current_ax.axvline(0, color='k', lw=.2)
            sns.despine(ax=current_ax, top=True, left=True, bottom=True,
                        right=True)
        else:
            ax.axvline(0, color='k', lw=.2)
            sns.despine(ax=ax, top=True, left=True, bottom=True, right=True)

    # Process rest fo params based on if for axis or global
    if ax is None:
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel('')
        plt.legend().remove()
        self._plot(title, show)

    else:
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel('')
        ax.get_legend().remove()
        return ax


def Plot_Local_Feat_Importances(self, feat_importances='most recent', top_n=10,
                                title='default', titles='default',
                                xlabel='default', one_class=None, show=True):
    '''Plots any local feature importance, e.g. shap, values per
    per prediction.

    Parameters
    ----------
    feat_importances : 'most recent' or Feat_Importances object
        Input should be either a Feat_Importances object as output from a
        call to Evaluate, or Test, or if left as default 'most recent',
        the passed params will be used to plot any valid calculated feature
        importances from the last call to Evaluate or Test.

        (default = 'most recent')

    top_n : int, optional
        The number of top features to display. In the case where
        show_abs is set to True, or the feature importance being plotted
        is only positive, then top_n features will be shown. On the other
        hand, when show_abs is set to False and the feature importances being
        plotted contain negative numbers, then the top_n highest and top_n
        lowest features will be shown.

        (default = 10)

    title : str, optional
        The title used during plotting, and also used
        to save a version of the figure
        (with spaces in title replaced by _, and as a png).

        With a multiclass / categorical problem type, this
        is only used if one_class is set. Otherwise, titles are used.

        (default = 'default')

    titles: list, optional
        This parameter is only used with a multiclass problem type.
        titles should be a list with the name for each class to plot.
        If left as default, it will use originally loaded class names.
        for that class.

        (default = 'default')

    xlabel : str, optional
        The xlabel, descriping the measure of feature importance.
        If left as 'default' it will change depend on what feature importance
        is being plotted.

        (default = 'default')

    one_class : int or None, optional
        If an underlying multiclass or categorical type, optionally
        provide an int here, corresponding to the single class to
        plot. If left as None, with make plots for all classes.

        (default = None)

    show : bool, optional
        If True, then plt.show(), the matplotlib command will be called,
        and the figure displayed. On the other hand, if set to False,
        then the user can customize the plot as they desire.
        You can think of plt.show() as clearing all of the loaded settings,
        so in order to make changes, you can't call this until you are done.

        (default = True)
    '''

    if feat_importances == 'most recent':
        for fis in self.Model_Pipeline:
            if 'local' in fis.scope:
                self.Plot_Local_Feat_Importances(
                 fis, top_n, title, titles, xlabel, one_class, show)

        return

    if feat_importances.local_df is None:
        raise AttributeError('You must pass a feature importances object with',
                             'local_df, try plot global feat importance.')
        return

    df = feat_importances.local_df

    # If multiclass
    if isinstance(df, list):

        target_key = self._get_targets_key(feat_importances.target)
        classes = self.targets_encoders[target_key].classes_

        if titles == 'default':
            base = ' Shap ' + str(top_n) + ' Features'
            titles = [cl + base for cl in classes]

        if one_class is None:

            for i in range(len(df)):
                self._plot_shap_summary(df[i], top_n, titles[i], xlabel, show)

            return

        # If just one class passed, treat as just one class
        else:
            df = df[one_class]

            if title == 'default':
                title = titles[one_class]

    self._plot_shap_summary(df, top_n, title, xlabel, show)


def _plot_shap_summary(self, shap_df, top_n, title, xlabel, show):

    shap_cols, shap_inds = list(shap_df), shap_df.index
    data = self.all_data.loc[shap_inds][shap_cols]

    shap.summary_plot(np.array(shap_df), data, max_display=top_n, show=False)

    if title == 'default':
        title = 'Shap Summary Top ' + str(top_n) + ' Features'

    plt.title(title)

    if xlabel != 'default':
        plt.xlabel(xlabel)

    self._plot(title, show)