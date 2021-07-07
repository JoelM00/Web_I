<?php

$nome = "Joel";
$a = 1;
$b = 3;
$c = 7;

function mostraNome() {
    global $nome;
    echo $nome;
}

mostraNome();

////////////////////////
function mostraCidade() {
    global $cidade;
    $cidade = "Viana";
}

mostraCidade();
echo $cidade;
echo "<br>";
////////////////////////

function soma() {
    echo $GLOBALS['a'] + $GLOBALS['b'] + $GLOBALS['c'];
}

soma();
