import tkinter as tk
import requests
import os
import json
from tkinter import ttk
from tkinter import messagebox

os.system("copy main.py main.py.1bak")
os.system("copy main.py.1bak main.py.2bak")
os.system("copy main.py.2bak main.py.3bak")

launcher = tk.Tk()
launcher.title("XCEN Uygulamaları Başlatıcısı [XCEN App Launcher Stable]")
launcher.geometry("1000x600")
launcher.configure(bg="#1C1C1C")
launcher.iconbitmap("AppIcon.ico")
launcher.resizable(False,False)

DEF_KEDIT_SETUPURL = "https://filesxcenapplauncherxcenbykilic.netlify.app/KEDIT/KEDIT Setup.exe"
DEF_KEDIT_RUNFILES = "C:\\Program Files\\KEDIT\\kedit.exe"
DEF_KEDIT_UNINSTAL = "C:\\Program Files\\KEDIT\\unins000.exe"
DEF_KEDIT_DATFILES = "C:\\Program Files\\KEDIT\\unins000.dat"

DEF_BASE96_DEVELOPER = "base96.exe"
DEF_BASE96_URL = "https://filesxcenapplauncherxcenbykilic.netlify.app/Base96_Files/base96.exe"
DEF_BASE96_DECODER_DEVELOPER = "base96_decoder.exe"
DEF_BASE96_DECODER_URL = "filesxcenapplauncherxcenbykilic.netlify.app/Base96_Files/base96_decoder.exe"


def UnInstall(UnInstallAppName):
    veri = json_kontrol_ve_oku()
    veri[UnInstallAppName+"_is_installed"] = False
    os.system(f"del {UnInstallAppName}"+".exe")
    json_yaz(veri)

def UnInstallSc(UnInstallAppEXEName,UnInstallAppJsonName):
    veri = json_kontrol_ve_oku()
    veri[f"{UnInstallAppJsonName}"] = False
    os.system(f"del {UnInstallAppEXEName}")
    json_yaz(veri)

class ModMotoru:
    def __init__(self):
        self.buton_golegeleri = {}
        self.kayitli_modlar = {} 

    def __getattr__(self, isim):
        if isim not in self.buton_golegeleri:
            self.buton_golegeleri[isim] = ErtelenenButon()
        return self.buton_golegeleri[isim]

    def olusturmadeficindemi(self, durum, defadi, buton):
        if durum == True:
            fonksiyon_ismi = defadi.__name__
            if fonksiyon_ismi not in self.kayitli_modlar:
                self.kayitli_modlar[fonksiyon_ismi] = []
            self.kayitli_modlar[fonksiyon_ismi].append(buton)

    def tetikle(self, fonksiyon_ismi):
        if fonksiyon_ismi in self.kayitli_modlar:
            for buton in self.kayitli_modlar[fonksiyon_ismi]:
                buton.simdi_gercekten_olustur(root)

mod_motoru = ModMotoru()

def modlari_otomatik_tara_ve_oynat():
    klasor = "plugins"
    if not os.path.exists(klasor):
        os.makedirs(klasor)
        return

    ana_kod_ortami = globals()
    
    for dosya_adi in os.listdir(klasor):
        if dosya_adi.endswith(".mod"):
            dosya_yolu = os.path.join(klasor, dosya_adi)
            
            # Mod dosyası çalışırken 'mod' kelimesini doğrudan tanısın diye ortam hazırlıyoruz
            tekil_mod_ortami = ana_kod_ortami.copy()
            tekil_mod_ortami["mod"] = mod_motoru

            try:
                with open(dosya_yolu, "r", encoding="utf-8") as f:
                    exec(f.read(), tekil_mod_ortami)
                print(f"[BAŞARILI] '{dosya_adi}' otomatik yüklendi.")
            except Exception as e:
                print(f"[HATA] '{dosya_adi}' yüklenirken hata: {e}")         

def addbase96():
    global installbase96, installbase96decoder
    
    installbase96 = ttk.Button(text="Base96 (Şifreleyici) Kur")
    installbase96.configure(command=lambda: ınstallapp_6(installbase96))
    installbase96.place(x=10, y=200, width=170, height=100)
    
    installbase96decoder = ttk.Button(text="Base96 (Çözücü) Kur")
    installbase96decoder.configure(command=lambda: ınstallapp_7(installbase96decoder))
    installbase96decoder.place(x=190, y=200, width=170, height=100)

    
def backcommand():
    launcher.destroy()
    os.system("g")

