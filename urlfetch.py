from Tkinter import *
from lxml import html
import requests
from bs4 import BeautifulSoup

tup=" "

def fetchit():
    url2=url1.get()
    r=requests.get(url2)
    data=r.text
    soup=BeautifulSoup(data)
    fo = open("D:/fileurl.txt", "w")
    for link in soup.find_all('a'):
            global tup
            tup=(str(link.get('href')))
            fo.write('\n'+tup)
    fo.close()
  

def fetchmeta():
    url2=url1.get()
    r=requests.get(url2)
    data=r.text
    soup=BeautifulSoup(data)
    for link in soup.find_all('a'):
        print(link.get('href'))

win=Tk()
url1=StringVar()

l1=Label(win,text="Enter URL")

tf1=Entry(win,textvariable=url1)

l2=Label(win)

l3=Label(win)
b1=Button(win,text="Fetch",command=fetchit)

b2=Button(win,text="Fetch",command=fetchmeta)


l1.grid(row=3,column=4)
tf1.grid(row=3,column=8)
l2.grid(row=6,column=8)
l3.grid(row=9,column=8)
b1.grid(row=18,column=6)
b2.grid(row=18,column=9)
win.mainloop()