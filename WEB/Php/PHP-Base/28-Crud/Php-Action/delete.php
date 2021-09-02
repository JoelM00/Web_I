<?php
//Sessao
session_start();

//Conexao
require_once 'db_connect.php';

if (isset($_POST['btn-deletar'])):
    $id = mysqli_escape_string($connect,$_POST['id']);

    $sql = "delete from clientes where id = '$id'";

    if (mysqli_query($connect,$sql)):
        $_SESSION['mensagem'] = "Apagado com sucesso!";
        header('Location: ../Associacao.php');
    else:
        $_SESSION['mensagem'] = "Erro ao apagar!";
        header('Location: ../Associacao.php');
    endif;


endif;