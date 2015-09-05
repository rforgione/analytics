from AnalyticsFrame import AnalyticsFrame
from nose import with_setup
import pandas as pd

class TestAnalyticsFrame(object):
    data = {'a': [1,2,3], 'b': [4,5,6]}
    g = AnalyticsFrame(data)

    def test_metric_1(self):
        assert self.g.metric('a', 'b') == sum([1,2,3]) / float(sum([4,5,6]))

    def test_metric_2(self):
        assert self.g.metric('a', 'b', denom_count=True) == sum([1,2,3])/float(3)

    def test_metric_3(self):
        assert self.g.metric('a', 'b', numer_count=True) == 3/float(sum([4,5,6]))

