import sys
import os

# 将项目根目录添加到sys.path
# 原因：使Python能够找到项目根目录中的main模块
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import test_web_form

def test_baidu_search():
    """
    测试百度搜索功能的函数
    该函数通过调用test_web_form方法来模拟百度搜索操作
    """
    # 调用main.py中的test_web_form方法
    # 可以传入自定义文本作为参数，例如'Hello Baidu'
    test_web_form('Hello CCI')
