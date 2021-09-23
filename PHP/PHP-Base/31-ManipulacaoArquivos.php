<?php

$arquivo = 'arquivo.txt';
$conteudo = "diufjnfgdfkjngfgghdfgdfgdfgdfgdfg\r\n";
$tamanhoArquivo = filesize($arquivo);

$arquivoAberto = fopen($arquivo,"r");
//fwrite($arquivoAberto,$conteudo);

while (!feof($arquivoAberto)):
    $linha = fgets($arquivoAberto,$tamanhoArquivo);
    echo $linha;
endwhile;


fclose($arquivoAberto);
