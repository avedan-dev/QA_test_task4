import pytest


class Test_case_1():
    # None отвечает за текущее время
    # Остальные значения показывают сколько времени в секунда прошло с начала эпохи
    PARAMS = [None, pytest.param(-1, marks=pytest.mark.xfail(reason='Ожидаемо для -1')), 0,
              pytest.param(1, marks=pytest.mark.xfail()), 2, 9999998, pytest.param(9999999, marks=pytest.mark.xfail())]
    IDS = ['Now', 'Negative num', 'Zero', '1', '2', 'Big even number', 'Big odd num']


class Test_case_2():
    # Проверяет объем оперативной памяти на ПК
    MEM_SIZE = [1, pytest.param(20, marks=pytest.mark.xfail(reason='Объем опреативной памяти меньше 20 Гб'))]
    # Id тестов для разного количества оперативной памяти
    IDS = ['1', '20 Gb']
    # Заведомо неверные имена файлов
    FILE_WRONG_NAMES = ['testing', 'testted']
    # Заведомо неверные размеры файлов
    FILE_WRONG_SIZE = [2000, 500, 1001, 999, 0, -1]
