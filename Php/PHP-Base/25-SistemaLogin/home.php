<?php
    //Conexao
    require_once 'db_connect.php';

    //Sessao
    session_start();

    //Verificacao
    if (!isset($_SESSION['logado'])):
        header('Location: Associacao.php');
    endif;

    //Dados
    $id = $_SESSION['id_user'];
    $sql = "select * from users where id = '$id'";

    $resultado = mysqli_query($connect,$sql);
    $dados = mysqli_fetch_array($resultado);

    mysqli_close($connect);
?>

<html>
<head>
    <meta charset="UTF-8">
    <title>Pagina restrita</title>
</head>
<body>

    <h1>Ola <?php echo $dados['nome'] ?></h1>

    <a href="logout.php">Sair</a>

</body>
</html>