def settingsmenu():
    def AboutMenu_SETTINGSMENU():
        def openweb_ABOUTMENU():
            os.system("start https://z7752ht0-9003.euw.devtunnels.ms/about.html")

        def closeabouttab():
            abouttext.destroy()
            openwebsite.destroy()
            closeabout.destroy()

        abouttext = ttk.Label(text="XCEN Launcher Projesi 2026 'Kılıçarslan Tiftik Tarafından Yapıldı'. (XCEN Launcher Project 2026 Created by Kılıçarslan Tiftik) \n Yapımcılar: \n Kılıçarslan \n XCEN Developers \n \n Eksta Linkler: \n youtube.com/@XCENDevelopers \n github.com/XCEN-Developers \n xcen-developers.github.io/XCEN-Web-Site",background="#1C1C1C",font="Verdana 9 bold")
        abouttext.place(x=100,y=50)

        openwebsite = ttk.Button(text="Siteyi Aç (Hakkında Sayfası)",command=openweb_ABOUTMENU)
        openwebsite.place(x=780,y=150)

        closeabout = ttk.Button(text="Kapat",command=closeabouttab)
        closeabout.place(x=700,y=150)
        
    def activatedevelop():
        dev_title = ttk.Label(text="XCEN Developers Mode", background="#1C1C1C", font="Verdana 10 bold", foreground="#FFD700")
        dev_title.place(x=100, y=50)

        key_entry = ttk.Entry(font="Verdana 10")
        key_entry.insert(0, "ANAHTAR YAZ...")
        key_entry.place(x=100, y=100, width=150)

        def clear_placeholder(event):
            if key_entry.get() == "ANAHTAR YAZ...":
                key_entry.delete(0, tk.END)
        def add_placeholder(event):
            if key_entry.get() == "":
                key_entry.insert(0, "ANAHTAR YAZ...")
            
        key_entry.bind("<FocusIn>", clear_placeholder)
        key_entry.bind("<FocusOut>", add_placeholder)

        def aktıve_et():
            girilen_anahtar = key_entry.get()
            if girilen_anahtar == "2X0C2E6N":
                veri = json_kontrol_ve_oku()
                veri["Developer_Mode"] = True
                json_yaz(veri)
                messagebox.showinfo("XCEN Developers", "Geliştirici Modu Başarıyla Aktif Edildi!\n - Base96 Araçları Açıldı. \n - Yeniden Başlatmanız Gerekli")
                
                evethayir = messagebox.askyesno("XCEN Developers", "Yeniden Başlatıcakmısınız?")
                
                if evethayir:
                    backcommand()
                else:
                    pass
            else:
                messagebox.showerror("Hata", "Geçersiz Geliştirici Anahtarı!")

        activate_btn = ttk.Button(text="Aktive Et", command=aktıve_et)
        activate_btn.place(x=300, y=100, width=100)

    def additionsadder():
        def light_mode_activate():
            os.system("cd plugins & ren lightmode.demod lightmode.mod")
            
        def light_mode_deactivate():
            os.system("cd plugins & ren lightmode.mod lightmode.demod")
            
        def red_mode_activate():
            os.system("cd plugins & ren redmode.demod redmode.mod")

        def red_mode_deactivate():
            os.system("cd plugins & ren redmode.mod redmode.demod")

        def blue_mode_activate():
            os.system("cd plugins & ren bluemode.demod bluemode.mod")

        def blue_mode_deactivate():
            os.system("cd plugins & ren bluemode.mod bluemode.demod")
            
        from pathlib import Path
        dosya_adlari = [f.name for f in Path('plugins').glob('*.mod')]

        for ad in dosya_adlari:
            if ad == "lightmode.mod":
                hedef_dosya = ad

                lightmodeaddition = ttk.Button(text="Beyaz Mod Eklentisi \nGeliştirici:XCEN Developers \nKaldırmak İçin Tıkla",command=light_mode_deactivate)
                lightmodeaddition.place(x=110, y=50, width=190, height=100)
                break
        else:
            lightmodeaddition = ttk.Button(text="Beyaz Mod Eklentisi \nGeliştirici:XCEN Developers \nKurmak İçin Tıkla",command=light_mode_activate)
            lightmodeaddition.place(x=110, y=50, width=190, height=100)
        
        for ad in dosya_adlari:
            if ad == "redmode.mod":
                hedef_dosya = ad

                redmodeaddition = ttk.Button(text="Kırmızı Mod Eklentisi \nGeliştirici:XCEN Developers \nKaldırmak İçin Tıkla",command=red_mode_deactivate)
                redmodeaddition.place(x=320, y=50, width=240, height=100)
                break
        else:
            redmodeaddition = ttk.Button(text="Kırmızı Mod Eklentisi \nGeliştirici:XCEN Developers \nKurmak İçin Tıkla",command=red_mode_activate)
            redmodeaddition.place(x=320, y=50, width=190, height=100)

        for ad in dosya_adlari:
            if ad == "bluemode.mod":
                hedef_dosya = ad

                bluemodeaddition = ttk.Button(text="Mavi Mod Eklentisi \nGeliştirici:XCEN Developers \nKaldırmak İçin Tıkla",command=blue_mode_deactivate)
                bluemodeaddition.place(x=530, y=50, width=190, height=100)
                break
        else:
            bluemodeaddition = ttk.Button(text="Mavi Mod Eklentisi \nGeliştirici:XCEN Developers \nKurmak İçin Tıkla",command=blue_mode_activate)
            bluemodeaddition.place(x=530, y=50, width=190, height=100)

    def noadded():
        messagebox.showinfo("XCEN Uygulama Başlatıcısı [XCEN App Launcher Stable]","Malesef Daha Kodlamadım Ama Kodlamayı Deniyiceğim")
        
    ınstallpytorrent.destroy()
    ınstallpysap.destroy()
    ınstallaternossh.destroy()
    ınstallkilicwatch.destroy()
    uninstallappmenu.destroy()
    ınstallkedit.destroy()
    settingsmenubtn.destroy()

    aboutbtn = ttk.Button(text="Hakkında",command=AboutMenu_SETTINGSMENU)
    aboutbtn.place(x=10,y=50)

    laungagebtn = ttk.Button(text="Dil",command=noadded)
    laungagebtn.place(x=10,y=100)
    
    developerbtn = ttk.Button(text="Geliştirici Modu",command=activatedevelop)
    developerbtn.place(x=10,y=150)
    
    additionsbtn = ttk.Button(text="Eklentiler",command=additionsadder)
    additionsbtn.place(x=10,y=200)
    
    backbtn = ttk.Button(text="<-- Geri",command=backcommand)
    backbtn.place(x=850, y=500)

