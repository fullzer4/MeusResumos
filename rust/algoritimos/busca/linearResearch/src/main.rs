extern crate rand;

use rand::prelude::*;
use std::time::Instant;

fn random_value(min: i32, max: i32) -> i32 {
    let mut rng = thread_rng();
    let random_number = rng.gen_range(min, max + 1);
    return random_number
}


fn main() {

    const INICIAL_LIST_NUMBER: i32 = 0;
    const FINAL_LIST_NUMBER: i32 = 100000000;

    let mut n = 0;
    let random_n = random_value(INICIAL_LIST_NUMBER, FINAL_LIST_NUMBER);

    let mut attempts = 0;

    let mut sucess = false;

    let start = Instant::now();

    n = FINAL_LIST_NUMBER / 2;

    while sucess == false {

        if n != random_n{
            n = n + 1;
            attempts = attempts + 1;
        }else{
            sucess = true;
            println!("");
            println!("Sucess");
            println!("");
        }

    }

    let duration = start.elapsed();

    println!("");
    println!("Numero aleatorio entre {} e 0 selecionado: {}", FINAL_LIST_NUMBER, random_n);
    println!("O algoritimo levou {:?}", duration);
    println!("Numero de tentativas {}", attempts);
    println!("");
}