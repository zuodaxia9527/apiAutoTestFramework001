import os
from HTMLTestRunner_PY3 import HTMLTestRunner
import unittest

import time

from script.Tpshow_login import TestTpshowlogin
from script.test_emp import TestEmp
from script.test_emp_login import TestEmpLogin




suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestTpshowlogin))
suite.addTest(unittest.makeSuite(TestEmpLogin))
suite.addTest(unittest.makeSuite(TestEmp))

report_path = os.path.dirname(os.path.abspath(__file__)) + "/report/ihrm.html"
#.format(time.strftime("%Y%m%d %H%M%S"))
with open(report_path,"wb") as f:
    runner = HTMLTestRunner(f,verbosity=2,title="綜合测试",description="win10-chrome-80.0")
    runner.run(suite)
print("hello word")





