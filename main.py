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
        \_/\_/   \___|  \__,_|  \__| |_| |_| |____/   \__| |_| |_|  \___/ 
\n""" + "-"*80 + "\nKaynak : https://mgm.gov.tr/"

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
        state = input("İlçe (varsayılan = merkez) : ")
        print("Yükleniyor...",end="")
        url = f"https://mgm.gov.tr/?il={city}&ilce={state}"

        try:
            #adrese gittik
            dr.get(url)
            
            #verileri çektik
            state = dr.find_element_by_xpath('//*[@id="siteBody"]/section[1]/div/div[2]/div[2]/h3[1]/span').text
            city = dr.find_element_by_xpath('//*[@id="siteBody"]/section[1]/div/div[2]/div[2]/h3[1]/ziko').text
            nTime = dr.find_element_by_xpath('//*[@id="siteBody"]/section[1]/div/div[2]/div[2]/p').text
            nT = dr.find_element_by_xpath('//*[@id="siteBody"]/section[1]/div/div[2]/div[2]/div/h3/span[1]/ziko').text + "°C"
            nH = "% " + dr.find_element_by_xpath('//*[@id="siteBody"]/section[1]/div/div[2]/div[2]/div/h3/span[2]/div/span[3]/span[3]').text
            nS = dr.find_element_by_xpath('//*[@id="siteBody"]/section[1]/div/div[2]/div[2]/div/p').text
            nI = dr.find_element_by_xpath('//*[@id="mainAlarm"]/a/div').text
            next1, next2, next3, next4, next5 = [],[],[],[],[]

            def listAdd(nextX, X):
                nextX.append(dr.find_element_by_xpath(f'//*[@id="t{X}"]/div/div[1]/div[1]').text)
                nextX.append(dr.find_element_by_xpath(f'//*[@id="t{X}"]/div/div[1]/div[5]/span[1]').text + "°C")
                nextX.append(dr.find_element_by_xpath(f'//*[@id="t{X}"]/div/div[1]/div[4]/span[1]').text + "°C")
                dr.find_element_by_xpath(f'//*[@id="t{X}"]').click()
                sleep(0.1) #Diğer günlere tıkladıktan sonra biraz beklesin diye
                nextX.append("% " + dr.find_element_by_xpath(f'//*[@id="t{X}"]/div/div[2]/div[2]').text)
                nextX.append(dr.find_element_by_xpath(f'//*[@id="t{X}"]/div/div[1]/div[3]').text)

            listAdd(next1, 1)
            listAdd(next2, 2)
            listAdd(next3, 3)
            listAdd(next4, 4)
            listAdd(next5, 5)

        except:
            print("\nBağlantı hatası!")
            dr.close()
            input("Kapatmak için bir tuşa basın...")
            break          

        #verileri ekrana yazdırdık
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{banner}\nİl : {city}\nİlçe : {state}\nGüncelleme Zamanı : {nTime}\n" + "-"*59)
        print(f"""          |  Sıcaklık  |   Nem   |          Durum         |
{"-"*59}
   Şuan   |{nT:^12}|{nH:^9}|{nS:^24}|
{"-"*80}
  Günler  | Sıcaklık (Max) | Sıcaklık (Min) |   Nem   |         Durum          |
{"-"*80}
{next1[0]:^10}|{next1[1]:^16}|{next1[2]:^16}|{next1[3]:^9}|{next1[4]:^24}|
{next2[0]:^10}|{next2[1]:^16}|{next2[2]:^16}|{next2[3]:^9}|{next2[4]:^24}|
{next3[0]:^10}|{next3[1]:^16}|{next3[2]:^16}|{next3[3]:^9}|{next3[4]:^24}|
{next4[0]:^10}|{next4[1]:^16}|{next4[2]:^16}|{next4[3]:^9}|{next4[4]:^24}|
{next5[0]:^10}|{next5[1]:^16}|{next5[2]:^16}|{next5[3]:^9}|{next5[4]:^24}|

Uyarılar : {nI}""")

        close = input("\nÇıkmak için 'Q' veya 'q' tuşuna basınız:: ") #programdan çıkılsın mı diye sorduk

if __name__ == '__main__':
    main()
