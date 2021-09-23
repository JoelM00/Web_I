<?php

class Newsletter {
    public function cadastrarEmail($email) {

        if (!filter_var($email,FILTER_VALIDATE_EMAIL)):
            throw new Exception("Este email nao e valido!",2341);
        else:
            echo "Email registado com sucesso!";
        endif;
    }
}

$newsletter = new Newsletter();
try {
    $newsletter->cadastrarEmail("o@ds");
} catch (Exception $e) {
    echo "Mensagem: ".$e->getMessage()."<br>";
    echo "Codigo: ".$e->getCode()."<br>";
    echo "Line: ".$e->getLine()."<br>";
    echo "Arquivo: ".$e->getFile()."<br>";
}
