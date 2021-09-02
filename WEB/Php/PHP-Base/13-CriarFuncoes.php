<?php

function exibirTexto($texto) {
    echo "O texto e: $texto <br>";
}

exibirTexto("Joel Martins");

function calculaMedia($n1,$n2,$n3,$n4,$n5) {
    $somatorio = $n1 + $n2 + $n3 + $n4 + $n5;
    echo $somatorio/5;
    echo "<br>";
}

calculaMedia(1,2,3,4,5);