def uninstallermenu():
    def uninstallkedit():
        veri["kdt_is_installed"] = False
        os.system(f'"{DEF_KEDIT_UNINSTAL}"')

    ınstallpytorrent.destroy()
    ınstallpysap.destroy()
    ınstallaternossh.destroy()
    ınstallkilicwatch.destroy()
    ınstallkedit.destroy()
    uninstallappmenu.destroy()
    installbase96.destroy()
    installbase96decoder.destroy()

    veri = json_kontrol_ve_oku()

    if veri.get("pysap_is_installed", False):
        pysap_durum = "normal"
    else:
        pysap_durum = "disabled"

    uninstallpysap = ttk.Button(text="PySap (UnStable) Kaldır",command=lambda: UnInstall("pysap"),state=pysap_durum)
    uninstallpysap.place(x=10, y=50, width=150, height=100)

    if veri.get("kdt_is_installed", False):
        kedit_durum = "normal"
    else:
        kedit_durum = "disable"
    
    if veri.get("pytorrent_is_installed", False):
        pytorrent_durum = "normal"
    else:
        pytorrent_durum = "disabled"

    if veri.get("aternossh_is_installed", False):
        aternossh_durum = "normal"
    else:
        aternossh_durum = "disable"

    uninstallpytorrent = ttk.Button(text="PyTorrent (LowStable) Kaldır",command=lambda:UnInstall("pytorrent"),state=pytorrent_durum)
    uninstallpytorrent.place(x=190, y=50, width=160, height=100)

    if veri.get("kv_is_installed"):
        kv_durum = "normal"
    else:
        kv_durum = "disable"
    
    uninstallaternossh = ttk.Button(text="Aternos Kısayoları (UnStable) Kaldır",command=lambda:UnInstallSc("AternosKısayoları.exe","aternossh_is_installed"),state=aternossh_durum)
    uninstallaternossh.place(x=370, y=50,width=200,height=100)

    uninstallkv = ttk.Button(text="Kılıc Watch (Stable) Kaldır",command=lambda:UnInstallSc("KılıcWatchv0.py","kv_is_installed"),state=kv_durum)
    uninstallkv.place(x=590,y=50,width=200,height=100)

    uninstallkedt = ttk.Button(text="KEDIT (ULTRA STABLE) Kaldır",command=uninstallkedit,state=kedit_durum)
    uninstallkedt.place(x=810,y=50,width=200,height=100)

    backbutton = ttk.Button(text="<-- Geri", command=backcommand)
    backbutton.place(x=850, y=500)
        
