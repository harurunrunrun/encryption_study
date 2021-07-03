from os.path import basename
from random import randint
name1=input("公開鍵ファイル名:").replace('"','')
name2=input("平文ファイル名:").replace('"','')
name3=basename(name2)
with open(name1) as f1:
  p=int(f1.readline())
  q=int(f1.readline())
  g=int(f1.readline())
  y=int(f1.readline())
  r=randint(1,q-1)
  with open(name2) as f2:
    m=int(f2.readline())
    c1=pow(g,r,p)
    c2=m*pow(y,r,p)
    with open(f"enc_{name3}",mode="w")as f3:
      f3.write(f"{c1}\n{c2}\n")
