<?php
//Constantes

define("NOME", "Joel Martins");
define("ALTURA", 23);
define("IDADE", 21);


echo 'Meu nome e:'.NOME.' e a minha idade e: '.IDADE.' e meco: '.ALTURA;
echo "<hr>";

/*define("TIMES", ['ola1','ola2','ola3']);

echo TIMES[0];
*/

function exibeNome() {
    echo NOME;
}

exibeNome();