def json_kontrol_ve_oku():
    dosya_adi = "installed_apps.json"
    if not os.path.exists(dosya_adi):
        varsayilan = {"pysap_is_installed": False, "pytorrent_is_installed": False, "aternossh_is_installed": False,"kv_is_installed": False, "kdt_is_installed":"False","Developer_Mode":False,"base96_is_installed":False,"base96_decoder_is_installed":False}
        with open(dosya_adi, "w", encoding="utf-8") as f:
            json.dump(varsayilan, f, indent=4)
        return varsayilan
    
    with open(dosya_adi, "r", encoding="utf-8") as AppsJson:
        return json.load(AppsJson)

def json_yaz(veri):
    with open("installed_apps.json", "w", encoding="utf-8") as dosya:
        json.dump(veri, dosya, ensure_ascii=False, indent=4)

def get_developer_mode():
    veri = json_kontrol_ve_oku()
    if veri["Developer_Mode"]:
        addbase96()
    else:
        pass
      
def ınstallapp_1():
    def startapp_1():
        os.system("start PySap.exe")
        
    response = requests.get("https://filesxcenapplauncherxcenbykilic.netlify.app/PySap/PySap.exe")

    with open("PySap.exe", "wb") as PySapInstall:
        PySapInstall.write(response.content)

    veri = json_kontrol_ve_oku()
    veri["pysap_is_installed"] = True 
    json_yaz(veri)

    if veri["pysap_is_installed"]:
        ınstallpysap.configure(text="Başlat", command=startapp_1)
    
def ınstallapp_2():
    def startapp2():
        os.system("start PyTorrent.exe")

    response2 = requests.get("https://filesxcenapplauncherxcenbykilic.netlify.app/PyTorrent/PyTorrent.exe")

    with open("PyTorrent.exe", "wb") as PyTorrentInstall:
        PyTorrentInstall.write(response2.content)

    veri = json_kontrol_ve_oku()
    veri["pytorrent_is_installed"] = True 
    json_yaz(veri)

    if veri["pytorrent_is_installed"]:
        ınstallpytorrent.configure(text="Başlat", command=startapp2)

def ınstallapp_3():
    def startapp3():
        os.system("start AternosKısayoları.exe")
    response3 = requests.get("https://filesxcenapplauncherbykilic.netlify.app/Shortcuts/aternos kısayoları.exe")

    with open("AternosKısayoları.exe", "wb") as AternosInstall:
        AternosInstall.write(response3.content)

    veri = json_kontrol_ve_oku()
    veri["aternossh_is_installed"] = True 
    json_yaz(veri)

    if veri["aternossh_is_installed"]:
        ınstallaternossh.configure(text="Başlat", command=startapp3)

def ınstallapp_4():
    def startapp3():
        os.system("venv\\Scripts\\py.exe kılıcWatchv0.py")
    response4 = requests.get("https://filesxcenapplauncherxcenbykilic.netlify.app/KılıcWATCH/kılıcWatchv0.py")

    with open("KılıcWatchv0.py", "wb") as KVInstall:
        KVInstall.write(response4.content)

    veri = json_kontrol_ve_oku()
    veri["kv_is_installed"] = True
    json_yaz(veri)

    if veri["kv_is_installed"]:
        ınstallkilicwatch.configure(text="Başlat", command=startapp3)

def ınstallapp_5():
    def startapp5():
        os.system(f"start {DEF_KEDIT_RUNFILES}")
    response4 = requests.get(DEF_KEDIT_SETUPURL)

    with open ("KEDIT_Setup_TEMP.exe", "wb") as KEDITInstall:
        KEDITInstall.write(response4.content)
    os.system("start KEDIT_Setup_TEMP.exe")

    veri = json_kontrol_ve_oku()
    veri["kdt_is_installed"] = True
    json_yaz(veri)

    if veri["kdt_is_installed"]:
        ınstallkedit.configure(text="Başlat", command=startapp5)

