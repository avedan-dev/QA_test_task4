import os
import time
import pytest


class TestCase1:
    def prep(self):
        assert not int(time.time()) % 2, 'Время не кратно двум'

    def clean_up(self):
        pass

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.prep()
        yield
        self.clean_up()

    def test_files(self):
        print(os.listdir())
        assert os.listdir()
