<?php

class Login {
    private $nome;
    private $email;
    private $senha;

    public function __construct($nome,$email,$senha) {
        $this->nome = $nome;
        $this->setEmail($email);
        $this->setSenha($senha);
    }

    public function logar() {
        if ($this->email == "teste@teste.com" and $this->senha=="123456"):
            echo "Logado com sucesso!";
        else:
            echo "Dados incorretos!";
        endif;
    }

    public function setEmail($email) {
        $email = filter_var($email,FILTER_SANITIZE_EMAIL);
        $this->email = $email;
    }

    public function setSenha($senha) {
        $this->senha = $senha;
    }

    public function getSenha() {
        return $this->senha;
    }

    public function getEmail() {
        return $this->email;
    }

    public function getNome() {
        return $this->nome;
    }


    public function setNome($nome) {
        $this->nome = $nome;
    }

}

$login = new Login("Joel Martins","teste@teste.com","123456");
$login->logar();
echo $login->getEmail()."<br>";
echo $login->getSenha()."<br>";