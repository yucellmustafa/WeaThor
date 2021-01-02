import os
from selenium import webdriver

def main():
    close = str()

    while close.lower() != "q":
        os.system('cls' if os.name == 'nt' else 'clear')
        banner = """
                __        __        _____ _
                \ \      / ___  __ |_   _| |__   ___  _ __
                 \ \ /\ / / _ \/ _` || | | '_ \ / _ \| '__|
                  \ V  V |  __| (_| || | | | | | (_) | |
                   \_/\_/ \___|\__,_||_| |_| |_|\___/|_|
\n""" + "-"*70 + "\nData Source : https://mgm.gov.tr/"
        print(banner)
        city = input("City : ")
        state = input("State (default = center) : ")
        url = f"https://mgm.gov.tr/?il={city}&ilce={state}"
        #tarayıcı oluşturup arka plana aldık
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')

        dr = webdriver.Chrome(options=options)
        dr.get(url)

        #verileri çektik
        state = dr.find_element_by_xpath('//*[@id="siteBody"]/section[1]/div/div[2]/div[2]/h3[1]/span').text
        city = dr.find_element_by_xpath('//*[@id="siteBody"]/section[1]/div/div[2]/div[2]/h3[1]/ziko').text
        nTime = dr.find_element_by_xpath('//*[@id="siteBody"]/section[1]/div/div[2]/div[2]/p').text
        nT = dr.find_element_by_xpath('//*[@id="siteBody"]/section[1]/div/div[2]/div[2]/div/h3/span[1]/ziko').text + "°C"
        nH = "% " + dr.find_element_by_xpath('//*[@id="siteBody"]/section[1]/div/div[2]/div[2]/div/h3/span[2]/div/span[3]/span[3]').text
        nS = dr.find_element_by_xpath('//*[@id="siteBody"]/section[1]/div/div[2]/div[2]/div/p').text

        next1, next2, next3, next4, next5 = [],[],[],[],[]

        def listAdd(nextX, X):
            nextX.append(dr.find_element_by_xpath(f'//*[@id="t{X}"]/div/div[1]/div[1]').text)
            nextX.append(dr.find_element_by_xpath(f'//*[@id="t{X}"]/div/div[1]/div[5]/span[1]').text + "°C")
            nextX.append(dr.find_element_by_xpath(f'//*[@id="t{X}"]/div/div[1]/div[4]/span[1]').text + "°C")
            dr.find_element_by_xpath(f'//*[@id="t{X}"]').click()
            nextX.append("% " + dr.find_element_by_xpath(f'//*[@id="t{X}"]/div/div[2]/div[2]').text)
            nextX.append(dr.find_element_by_xpath(f'//*[@id="t{X}"]/div/div[1]/div[3]').text)

        listAdd(next1, 1)
        listAdd(next2, 2)
        listAdd(next3, 3)
        listAdd(next4, 4)
        listAdd(next5, 5)

        dr.close() #tarayıcıyı kapattık
        #verileri ekrana yazdırdık
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{banner}\nCity : {city}\nState : {state}\nUpdate DateTime : {nTime}\n" + "-"*70)
        print(f"""
          |  Temp  | Humidity |       Status       |
----------------------------------------------------
   Now    |{nT:^8}|{nH:^10}|{nS:^20}|
----------------------------------------------------
   Days   | Temp (High) | Temp (Low) | Humidity |       Status       |
----------------------------------------------------------------------
{next1[0]:^10}|{next1[1]:^13}|{next1[2]:^12}|{next1[3]:^10}|{next1[4]:^20}|
{next2[0]:^10}|{next2[1]:^13}|{next2[2]:^12}|{next2[3]:^10}|{next2[4]:^20}|
{next3[0]:^10}|{next3[1]:^13}|{next3[2]:^12}|{next3[3]:^10}|{next3[4]:^20}|
{next4[0]:^10}|{next4[1]:^13}|{next4[2]:^12}|{next4[3]:^10}|{next4[4]:^20}|
{next5[0]:^10}|{next5[1]:^13}|{next5[2]:^12}|{next5[3]:^10}|{next5[4]:^20}|""")

        close = input("\nInput 'Q' or 'q' to close :: ") #programdan çıkılsın mı diye sorduk

if __name__ == '__main__':
    main()
