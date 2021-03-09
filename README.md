# WeathStilo
Hava durumu tahminlerini siteden çeken bir uygulama.

Selenium kütüphanesi kullanıldı. (pip install selenium)

---

- Kullanmadan önce işletim sisteminize uygun chromedriver dosyasını indiriniz. ([chromedriver](https://chromedriver.chromium.org/downloads))
- Daha sonra ana klasördeki 'win' (windows için) veya 'linux' (linux için) klasörlerinin içindeki dosya ile değiştiriniz.
- ChromeDriver mevcut versiyon : 89.0.4389.23
- Kaynak : https://mgm.gov.tr/

---

Windows kullananlar "releases kısmından gerekli dosyaları indirip kullanabilirler."

---

Linux kullanım : 

- Sistemize göre pip3 indirme komutunu terminale yazarak kurunuz : 

Debian/Ubuntu : ```apt install python3-pip```

CentOS and RHEL : ```yum install python-pip```

Fedora : ```dnf install python3```

Arch : ```pacman -S python-pip```

OpenSUSE : ```zypper install python3-pip```

- Selenium kütüphanesini kurunuz : ```pip3 install selenium```

- Daha sonra projenin kaynak dosyalarını indirin. 

- Projenin ana dizininde bu komut ile programı kullanabilirsiniz : ```python3 ./main.py```

---

Program Screen Shoots :

<img width="450px" src="https://user-images.githubusercontent.com/49123562/110549467-28121e00-8143-11eb-83ef-2206d05f37be.png">

<img width="450px" src="https://user-images.githubusercontent.com/49123562/110549470-28aab480-8143-11eb-84d3-5bdf85ed0f8a.png">

---

**MIT License**

Copyright (c) 2021 Mustafa Yücel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
