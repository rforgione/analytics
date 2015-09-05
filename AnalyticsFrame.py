import numpy as np
import pandas as pd

class AnalyticsFrame(pd.DataFrame):

    def __init__(self, data=None, index=None, columns=None, dtype=None,
                copy=False):
        super(AnalyticsFrame, self).__init__(data, index, columns, dtype, copy) # df args go here
        self._formatted = pd.DataFrame(self._data)

    def apply_format(self, field, format_func):
        self._formatted[field] = self._formatted[field].apply(format_func)

    def metric(self, numer, denom):
        return self.loc[:,numer].sum() / self.loc[:,denom].sum()

    def _formatted(self):
        return self._formatted


data = {'a': [1,2,3], 'b': [4,5,6]}
g = AnalyticsFrame(data)




