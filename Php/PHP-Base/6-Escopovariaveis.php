<?php
//Escopo Global
$nome = "Joel Martins";
$a = 1;
$b = 3;
$c = 8;

function exibeNome() {
    //Escopo local
    global $nome;
    echo $nome;
}

exibeNome();
echo "<hr>";

function exibeCidade() {
    global $cidade;
    $cidade = "Lisboa";
}

exibeCidade();
echo $cidade;
echo "<hr>";

///////////////////
function soma() {
    //Acesso a variaveis globais
    echo $GLOBALS['a'] + $GLOBALS['b'] + $GLOBALS['c'];
}

soma();