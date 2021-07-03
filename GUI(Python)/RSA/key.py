from math import gcd
from os.path import *
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import *
from tkinter import messagebox
import time
import sys
from random import randint
from datetime import datetime
tk=Tk()
ent1=StringVar()
def lcm(a,b):
  return a*b//gcd(a,b)

def click_dialog1():
  dirc=abspath(dirname(__file__))
  dircpath=askdirectory(initialdir=dirc)
  ent1.set(dircpath)
  return

def prime():
  k=2048
  while True:
    p=randint(pow(2,k-1),pow(2,k)-1)
    f=[]
    i=0
    cnt=0
    while i<40:
      a=randint(2,p-1)
      if a in f:
        continue
      f.append(a)
      if pow(a,p-1,p)==1:
        cnt+=1
      else:
        break
      i+=1
    if cnt==40:
      return p

def e_set(l):
  while True:
    e=randint(1,l)
    if gcd(l,e)==1:
      return e

def ext_gcd(a,b):
  if b>a:
    a,b=b,a
  a0,x0,y0=a,1,0
  a1,x1,y1=b,0,1
  while a1!=0:
    q=a0//a1
    a2,x2,y2=a0-q*a1,x0-q*x1,y0-q*y1
    a0,x0,y0=a1,x1,y1
    a1,x1,y1=a2,x2,y2
  return a0,x0,y0

def inv_mod(N,a):
  d,x,y=ext_gcd(N,a)
  return y

def sub2():
  try:
    p=prime()
    q=prime()
    N=p*q
    l=lcm(p-1,q-1)
    e=e_set(l)
    d=inv_mod(l,e)
    now_time=datetime.now()
    public_name=now_time.strftime("%Y%m%d%H%M%S_public.txt")
    with open(f"{ent1.get()}/{public_name}",mode="w")as f1:
      f1.write(f"{N}\n{e}\n")
    private_name=now_time.strftime("%Y%m%d%H%M%S_private.txt")
    with open(f"{ent1.get()}/{private_name}",mode="w")as f2:
      f2.write(f"{N}\n{d}\n")#Nは復号化に必要
  except:
    messagebox.showerror("Error","エラーが発生しました。")
    sys.exit()
    return
  messagebox.showinfo("Success",f"鍵の生成が完了しました。\n 実行時間 {time.time()-starttime}秒 \n ファイル名:\n 公開鍵:{public_name}\n 秘密鍵:{private_name}")
  return




def ok_button():
  global starttime
  starttime=time.time()
  file1=ent1.get()
  if file1:
    tk.quit()
    sub2()
    return
  else:
    messagebox.showerror("Error","フォルダが指定されていません。")
  return

def sub1():
  tk.title("RSA暗号 鍵生成")
  f0=ttk.Frame(tk,padding=10)
  f0.grid(row=0,column=1)
  explain0=ttk.Label(f0,text="鍵を生成するフォルダを選択してください。\n(日本語はエラーになります。)")
  explain0.pack()

  f1=ttk.Frame(tk,padding=10)
  f1.grid(row=1,column=1)
  display1=ttk.Label(f1,text="フォルダ : ")
  display1.pack(side=LEFT)

  pathentry1=ttk.Entry(f1,textvariable=ent1,width=30)
  pathentry1.pack(side=LEFT)
  pathButton=ttk.Button(f1,text="参照",command=click_dialog1)
  pathButton.pack()

  f2=ttk.Frame(tk,padding=10)
  f2.grid(row=3,column=1)
  button1=ttk.Button(f2,text="キャンセル",command=tk.quit)
  button1.pack(padx=30,side="left")
  button2=ttk.Button(f2,text="OK",command=ok_button)
  button2.pack(padx=30,side="left")
  return


def main():
  sub1()
  return

if __name__=="__main__":
  main()
  tk.mainloop()