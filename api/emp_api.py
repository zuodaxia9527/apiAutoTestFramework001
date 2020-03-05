import requests


class EmpApi():
    def __init__(self):
        self.auto_url = "http://182.92.81.159/api/sys/login"

    def login_auto(self,mobile,password):
        jsonData = {"mobile": mobile, "password": password}
        return requests.post(self.auto_url,json=jsonData)

    def add_emp(self,mobile,password,headers):
        add_url = "http://182.92.81.159/api/sys/user"
        add_data = {"username": mobile,
                "mobile": password,
                "timeOfEntry": "2019-07-01",
                "formOfEmployment": 1,
                "workNumber": "1322131",
                "departmentName": "开发部",
                "departmentId": "1066240656856453120",
                "correctionTime": "2019-11-30"}
        return requests.post(add_url,json=add_data,headers=headers)

    def index_emp(self,emp_id,headers):
        index_url = "http://182.92.81.159/api/sys/user/"+emp_id
        return requests.get(index_url,headers=headers)

    def put_emp(self,emp_id,username,headers):
        put_url = "http://182.92.81.159/api/sys/user/"+emp_id
        return requests.put(put_url,json={"username":username},headers=headers)

    def delete_emp(self,emp_id,headers):
        delete_url = "http://182.92.81.159/api/sys/user/"+emp_id
        return requests.delete(delete_url,headers=headers)