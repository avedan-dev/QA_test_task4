import pytest
import os
from .vars import Test_case_2


class TestCase2:
    # n объем оперативной памяти в гб, которую проверяет тест
    def prep(self, n):
        with open('/proc/meminfo', 'r') as mem:
            total_mem = 0
            for i in mem:
                sline = i.split()
                if str(sline[0]) == 'MemTotal:':
                    total_mem = int(sline[1])
        assert total_mem // 1024 ** 2 >= n, f'Объем оперативной памяти меньше {n} Гб'

    # Удаляет файлы созданные во время теста
    def clean_up(self):
        for i in os.listdir():
            if i in Test_case_2.FILE_WRONG_NAMES or i == 'test':
                os.remove(i)
        assert 'test' not in os.listdir(), 'В директории остался файл test'

    # Выполняется перед каждым тестом
    @pytest.fixture(scope="function", autouse=True, params=Test_case_2.MEM_SIZE, ids=Test_case_2.IDS)
    def run_test(self, request):
        self.prep(request.param)
        yield
        self.clean_up()

    # Создает файл test необходимой длинны
    def test_create_file(self):
        with open('test', 'wb') as f:
            f.write(os.urandom(1000))
        assert os.path.getsize('test') == 1000

    # Xfail тесты, которые создают файлы с неверным названием
    @pytest.mark.xfail(reason='Намеренно создали файл с другим названием')
    @pytest.mark.parametrize("name", Test_case_2.FILE_WRONG_NAMES)
    def test_create_file_failed(self, name):
        with open(name, 'wb') as f:
            f.write(os.urandom(1000))
        assert os.path.getsize('test') == 1000

    # Xfail тесты, которые создают файлы с неверного размера
    @pytest.mark.xfail(reason='Намеренно создали файл другого размера')
    @pytest.mark.parametrize("size", Test_case_2.FILE_WRONG_SIZE)
    def test_create_wrong_size(self, size):
        with open('test', 'wb') as f:
            f.write(os.urandom(size))
        assert os.path.getsize('test') == 1000
