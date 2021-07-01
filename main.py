import os
from selenium import webdriver
from time import sleep
import chromedriver_autoinstaller

drVer = str(chromedriver_autoinstaller.get_chrome_version())
drVer = drVer[0:drVer.index(".")]

banner = """
__        __               _     _       ____    _     _   _         
\ \      / / ___    __ _  | |_  | |__   / ___|  | |_  (_) | |   ___  
 \ \ /\ / / / _ \  / _` | | __| | '_ \  \___ \  | __| | | | |  / _ \ 
  \ V  V / |  __/ | (_| | | |_  | | | |  ___) | | |_  | | | | | (_) |
   \_/\_/   \___|  \__,_|  \__| |_| |_| |____/   \__| |_| |_|  \___/
----------------------------------------------------------------"""

def printBanner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(banner)

def printData(city,days,alert):
    printBanner()

    print(f"""Şehir : {city[0]} - {'Merkez' if city[1] == '' else city[1]}
Güncelleme Zamanı : {city[2]}
----------------------------------------------------------------
Günler    |  Sıcaklık  |   Nem   |             Durum            |
----------------------------------------------------------------
Şuan      |{city[3]:^12}|{city[4]:^9}|{city[5]:^30}|
{days[0][0]:<10}|{days[0][1]:^12}|{days[0][2]:^9}|{days[0][3]:^30}|
{days[1][0]:<10}|{days[1][1]:^12}|{days[1][2]:^9}|{days[1][3]:^30}|
{days[2][0]:<10}|{days[2][1]:^12}|{days[2][2]:^9}|{days[2][3]:^30}|
{days[3][0]:<10}|{days[3][1]:^12}|{days[3][2]:^9}|{days[3][3]:^30}|
{days[4][0]:<10}|{days[4][1]:^12}|{days[4][2]:^9}|{days[4][3]:^30}|
----------------------------------------------------------------

Uyarılar : {alert}""")

def main():
    close = str()
    
    #tarayıcı oluşturup arka plana aldık
    try:
        chromedriver_autoinstaller.install("./")
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--log-level=3')
        if(os.name == "nt"):
            dr = webdriver.Chrome(f'./{drVer}/chromedriver.exe',options=options)
        else:
            dr = webdriver.Chrome(f'./{drVer}/chromedriver',options=options)
        
    except:
        print("'chromedriver' bulunamadı veya güncel değil. Internet bağlantınızı kontrol edin !")
        input("Kapatmak için 'enter'a basınız...")
        exit()
    
    while close.lower() != "q":
        printBanner()
        cityn = input("İl : ")
        state = input("İlçe (varsayılan - merkez) : ")
        print("Yükleniyor...")
        url = f"https://mgm.gov.tr/?il={cityn}&ilce={state}"

        try:
            dr.get(url) #adrese gittik
            city, days = [],[[],[],[],[],[]]
            sleep(0.1)

            #verileri çektik
            city.append(dr.find_element_by_xpath('//*[@id="siteBody"]/section[1]/div/div[2]/div[2]/h3[1]/ziko').text) #sehir
            city.append(dr.find_element_by_xpath('//*[@id="siteBody"]/section[1]/div/div[2]/div[2]/h3[1]/span').text) #ilçe
            city.append(dr.find_element_by_xpath('//*[@id="siteBody"]/section[1]/div/div[2]/div[2]/p').text) #anlık zaman
            city.append(dr.find_element_by_xpath('//*[@id="siteBody"]/section[1]/div/div[2]/div[2]/div/h3/span[1]/ziko').text + "°C") #anlık sıcaklık
            city.append("% " + dr.find_element_by_xpath('//*[@id="siteBody"]/section[1]/div/div[2]/div[2]/div/h3/span[2]/div/span[3]/span[3]').text) #anlık nem
            city.append(dr.find_element_by_xpath('//*[@id="siteBody"]/section[1]/div/div[2]/div[2]/div/p').text) #anlık durum

            #diğer günlerin bilgilerini çektik
            for i in range(1,6):
                days[i-1].append(dr.find_element_by_xpath(f'//*[@id="t{i}"]/div/div[1]/div[1]').text) #tarih bilgisi
                days[i-1].append(dr.find_element_by_xpath(f'//*[@id="t{i}"]/div/div[1]/div[4]/span[1]').text + " - " + dr.find_element_by_xpath(f'//*[@id="t{i}"]/div/div[1]/div[5]/span[1]').text + "°C") #sıcaklık
                dr.find_element_by_xpath(f'//*[@id="t{i}"]').click() #diğer günlerin penceresini açtık
                sleep(0.1) #Diğer günlere tıkladıktan sonra biraz beklesin diye
                days[i-1].append("% " + dr.find_element_by_xpath(f'//*[@id="t{i}"]/div/div[2]/div[2]').text) #nem
                days[i-1].append(dr.find_element_by_xpath(f'//*[@id="t{i}"]/div/div[1]/div[3]').text) #durum

            alert = dr.find_element_by_xpath('//*[@id="mainAlarm"]/a/div').text #uyarılar

        except:
            print("\nBağlantı hatası!")
            input("Kapatmak için bir tuşa basın...")
            exit()          

        printData(city,days,alert) #bilgileri ekrana yazdırdık

        close = input("\nÇıkmak için 'Q' giriniz :: ")

if __name__ == '__main__':
    main()