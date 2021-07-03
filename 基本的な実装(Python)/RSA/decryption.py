from os.path import basename
name1=input("公開鍵ファイル名")
name2=input("暗号化するファイル名")
name3=basename(name2)
with open(name1) as key_f:
  N=int(key_f.readline())
  e=int(key_f.readline())
  with open(name2)as en_f:
    g=int(en_f.read())
    c=pow(g,e,N)
    with open(f"enc_{name3}",mode="w") as new_f:
      new_f.write(f"{c}\n")
