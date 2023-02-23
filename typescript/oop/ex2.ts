{
    interface user {
        nome: string;
        sobrenome: string;
        idade: number;
        cpf: number;
      
        login(): void;
    }
      
    class Usuario implements user {
        constructor(
        public nome: string,
        public sobrenome: string,
        public idade: number,
        public cpf: number
    ) {}
      
        login(): void {
          console.log(`voce foi logado com sucesso: ${this.nome} ${this.sobrenome}`);
        }
    }
      
    const usuario1 = new Usuario("gabriel", "pelizzaro", 16, 43242532);
      
    usuario1.login();
}