import requests
from bs4 import BeautifulSoup
import sys


# crawler for codechef
def getl(url, l):
    l1 = url.split('/')
    # getting username from the url 
    username = l1[-1]
    print(username, end="  ")
    r = requests.get(url)
    # accessing html of profile page
    sp = BeautifulSoup(r.content, "html.parser")
    # finding tag that has rating data and accessing the contents
    tag = sp.find('span', class_='rating').contents[0]
    # print(tag)
    # (ignore)fh = open(r"C:\Users\deepa\Desktop\resf.txt", 'w')
    tg = tag[0] + "  "
    print(tg)
    # (ignore)fh.write(tg)
    # (ignore)fh.write(username)
    # (ignore)fh.close()
    '''for ps in sp.find_all('div', class_='content'):
        try:
            print(ps.h5.contents[0])
        except:
            continue'''


# crawler for leetcode
'''def getlc(lc, res):
    l1 = lc.split('/')
    usrname = l1[-2]
    print('UserName lc:', usrname, end="  ")
    r = requests.get(lc)
    sp = BeautifulSoup(r.content, "html.parser")
    # print('Rating :', end=" ")
    # tag = sp.find('span', class_='rating').contents[0]
    # print(tag)
    co = sp.find('body')
    print(co)
    le = co.find('div')
    print(le)
    ole = le.find('div', attr={'class': 'total-solved-count__2El1'})
    print(ole)'''
# opening data file that contains urls adn roll numbers
f = open(r"C:\Users\deepa\Desktop\data.txt", 'r')
res = []
# reading the stdout from console into a file
sys.stdout = open(r"C:\Users\deepa\PycharmProjects\webcrw\resf.txt", 'w')
for line in f:
    lst = line.split()
    print(lst[0], end=" ")
    print(lst[1], end=" ")
    url = lst[2]
    # lc = lst[1]
    # calling codechef crawler
    getl(url, res)
    # print(lc)
    # getlc(lc, res)
f.close()
sys.stdout.close()
