import time
from random import randint
from datetime import datetime
l=1024

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


def main():
  starttime=time.time()
  p,q=step1()
  #print("step1 finish")
  g=step2(p,q)
  #print("step2 finish")
  x=randint(2,q-2)
  y=pow(g,x,p)
#   now_time=datetime.now()

#   public_name=now_time.strftime("%Y%m%d%H%M%S_public.txt")
#   with open(public_name,mode="w")as f1:
#     f1.write(f"{p}\n{q}\n{g}\n{y}\n")
#   private_name=now_time.strftime("%Y%m%d%H%M%S_private.txt")
#   with open(private_name,mode="w")as f2:
#     f2.write(f"{x}\n{p}\n")#qは復号化に必要
  print(f"{p}\n{q}\n{g}\n{y}\n")
  print(f"{x}\n")
  print(time.time()-starttime)
if __name__=="__main__":
  main()