import requests
import json
from pprint import pprint


class usertest :
    def __init__(self,user_param) -> None:
        self.user_param = user_param

        #id creer leors de la methode create
        self.id = 0
        #jwt creer lors de la methode logn
        self.jwt = ""

        with open('params.json', 'r') as f:
            params = f.read()
        self.params = json.loads(params)
        self.url = self.params.get("url")

    def create(self,save=False):
        try:
            url = f"{self.url}api/register/"
        
            headers = {
            'Content-Type': 'application/json'
            }
            requests.packages.urllib3.disable_warnings()
            response = requests.request("POST", url, headers=headers, data=json.dumps(self.user_param, indent = 4), verify=False)
            responsedict = dict(response.json())
            if save:
                with open("responses/create_user.json" ,"w") as f:
                    json.dump(response.json(), f,indent = 4)
            else:
                with open("responses/create_user.json" ,"r") as f:
                    rep = json.load(f)

                # retrait de l'ID
                self.id = responsedict.get("id")
                rep.pop("id")     
                responsedict.pop("id")

                return f"TEST CREATE USER : {rep == responsedict}"
        except Exception:
            return f"TEST CREATE USER : {rep == responsedict}"


    
    def login(self):
        try:
            url = f"{self.url}api/login/"

            payload = json.dumps({
            "email": self.user_param.get("email"),
            "password": self.user_param.get("password")
            })

            headers = {
            'Content-Type': 'application/json'
            }

            requests.packages.urllib3.disable_warnings()
            response = requests.request("POST", url, headers=headers, data=payload, verify=False)
            responsedict = dict(response.json())
            self.jwt = responsedict.get("jwt")

            # retrait de l'ID
            if responsedict["message"] == "success" and "jwt" in responsedict.keys():
                return f"TEST LOGIN : {True}"
            return f"TEST LOGIN : {False}"
        except Exception:
            return f"TEST LOGIN : {False}"
    
    def userview(self):
        try:
            url = f"{self.url}api/user/"

            payload = json.dumps({
                "jwt":self.jwt
            })
            headers = {
            'Content-Type': 'application/json'
            }

            # retrait de l'ID et password
            user = self.user_param
            user.pop("password")

            requests.packages.urllib3.disable_warnings()
            response = requests.request("POST", url, headers=headers, data=payload, verify=False)
            responsedict = dict(response.json())
            responsedict.pop("id")

            # Obtenir les clés des deux dictionnaires
            keys1 = responsedict.keys()

            for key in keys1:
                if str(responsedict[key])==str(self.user_param[key]):
                    return f"TEST USERVIEW : {True}"
            return f"TEST USERVIEW : {False}"
        except Exception:
            return f"TEST USERVIEW : {False}"


    def deleteuser(self):
        try:
            url = f"{self.url}delete_user/{self.id}"

            payload = {}
            headers = {}

            response = requests.request("DELETE", url, headers=headers, data=payload, verify=False)
            if (response.text == "Le formulaire UsersForm a été update avec succès !"):
                    return f"TEST DELETE USER : {True}"
            return f"TEST DELETE USER : {False}"
        except Exception:
            return f"TEST DELETE USER : {False}"
        
if __name__ == "__main__":

    payload ={
        "username": "usertest",
        "first_name": "test",
        "last_name": "user",
        "email": "test-user@gmail.fr",
        "password": "testpassword",
        "is_admin": False,
        "street": "test street",
        "zipcode": "test zipcode",
        "city": "test city",
        "phone_number": "123456789",
        "contract_number": "789456"
        }
    
    usertest = usertest(payload)
    print(usertest.create())
    print(usertest.login())
    print(usertest.userview())
    print(usertest.deleteuser())

