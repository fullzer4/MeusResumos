from random import randint
import time

min = 0
max = 0
n = 0

inicialListNumber = 0
finalListNumber = 100000000
randomN = 0
attempts = 0

sucess = False

def start():
    
    global finalListNumber, n, randomN, max, attempts
    
    inicial = time.time()
    
    n = finalListNumber / 2
    randomValue()
    if(randomN > n):
        max = finalListNumber
    
    attempt()
    
    while(sucess == False):
        predicts()
        if( n == 0):
            break
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
    
def predicts():
    
    global n, max, min
    
    n = (max + min) / 2
    n = round(n)
    
    attempt()
    
def attempt():
    
    global n, max, min, randomN, sucess
    
    if(n > randomN):
        max = n
    elif(n < randomN):
        min = n
    else:
        sucess = True
        print("")
        print("sucess")
        print("")
        
start()