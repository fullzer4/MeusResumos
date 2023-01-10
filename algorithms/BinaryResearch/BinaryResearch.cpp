#include <iostream>
#include <cstdlib>
#include <ctime>
#include <cmath>

int min = 0;
int max = 0;
int n = 0;

int inicialListNumber = 0;
int finalListNumber = 1000;
int randomN = 0;
int attempts = 0;

bool sucess = false;

int randomValue(){

    srand((unsigned)time(0));
    randomN = rand()%(finalListNumber-inicialListNumber+1) + inicialListNumber;
    
    return 0;
}

int attempt(){

    if(n > randomN){
        max = n;
    }else if (n < randomN){
        min = n;
    }else{
        sucess = true;
        printf("/n sucess");
    }
    
    return 0;
}

int predicts(){

    n = ( max + min ) / 2;
    n - round(n);
    
    attempt();

    return 0;
}

int main (int argc, char const* argv[]){
    
    time_t start, end;
    randomValue();
    n = finalListNumber / 2;
    if(randomN > n){
        max = finalListNumber;
    }
    attempt();

    while (sucess == false){
        predicts();
        if (n == 0){
            break;
        }
        attempts++;
    }
    
    std::cout << "Numero Aleatorio entre " << finalListNumber << " e 0 selecionado: " << randomN << std::endl;
    std::cout << "O algoritimo levou " << end - start << std::endl;
    std::cout << "Numero de tentativas " << attempts << std::endl;
    return 0;
}