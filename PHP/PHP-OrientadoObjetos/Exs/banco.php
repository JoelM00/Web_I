<?php

abstract class Banco {
    protected $saldo;
    protected $limiteSaque;
    protected $juros;

    public function setSaldo($saldo) {
        $this->saldo = $saldo;
    }

    abstract public function sacar();

    public function depositar() {
        echo "Depositado";
    }

}

class Santander extends Banco {
    public function sacar() {
        echo "Sacar dinheiro no banco Santader";
    }
}

class Montepio extends Banco {
    public function sacar() {
        echo "Sacar dinheiro no banco Montepio";
    }
}

$santander = new Santander();
$montepio = new Montepio();

$santander->sacar();
$montepio->sacar();
