from ABCD_ML.helpers.ML_Helpers import get_objects_by_type, get_objects
from ABCD_ML.pipeline.Metrics import get_metrics_by_type

from ABCD_ML.pipeline.Models import AVALIABLE as AVALIABLE_MODELS
from ABCD_ML.pipeline.Models import MODELS

from ABCD_ML.pipeline.Loaders import LOADERS
from ABCD_ML.pipeline.Transformers import TRANSFORMERS
from ABCD_ML.pipeline.Scalers import SCALERS
from ABCD_ML.pipeline.Imputers import IMPUTERS
from ABCD_ML.pipeline.Samplers import SAMPLERS

from ABCD_ML.pipeline.Feature_Selectors import AVALIABLE as AVALIABLE_SELECTORS
from ABCD_ML.pipeline.Feature_Selectors import SELECTORS

from ABCD_ML.pipeline.Ensembles import AVALIABLE as AVALIABLE_ENSEMBLES
from ABCD_ML.pipeline.Ensembles import ENSEMBLES

from ABCD_ML.pipeline.Feat_Importances import IMPORTANCES

from ABCD_ML.helpers.Default_Params import PARAMS


def get_name(obj):

    name = obj.__module__ + '.' + obj.__qualname__

    if '.<locals>.child' in name:
        name = obj.__parent_name__

    name = name.replace('.tree.tree', '.tree')
    name = name.replace('.tree.tree', '.tree')

    base_replace_list = ['logistic', 'gpc', 'gpr', 'classification',
                         'regression', 'coordinate_descent', 'sklearn',
                         'forest', 'classes', 'base', 'multilayer_perceptron',
                         'univariate_selection', 'minimum_difference', 'deskl',
                         'exponential', 'logarithmic', 'rrc', 'data',
                         'variance_threshold']

    for r in base_replace_list:
        name = name.replace('.' + r + '.', '.')

    splits = name.split('.')
    for split in splits:
        if split.startswith('_'):
            name = name.replace('.' + split + '.', '.')

    name = name.replace('ABCD_ML.pipeline.extensions.Feat_Selectors.RFE_Wrapper',
                        'sklearn.feature_selection.RFE')

    return name


def get_metric_name(obj):

    name = obj.__name__
    name = name.replace('_wrapper', '')
    name = 'sklearn.metrics.' + name

    return name


def main_category(lines, name):

    lines.append('.. _' + name + ':')
    lines.append(' ')

    stars = ''.join('*' for i in range(len(name)))
    lines.append(stars)
    lines.append(name)
    lines.append(stars)

    lines.append('')

    return lines


def add_block(lines, problem_types, AVALIABLE=None, OBJS=None):
    '''If AVALIABLE and OBJS stay none, assume that showing metrics'''

    for pt in problem_types:
        lines.append(pt)
        lines.append(''.join('=' for i in range(len(pt))))

        if AVALIABLE is None and OBJS is None:
            objs = get_metrics_by_type(pt)
            metric = True

        else:
            objs = get_objects_by_type(pt, AVALIABLE, OBJS)
            metric = False

        for obj in objs:
            lines = add_obj(lines, obj, metric=metric)

        lines.append('')

    return lines


def add_no_type_block(lines, OBJS):

    lines.append('All Problem Types')
    lines.append('=================')

    objs = get_objects(OBJS)

    for obj in objs:
        lines = add_obj(lines, obj, metric=False)

    lines.append('')
    return lines


def add_obj(lines, obj, metric=False):
    '''Obj as (obj_str, obj, obj_params),
    or if metric = True, can have just
    obj_str and obj.'''

    obj_str = '"' + obj[0] + '"'
    lines.append(obj_str)
    lines.append(''.join(['*' for i in range(len(obj_str))]))
    lines.append('')

    if metric:
        o_path = get_metric_name(obj[1])
        lines.append('  Base Func Documenation: :func:`' + o_path + '`')
    else:
        o_path = get_name(obj[1])
        lines.append('  Base Class Documenation: :class:`' + o_path + '`')
        lines = add_params(lines, obj[2])

    lines.append('')
    return lines


def add_params(lines, obj_params):

    lines.append('')
    lines.append('  Param Distributions')
    lines.append('')

    for p in range(len(obj_params)):

        # Get name
        params_name = obj_params[p]
        lines.append('\t' + str(p) + '. "' + params_name + '" ::')
        lines.append('')

        # Show info on the params
        params = PARAMS[params_name].copy()
        if len(params) > 0:
            lines = add_param(lines, params)
        else:
            lines.append('\t\tdefaults only')

        lines.append('')

    return lines


def add_param(lines, params):

    for key in params:

        line = '\t\t' + key + ': '
        value = params[key]
        line += str(value)
        lines.append(line)

    return lines


problem_types = ['binary', 'regression', 'categorical']

lines = []

lines = main_category(lines, 'Models')
lines.append('Different base obj choices for the :class:`Model<ABCD_ML.Model>` are shown below')
lines.append('The exact str indicator, as passed to the `obj` param is represented' +
             ' by the sub-heading (within "")')
lines.append('The avaliable models are further broken down by which can work' +
             'with different problem_types.')
lines.append('Additionally, a link to the original models documentation ' +
             'as well as the implemented parameter distributions are shown.')
