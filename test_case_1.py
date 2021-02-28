import os
import time
import pytest
from .vars import Test_case_1


class TestCase1:
    # n отвечает за количество секунд с начала эпохи
    def prep(self, n):
        t = time.localtime(n)
        assert not int(time.mktime(t)) % 2, 'Время не кратно двум'

    def clean_up(self):
        pass

    @pytest.fixture(scope="function", autouse=True, params=Test_case_1.PARAMS, ids=Test_case_1.IDS)
    def setup(self, request):
        self.prep(request.param)
        yield
        self.clean_up()

    def test_files(self):
        print(os.listdir())
        assert os.listdir()
