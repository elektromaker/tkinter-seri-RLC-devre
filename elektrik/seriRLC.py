import tkinter as tk
from tkinter import ttk
import math
import seri_RLC as seri

pencere=tk.Tk()
pencere.title("Seri RLC Devresi Hesaplamaları")
pencere.geometry("500x300")
pencere.minsize(500, 300)
pencere.maxsize(500, 300)
background_img = tk.PhotoImage(file=f"Frame 2.png")
buton_img = tk.PhotoImage(file=f"buton 2.png")
resim =ttk.Label(pencere, image=background_img, background='black')
resim.place(x=0, y=0, relwidth=1, relheight=1)

def hesapla():
    R = float(R_giris.get())
    L = float(L_giris.get())
    C = float(C_giris.get())
    f = float(f_giris.get())
    V = float(V_giris.get())
    EnduktifReaktans = seri.SeriRLC.enduktifReaktans(f, L)
    KapasitifReaktans = seri.SeriRLC.kapasitifReaktans(f,C)
    Empedans = math.sqrt(R**2 + (KapasitifReaktans-EnduktifReaktans)**2)
    Akim = (V/Empedans)*1000
    rGerilim = (Akim/1000)*R
    lGerilim = (Akim/1000)*EnduktifReaktans
    cGerilim = (Akim/1000)*KapasitifReaktans
    fazAcisi = math.degrees(math.atan((KapasitifReaktans-EnduktifReaktans)/R))

    XL = tk.Label(bg="white", bd=0)
    XL.place(x=254, y=37)
    Xc = tk.Label(bg="white", bd=0)
    Xc.place(x=254, y=69)
    Z = tk.Label(bg="white", bd=0)
    Z.place(x=254, y=95)
    I = tk.Label(bg="white", bd=0)
    I.place(x=254, y=124)
    VR = tk.Label(bg="white", bd=0)
    VR.place(x=254, y=153)
    VL = tk.Label(bg="white", bd=0)
    VL.place(x=254, y=182)
    Vc = tk.Label(bg="white", bd=0)
    Vc.place(x=254, y=211)
    aci = tk.Label(bg="white", bd=0)
    aci.place(x=254, y=241)

    XL.config(text="XL = "+ str(EnduktifReaktans)[:5] + " ohm")
    Xc.config(text="Xc = " + str(KapasitifReaktans)[:5] + " ohm")
    Z.config(text="Z = "+ str(Empedans)[:5] + " ohm")
    I.config(text="I = "+ str(Akim)[:5] + " mA")
    VR.config(text="VR = " + str(rGerilim)[:5] + " Volt")
    VL.config(text="VL = " + str(lGerilim)[:5] + " Volt")
    Vc.config(text="Vc = " + str(cGerilim)[:5] + " Volt")
    aci.config(text="θ = " + str(fazAcisi)[:5] + " °")
#değer girişi
R_giris=tk.Entry(bg='white',bd=0)
R_giris.place(x=62,y=42,width=50)
L_giris=tk.Entry(bg='white',bd=0)
L_giris.place(x=62,y=69,width=50)
C_giris=tk.Entry(bg='white',bd=0)
C_giris.place(x=62,y=98,width=50)
f_giris=tk.Entry(bg='white',bd=0)
f_giris.place(x=62,y=127,width=50)
V_giris=tk.Entry(bg='white',bd=0)
V_giris.place(x=62,y=156,width=50)
#buton
btn1=tk.Button(text="HESAPLA",command=hesapla, image=buton_img, bd=0,bg="#D9D9D9",activebackground="#D9D9D9")
btn1.place(x=44,y=199)
#çalıştır
pencere.mainloop()