from os.path import *
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import *
from tkinter import messagebox
from time import time
import sys
from random import randint
from datetime import datetime
tk=Tk()
ent1=StringVar()#n
ent2=StringVar()#g
ent3=StringVar()#m
ent4=StringVar()#c
ent5=StringVar()#la
ent6=StringVar()#u
ent7=StringVar()#c
ent8=StringVar()#m'
#ent9=StringVar()#mfile
#ent10=StringVar()#cfile
bl1=BooleanVar()
bl2=BooleanVar()
bl3=BooleanVar()

def verify(n,g,la,u):
  m1=randint(0,min(n,101)-1)
  r=randint(0,n-1)
  c=(pow(g,m1,n*n)*pow(r,n,n*n)%(n*n))
  L=(pow(c,la,n*n)-1)//n
  m2=(L*u)%n
  return m1==m2

def click_dialog1():
  fp0=abspath(dirname(__file__))
  fpath0=askopenfilename(initialdir=fp0)
  if isfile(fpath0):
    try:
      with open(fpath0) as file0:
        n0=file0.readline()
        g0=file0.readline()
        ent1.set(n0)
        ent2.set(g0)
        if int(n0)+1!=int(g0):
          messagebox.showerror("Error",f"正しいファイルではない可能性があります。\nファイルパス:{fpath0}")
    except:
      messagebox.showerror("Error",f"正しいファイルではない可能性があります。\nファイルパス:{fpath0}")
  return

def click_dialog2():
  fp1=abspath(dirname(__file__))
  fpath1=askopenfilename(initialdir=fp1)
  #ent9.set(fpath1)
  if isfile(fpath1):
    try:
      with open(fpath1) as file1:
        m0=file1.readline()
        ent3.set(m0)
    except:
      messagebox.showerror("Error", f"正しいファイルではない可能性があります。\nファイルパス:{fpath1}")
  return

def enc1():
  if (not ent2.get()) and ent1.get():
    ent2.set(int(ent1.get())+1)
  if not (ent1.get() and ent2.get() and ent3.get()):
    messagebox.showerror("Error","変数が入力されていません。")
    return
  try:
    n=int(ent1.get())
    g=int(ent2.get())
    m=int(ent3.get())
  except:
    messagebox.showerror("Error", "変数のいずれかにエラーがあります。")
    return
  if n<0:
    messagebox.showerror("Error","nは正である必要があります。")
    return
  if n+1!=g:
    messagebox.showerror("Error","n+1=gである必要があります。")
    return
  if m<0 or n<=m:
    messagebox.showerror("Error","平文は0以上n未満である必要があります。")
    return
  try:
    r=randint(0,n-1)
    N=n*n
    c=(pow(g,m,N)*pow(r,n,N))%N
    ent4.set(c)
  except:
    messagebox.showerror("Error","暗号化中にエラーが発生しました。")
    return
  if bl1.get():
    ent7.set(c)
  if bl2.get():
    nowtime=datetime.now()
    fw=nowtime.strftime("%Y%m%d%H%M%S_enc.txt")
    try:
      with open(fw,mode="w")as fl:
        fl.write(f"{c}\n")
    except:
      messagebox.showerror("Error","ファイル書き込み時にエラーが発生しました。")
      return
    messagebox.showinfo("Succes",f"暗号化が完了しました。\nファイル名:{fw}")
  else:
    messagebox.showinfo("Succes","暗号化が完了しました。")
  return

def click_dialog3():
  fp2=abspath(dirname(__file__))
  fpath2=askopenfilename(initialdir=fp2)
  if isfile(fpath2):
    try:
      with open(fpath2) as file2:
        la0=file2.readline()
        u0=file2.readline()
        ent5.set(la0)
        ent6.set(u0)
    except:
      messagebox.showerror("Error",f"正しいファイルではない可能性があります。\nファイルパス:{fpath2}")
  return

def click_dialog4():
  fp3=abspath(dirname(__file__))
  fpath3=askopenfilename(initialdir=fp3)
  if isfile(fpath3):
    try:
      with open(fpath3) as file3:
        c0=file3.readline()
        ent7.set(c0)
    except:
      messagebox.showerror("Error", f"正しいファイルではない可能性があります。\nファイルパス:{fpath3}")
  return

def dec1():
  if not ent1.get():
    messagebox.showerror("Error", "公開鍵も入力してください。")
    return
  if not(ent5.get() and ent6.get() and ent7.get()):
    messagebox.showerror("Error","変数が正しく入力されていません。")
    return
  try:
    n=int(ent1.get())
    c=int(ent7.get())
    la=int(ent5.get())
    u=int(ent6.get())
  except:
    messagebox.showerror("Error","変数が正しくありません。")
    return
  if n<=0:
    messagebox.showerror("Error","nは正である必要があります。")
    return
  if not verify(n, n+1, la, u):
    messagebox.showerror("Error","秘密鍵が正しくありません。")
    return
  try:
    L=(pow(c,la,n*n)-1)//n
    m=(L*u)%n
    ent8.set(m)
  except:
    messagebox.showerror("Error","復号化中にエラーが発生しました。")
    return
  if bl3.get():
    nowtime=datetime.now()
    fw=nowtime.strftime("%Y%m%d%H%M%S_dec.txt")
    try:
      with open(fw,mode="w") as fl:
        fl.write(f"{m}\n")
    except:
      messagebox.showerror("Error","ファイルの書き込み時にエラーが発生しました。")
      return
    messagebox.showinfo("Succes",f"復号化が完了しました。\nファイル名:{fw}")
  else:
    messagebox.showinfo("Succes","復号化が完了しました。")
  return

