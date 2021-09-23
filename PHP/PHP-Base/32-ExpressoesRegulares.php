<?php

$string = "abc";
$padrao = "/^[a-z]/";

if (preg_match($padrao,$string)):
    echo "Valido";
else:
    echo "Invalido!";
endif;