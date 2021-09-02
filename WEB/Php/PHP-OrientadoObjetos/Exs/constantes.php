<?php

class Pessoa {
    const nome = "Joel";

    public function exibirNome() {
        echo self::nome;
    }
}

class Joel extends Pessoa {
    const nome = "Martins";

    public function exibirNome() {
        echo parent::nome;
        echo self::nome;
    }
}


$joel = new Joel();
$joel->exibirNome();

