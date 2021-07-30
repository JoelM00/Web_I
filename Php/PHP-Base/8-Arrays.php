<?php
$carros = array("BM","MB","LB");
print_r($carros);
echo "<br>";

$carros[] = "BG";

print_r($carros);
echo "<br>";

echo $carros[2];
echo "<br>";

$motos = array();
$motos[] = "yamaha";
$motos[] = "honda";
$motos[100] = "ducati";

print_r($motos);
echo "<br>";

$clientes = ["Joel","Joana","Joao","Joel","Joana","Joao"];
print_r($clientes);
echo "<br>";

//Count
$totalClientes = count($clientes);
echo $totalClientes;
echo "<br>";

//Foreach
foreach ($clientes as $valor) {
    echo $valor."<br>";
}

echo "<br>";echo "<br>";

//Arrays associativos
$pessoa = array("nome"=>"Joel", "idade"=>21, "altura"=>1.80);
$pessoa["cidade"] = "Viana";
print_r($pessoa);

echo "<br>";echo "<br>";

foreach ($pessoa as $key=>$valor) {
    echo $key." : ".$valor."<br>";
}

echo "<br>";echo "<br>";

//Arrays multidimensionais
$times = array(
    "cariocas"=>array("vasco","flamengo","botafogo"),
    "paulistas"=>array("um"=>"santos","dois"=>"sao","tres"=>"palmeiuras"),
    "baianos"=>array("vencedor"=>"bahia","perdedor"=>"vitorias"));

echo $times["cariocas"][2];
echo "<br>";

foreach ($times["baianos"] as $key => $valor) {
    echo $key.":".$valor."<br>";
}

foreach ($times["paulistas"] as $key => $valor) {
    echo $key.":".$valor."<br>";
}