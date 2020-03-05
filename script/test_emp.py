import logging
import app
import unittest
import requests
from api.emp_api import EmpApi
from utils import assert_conmm_utils, SqlUtils,case_data_emp
import pymysql
from parameterized import parameterized
add_emp,index_emp,put_emp,delete_emp  = case_data_emp()


class TestEmp(unittest.TestCase):
    def setUp(self):
        self.login_api = EmpApi()
    def tearDown(self):
        pass


    def test01_login_emp_case(self):
        app.init_logger()
        reponse = self.login_api.login_auto("13800000002","123456")
        logging.info(reponse.json())
        token = "Bearer " + reponse.json().get("data")
        logging.info("id:{}".format(token))
        #设置请求头
        headers = {"Content-Type":"application/json","Authorization":token}
        app.HEADERS = headers

        #调用添加员工接口
    @parameterized.expand(add_emp)
    def test02_add_emp(self,username,mobile,http_code,success,code,message):

        reponse_add_emp = self.login_api.add_emp(username,mobile,app.HEADERS)

        logging.info("添加员工结果为:{}".format(reponse_add_emp.json()))

        assert_conmm_utils(self,reponse_add_emp,http_code,success,code,message)
        emp_id = reponse_add_emp.json().get("data").get("id")
        app.EMP_ID = emp_id
        logging.info("保存的员工id:{}".format(reponse_add_emp.json()))

        #查询员工
    @parameterized.expand(index_emp)
    def test03_index_emp(self,http_code,success,code,message):
        reponse_index_emp = self.login_api.index_emp(app.EMP_ID,headers=app.HEADERS)
        logging.info("查询员工结果为:{}".format(reponse_index_emp.json()))
        assert_conmm_utils(self,reponse_index_emp,http_code,success,code,message)

        #修改员工

    @parameterized.expand(put_emp)
    def test04_put_emp(self,username,http_code,success,code,message):
        reponse_set_emp =self.login_api.put_emp(app.EMP_ID,username,headers=app.HEADERS)
        logging.info("修改员工结果为:{}".format(reponse_set_emp.json()))
        #连接数据库
        with SqlUtils() as db:
            # conn = pymysql.connect(host="182.92.81.159",user="readuser",password="iHRM_user_2019",database="ihrm",)
            # cursor = conn.cursor()
            sql = "select username from bs_user where id={};".format(app.EMP_ID)
            db.execute(sql)
            logging.info("要查询的语句为:{}".format(sql))
            result = db.fetchone()
            logging.info("查询结果为:{}".format(result))
            self.assertEqual(username,result[0])

        assert_conmm_utils(self,reponse_set_emp, http_code,success,code,message)

        #删除员工

    @parameterized.expand(delete_emp)
    def test05_delete_emp(self,http_code,success,code,message):
        reponse_delete_emp =self.login_api.delete_emp(app.EMP_ID,headers=app.HEADERS)
        logging.info("删除员工结果为:{}".format(reponse_delete_emp.json()))
        assert_conmm_utils(self,reponse_delete_emp,http_code,success,code,message)