def sub1():
  tk.title("Pailler暗号")

  f01=ttk.Frame(tk,padding=10)
  f01.grid(row=0,column=1)
  f02=ttk.Frame(tk,padding=10)
  f02.grid(row=0,column=2)
  f03=ttk.Frame(tk,padding=10)
  f03.grid(row=0,column=3)
  f04=ttk.Frame(tk,padding=10)
  f04.grid(row=0,column=4)
  f11=ttk.Frame(tk,padding=10)
  f11.grid(row=1,column=1)
  f12=ttk.Frame(tk,padding=10)
  f12.grid(row=1,column=2)
  f13=ttk.Frame(tk,padding=10)
  f13.grid(row=1,column=3)
  f14=ttk.Frame(tk,padding=10)
  f14.grid(row=1,column=4)
  f21=ttk.Frame(tk,padding=10)
  f21.grid(row=2,column=1)
  f22=ttk.Frame(tk,padding=10)
  f22.grid(row=2,column=2)
  f23=ttk.Frame(tk,padding=10)
  f23.grid(row=2,column=3)
  f24=ttk.Frame(tk,padding=10)
  f24.grid(row=2,column=4)
  f31=ttk.Frame(tk,padding=10)
  f31.grid(row=3,column=1)
  f32=ttk.Frame(tk,padding=10)
  f32.grid(row=3,column=2)
  f33=ttk.Frame(tk,padding=10)
  f33.grid(row=3,column=3)
  f34=ttk.Frame(tk,padding=10)
  f34.grid(row=3,column=4)
  f41=ttk.Frame(tk,padding=10)
  f41.grid(row=4,column=1)
  f42=ttk.Frame(tk,padding=10)
  f42.grid(row=4,column=2)
  f43=ttk.Frame(tk,padding=10)
  f43.grid(row=4,column=3)
  f44=ttk.Frame(tk,padding=10)
  f44.grid(row=4,column=4)

  ttk.Style().configure("TButton",relief="raised",background="#A9A9A9",foreground="#000000")

  #f01
  explain0=ttk.Label(f01,text="公開鍵:")
  explain0.pack(side=LEFT)

  #f02
  wind1=ttk.Entry(f02,textvariable=ent1,width=30)
  wind1.pack(side=RIGHT)
  num_1=ttk.Label(f02,text="n ")
  num_1.pack(side=RIGHT)

  #f11
  button1=ttk.Button(f11,text="参照(公開鍵)",command=click_dialog1)
  button1.pack(side=LEFT)

  #f12
  num_2=ttk.Label(f12,text="g ")
  num_2.pack(side=LEFT)
  wind2=ttk.Entry(f12,textvariable=ent2,width=30)
  wind2.pack()

  #f21
  explain1=ttk.Label(f21,text="平文:")
  explain1.pack()

  #f22
  wind3=ttk.Entry(f22,textvariable=ent3,width=30)
  wind3.pack(side=LEFT)
  button2=ttk.Button(f22,text="参照(平文)",command=click_dialog2)
  button2.pack(side=RIGHT)

  #f31
  bl1.set(True)
  cb1=ttk.Checkbutton(f31,text="実行結果を右にも表示する。",variable=bl1)
  cb1.pack()
  bl2.set(False)
  cb2=ttk.Checkbutton(f31,text="実行結果をファイルに保存する。\n(カレントディレクトリに保存されます。)",variable=bl2)
  cb2.pack()

  #f32
  button3=ttk.Button(f32,text="暗号化",command=enc1)
  button3.pack()

  #f41
  explain2=ttk.Label(f41,text="実行結果(暗号文): ")
  explain2.pack()

  #f42
  wind4=ttk.Entry(f42,textvariable=ent4,width=30)
  wind4.pack()

  #f03
  explain3=ttk.Label(f03,text="秘密鍵: ")
  explain3.pack()

  #f04
  num_3=ttk.Label(f04,text="λ ")
  num_3.pack(side=LEFT)
  wind5=ttk.Entry(f04,textvariable=ent5,width=30)
  wind5.pack()

  #f13
  button4=ttk.Button(f13,text="参照(秘密鍵)",command=click_dialog3)
  button4.pack()

  #f14
  num_4=ttk.Label(f14,text="μ ")
  num_4.pack(side=LEFT)
  wind6=ttk.Entry(f14,textvariable=ent6,width=30)
  wind6.pack()

  #f23
  explain4=ttk.Label(f23,text="暗号文: ")
  explain4.pack()

  #f24
  wind7=ttk.Entry(f24,textvariable=ent7,width=30)
  wind7.pack(side=LEFT)
  button5=ttk.Button(f24,text="参照(暗号文)",command=click_dialog4)
  button5.pack()

  #f33
  bl3.set(False)
  cb3=ttk.Checkbutton(f33,text="実行結果をファイルに保存する。\n(カレントディレクトリに保存されます。)",variable=bl3)
  cb3.pack()

  #f34
  button6=ttk.Button(f34,text="復号化",command=dec1)
  button6.pack()

  #f43
  explain5=ttk.Label(f43,text="実行結果(平文): ")
  explain5.pack()

  #f44
  wind8=ttk.Entry(f44,textvariable=ent8,width=30)
  wind8.pack()
  return

def main():
  sub1()
  return

if __name__=="__main__":
  main()
  tk.mainloop()
