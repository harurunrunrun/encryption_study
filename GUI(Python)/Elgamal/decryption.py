from os.path import *
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import *
from tkinter import messagebox
from time import time
import sys
from random import randint
tk=Tk()
ent1=StringVar()
ent2=StringVar()

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

def click_dialog1():
  fp0=abspath(dirname(__file__))
  fpath0=askopenfilename(initialdir=fp0)
  ent1.set(fpath0)
  return

def click_dialog2():
  fp1=abspath(dirname(__file__))
  fpath1=askopenfilename(initialdir=fp1)
  ent2.set(fpath1)
  return

def sub2():
  try:
    name1=ent1.get()
    name2=ent2.get()
    name3=basename(name2)
    with open(name1)as f1:
      x=int(f1.readline())
      p=int(f1.readline())
      with open(name2)as f2:
        c1=int(f2.readline())
        c2=int(f2.readline())
        t=inv_mod(p,c1)
        m=c2*pow(t,x,p)%p
        with open(f"{dirname(name2)}/dec_{name3}",mode="w")as f3:
          f3.write(f"{m}\n")
  except:
    messagebox.showerror("Error","エラーが発生しました。")
    sys.exit()
    return
  messagebox.showinfo("Success", f"復号化が完了しました。\n 実行時間 {time()-starttime}秒\n ファイル名:dec_{name3}")
  return


def ok_button():
  global starttime
  starttime=time()
  file1=ent1.get()
  file2=ent2.get()
  if file1 and file2:
    tk.quit()
    sub2()
  else:
    messagebox.showerror("Error","ファイルが指定されていません。")
  return

def sub1():
  tk.title("Elgamal暗号 復号化")

  f0=ttk.Frame(tk,padding=10)
  f0.grid(row=0,column=1)
  explain0=ttk.Label(f0,text="秘密鍵ファイルを選択してください。\n(日本語はエラーになります。)")
  explain0.pack()

  f1=ttk.Frame(tk,padding=10)
  f1.grid(row=1,column=1)
  display1=ttk.Label(f1,text="秘密鍵ファイル : ")
  display1.pack(side=LEFT)

  pathentry1=ttk.Entry(f1,textvariable=ent1,width=30)
  pathentry1.pack(side=LEFT)
  pathButton=ttk.Button(f1,text="参照",command=click_dialog1)
  pathButton.pack()

  f2=ttk.Frame(tk,padding=10)
  f2.grid(row=2,column=1)
  explain1=ttk.Label(f2,text="復号化するファイルを選択してください。\n(日本語はエラーになります。)")
  explain1.pack()

  f3=ttk.Frame(tk,padding=10)
  f3.grid(row=3,column=1)
  display2=ttk.Label(f3,text="復号化ファイル : ")
  display2.pack(side=LEFT)

  pathentry2=ttk.Entry(f3,textvariable=ent2,width=30)
  pathentry2.pack(side=LEFT)
  pathButton=ttk.Button(f3,text="参照",command=click_dialog2)
  pathButton.pack()

  f4=ttk.Frame(tk,padding=10)
  f4.grid(row=5,column=1)
  button1=ttk.Button(f4,text="キャンセル",command=tk.quit)
  button1.pack(padx=30,side="left")
  button2=ttk.Button(f4,text="OK",command=ok_button)
  button2.pack(padx=30,side="left")
  return

def main():
  sub1()
  return

if __name__=="__main__":
  main()
  tk.mainloop()
