
__author__ = 'Wayne'
import urllib.request#网站抓取
import os#文件操作
import re#正则表达式

def url_open(url):
    url = re.sub(r'^//*',"http://", url)#在网址前面加上http
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0')

    response = urllib.request.urlopen(req)#通过链接抓取网站的HTML代码，返回的类型是HTTPResposne类型的对象
    return response.read()

def get_page(url):
    url = re.sub(r'^//*', "http://", url)  # 在网址前面加上http
    html = url_open(url).decode('utf-8')
    pattern = r'<span class="current-comment-page">\[(\d{4})\]</span>' #正则表达式寻找页面地址
    print(re.findall(pattern,html))
    page = int(re.findall(pattern,html)[0])
    return page



def find_imgs(page_url):#通过正则表达式图片的标签来下载图片
    pattern = r'<img src="(.*?\.jpg)"'
    html = url_open(page_url).decode('utf-8')
    img_addrs = re.findall(pattern,html)
    return img_addrs


def save_imgs(img_addrs,page_num,folder):#保存图片
    os.mkdir(str(page_num))
    os.chdir(str(page_num))
    for i in img_addrs:
        pattern = r'sinaimg.cn/mw600/(.*?).jpg'
        filename = i.split('/')[-1]
        image = url_open(i)
        with open(filename,'wb') as f:
            f.write(image)
            f.close()


def download_mm(folder='ooxx',pages=10):
    os.mkdir(folder) #新建文件夹
    os.chdir(folder) #跳转到文件夹
    folder_top = os.getcwd() #获取当前工作目录
    url = 'http://jandan.net/ooxx/'
    page_num = get_page(url) #获取网页最新的地址
    for i in range(pages):
        page_num -= i #递减下载几个网页
        page_url = url + 'page-' + str(page_num) + '#comments' #组合网页地址
        img_addrs = find_imgs(page_url) #获取图片地址
        save_imgs(img_addrs,page_num,folder) #保存图片
        os.chdir(folder_top)

if __name__ == '__main__':
    folder = input("Please enter a folder(default is 'ooxx'): " )
    pages = input("How many pages do you wan to download(default is 10): ")
    download_mm(str(folder),int(pages))
