import pytest
import os
from .vars import Test_case_2

class TestCase2:
    def prep(self,n):
        with open('/proc/meminfo', 'r') as mem:
            total_mem = 0
            for i in mem:
                sline = i.split()
                if str(sline[0]) == 'MemTotal:':
                    total_mem = int(sline[1])
        assert total_mem // 1024 ** 2 >= 1, f'Объем оперативной памяти меньше {n} Гб'

    def clean_up(self):
        os.remove('test')
        assert 'test' not in os.listdir(), 'В директории остался файл test'

    @pytest.fixture(scope="function", autouse=True, params=Test_case_2.PARAMS, ids=Test_case_2.IDS)
    def setup(self, request):
        self.prep(request.param)
        yield
        self.clean_up()

    def test_create_file(self):
        with open('test', 'wb') as f:
            f.write(os.urandom(1000))
        assert os.path.getsize('test') == 1000

    @pytest.mark.xfail
    def test_create_file_failed(self):
        with open('test_fail', 'wb') as f:
            f.write(os.urandom(1000))
        assert os.path.getsize('test') == 1000
