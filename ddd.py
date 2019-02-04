import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""
    """定义测试函数，以test开头，运行该模块时，所有test开头的函数将自动运行"""
    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        """assertEqual函数，判断函数返回结果，是否正确"""
        self.assertEqual(formatted_name, 'Janis2 Joplin')


unittest.main()


