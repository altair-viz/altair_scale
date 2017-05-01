"""Visualization scales for Python

Meant to be compatible with ipywidgets, based on Vega 3 scales:

https://github.com/vega/vega-scale
"""

import traitlets as T


class Scale(T.HasTraits):

    name = T.Unicode('')
    type = T.Unicode('')
    domain = T.Union([T.List, T.Tuple])
    domainMax = T.CFloat()
    domainMin = T.CFloat()
    domainMid = T.CFloat()
    domainRaw = T.Union([T.List, T.Tuple])
    range = T.Union([
        T.List,
        T.Tuple,
        T.Enum(['width', 'height', 'symbol', 'category', 'diverging', 'ordinal', 'ramp', 'heatmap'])
    ])
    reverse = T.Bool()
    round = T.Bool()

    def __call__(self, *args, **kwargs):
        raise NotImplementedError('Scale operation not implemented, use a subclass.')


#-----------------------------------------------------------------------------
# Quantitative Scales
#-----------------------------------------------------------------------------


class QuantitativeScale(Scale):

    type = T.Unicode('quantitative')
    clamp = T.Bool()
    interploate = T.Unicode()
    nice = T.Union([T.Bool(), T.CFloat])
    zero = T.Bool()


class LinearScale(QuantitativeScale):

    type = T.Unicode('linear')


class PowerScale(QuantitativeScale):

    type = T.Unicode('power')
    exponent = T.CFloat()


class LogScale(QuantitativeScale):

    type = T.Unicode('log')
    base = T.CFloat()


class TimeScale(QuantitativeScale):

    type = T.Unicode('time')
    nice = T.Union([
         T.Unicode,
         T.CFloat,
         T.Enum(['second', 'minute', 'hour', 'day', 'week', 'month', 'year'])
    ])


class UTCScale(TimeScale):

    type = T.Unicode('utc')


class SequentialScale(QuantitativeScale):

    type = T.Unicode('sequential')
    clamp = T.Bool()


#-----------------------------------------------------------------------------
# Discrete Scales
#-----------------------------------------------------------------------------


class DiscreteScale(Scale):

    type = T.Unicode('discrete')


class OrdinalScale(DiscreteScale):

    type = T.Unicode('band')


class BandScale(DiscreteScale):

    type = T.Unicode('band')
    align = T.CFloat()
    padding = T.Float()
    paddingInner = T.CFloat()
    paddingOuter = T.CFloat()


class PointScale(DiscreteScale):

    type = T.Unicode('point')
    align = T.CFloat()
    padding = T.Float()
    paddingOuter = T.CFloat()


#-----------------------------------------------------------------------------
# Discretizing Scales
#-----------------------------------------------------------------------------


class DiscretizingScale(Scale):

    type = T.Unicode('discretizing')


class QuantileScale(DiscretizingScale):

    type = T.Unicode('quantile')


class QuantizeScale(DiscretizingScale):

    type = T.Unicode('quantize')
    nice = T.Union([T.Bool, T.CFloat])
    zero = T.Bool()


class ThresholdScale(DiscretizingScale):

    type = T.Unicode('threshold')


class BinLinearScale(DiscretizingScale):

    type = T.Unicode('bin-learn')


class BinOrdinalScale(DiscretizingScale):

    type = T.Unicode('bin-ordinal')



