# 导入sys模块
# 原因：sys模块提供了访问与Python解释器紧密相关的变量和函数
import sys

# 导入os模块
# 原因：os模块提供了与操作系统交互的功能，特别是文件路径操作
import os

# 将项目根目录添加到Python路径(sys.path)中
# 原因：Python解释器只在sys.path列出的目录中搜索模块
# 这行代码的目的是让Python能够找到项目根目录中的main模块
# os.path.dirname(__file__)获取当前文件(test_baidu.py)所在目录的绝对路径
# os.path.join()将路径片段拼接成跨平台兼容的路径
# os.path.abspath()将相对路径转换为绝对路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 从main模块导入web_form函数
# 原因：现在Python可以在项目根目录找到main模块，因为上面已经将其添加到sys.path
from main import web_form


# 定义测试函数test_baidu_search
# 原因：pytest会自动收集以"test_"开头的函数作为测试用例
def test_baidu_search():
    # 调用web_form函数并传入"Hello CI"作为参数
    # 原因：测试web_form函数是否能正常处理输入并提交表单
    result = web_form("Hello CI")

    # 断言结果为True
    # 原因：如果web_form函数返回True，表示表单提交成功，测试通过
    # 如果返回False或抛出异常，测试失败并显示"测试失败：表单提交未成功"
    assert result is True, "测试失败：表单提交未成功"
