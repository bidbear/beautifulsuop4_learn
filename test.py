import requests
from bs4 import BeautifulSoup

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
link ='http://politics.people.com.cn/n1/2019/0226/c1024-30901551.html'

r = requests.get(link,headers=header)
suop = BeautifulSoup(r.content,'lxml')
# with open('index.txt','a+') as f:
    # f.write(r.content)
print(suop.h3) #获取还h3的html标签
print(suop.h3.name) #获取标签名
print(suop.h3.text) #获取标签的的内容
print(suop.h3.string) #获取标签的内容
#print(type(suop.h3.string))
print(suop.p) #获取html中第一个再出现的P标签
print(suop.find_all('p')) #获取所有p标签的列表
print(suop.find(id='txz_dlq'))#获取指定ID值的标签数据

# for link in suop.find_all('a'): 
#     print(link.get('href')) #从文档中找到所有<a>标签的链接
#     print(link.text) #从文档中找到所有<a>标签的文本
# print(suop.get_text())#从文档中获取所有文字内容:
print(suop.name)
