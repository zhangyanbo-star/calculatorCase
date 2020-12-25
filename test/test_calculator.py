# 测试计算器源代码的case
import pytest
import yaml

from src.calculator import Calculator


def get_data_from_yml():
    with open("datasource/calculator.yml") as f:
        datas = yaml.safe_load(f)
        print(datas)
        id_alias = datas["id_alias"]
        addition_data = datas["addition_data"]
        subtraction_data = datas["subtraction_data"]
        multiplication_data = datas["multiplication_data"]
        division_data = datas["division_data"]
        return [id_alias, addition_data, subtraction_data, multiplication_data, division_data]


class TestCalculator:
    # 实例化被测对象
    def setup_class(self):
        self.calc = Calculator()

    def setup_method(self):
        print("\n开始计算")

    def teardown_method(self):
        print("\n计算结束")

    @pytest.mark.parametrize("x, y, expectedValue", get_data_from_yml()[1], ids=get_data_from_yml()[0])
    def test_addition(self, x, y, expectedValue):
        result = self.calc.addition(x, y)
        assert result == expectedValue

    @pytest.mark.parametrize("x, y, expectedValue", get_data_from_yml()[2], ids=get_data_from_yml()[0])
    def test_subtraction(self, x, y, expectedValue):
        result = self.calc.subtraction(x, y)
        assert result == expectedValue

    @pytest.mark.parametrize("x, y, expectedValue", get_data_from_yml()[3], ids=get_data_from_yml()[0])
    def test_multiplication(self, x, y, expectedValue):
        result = self.calc.multiplication(x, y)
        assert result == expectedValue

    @pytest.mark.parametrize("x, y, expectedValue", get_data_from_yml()[4], ids=get_data_from_yml()[0])
    def test_division(self, x, y, expectedValue):
        result = self.calc.division(x, y)
        assert result == expectedValue

# if __name__ == '__main__':
#     get_data_from_yml()
