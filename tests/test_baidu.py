import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import web_form

def test_baidu_search():
    result = web_form("Hello CI")
    assert result is True, "测试失败：表单提交未成功"