'''
实战二:推算几天后的日期
需求:编写一个程序,输入开始日期和间隔天数,可以推算出结
束日期,使用内置的datetime模块
'''
from datetime import datetime, timedelta

def calculate_end_date(start_date, days):
    end_date = start_date + timedelta(days=days)
    return end_date

start_date = datetime(2021, 1, 1)
days = 10
end_date = calculate_end_date(start_date, days)
print(f"The end date is: {end_date}")
print(f"The end date in format 'YYYY-MM-DD' is: {end_date.strftime('%Y-%m-%d')}")

# 测试
import unittest
class TestCalculateEndDate(unittest.TestCase):

    def test_calculate_end_date(self):
        start_date = datetime(2021, 1, 1)
        days = 10
        end_date = calculate_end_date(start_date, days)
        self.assertEqual(end_date, datetime(2021, 1, 11))

        start_date = datetime(2021, 1, 1)
        days = 0
        end_date = calculate_end_date(start_date, days)
        self.assertEqual(end_date, start_date)

        start_date = datetime(2021, 2, 28)
        days = 1
        end_date = calculate_end_date(start_date, days)
        self.assertEqual(end_date, datetime(2021, 3, 1))

        start_date = datetime(2020, 2, 29)
        days = 1
        end_date = calculate_end_date(start_date, days)
        self.assertEqual(end_date, datetime(2020, 3, 1))

        start_date = datetime(2020, 2, 29)
        days = 30
        end_date = calculate_end_date(start_date, days)
        self.assertEqual(end_date, datetime(2020, 3, 31))

if __name__ == '__main__':
    unittest.main()

# 生成文档
import os
import subprocess

# 安装sphinx
subprocess.check_call(['pip', 'install', 'sphinx'])

# 生成文档
subprocess.check_call(['sphinx-apidoc', '-f', '-o', 'docs', '.'])
subprocess.check_call(['sphinx-build', '-b', 'html', 'docs', 'docs/_build'])

# 打开生成的文档
webbrowser.open('file://' + os.path.realpath('docs/_build/index.html'))

# 测试
import unittest

class TestCalculateEndDate(unittest.TestCase):

    def test_calculate_end_date(self):
        start_date = datetime(2021, 1, 1)
        days = 10
        end_date = calculate_end_date(start_date, days)
        self.assertEqual(end_date, datetime(2021, 1, 11))

        start_date = datetime(2021, 1, 1)
        days = 0
        end_date = calculate_end_date(start_date, days)
        self.assertEqual(end_date, datetime(2021, 1, 1))

        start_date = datetime(2021, 2, 28)
        days = 1
        end_date = calculate_end_date(start_date, days)
        self.assertEqual(end_date, datetime(2021, 3, 1))

        start_date = datetime(2020, 2, 29)
        days = 30
        end_date = calculate_end_date(start_date, days)
        self.assertEqual(end_date, datetime(2020, 3, 31))
        start_date = datetime(2020, 2, 29)
        days = 31
        end_date = calculate_end_date(start_date, days)
        self.assertEqual(end_date, datetime(2020, 3, 31))

if __name__ == '__main__':
    unittest.main()

# 生成API文档
subprocess.check_call(['sphinx-apidoc', '-f', '-o', 'docs/', '.'])

# 构建文档
subprocess.check_call(['sphinx-build', '-E', '-W', '-b', 'html', 'docs/', 'docs/_build/html/'])
