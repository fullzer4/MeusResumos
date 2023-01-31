extern crate rand;

use rand::prelude::*;
use std::time::Instant;

fn random_value(min: f32, max: f32) -> f32 {
    let mut rng = thread_rng();
    let random_number = rng.gen_range(min, max + 1.0);
    return random_number
}

fn predict(min: f32, max: f32 ) -> f32 {

    let mut n = (max + min) / 2.0;
    n =  n.round();
    return n
}

fn attempt(n: f32, min: f32, max: f32, random_n: f32, sucess: bool) -> (f32, f32, f32, bool) {
    
    if n > random_n {
        let mut max = n;
        println!("maior {}", n);
    }else if n < random_n {
        let mut min = n;
        println!("menor {}", n);
    }else{
        let mut sucess = true;
    }

    let value = (n, min, max, sucess);
    
    return value;
}


fn main() {

    let mut INICIAL_LIST_NUMBER: f32 = 0.0;
    let mut FINAL_LIST_NUMBER: f32 = 100000000.0;

    let mut n: f32 = 0.0;
    let random_n = random_value(INICIAL_LIST_NUMBER, FINAL_LIST_NUMBER);

    let mut attempts = 0;

    let mut sucess = false;

    let start = Instant::now();

    n = FINAL_LIST_NUMBER / 2.0;

    while sucess == false {

        n = predict(INICIAL_LIST_NUMBER, FINAL_LIST_NUMBER);
        let mut values = attempt(n, INICIAL_LIST_NUMBER, FINAL_LIST_NUMBER, random_n, sucess);
        
        if values.3 == true{
            sucess = true;
        }else{
            n = values.0;
            INICIAL_LIST_NUMBER = values.1;
            FINAL_LIST_NUMBER = values.2;
            attempts = attempts + 1;
            println!("{}", n)
        }

    }

    let duration = start.elapsed();

    println!("");
    println!("Numero aleatorio entre {} e 0 selecionado: {}", FINAL_LIST_NUMBER, random_n);
    println!("O algoritimo levou {:?}", duration);
    println!("Numero de tentativas {}", attempts);
    println!("");
}