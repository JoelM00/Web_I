<?php
$senha = "123456";

$novaSenha = base64_encode($senha);
echo "base64: ".$novaSenha."<br>";
echo "Sua senha e: ".base64_decode($novaSenha)."<br>";

echo "<br>";

echo "Md5: ".md5($senha)."<br>";
echo "Sha1: ".sha1($senha)."<br>";

echo "<br>";

$options = [
    'cost' => 13, //seguranca do hash
];

$senha_db = '$2y$13$T/ckg.3Qh/tc3ppa/wJOs.6PevbhNcxRvaifkm42.6Gb8RgaXZqky';

$senhaSegura = password_hash($senha,PASSWORD_DEFAULT, $options);
echo $senhaSegura."<br>";

if (password_verify($senha,$senha_db)):
    echo "Senha valida!";
else:
    echo "Senha invalida!";
endif;