def ınstallapp_6(btn):
    global installbase96
    def startapp6():
        os.system(f"start cmd /c '{DEF_BASE96_DEVELOPER}' ")
    response4 = requests.get(DEF_BASE96_URL)

    with open ("base96.exe", "wb") as INSTALLBase96_Developer:
        INSTALLBase96_Developer.write(response4.content)

    veri = json_kontrol_ve_oku()
    veri["base96_is_installed"] = True
    json_yaz(veri)
    if btn:
        btn.configure(text="Başlat (Terminal Uygulaması)", command=startapp6)

def ınstallapp_7(btn):
    global installbase96decoder
    def startapp5():
        os.system(f"start cmd /c '{DEF_BASE96_DECODER_DEVELOPER}' ")
    response4 = requests.get(DEF_BASE96_DECODER_URL)

    with open ("base96_decoder.exe", "wb") as INSTALLBase96_Developer:
        INSTALLBase96_Developer.write(response4.content)

    veri = json_kontrol_ve_oku()
    veri["base96_decoder_is_installed"] = True
    json_yaz(veri)

    if btn:
        btn.configure(text="Başlat (Terminal Uygulaması)", command=startapp6)
    
settingsmenubtn = ttk.Button(text="Ayarlar",command=settingsmenu)
settingsmenubtn.place(x=10,y=10)

uninstallappmenu = ttk.Button(text="Uygulama Kaldır",command=uninstallermenu)
uninstallappmenu.place(x=900,y=10)

ınstallertext = ttk.Label(text="XCEN Uygulamaları Başlatıcısı", background="#1C1C1C", font="Verdana 20 bold")
ınstallertext.place(x=300, y=10)

ınstallpysap = ttk.Button(text="PySap (UnStable) Kur", command=ınstallapp_1)
ınstallpysap.place(x=10, y=50, height=100, width=150)

ınstallpytorrent = ttk.Button(text="PyTorrent (LowStable) Kur", command=ınstallapp_2)
ınstallpytorrent.place(x=190, y=50, height=100, width=150)

ınstallaternossh = ttk.Button(text="Aternos Kısayoları (UnStable) Kur",command=ınstallapp_3)
ınstallaternossh.place(x=370, y=50,width=190,height=100)

ınstallkilicwatch = ttk.Button(text="Kılıc Watch (Stable) Kur",command=ınstallapp_4)
ınstallkilicwatch.place(x=590,y=50,width=190,height=100)

ınstallkedit = ttk.Button(text="KEDIT (ULTRA STABLE) Kur",command=ınstallapp_5)
ınstallkedit.place(x=810,y=50,width=190,height=100)

get_developer_mode()
modlari_otomatik_tara_ve_oynat()

try:
    mevcut_veri = json_kontrol_ve_oku()
    if mevcut_veri.get("pysap_is_installed"):
        ınstallpysap.configure(text="Başlat", command=lambda: os.system("start PySap.exe"))
    if mevcut_veri.get("pytorrent_is_installed"):
        ınstallpytorrent.configure(text="Başlat", command=lambda: os.system("start PyTorrent.exe"))
    if mevcut_veri.get("aternossh_is_installed"):
        ınstallaternossh.configure(text="Başlat", command=lambda: os.system("start AternosKısayoları.exe"))
    if mevcut_veri.get("kv_is_installed"):
        ınstallkilicwatch.configure(text="Başlat", command=lambda: os.system("start venv\\Scripts\\py.exe kılıcWatchv0.py"))
    if mevcut_veri.get("kdt_is_installed"):
        ınstallkedit.configure(text="Başlat", command=lambda: os.system(f'"{DEF_KEDIT_RUNFILES}"'))
    if mevcut_veri.get("base96_is_installed") and 'installbase96' in globals() and installbase96:
        installbase96.configure(text="Başlat (Terminal Uygulaması)", command=lambda: os.system(f"start cmd /c '{DEF_BASE96_DEVELOPER}' "))
    if mevcut_veri.get("base96_decoder_is_installed") and 'installbase96decoder' in globals() and installbase96decoder:
        installbase96decoder.configure(text="Başlat (Terminal Uygulaması) ", command=lambda: os.system(f"start cmd /c '{DEF_BASE96_DECODER_DEVELOPER}' "))
except Exception as e:
    if MemoryError:
        print("FATAL MEMORY ERROR:"+str(e))
    elif NameError:
        print("FATAL MAIN ERROR:"+str(e))
    elif ImportError:
        messagebox.showerror("XCEN Import Error","Cannot Import Module:"+str(e))
    else:
        print("FATAL:"+str(e))

launcher.mainloop()