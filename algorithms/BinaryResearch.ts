{
    let min:number = 0
    let max:number = 0
    let n:number = 0

    let inicialListNumber:number = 0
    let finalListNumber:number = 1000
    let randomN:number = 0
    let attempts:number = 0

    let sucess:boolean = false

    const start = () => {

        //start
        const inicial = performance.now();
        randomValue()
        n = finalListNumber/2
        if(randomN > n){ // prevent failure
            max = finalListNumber
        }
        attempt() // delete initial forecast

        //loop
        while(sucess === false){
            predicts()
            if( n === 0){
                break
            }
            attempts++
        }

        //sucess
        const end = performance.now();
        console.log("")
        console.log(`Numero aleatorio entre ${finalListNumber} e 0 selecionado: ${randomN}`)
        console.log(`O algoritimo levou ${end - inicial} ms`);
        console.log(`Numero de tentativas ${attempts}`);
        console.log("")

    }

    const randomValue = () => {

        randomN = Math.floor(Math.random() * (finalListNumber - inicialListNumber) + inicialListNumber)

    }

    const predicts = () => {
    
        n = (max + min) / 2
        Math.round(n)
        

        attempt()

    }

    const attempt = () => {

        if(n > randomN){
            max = n
        }else if(n < randomN){
            min = n
        }else{
            sucess = true
            console.log("")
            console.log("sucess")
            console.log("")
        }

    }

    start()
}