from os.path import *
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import *
from tkinter import messagebox
import time
import sys
from random import randint
from datetime import datetime
l=256
tk=Tk()
ent1=StringVar()

def click_dialog1():
  dirc=abspath(dirname(__file__))
  dircpath=askdirectory(initialdir=dirc)
  ent1.set(dircpath)
  return



def prime(p):
  i=0
  f=[]
  while i<40:
    a=randint(2,p-1)
    if a in f:continue
    if pow(a,p-1,p)!=1:return False
    i+=1
  return True

def step1():#lbitの素数qを生成し、p=2q+1が素数かどうか判定
  while True:
    q=randint(pow(2,l-1),pow(2,l)-1)
    if prime(q):
      p=2*q+1
      if prime(p):
        return p,q

def step2(p,q):#gを探す
  while True:
    g=randint(2,p-2)
    if pow(g,q,p)==1:
      return g

def sub2():
  try:
    p,q=step1()
    #print("step1 finish")
    g=step2(p,q)
    #print("step2 finish")
    x=randint(2,q-2)
    y=pow(g,x,p)
    now_time=datetime.now()
    public_name=now_time.strftime("%Y%m%d%H%M%S_public.txt")
    with open(f"{ent1.get()}/{public_name}",mode="w")as f1:
      f1.write(f"{p}\n{q}\n{g}\n{y}\n")
    private_name=now_time.strftime("%Y%m%d%H%M%S_private.txt")
    with open(f"{ent1.get()}/{private_name}",mode="w")as f2:
      f2.write(f"{x}\n{p}\n")#pは復号化に必要
  except:
    messagebox.showerror("Error", "エラーが発生しました。")
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
  tk.title("Elgamal暗号 鍵生成")
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