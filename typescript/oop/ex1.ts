abstract class user {
    public nome: string;
    public sobrenome: string;
    public idade: number;
    private cpf: number;
    static createat: Date = new Date();

    constructor(nome: string, sobrenome: string, idade: number, cpf: number){
        this.nome = nome
        this.sobrenome = sobrenome
        this.idade = idade
        this.cpf= cpf
    }
}

class Usuario extends user {

    login() :void { //metodo login
        console.log(`voce foi logado com sucesso: ${this.nome} ${this.sobrenome}`);

    }
}

const usuario1 = new Usuario("gabriel","pelizzaro",16,43242532)

usuario1.login()