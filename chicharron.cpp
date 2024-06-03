#include <iostream>
#include <math.h>
 
 using namespace std;
 int main (){
    float a, b, c, x, z, raiz, resta = 0;
    cout<<"ingrese el valor de A: "; cin>>a;
    cout<<"ingrese el valor de B: "; cin>>b;
    cout<<"ingrese el valor de c: "; cin>>c;

    resta = (-4*a*c);
    raiz = pow(b,2) - resta;
    x = (-(b) + sqrt(raiz))/2;
    z = (-(b) - sqrt(raiz))/2;

    cout<<"el valor de la funcion positiva es: "<<x<<endl;
    cout<<"el valor de la funcion negativa es: "<<z<<endl;

    return 0;
 }