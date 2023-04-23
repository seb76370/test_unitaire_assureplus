import sys
from sinistre_test import sinistretest
from user_test import usertest
from colorama import init, Fore, Back, Style
from test_fonctionnel import open_chrome
test =True
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

userTest = usertest(payload)
iduser = ""
jwt = ""
listtestuser = [
    userTest.create(),
    userTest.login(),
    userTest.userview(),
    # usertest.deleteuser()
]

print(Fore.GREEN + "#"*30)
print(Fore.GREEN + "DEBUT DES TEST ASSUREPLUS")
print(Fore.GREEN + "#"*30)


for test in listtestuser:
    if "False" in test:
        print(Fore.RED + test)
        test = False
    else:
        print(Fore.YELLOW + test)

iduser = userTest.id
jwt = userTest.jwt

sinsitreTest = sinistretest(iduser)

listtestsinistre = [
    sinsitreTest.create(),
    sinsitreTest.upload_files(),
    sinsitreTest.add_comment(jwt),
]

for test in listtestsinistre:
    if "False" in test:
        print(Fore.RED + test)
        test = False
    else:
        print(Fore.YELLOW + test)


print(Fore.YELLOW + userTest.deleteuser())

if test:
    print(Fore.BLUE + "#"*30)
    print(Fore.BLUE + "FIN DE TEST : SUCESS")
    print(Fore.BLUE + "#"*30)
else:
    print(Fore.RED + "#"*30)
    print(Fore.RED + "FIN DE TEST : FAIL")
    print(Fore.RED + "#"*30)
