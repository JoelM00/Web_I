<?php

class Produtos {
    public $nome;
    public $valor;

    public function __construct($nome,$valor) {
        $this->nome = $nome;
        $this->valor = $valor;
    }
}

class Carrinho {
    public $produtos;

    public function adiciona(Produtos $produtos) {
        $this->produtos[] = $produtos;
    }

    public function showProdutos() {
        foreach ($this->produtos as $produto) {
            echo $produto->nome."<br>";
            echo $produto->valor."<hr>";
        }
    }
}

$produto1 = new Produtos("sony","1241");
$produto2 = new Produtos("mouse","50");

$carrinho = new Carrinho();
$carrinho->adiciona($produto1);
$carrinho->adiciona($produto2);

$carrinho->showProdutos();