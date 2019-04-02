#include <iostream>
#include <random>
#include <stdlib.h>

int main(){
  int i;
  float x;
  float y;
      
  srand48(0);

  for (i=0;i<1000;i++){  
    x += drand48();
    y += drand48();
    std::cout << x << " " << y << std::endl;
  }
  
  return 0;
}
