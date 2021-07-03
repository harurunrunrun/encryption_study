from random import randint
import sys
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

def sub1():
  p,q=step1()
  n=p*q
  la=lcm(p-1, q-1)
  g=n+1
  L=(pow(g,la,n*n)-1)//n
  #-1乗がバグってる->n:素数じゃない。
  u=inv_mod(L,n)
  print(p)
  print(q)
  print("公開鍵n,g")
  print(n)
  print(g)
  print("秘密鍵la,u")
  print(la)
  print(u)
  return

def main():
  sub1()
  return

if __name__=="__main__":
  main()
