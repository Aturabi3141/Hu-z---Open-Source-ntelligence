from tkinter import *
import tkinter as tk
#from PIL import Image, ImageTk 

#from PIL import Image, ImageTk


master=Tk('Arayüz Tasarımı')

master.title('ara yüz')
canvas= Canvas(master, height=450, width=750)
canvas.pack()


  

  



frame_ust= Frame(master)
frame_ust.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.1)



frame_alt_sol= Frame(master, bg='#808080')
frame_alt_sol.place(relx=0.1,rely=0.21,relwidth=0.80,relheight=0.70)






baslık_etiket=Label(frame_ust,bg='black',text="HuIz",fg=('white'),font="Verdana 22 bold")
baslık_etiket.pack(padx=10,pady=10,side=LEFT)


giris=Label(frame_alt_sol,text="HuIz'e Hoşgeldiniz ",bg='#808080',font="Verdana 14 bold").pack(padx=10,pady=10,anchor=NW)
giris2=Label(frame_alt_sol,text="Lütfen Yapmak İstediğiniz İşlemi seçiniz",bg='#808080',font="Verdana 14 bold").pack(padx=10,pady=10,anchor=NW)










giris=tk.Label(frame_alt_sol, text='Girdiğiniz İşlem')
giris.pack(padx=20,pady=30,anchor=NW)

giris3=Label(frame_alt_sol,text="1-) Genaral Engine araması",bg='#808080',font="Verdana 14 bold").pack(padx=10,pady=10,anchor=NW)



giris7=Label(frame_alt_sol,text="2-)Veri Tabanında Kişi Arat ",bg='#808080',font="Verdana 14 bold").pack(padx=10,pady=10,anchor=NW)



giris=tk.Entry(bg='black',fg='white')
giris.place(x =200,y=300)


def verial():
    giris['text']=giris.get()

buton=tk.Button(frame_alt_sol, text='verial',command=verial)
buton.pack(pady=10,padx=20,anchor=NW)






master.mainloop()
