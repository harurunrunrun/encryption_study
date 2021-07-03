#include "multipleintegers/int_multiple.h"
#include <string>
#include <vector>
#include <iostream>
#include <time.h>
using namespace std;
using namespace multipleintegers;

bool prime(string p){
  int i=0;
  string a,p1=sub(p,"1");
  while(i<40){
    a=random_range("2",p1);
    if(pow(a,p1,p)!="1")return false;
    i++;
  }
  return true;
}

vector<string> step1(int l){
  string p,q;
  vector<string> ret;
  while(true){
    q=randbit(l);
    if(prime(q)){
      p=add(mul(q,"2"),"1");
      if(prime(p)){
        ret={p,q};
        return ret;
      }
    }
  }
}

string step2(string p,string q){
  string g,p2=sub(p,"2");
  while(true){
    g=random_range("2",p2);
    if(pow(g,q,p)!="1"){
      return g;
    }
  }
}

int main(){
  clock_t start=clock();
  vector<string> st=step1(1024);
  cout<<"step1 finish"<<endl;
  string p=st.at(0),q=st.at(1);
  string q2=sub(q,"2");
  string g=step2(p,q);
  cout<<"step2 finish"<<endl;
  string x=random_range("2",q2);
  string y=pow(g,x,p);
  clock_t end=clock();
  cout<<"p"<<endl<<p<<endl<<endl;
  cout<<"q"<<endl<<q<<endl<<endl;
  cout<<"g"<<endl<<g<<endl<<endl;
  cout<<"y"<<endl<<y<<endl<<endl;

  cout<<"x"<<endl<<x<<endl<<endl;


  double time=static_cast<double>(end-start)/CLOCKS_PER_SEC*100.0;
  cout<<"time: "<<time<<endl;
  return 0;
}