import requests,unittest

from api.tpshow_verify_code_get_api import TpshopLoginApi

class TestTpshowlogin(unittest.TestCase):
    def setUp(self) -> None:
        self.session = requests.session()
        self.login_api = TpshopLoginApi()

    def tearDown(self) -> None:
        self.session.close()

    def test01_case(self):
        requests_verify = self.login_api.get_verify(self.session)
        print("验证码接口返回响应头:",requests_verify.headers)
        self.assertEqual("image/png",requests_verify.headers.get("Content-Type"))

        requests_login = self.login_api.get_login(self.session,data={
                                                "username":"18285109703",
                                                "password":"123456",
                                                "verify_code":"8888"})

        jsonData = requests_login.json()#type:dict
        print("返回登录接口数据:",jsonData)
        self.assertEqual(200,requests_login.status_code)
        self.assertEqual(1,jsonData.get("status"))
        self.assertEqual("登陆成功",jsonData.get("msg"))

    def test_username_none(self):
        requests_verify = self.login_api.get_verify(self.session)
        print("验证码接口返回响应头:", requests_verify.headers)
        self.assertEqual("image/png", requests_verify.headers.get("Content-Type"))

        requests_login = self.login_api.get_login(self.session,
                                           data={"username": "18985109703",
                                                 "password": "123456",
                                                 "verify_code": "8888"})

        jsonData = requests_login.json()  # type:dict
        print("返回登录接口数据:", jsonData)
        self.assertEqual(200, requests_login.status_code)
        self.assertEqual(-1, jsonData.get("status"))
        self.assertIn("账号不存在", jsonData.get("msg"))
    def test_password_erorr(self):
        requests_verify = self.login_api.get_verify(self.session)
        print("验证码接口返回响应头:", requests_verify.headers)
        self.assertEqual("image/png", requests_verify.headers.get("Content-Type"))

        requests_login = self.login_api.get_login(self.session,
                                           data={"username": "18285109703",
                                                 "password": "1234567",
                                                 "verify_code": "8888"})

        jsonData = requests_login.json()  # type:dict
        print("返回登录接口数据:", jsonData)
        self.assertEqual(200, requests_login.status_code)
        self.assertEqual(-2, jsonData.get("status"))
        self.assertIn("密码错误", jsonData.get("msg"))