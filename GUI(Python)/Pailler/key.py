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

def inv_mod(a,N):
  d,x,y=ext_gcd(a,N)
  if d!=1:
    print("乗法逆数が存在しません。")
    raise Exception
  return y%N


def gcd(a,b):
  if b==0:
    return a
  return gcd(b,a%b)

def lcm(a,b):
  return a*b//gcd(a,b)

def step1():
  rd=pow(2,1024)
  rl=pow(2,1025)
  while 1:
    p=randint(rd,rl-1)
    i=0
    while i<40:
      r=randint(2,p-1)
      if pow(r,p-1,p)!=1:
        break
      i+=1
    else:
      while 1:
        q=randint(rd,rl-1)
        j=0
        while j<40:
          rr=randint(2,q-1)
          if pow(rr,q-1,q)!=1:
            break
          j+=1
        else:
          if gcd(p*q,(p-1)*(q-1))==1:
            return p,q
  sys.stderr.write("step1 error\n")
  return

def click_dialog1():
  dirc=abspath(dirname(__file__))
  dircpath=askdirectory(initialdir=dirc)
  ent1.set(dircpath)
  return

def sub3():
  p,q=step1()
  n=p*q
  la=lcm(p-1,q-1)
  g=n+1
  L=(pow(g,la,n*n)-1)//n
  try:
    u=inv_mod(L,n)
  except:
    return sub3()
  return p,q,n,la,g,L,u

def sub2():
  try:
    p,q,n,la,g,L,u=sub3()
    now_time=datetime.now()
    public_name=now_time.strftime("%Y%m%d%H%M%S_public.txt")
    with open(f"{ent1.get()}/{public_name}",mode="w")as f1:
      f1.write(f"{n}\n{g}\n")
    private_name=now_time.strftime("%Y%m%d%H%M%S_private.txt")
    with open(f"{ent1.get()}/{private_name}",mode="w")as f2:
      f2.write(f"{la}\n{u}\n")
  except:
    messagebox.showerror("Error","エラーが発生しました。")
    sys.exit()
    return
  messagebox.showinfo("Success",f"鍵の生成が完了しました。\n実行時間{time.time()-starttime}秒\nファイル名:\n公開鍵:{public_name}\n秘密鍵:{private_name}")

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
  tk.title("Paillier暗号鍵の生成")
  f0=ttk.Frame(tk,padding=10)
  f0.grid(row=0,column=1)
  explain0=ttk.Label(f0,text="鍵を生成するフォルダを選択してください。")
  explain0.pack()

  f1=ttk.Frame(tk,padding=10)
  f1.grid(row=1,column=1)
  display1=ttk.Label(f1,text="フォルダ：")
  display1.pack(side=LEFT)

  pathentry1=ttk.Entry(f1,textvariable=ent1,width=30)
  pathentry1.pack(side=LEFT)
  pathButton=ttk.Button(f1,text="参照",command=click_dialog1)
  pathButton.pack(side=RIGHT)

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
