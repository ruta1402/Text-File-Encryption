import encryptFile
import decryptFile
import generateAKey

username="b.ghanchi"
password="b.ghanchi"


def login():
    user=input("\nUsername : ")
    passw=input("Password : ")
    
    if user==username and passw==password:
        return 1
    else:
        return 0

def main():
    while (True):
        choice=int(input("1. Login\n0. Exit\n\tEnter choice - "))
        if choice==1:
            if login():
                generateAKey.gen_key()
                encryptFile.encryp()
                decryptFile.decryp()
            else:
                print("\nInvalid login")
                continue
        elif choice==0:
            print("Thank you!")
            break

if __name__=="__main__":
    main()
        
