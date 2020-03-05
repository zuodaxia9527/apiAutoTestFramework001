import requests

class TpshopLoginApi:
    def __init__(self):
        self.session = requests.session()
        self.verify_url = "http://localhost/index.php?m=Home&c=User&a=verify"
        self.login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"

    
    def get_verify(self,session):
        request_verify = session.get(self.verify_url)
        return request_verify

    def get_login(self,session,data):
        requests_login = session.post(self.login_url,
             data=data)
        return requests_login