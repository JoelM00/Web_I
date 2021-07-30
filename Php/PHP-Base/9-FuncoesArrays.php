<?php

$nomes = array("primo"=>"Rodrigo","ton"=>"Joel","javardo"=>"Filipe");
$carros = array("top"=>"mustang","super"=>"Lambo","hyper"=>"Bug");


if (is_array($nomes)):
    echo "e um array";
else:
    echo "nao e um array";
endif;

////////////////////////////////////////////////
echo "<br>";
echo in_array("Rodrigo",$nomes);
echo "<br>";

////////////////////////////////////////////////
if (in_array("Joel",$nomes)):
    echo "Existe no array";
else:
    echo "Nao existe no array";
endif;

////////////////////////////////////////////////
echo "<br>";
$keys = array_keys($nomes);
print_r($keys);

////////////////////////////////////////////////
echo "<br>";
$values = array_values($nomes);
print_r($values);

////////////////////////////////////////////////
echo "<br>";
$donos = array_merge($carros,$nomes);
print_r($donos);

////////////////////////////////////////////////
echo "<br>";
print_r($donos);
echo "<br>";
echo array_pop($donos);
echo "<br>";
print_r($donos);
echo "<br>";
echo array_shift($donos);
echo "<br>";
print_r($donos);
echo "<br>";

////////////////////////////////////////////////
$frutas = array("uva","laranga","maca");
print_r($frutas);
array_push($frutas,"MANGA","PEssego");
array_unshift($frutas,"ANANAS","KIWI");
echo "<br>";
print_r($frutas);
echo "<br>";

////////////////////////////////////////////////
$keys = array("campeao","vice","terceiro");
$values = array("Vasco","Flamengo","BotaFogo");

$times = array_combine($keys,$values);
print_r($times);
echo "<br>";

////////////////////////////////////////////////
$soma = array(5,6,7,4,10.234234);
$total = array_sum($soma);
echo $total;
echo "<br>";

////////////////////////////////////////////////
$data = "10/12/2019";
$novaData = explode('/',$data);
print_r($novaData);
echo "<br>";

$frase = "O meu nome nao e joel";
$array = explode(' ',$frase);

print_r($array);
echo "<br>";

////////////////////////////////////////////////
$nomes = array("Joel","Martins","Neusa","Deusa");
$string = implode(", ",$nomes);

echo $string;