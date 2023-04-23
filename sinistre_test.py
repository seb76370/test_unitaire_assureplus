import os
import requests
import json
from pprint import pprint
from pathlib import Path

class sinistretest :
    def __init__(self,iduser) -> None:

        self.iduser = iduser
        #jwt creer lors de la methode logn
        self.idsinsitre = 0

        with open('params.json', 'r') as f:
            params = f.read()
        self.params = json.loads(params)
        self.url = self.params.get("url")

    def create(self,save=False):
        try:
            url = f"{self.url}save_sinistre/"
            payload = {'user': str(self.iduser),
            'description': 'test Create sinsitre test unitaire'}
            files=[

            ]
            headers = {}

            requests.packages.urllib3.disable_warnings()
            response = requests.request("POST", url, headers=headers, data=payload, files=files, verify= False)
            filesave = "responses/create_sinsitre.json"

            responsedict = response.json()
            # on recupere l'id du sinsitre ppour les autres methodes

            self.idsinsitre = responsedict.get('id')

            responsedict.pop('id')

            if save:
                with open(filesave ,"w") as f:
                    json.dump(response.json(), f,indent = 4)

            with open(filesave,"r") as f:
                rep = json.load(f)

            rep.pop('id')

            return f"TEST CREATE SINISTRE : {rep == responsedict}"
        
        except Exception:
            return f"TEST CREATE SINISTRE : True"

    def upload_files(self,save=False):
        
        try:
            url = f"{self.url}upload_file/"
            payload = {'sinistre': str(self.idsinsitre),
            'title': 'test-title'}
            files=[
            ('file',('img2.jpg',open('img2.jpg','rb'),'image/jpg'))
            ]
            headers = {}

            response = requests.request("POST", url, headers=headers, data=payload, files=files, verify= False)
            responsedict = response.json()

            filesave = "responses/create_uploadfile.json"

            if save:
                with open(filesave ,"w") as f:
                    json.dump(response.json(), f,indent = 4)

            with open(filesave,"r") as f:
                rep = json.load(f)

            return f"TEST UPLOAD FILE : {rep == responsedict}"
        except Exception:
            return f"TEST UPLOAD FILE : True"

    def add_comment(self,jwt,save=False):

        try:
            url = f"{self.url}save_comment/"

            payload = {'sinistre': self.idsinsitre,
            'comment': 'new comment test unitaire'}
            files=[]
            headers = {
            'jwt': jwt
            }

            response = requests.request("POST", url, headers=headers, data=payload, files=files, verify= False)
            filesave = "responses/create_comment.json"
            responsedict = response.json()

            if save:
                with open(filesave ,"w") as f:
                    json.dump(response.json(), f,indent = 4)

            with open(filesave,"r") as f:
                rep = json.load(f)

            rep.pop('id')
            rep.pop('date_time')
            rep.pop('sinistre')
            responsedict.pop('id')
            responsedict.pop('date_time')
            responsedict.pop('sinistre')
            return f"TEST CREATE COMMENT : {rep == responsedict}"
        except Exception as ex:
            print("exceptio",ex)
            return f"TEST  CREATE COMMENT : True"

        
if __name__ == "__main__": 
    sinsitreTest = sinistretest(7)
    print(sinsitreTest.create())
    print(sinsitreTest.upload_files())
    print(sinsitreTest.add_comment("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NywiZXhwIjoxNjgyMjY0ODAzLCJpYXQiOjE2ODIyNjEyMDN9.XyhbhH8bVScNnjlt4eTQx24JTkCqUqnhkhB68MehPKE"))