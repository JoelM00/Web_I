<?php

$db = 1234.56;
$preco = number_format($db,2,",",".");
echo "Valor do produto e $preco";

echo "<br>";

echo "Arredondado: ".round(5.134543)."<br>";
echo "Arredondado para cima: ".ceil(5.134543)."<br>";
echo "Arredondado para baixo ".floor(5.134543)."<br>";
echo rand(1,20);