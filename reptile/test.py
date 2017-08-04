import urllib.request
response=urllib.request.urlopen('http://www.python.org')
#print(response.read().decode('utf-8'))#读取网页数据并将byte装换为utf-8的格式显示出来
#print(response.getheader('Server'))
data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())