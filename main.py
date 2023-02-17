import encryptFile
import decryptFile
import generateAKey

username="b.ghanchi"
password="b.ghanchi"


def login():
    user=input("Username : ")
    passw=input("Password : ")
    
    if user==username and passw==password:
        return 1
    else:
        return 0

def main():
    while (True):
        choice=int(input("1. Login\n0. Exit\n"))
        if choice==1:
            if login():
                print("Successful login")
                generateAKey.gen_key()
                encryptFile.encryp()
                decryptFile.decryp()
            else:
                print("Login again")
                continue
        elif choice==0:
            print("Thank you")
            break

if __name__=="__main__":
    main()
        
