<?php

$nome = "Joel Martins";
var_dump($nome);

if (is_string($nome)):
    echo " -> E uma string";
else:
    echo " -> Nao e uma string";
endif;

//Array
$carros = array("Gol","Uno","Camaro",34,true);

var_dump($carros);

//Object
class Cliente {
    public $nome;

    public function atribuirNome($nome) {
        $this->$nome = $nome;
    }
}

$cliente = new Cliente();
$cliente->atribuirNome("Joel Martins");
var_dump($cliente);

//Especiais
$cidade = "NULL";
var_dump($cidade);
