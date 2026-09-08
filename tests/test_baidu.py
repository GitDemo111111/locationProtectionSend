from ..main import test_web_form


def test_baidu_search():
    # 调用main.py中的test_web_form方法
    # 可以传入自定义文本作为参数，例如'Hello Baidu'
    test_web_form('Hello ACI')
