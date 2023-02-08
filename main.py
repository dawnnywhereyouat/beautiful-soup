from bs4 import BeautifulSoup
import urllib.request

url =  'https://tuoitre.vn/doanh-nghiep-bat-dong-san-keu-kho-tiep-can-von-ngan-hang-noi-se-giam-lai-vay-20230208140740301.htm'
url = 'https://tuoitre.vn/nhung-nguoi-tay-nguyen-lam-du-lich-mot-cau-chuyen-khong-co-vai-phu-20230202155129983.htm'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

# detail-title article-title
# print(soup)

# h1 = soup.find('h1', class_='detail-title article-title')
title = soup.find('title')
# title = h1.get('title')
# ohno = h1.text
ohno = title.text.strip()

try:
    mege = soup.find('a', class_='header__m-name')
    mege_title = mege.text.strip()
    print(mege_title)
    if mege_title == 'MEGASTORY':
        link_type = 'mega'
except:
    link_type = 'news'

print(url)
print(ohno)
print(
    link_type
)


# print(soup.prettify())

# for link in soup.find_all('a'):
#     print(link.get('href'))


# print(soup.get_text())