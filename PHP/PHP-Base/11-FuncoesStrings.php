<?php

$nome = "Joel Martins";

$novoNome = strtolower($nome);
echo $novoNome;

echo "<br>";

$mensagem = "Ola, mundo!";
echo substr($mensagem, 4,3);

echo "<br>";

$objeto = "mouse";
$novoObjeto = str_pad($objeto,10, "*",STR_PAD_BOTH);
echo $novoObjeto;
echo "<br>";

$string = str_repeat("Sucesso!",5);
echo $string;
echo "<br>";

$mensagem = "ola, mundo!";
echo strlen($mensagem);
echo "<br>";

$texto = "ola meu ksjdfs ikjdnfgl; jsdfgjun ola joel ola sdkhjgbn ola";
$novoTexto = str_replace("ola","alo",$texto);
echo $novoTexto;
echo "<br>";

echo strpos($texto,"joel");
