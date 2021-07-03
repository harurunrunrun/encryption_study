from os.path import basename
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

name1=input("秘密鍵ファイル名:").replace('"','')
name2=input("暗号文ファイル名:").replace('"','')
name3=basename(name2)
with open(name1)as f1:
  x=int(f1.readline())
  p=int(f1.readline())
  with open(name2)as f2:
    c1=int(f2.readline())
    c2=int(f2.readline())
    #t=inv_mod(p,c1)
    t=pow(c1,p-2,p)
    m=c2*pow(t,x,p)%p
    with open(f"dec_{name3}",mode="w")as f3:
      f3.write(f"{m}\n")
