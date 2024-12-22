import requests as rq
from bs4 import BeautifulSoup as bs
import tkinter as tk
from tkinter import messagebox
import time
import sys

headers ={
    'Referer' : 'https://bulletin.nuist.edu.cn/791/list.htm',
    'Host' : 'bulletin.nuist.edu.cn',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
}

class RedirectOutput:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, string):
        self.text_widget.insert(tk.END, string)
        self.text_widget.see(tk.END)

    def flush(self):
        pass

def main():
    url = "https://bulletin.nuist.edu.cn/791/list.htm"
    s=rq.session()
    page = s.get(url, headers=headers).content
    soup = bs(page,'lxml')
#    print (soup)
    for i in range(1,21):
        news_class = "news n" + str(i) + " clearfix"
        news = soup.find('li', {'class': news_class})
        date = news.find('span',{'class': "arti_bs"}).text
#        print(title)
#        print(date)
        if date == time.strftime("%Y-%m-%d", time.localtime()):
            title = news.find('span', {'class': "btt"}).text
            print(title)
#            print(date)
            break

root =  tk.Tk()
root.title("校园信息小帮手")

tk.Label(root, text="校园信息小帮手", font=('Arial', 20)).pack()
output_text = tk.Text(root, height=10, width=50)
output_text.pack(pady=20)

sys.stdout = RedirectOutput(output_text)

tk.Button(root, text="检查今日通知", command=main).pack(pady=20)

root.mainloop()



