from os.path import abspath,dirname,isfile
from tkinter import ttk,messagebox,Tk,StringVar,BooleanVar,LEFT,RIGHT
from tkinter.filedialog import askopenfilename
from datetime import datetime

tk=Tk()
ent1=StringVar()#N
ent2=StringVar()#e
ent3=StringVar()#m1
ent4=StringVar()#c1
ent5=StringVar()#c2
ent6=StringVar()#d
ent7=StringVar()#m2
bl1=BooleanVar()#右に表示
bl2=BooleanVar()#実行結果をファイルに表示(enc)
bl3=BooleanVar()#実行結果をファイルに表示(dec)


def click_dialog1():
  fp0=abspath(dirname(__file__))
  fpath0=askopenfilename(initialdir=fp0)
  if isfile(fpath0):
    try:
      with open(fpath0) as file0:
        n0=file0.readline()
        e0=file0.readline()
        ent1.set(n0)
        ent2.set(e0)
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

def enc_dec(u):
  #0:enc, 1:dec
  if u==0 and not (ent1.get() and ent2.get() and ent3.get()) or u==1 and not (ent1.get() and ent5.get() and ent6.get()):
    messagebox.showerror("Error", "変数が入力されていません。")
    return
  N,e,m=0,0,0#初期化
  if u==0:
    try:
      N=int(ent1.get())
      e=int(ent2.get())
      m=int(ent3.get())
    except:
      messagebox.showerror("Error","変数のいずれかにエラーがあります。")
  else:
    try:
      N=int(ent1.get())
      e=int(ent6.get())
      m=int(ent5.get())
    except:
      messagebox.showerror("Error","変数のいずれかにエラーがあります。")
  if N<0:
    messagebox.showerror("Error", "Nは正である必要があります。")
    return
  if m<0 or N<=m:
    messagebox.showerror("Error","対象は0以上N未満である必要があります。")
    return
  try:
    c=pow(m,e,N)
    if u==0:
      ent4.set(c)
    else:
      ent7.set(c)
  except:
    messagebox.showerror("Error","実行中にエラーが発生しました。")
    return
  if u==0 and bl1.get() :
    ent5.set(c)
  if bl2.get() and u==0 or bl3.get() and u==1:
    nowtime=datetime.now()
    fw=nowtime.strftime("%Y%m%d%H%M%S_enc.txt")
    if u==1:
      fw=nowtime.strftime("%Y%m%d%H%M%S_dec.txt")
    try:
      with open(fw,mode="w")as fl:
        fl.write(f"{c}\n")
    except:
      messagebox.showerror("Error","ファイル書き込み時にエラーが発生しました。")
      return
    messagebox.showinfo("Succes",f"実行が完了しました。\nファイル名:{fw}")
  else:
    messagebox.showinfo("Succes","実行が完了しました。")
  return

def click_dialog3():
  fp2=abspath(dirname(__file__))
  fpath2=askopenfilename(initialdir=fp2)
  if isfile(fpath2):
    try:
      with open(fpath2) as file2:
        d=file2.readline()
        ent6.set(d)
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
        ent5.set(c0)
    except:
      messagebox.showerror("Error", f"正しいファイルではない可能性があります。\nファイルパス:{fpath3}")
  return

def enc1():
  enc_dec(0)
  return

def dec1():
  enc_dec(1)
  return

def sub():
  tk.title("RSA暗号")

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
  num_1=ttk.Label(f02,text="N ")
  num_1.pack(side=RIGHT)

  #f11
  button1=ttk.Button(f11,text="参照(公開鍵)",command=click_dialog1)
  button1.pack(side=LEFT)

  #f12
  num_2=ttk.Label(f12,text="e ")
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
  num_3=ttk.Label(f04,text="d ")
  num_3.pack(side=LEFT)
  wind5=ttk.Entry(f04,textvariable=ent6,width=30)
  wind5.pack()

  #f13
  button4=ttk.Button(f13,text="参照(秘密鍵)",command=click_dialog3)
  button4.pack()

  #f14
#   num_4=ttk.Label(f14,text="d ")
#   num_4.pack(side=LEFT)
#   wind6=ttk.Entry(f14,textvariable=ent6,width=30)
#   wind6.pack()

  #f23
  explain4=ttk.Label(f23,text="暗号文: ")
  explain4.pack()

  #f24
  wind7=ttk.Entry(f24,textvariable=ent5,width=30)
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
  wind8=ttk.Entry(f44,textvariable=ent7,width=30)
  wind8.pack()

  return


def main():
  sub()
  return

if __name__=="__main__":
  main()
  tk.mainloop()

