import requests
import unittest

class EmpLoginApi():
    def __init__(self):
        self.auto_url = "http://182.92.81.159/api/sys/login"

    def login_auto(self, mobile, password):
        jsonData = {"mobile": mobile, "password": password}
        return requests.post(self.auto_url, json=jsonData)

    #对多参、少参处理
    def login_parmae(self,jsonData):
        return requests.post(self.auto_url,json=jsonData)
