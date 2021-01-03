import pytest
import yaml
import os

from src.calculator import Calculator


# 实例化被测对象
@pytest.fixture(scope="class")
def get_instance():
    print("获取计算器实例")
    return Calculator()


@pytest.fixture(scope="module")
def setup_info():
    print("\n开始计算")
    yield
    print("\n计算结束")


# 获取当前文件所在路径 os.path.dirname(__file__)
yaml_path = os.path.dirname(__file__) + "/datasource/calculator_upgrade.yml"


def get_data_from_yml():
    with open(yaml_path) as f:
        datas = yaml.safe_load(f)
        print(datas)
        id_alias = datas["id_alias"]
        addition_data = datas["addition_data"]
        division_data = datas["division_data"]
        subtraction_data = datas["subtraction_data"]
        multiplication_data = datas["multiplication_data"]
        return [id_alias, addition_data, division_data, subtraction_data, multiplication_data]


@pytest.fixture(params=get_data_from_yml()[1], ids=get_data_from_yml()[0])
def get_addition_data(request):
    datas = request.param
    print(f"参数：{datas}")
    return datas


@pytest.fixture(params=get_data_from_yml()[2], ids=get_data_from_yml()[0])
def get_division_data(request):
    datas = request.param
    print(f"参数：{datas}")
    return datas


@pytest.fixture(params=get_data_from_yml()[3], ids=get_data_from_yml()[0])
def get_subtraction_data(request):
    datas = request.param
    print(f"参数：{datas}")
    return datas


@pytest.fixture(params=get_data_from_yml()[4], ids=get_data_from_yml()[0])
def get_multiplication_data(request):
    datas = request.param
    print(f"参数：{datas}")
    return datas
