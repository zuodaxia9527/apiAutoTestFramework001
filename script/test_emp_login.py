import logging
import requests
import unittest
import app
from api.emp_login_api import EmpLoginApi
from utils import assert_conmm_utils,case_data_login
from parameterized import parameterized


class TestEmpLogin(unittest.TestCase):
    def setUp(self):
        self.login_api = EmpLoginApi()
    def tearDown(self):
        pass

    @parameterized.expand(case_data_login)
    def test001_login_is_success(self,case_name,mobile,password,http_code,success,code,message):
        app.init_logger()
        reponse = self.login_api.login_auto(mobile,password)
        logging.info("登陆成功的结果为:{}".format(reponse.json()))
        assert_conmm_utils(self,reponse,http_code,success,code,message)
    # def test002_username_not_exist(self):
    #     reponse = self.login_api.login_auto("1390000002","123456")
    #     logging.info("用户名不存在的结果为:{}".format(reponse.json()))
    #     assert_conmm_utils(self,reponse,200,False,20001,"用户名或密码错误")
    #
    # def test003_username_is_none(self):
    #     reponse = self.login_api.login_auto("1380000002","")
    #     logging.info("用户名为空的结果为:{}".format(reponse.json()))
    #     assert_conmm_utils(self,reponse,200,False,20001,"用户名或密码错误")
    # def test004_password_erorr(self):
    #     reponse = self.login_api.login_auto("1380000002","")
    #     logging.info("密码错误的结果为:{}".format(reponse.json()))
    #     assert_conmm_utils(self,reponse,200,False,20001,"用户名或密码错误")
    # def test005_password_is_none(self):
    #     reponse = self.login_api.login_auto("1380000002","")
    #     logging.info("密码为空的结果为:{}".format(reponse.json()))
    #     assert_conmm_utils(self,reponse,200,False,20001,"用户名或密码错误")
    def test006_less_mobile_parame(self):
        reponse =self.login_api.login_parmae({"password":"123456"})
        logging.info("缺少mobile的结果为:{}".format(reponse.json()))
        assert_conmm_utils(self,reponse,200,False,20001,"用户名或密码错误")
    def test007_less_password_parame(self):
        reponse =self.login_api.login_parmae({"mobile":"13800000002"})
        logging.info("缺少password的结果为:{}".format(reponse.json()))
        assert_conmm_utils(self,reponse,200,False,20001,"用户名或密码错误")
    def test008_many_parmae(self):
        reponse =self.login_api.login_parmae({"mobile":"13800000002",
                                              "password":"123456",
                                              "a":"1"})
        logging.info("多参的结果为:{}".format(reponse.json()))
        assert_conmm_utils(self,reponse,200,True, 10000,"操作成功！")
    def test009_erorr_parame(self):
        reponse =self.login_api.login_parmae({"mbile":"13800000002",
                                              "password":"123456"})
        logging.info("错参的结果为:{}".format(reponse.json()))
        assert_conmm_utils(self,reponse,200,False,20001,"用户名或密码错误")
    def test010_none_paeame(self):
        reponse =self.login_api.login_parmae(None)
        logging.info("无参的结果为:{}".format(reponse.json()))
        assert_conmm_utils(self,reponse,200,False,99999,"抱歉，系统繁忙，请稍后重试！")