#封装通用断言函数
import json
import os

import pymysql


def assert_conmm_utils(self,reponse,http_code,is_success,code,message1):
    self.assertEqual(http_code, reponse.status_code)
    self.assertEqual(is_success, reponse.json().get("success"))
    self.assertEqual(code, reponse.json().get("code"))
    self.assertEqual(message1, reponse.json().get("message"))

class SqlUtils():
    def __init__(self,host="182.92.81.159",user="readuser",password="iHRM_user_2019",database="ihrm"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def __enter__(self):
        self.conn = pymysql.connect(self.host,self.user,self.password,self.database)
        self.cursor = self.conn.cursor()
        return self.cursor


    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()



def case_data_login():
    login_data_path = os.path.dirname(os.path.abspath(__file__)) + "/data/login.json"

    with open(login_data_path,"r",encoding="utf-8") as f:
        jsonData = json.load(f)
        result_list = []
        for case_data in jsonData:
            mobile = case_data.get("mobile")
            password = case_data.get("password")
            http_code = case_data.get("http_code")
            success = case_data.get("success")
            code = case_data.get("code")
            message = case_data.get("message")
            # result_list.append((mobile,password,http_code,success,code,message))
            result_list.append(tuple(case_data.values()))

    print("测试数据为:",result_list)
    return result_list

#员工管理模块参数化
def case_data_emp():
    emp_data_path = os.path.dirname(os.path.abspath(__file__)) + "/data/emp_data.json"
    with open(emp_data_path,"r",encoding="utf-8") as f:
        jsonData = json.load(f)
        result_list = []
        result_list1 = []
        result_list2 = []
        result_list3 = []
        add_emp_data = jsonData.get("add_emp")
        result_list.append(tuple(add_emp_data.values()))

        index_emp_data = jsonData.get("index_emp")
        result_list1.append(tuple(index_emp_data.values()))

        put_emp_data = jsonData.get("put_emp")
        result_list2.append(tuple(put_emp_data.values()))

        delete_emp_data = jsonData.get("delete_emp")
        result_list3.append(tuple(delete_emp_data.values()))

    print(result_list)
    print(result_list1)
    print(result_list2)
    print(result_list3)
    return result_list,result_list1,result_list2,result_list3




if __name__ == '__main__':
    # case_data_login()
    case_data_emp()




