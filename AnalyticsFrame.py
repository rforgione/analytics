import numpy as np
import pandas as pd

class AnalyticsFrame(pd.DataFrame):

    def __init__(self, data=None, index=None, columns=None, dtype=None,
                copy=False):
        super(AnalyticsFrame, self).__init__(data, index, columns, dtype, copy) # df args go here
        self._formatted = pd.DataFrame(self._data)

    def apply_format(self, field, format_func):
        self._formatted[field] = self._formatted[field].apply(format_func)

    def metric(self, numer, denom, numer_count=False, denom_count=False):
        numer_qty = float(self[numer].sum())
        denom_qty = float(self[denom].sum())

        if numer_count:
            numer_qty = float(len(pd.unique(self[numer])))
        elif denom_count:
            denom_qty = float(len(pd.unique(self[denom])))

        return numer_qty / denom_qty

    def _formatted(self):
        return self._formatted


data = {'a': [1,2,3], 'b': [4,5,6]}
g = AnalyticsFrame(data)




