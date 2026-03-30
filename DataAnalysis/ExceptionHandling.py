# IndexError 索引错误
# ZeroDivisionError 除零错误
# FileNotFoundError 找不到文件错位u
# TypeError 类型错误


# 捕捉异常
# try:
#   放入可能报错的代码
# except ValueError（此处为放入捕捉错误的名字，或不放）:
#   print("放入需要的操作")
# else:
#   print("当前面的代码没有错误时，会执行该句")
# finally:
#   print("无论前面代码有无错误，都会被执行的语句")

# unittest ————测试代码的库，其会自动搜寻test_开头的方法，且只把test_开头的当成测试用例
# 在命令终端，输入 python -m unittest，表示运行unittest，
# 这个库便会自动搜寻所有继承了unittest库里TestClass类的子类，运行他们所有以test_开头的方法，并一次性展示测试结果
# . 有几个表示测试通过几个

# assertEqual(A,B)  类似于 assert A == B
# assertTrue(A)   类似于  assert A is True


import unittest
from shopping_list import ShoppingList

class TestShoppingList(unittest.TestCase):
    def setUp(self):   # setUp()方法
        self.shopping_list = ShoppingList({"纸巾": 8, "帽子": 30, "拖鞋": 15})

    def test_get_item_count(self):
        self.assertEqual(self.shopping_list.get_item_count(), 3)

    def test_get_total_price(self):
        self.assertEqual(self.shopping_list.get_total_price(), 55)



