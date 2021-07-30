<?php

require_once 'Projeto/autoload.php';

$produto = new App\Model\Produto();
$produto->setNome('Sony xperia');
$produto->setDescricao('256gb');

$produtoDAO = new \App\Model\ProdutoDAO();
$produtoDAO->create($produto);