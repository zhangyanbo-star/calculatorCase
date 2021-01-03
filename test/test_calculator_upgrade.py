# 测试计算器源代码的case -- 完善版
"""
   1 使用了 conftest.py 存放全局配置
   2 设定 fixture 方法，通过 params 实现参数化
   3 获取 yaml 文件所在路径
   4 完善浮点数的计算，增强代码的健壮性
   5 增加了对异常的处理
   6 使用 pytest-ordering 插件控制用例执行的顺序
   7 使用 allure-pytest 插件生成测试报告
"""
import pytest
import allure


@allure.feature("计算器功能模块")
class TestCalculator:
    @allure.story("加法计算子模块")
    @pytest.mark.run(order=1)
    def test_addition(self, get_instance, get_addition_data, setup_info):
        result = None
        try:
            result = get_instance.addition(get_addition_data[0], get_addition_data[1])
            # 判断结果的类型，如果是浮点数就强制保留n位，这里指定了8位，超出8位会报错
            if isinstance(result, float):
                result = round(result, 8)
        except Exception as e:
            print(e)
        assert result == get_addition_data[2]

    @allure.story("除法计算子模块")
    @pytest.mark.run(order=4)
    def test_division(self, get_instance, get_division_data):
        result = None
        try:
            result = get_instance.division(get_division_data[0], get_division_data[1])
            # 判断结果的类型，如果是浮点数就强制保留n位，这里指定了8位，超出8位会报错
            if isinstance(result, float):
                result = round(result, 8)
        except Exception as e:
            print(e)
        assert result == get_division_data[2]

    @allure.story("减法计算子模块")
    @pytest.mark.run(order=2)
    def test_subtraction(self, get_instance, get_subtraction_data):
        result = None
        try:
            result = get_instance.subtraction(get_subtraction_data[0], get_subtraction_data[1])
            # 判断结果的类型，如果是浮点数就强制保留n位，这里指定了8位，超出8位会报错
            if isinstance(result, float):
                result = round(result, 8)
        except Exception as e:
            print(e)
        assert result == get_subtraction_data[2]

    @allure.story("乘法计算子模块")
    @pytest.mark.run(order=3)
    def test_multiplication(self, get_instance, get_multiplication_data):
        result = None
        try:
            result = get_instance.multiplication(get_multiplication_data[0], get_multiplication_data[1])
            # 判断结果的类型，如果是浮点数就强制保留n位，这里指定了8位，超出8位会报错
            if isinstance(result, float):
                result = round(result, 8)
        except Exception as e:
            print(e)
        assert result == get_multiplication_data[2]
