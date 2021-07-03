from time import time
from math import gcd
import datetime
from random import randint
def lcm(a,b):
  return a*b//gcd(a,b)

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
  return y%N

time_start=time()
p=prime()
q=prime()
N=p*q
l=lcm(p-1,q-1)
e=e_set(l)
d=inv_mod(l,e)


now=datetime.datetime.now()
t=now.strftime("%Y%m%d%H%M%S_public.txt")
with open(t,mode="w") as public_file:
  public_file.write(f"{N}\n{e}\n")
s=now.strftime("%Y%m%d%H%M%S_private.txt")
with open(s,mode="w") as private_file:
  private_file.write(f"{d}\n")
print(time()-time_start)