lines.append('')
lines = add_block(lines, problem_types, AVALIABLE_MODELS, MODELS)

lines = main_category(lines, 'Metrics')

lines.append('Different availible choices for the `metric` parameter' +
             ' are shown below.')
lines.append('`metric` is accepted by ' +
             ':class:`Problem_Spec<ABCD_ML.Problem_Spec>`, :class:`Param_Search<ABCD_ML.Param_Search>`' +
             ' and :class:`Feat_Importance<ABCD_ML.Feat_Importance>`)
lines.append('The str indicator for each `metric` is represented by' +
             'the sub-heading (within "")')
lines.append('The avaliable metrics are further broken down by which can' +
             ' work with different problem_types.')
lines.append('Additionally, a link to the original models documentation ' +
             'is shown.')
lines.append('Note: When supplying the metric as a str indicator you do' +
             'not need to include the prepended "multiclass"')
lines.append('')

lines = add_block(lines, problem_types)


lines = main_category(lines, 'Loaders')
lines.append('Different base obj choices for the :class:`Loader<ABCD_ML.Loader>` are shown below')
lines.append('The exact str indicator, as passed to the `obj` param is represented' +
             ' by the sub-heading (within "")')
lines.append('Additionally, a link to the original models documentation ' +
             'as well as the implemented parameter distributions are shown.')
lines.append('')
lines = add_no_type_block(lines, LOADERS)


lines = main_category(lines, 'Imputers')
lines.append('Different base obj choices for the :class:`Imputer<ABCD_ML.Imputer>` are shown below')
lines.append('The exact str indicator, as passed to the `obj` param is represented' +
             ' by the sub-heading (within "")')
lines.append('Additionally, a link to the original models documentation ' +
             'as well as the implemented parameter distributions are shown.')
lines.append('Note that if the iterative imputer is requested, base_model must also be passed.')
lines.append('')
lines = add_no_type_block(lines, IMPUTERS)


lines = main_category(lines, 'Scalers')
lines.append('Different base obj choices for the :class:`Scaler<ABCD_ML.Scaler>` are shown below')
lines.append('The exact str indicator, as passed to the `obj` param is represented' +
             ' by the sub-heading (within "")')
lines.append('Additionally, a link to the original models documentation ' +
             'as well as the implemented parameter distributions are shown.')
lines.append('')
lines = add_no_type_block(lines, SCALERS)


lines = main_category(lines, 'Transformers')
lines.append('Different base obj choices for the :class:`Transformer<ABCD_ML.Transformer>` are shown below')
lines.append('The exact str indicator, as passed to the `obj` param is represented' +
             ' by the sub-heading (within "")')
lines.append('Additionally, a link to the original models documentation ' +
             'as well as the implemented parameter distributions are shown.')
lines.append('')
lines = add_no_type_block(lines, TRANSFORMERS)


lines = main_category(lines, 'Samplers')
lines.append('Different base obj choices for the :class:`Sampler<ABCD_ML.Sampler>` are shown below')
lines.append('The exact str indicator, as passed to the `obj` param is represented' +
             ' by the sub-heading (within "")')
lines.append('Additionally, a link to the original models documentation ' +
             'as well as the implemented parameter distributions are shown.')
lines.append('')
lines = add_no_type_block(lines, SAMPLERS)


lines = main_category(lines, 'Feat Selectors')
lines.append('Different base obj choices for the :class:`Feat_Selector<ABCD_ML.Feat_Selector>` are shown below')
lines.append('The exact str indicator, as passed to the `obj` param is represented' +
             ' by the sub-heading (within "")')
lines.append('The avaliable feat selectors are further broken down by which can work' +
             'with different problem_types.')
lines.append('Additionally, a link to the original models documentation ' +
             'as well as the implemented parameter distributions are shown.')
lines.append('')
lines = add_block(lines, problem_types, AVALIABLE_SELECTORS, SELECTORS)


lines = main_category(lines, 'Ensemble Types')
lines.append('Different base obj choices for the :class:`Ensemble<ABCD_ML.Ensemble>` are shown below')
lines.append('The exact str indicator, as passed to the `obj` param is represented' +
             ' by the sub-heading (within "")')
lines.append('The avaliable ensembles are further broken down by which can work' +
             'with different problem_types.')
lines.append('Additionally, a link to the original models documentation ' +
             'as well as the implemented parameter distributions are shown.')
lines.append('Also note that ensemble require a few extra params! I.e., in general, all DESlib based ensemble need needs_split = True')
lines.append('')
lines = add_block(lines, problem_types, AVALIABLE_ENSEMBLES, ENSEMBLES)


with open('options.rst', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')


with open('base_feature_importance.txt', 'r') as f:
    lines = f.readlines()
    lines = [line.replace('\n', '') for line in lines]

for imp in IMPORTANCES:
    name = imp
    try:
        ri = lines.index('replacewithparams--'+name)
    except ValueError:
        continue

    p_name = IMPORTANCES[imp][1]
    rel_lines = add_params([], p_name)
    lines = lines[:ri] + rel_lines + lines[ri+1:]

lines = ['.. _Feat Importances:', ''] + lines

with open('feat_importances.rst', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')

