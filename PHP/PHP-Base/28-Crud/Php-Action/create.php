<?php
//Sessao
session_start();

//Conexao
require_once 'db_connect.php';

//Clear
function clear($input) {
    global $connect;
    //Sql
    $var = mysqli_escape_string($connect,$input);
    //Xss
    $var = htmlspecialchars($var);
    return $var;
}

if (isset($_POST['btn-registar'])):
    $nome = clear($_POST['nome']);
    $sobrenome = clear($_POST['sobrenome']);
    $email = clear($_POST['email']);
    $idade = clear($_POST['idade']);

    $sql = "INSERT INTO clientes (nome,sobrenome,email,idade) VALUES ('$nome','$sobrenome','$email','$idade')";

    if (mysqli_query($connect,$sql)):
        $_SESSION['mensagem'] = "Registo com sucesso!";
        header('Location: ../Associacao.php');
    else:
        $_SESSION['mensagem'] = "Erro ao registar!";
        header('Location: ../Associacao.php');
    endif;


endif;