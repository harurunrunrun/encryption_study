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
      p=int(f1.readline())
      q=int(f1.readline())
      g=int(f1.readline())
      y=int(f1.readline())
      r=randint(1,q-1)
      with open(name2)as f2:
        m=int(f2.readline())
        c1=pow(g,r,p)
        c2=m*pow(y,r,p)
        with open(f"{dirname(name2)}/enc_{name3}",mode="w")as f3:
          f3.write(f"{c1}\n{c2}\n")
  except:
    messagebox.showerror("Error","エラーが発生しました。")
    sys.exit()
    return
  messagebox.showinfo("Success",f"暗号化が完了しました。\n 実行時間 {time()-starttime}秒\n ファイル名:enc_{name3}")
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
  tk.title("Elgamal暗号 暗号化")

  f0=ttk.Frame(tk,padding=10)
  f0.grid(row=0,column=1)
  explain0=ttk.Label(f0,text="公開鍵ファイルを選択してください。\n(日本語はエラーになります。)")
  explain0.pack()

  f1=ttk.Frame(tk,padding=10)
  f1.grid(row=1,column=1)
  display1=ttk.Label(f1,text="公開鍵ファイル : ")
  display1.pack(side=LEFT)

  pathentry1=ttk.Entry(f1,textvariable=ent1,width=30)
  pathentry1.pack(side=LEFT)
  pathButton=ttk.Button(f1,text="参照",command=click_dialog1)
  pathButton.pack()

  f2=ttk.Frame(tk,padding=10)
  f2.grid(row=2,column=1)
  explain1=ttk.Label(f2,text="暗号化するファイルを選択してください。\n(日本語はエラーになります。)")
  explain1.pack()

  f3=ttk.Frame(tk,padding=10)
  f3.grid(row=3,column=1)
  display2=ttk.Label(f3,text="暗号化ファイル : ")
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
