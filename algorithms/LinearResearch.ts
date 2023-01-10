{
    let n:number = 0
    let randomN:number = 0

    let inicialListNumber:number = 0
    let finalListNumber:number = 1000

    let attempts:number = 0

    let sucess:boolean = false

    const start = () => {

        //start
        const inicial = performance.now();
        randomValue()

        //loop
        while(sucess === false){
            
            attempt()
            attempts++

        }

        //sucess
        const end = performance.now();
        console.log("")
        console.log(`O algoritimo levou ${end - inicial} ms`);
        console.log(`Numero aleatorio entre ${finalListNumber} e 0 selecionado: ${randomN}`)
        console.log(`Numero de tentativas ${attempts}`);
        console.log("")

    }

    const randomValue = () => {

        randomN = Math.floor(Math.random() * (finalListNumber - inicialListNumber) + inicialListNumber)

    }

    const attempt = () => {
        if(n != randomN){
            n++
            console.log(n)
        }else{
            sucess = true
            console.log("")
            console.log("sucess")
            console.log("")
        }
    }

    start()
}