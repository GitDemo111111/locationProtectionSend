import sys
import os

# 将项目根目录添加到sys.path（确保能找到 main.py）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import test_web_form


def test_baidu_search():
    """
    CI 测试入口：调用 main.py 中的核心业务逻辑
    """
    text = 'Hello CI'
    # 调用 main.py 的方法，并拿到执行结果（True/False）
    result = test_web_form(text)

    # ⚠️ 关键：必须用 assert 断言，pytest 才能判断用例是否通过
    assert result is True, "测试失败：表单提交未成功"