from bs4 import BeautifulSoup
import requests
import urllib.request
#step1.使用beautifusoup解析网页
def req_web(n):
    url = 'http://tieba.baidu.com/p/2115469960?see_lz=1&pn='
    for i in range(n):
        wb_data = requests.get(url+str(i))
        soup = BeautifulSoup(wb_data.text, 'lxml')
        # step2.描述要爬取的东西在哪
        biographys = soup.select('#j_p_postlist > div > div.d_post_content_main > div.p_content > cc')
        photos = soup.select('img[width="436"]')
        # 将数据写入文件
        with open('日本战国分郡.txt', 'w') as f:
            for biography,one in zip(biographys,photos):
                text=biography.get_text()
                f.write(text)
                f.write('=' * 100)
                with open(r'C:\Users\wenhuan\Desktop\Sengoku\图片' + '\\' + text.strip()[:6]+'.jpg', 'wb') as fm:
                    url_p = one.get('src')
                    photo_data = urllib.request.urlopen(url_p).read() 
                    fm.write(photo_data)
req_web(4)




