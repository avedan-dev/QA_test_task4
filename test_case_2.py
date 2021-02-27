import pytest
import os


class TestCase2:
    def prep(self):
        with open('/proc/meminfo', 'r') as mem:
            total_mem = 0
            for i in mem:
                sline = i.split()
                if str(sline[0]) == 'MemTotal:':
                    total_mem = int(sline[1])
        assert total_mem // 1024 ** 2 >= 1, 'Объем оперативной памяти меньше 1 Гб'

    def clean_up(self):
        os.remove('test')
        assert 'test' not in os.listdir(), 'В директории остался файл test'

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.prep()
        yield
        self.clean_up()

    def test_create_file(self):
        with open('test', 'wb') as f:
            f.write(os.urandom(1000))
        assert os.path.getsize('test') == 1000

'''
    def test_file_delete(self):
        os.remove('test')
        assert 'test' not in os.listdir()
'''