<?php

class Pessoa {
    public $idade;

    public function __clone() {
        echo "Clonagem de objetos";
    }
}

$pessoa = new Pessoa();
$pessoa->idade = 25;

$pessoa2 = $pessoa; //apontador
$pessoa2->idade = 34;

$pessoa3 = clone($pessoa);
$pessoa3->idade = 10;

echo $pessoa->idade."<br>";
echo $pessoa3->idade."<br>";