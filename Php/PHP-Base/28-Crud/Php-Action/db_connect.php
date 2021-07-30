<?php
//Conexao com a base de dados
$servername = "localhost";
$username = "root";
$password = "";
$db_name = "crud";

$connect = mysqli_connect($servername,$username,$password,$db_name);
mysqli_set_charset($connect,"utf8");

if (mysqli_connect_error()):
    echo "Connection error!".mysqli_connect_error();
endif;
