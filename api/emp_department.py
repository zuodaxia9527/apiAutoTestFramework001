import requests


class EmpDepartmentApi():
    def __init__(self):
        self.login_token_url = "http://182.92.81.159/api/sys/login"

    def get_login(self,mobile,password):
        jsonData = {"mobile":mobile,"password":password}
        return requests.post(self.login_token_url,json=jsonData)
    def department(self):
        pass