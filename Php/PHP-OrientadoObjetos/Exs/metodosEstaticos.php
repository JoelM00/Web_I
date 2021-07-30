<?php

class Login {
    public static $user;
    public static function verificaLogin() {
        echo "O user ".self::$user." esta logado!";
    }

    public function sairSistema() {
        echo "O user deslogou!";
    }
}

Login::$user = "admin";
Login::verificaLogin();

$login = new Login();
$login->sairSistema();