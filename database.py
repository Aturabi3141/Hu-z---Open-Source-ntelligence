import sqlite3 as sql

data = sql.connect("users.db")
crsr = data.cursor()

class database(): 

    def createTable():
        crsr.execute("CREATE TABLE IF NOT EXISTS users(username TEXT, usersurname TEXT, email TEXT, phonenumber int )")    
    def addTable():
        userName = input("İsim giriniz: ")
        userSurName = input("Soyad giriniz: ")
        userEmail = input("E-mail adres ekleyiniz: ")
        userPhoneNumber = int(input("Telefon numarası ekleyiniz: "))

        crsr.execute("INSERT INTO users(username, usersurname, email, phonenumber) VALUES (?,?,?,?)", (userName,userSurName,userEmail,userPhoneNumber))
        #crsr.execute("INSERT INTO users VALUES ('AYETULLAH TURABİ','KONUKLU','ayetullahturabi@gmail.com','05468464474')")
        
    print("Desteğiniz için teşekkür ederiz...")
    addTable()
   
    def listData():
        def kisi():
            if (True):        
                data = sql.connect("users.db")
                crsr = data.cursor()
                name = input("Kullanıcı adı giriniz: ")   
                crsr.execute("SELECT * FROM users WHERE userName ='{}' ".format(username))
                find = crsr.fetchone()
                print(find[1])
            else:
                print("Kullanıcı bulunamadı.")
        kisi.commit()
        kisi()
        kisi.close()
    

            
    
    

        