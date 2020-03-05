import unittest
import requests
import logging

import app
from utils import assert_conmm_utils
from api.emp_department import EmpDepartmentApi


class TestDepartment(unittest.TestCase):
    def setUp(self):
        self.login_token = EmpDepartmentApi()
    def tearDown(self):
        pass
    def test001_login_success(self):
        app.init_logger()
        reponse = self.login_token.get_login("13800000002","123456")
        logging.info("登录结果为:{}".format(reponse.json()))
        token = "Bearer " + reponse.json().get("data")
        logging.info("获取的令牌为:{}".format(token))
        headers = {"Content-Type":"application/json","Authorization":token}


        reponse1 = requests.get("http://182.92.81.159/api/company/department",headers=headers)
        logging.info("获取的部门信息为:{}".format(reponse1.json().get("data").get("depts")))

        #添加部门
        reponse2 = requests.post("http://182.92.81.159/api/company/department",
                                json={"name":"乔巴","code":"9527"},headers=headers,)
        logging.info("添加的结果为:{}".format(reponse2.json().get("data")))
        assert_conmm_utils(self,reponse2,200,True,10000,"操作成功！")
        #
        # #查询部门
        # reponse3 = requests.get()

    # def obtion_department_info(self):
    #     pass
    # def test002_add_department(self):
    #     pass
    # def test003_index_department(self):
    #     pass
    # def test004_delete_department(self):
    #     pass