#! /usr/bin/env python3

import os
import json
import sqlite3 as sql


print("""
      ___________________________________________________________________________________________________|
      Uyarı: Girdiğiniz Kullanıcı Adı Sitede Yoksa Eğer Aynı Kişiye Ait Başka Bir Kullanıcı Adı Deneyin! |
      ___________________________________________________________________________________________________|
      Araştırmak istediğiniz alanı seçin: |
      ___________________________________ |
      1)Genel Arama | General Search: 
      
      2)Veritabanında Kişi Ara | Search for People in the Database:

      """)

choise = int(input("BİR iŞLEM GİRİNİZ : "))
try:
      if choise == 1:
            from new import url
            print("Birinci Seçeneği seçtiniz.")

      elif choise == 2:
    
            def kisi():
                  if (True):        
                      data = sql.connect("users.db")
                      crsr = data.cursor()
                      name = input("Kullanıcı adı giriniz: ")
                      crsr.execute("SELECT * FROM users WHERE userName ")
                      find = crsr.fetchone()
                      print(name, "BULUNDU")
                  else:
                      print("Kullanıcı bulunamadı.")
            kisi()
except:
            
      print("Hata ile karşılaşıldı!")

