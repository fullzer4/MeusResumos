from random import randint
import time

n = 0
randomN = 0

inicialListNumber = 0
finalListNumber = 100000000

attempts = 0

sucess = False

def start():
    
    global finalListNumber, n, randomN, attempts
    
    inicial = time.time()
    
    n = finalListNumber / 2
    randomValue()
    
    while(sucess == False):
        
        attempt()
        attempts = attempts + 1
        
    end = time.time()
    result = end - inicial
    print("")
    print("Numero aleatorio entre {0} e 0 selecionado: {1}".format(finalListNumber, randomN))
    print("O algoritimo levou {0}".format(result))
    print("Numero de tentativas {0}".format(attempts))
    print("")
    
def randomValue():
    
    global randomN
    
    randomN = randint(inicialListNumber, finalListNumber)
    
def attempt():
    
    global n, randomN, sucess
    
    if(n != randomN):
        n = n + 1
    else:
        sucess = True
        print("")
        print("sucess")
        print("")
        
start()