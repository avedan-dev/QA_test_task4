import pytest


class Test_case_1():
    PARAMS = [None, pytest.param(-1, marks=pytest.mark.xfail(reason='Ожидаемо для -1')), 0,
              pytest.param(1, marks=pytest.mark.xfail()), 2, 9999998, pytest.param(9999999, marks=pytest.mark.xfail())]
    IDS = ['Now', 'Negative num', 'Zero', '1', '2', 'Big even number', 'Big odd num']


class Test_case_2():
    PARAMS = [1]
    IDS = ['1']
