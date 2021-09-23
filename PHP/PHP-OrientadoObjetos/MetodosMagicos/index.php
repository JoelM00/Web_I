<?php

class Pessoa {
    private $dados = array();

    public function __set($nome,$valor) {
        $this->dados[$nome] = $valor;
    }

    public function __get($nome) {
        return $this->dados[$nome];
    }

    public function __tostring() {
        return "Tentei imprimir o objeto!<br>";
    }

    public function __invoke() {
        return "Tentei usar um objeto como funcao <br>";
    }
}

$pessoa = new Pessoa();
$pessoa->nome = "Joel";
$pessoa->idade = 50;
$pessoa->sexo = "M";

echo $pessoa->nome."<br>";
echo $pessoa->idade."<br>";
echo $pessoa->sexo."<br>";

echo $pessoa;
echo $pessoa();