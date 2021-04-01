import os
from selenium import webdriver
from time import sleep

def main():
    close = str()
    banner = """
__        __               _     _       ____    _     _   _         
\ \      / / ___    __ _  | |_  | |__   / ___|  | |_  (_) | |   ___  
 \ \ /\ / / / _ \  / _` | | __| | '_ \  \___ \  | __| | | | |  / _ \ 
  \ V  V / |  __/ | (_| | | |_  | | | |  ___) | | |_  | | | | | (_) |
   \_/\_/   \___|  \__,_|  \__| |_| |_| |____/   \__| |_| |_|  \___/ \n""" + "-"*59

    #tarayıcı oluşturup arka plana aldık
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--log-level=3')
        if(os.name == "nt"):
            dr = webdriver.Chrome("win/chromedriver.exe",options=options)
        else:
            dr = webdriver.Chrome("linux/chromedriver",options=options)
        
    except:
        print("'chromedriver' bulunamadı !")
        input("Kapatmak için bir tuşa basınız...")
        exit()
    
    while close.lower() != "q":
        os.system('cls' if os.name == 'nt' else 'clear') #terminali temizledik
        print(banner)
        city = input("İl : ")
        state = input("İlçe (varsayılan - merkez) : ")
        print("Yükleniyor...")
        url = f"https://mgm.gov.tr/?il={city}&ilce={state}"

        try:
            dr.get(url) #adrese gittik
            city, days = [],[[],[],[],[],[]]
            
            #verileri çektik
            city.append(dr.find_element_by_xpath('//*[@id="siteBody"]/section[1]/div/div[2]/div[2]/h3[1]/ziko').text) #sehir
            city.append(dr.find_element_by_xpath('//*[@id="siteBody"]/section[1]/div/div[2]/div[2]/h3[1]/span').text) #ilçe
            city.append(dr.find_element_by_xpath('//*[@id="siteBody"]/section[1]/div/div[2]/div[2]/p').text) #anlık zaman
            city.append(dr.find_element_by_xpath('//*[@id="siteBody"]/section[1]/div/div[2]/div[2]/div/h3/span[1]/ziko').text + "°C") #anlık sıcaklık
            city.append("% " + dr.find_element_by_xpath('//*[@id="siteBody"]/section[1]/div/div[2]/div[2]/div/h3/span[2]/div/span[3]/span[3]').text) #anlık nem
            city.append(dr.find_element_by_xpath('//*[@id="siteBody"]/section[1]/div/div[2]/div[2]/div/p').text) #anlık durum
            alert = dr.find_element_by_xpath('//*[@id="mainAlarm"]/a/div').text #uyarılar

            for i in range(1,6):
                days[i-1].append(dr.find_element_by_xpath(f'//*[@id="t{i}"]/div/div[1]/div[1]').text)
                days[i-1].append(dr.find_element_by_xpath(f'//*[@id="t{i}"]/div/div[1]/div[5]/span[1]').text + " - " + dr.find_element_by_xpath(f'//*[@id="t{i}"]/div/div[1]/div[4]/span[1]').text + "°C")
                dr.find_element_by_xpath(f'//*[@id="t{i}"]').click()
                sleep(0.1) #Diğer günlere tıkladıktan sonra biraz beklesin diye
                days[i-1].append("% " + dr.find_element_by_xpath(f'//*[@id="t{i}"]/div/div[2]/div[2]').text)
                days[i-1].append(dr.find_element_by_xpath(f'//*[@id="t{i}"]/div/div[1]/div[3]').text)

        except:
            print(f"\nBağlantı hatası!")
            dr.close()
            input("Kapatmak için bir tuşa basın...")
            break          

        #verileri ekrana yazdırdık
        os.system('cls' if os.name == 'nt' else 'clear')
        print(banner)
        print(f"Şehir : {city[0]} - {city[1]}\nGüncelleme Zamanı : {city[2]}\n" + "-"*59)
        print(f"""Günler    |  Sıcaklık  |   Nem   |          Durum         |
{"-"*59}
Şuan      |{city[3]:^12}|{city[4]:^9}|{city[5]:^24}|
{days[0][0]:<10}|{days[0][1]:^12}|{days[0][2]:^9}|{days[0][3]:^24}|
{days[1][0]:<10}|{days[1][1]:^12}|{days[1][2]:^9}|{days[1][3]:^24}|
{days[2][0]:<10}|{days[2][1]:^12}|{days[2][2]:^9}|{days[2][3]:^24}|
{days[3][0]:<10}|{days[3][1]:^12}|{days[3][2]:^9}|{days[3][3]:^24}|
{days[4][0]:<10}|{days[4][1]:^12}|{days[4][2]:^9}|{days[4][3]:^24}|

Uyarılar : {alert}""")

        close = input("\nÇıkmak için 'Q' veya 'q' tuşuna basınız:: ") #programdan çıkılsın mı diye sorduk

if __name__ == '__main__':
    main()
