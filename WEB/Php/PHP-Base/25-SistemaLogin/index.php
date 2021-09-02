<?php
    //Conexao
    require_once 'db_connect.php';

    //Sessao
    session_start();

    //botao enviar
    if (isset($_POST['btn-entrar'])):
        $erros = array();
        $login = mysqli_escape_string($connect,$_POST['login']);
        $senha = mysqli_escape_string($connect,$_POST['senha']);

        if (empty($login) or empty($senha)):
            $erros[] = "<li> O campo login/senha precisa de ser preenchido </li>";
        else:
            $sql = "select login from users where login = '$login'";
            $resultado = mysqli_query($connect,$sql);

            if (mysqli_num_rows($resultado) > 0):
                $sql = "select * from users where login = '$login' and senha = '$senha'";
                $resultado = mysqli_query($connect,$sql);

                if (mysqli_num_rows($resultado) == 1):
                    $dados = mysqli_fetch_array($resultado);
                    mysqli_close($connect);

                    $_SESSION['logado'] = true;
                    $_SESSION['id_user'] = $dados['id'];
                    header('Location: home.php');
                else:
                    $erros[] = "<li> User e senha nao fazer match! </li>";
                endif;
            else:
                $erros[] = "<li> User inexistente </li>";
            endif;
        endif;
    endif;
?>

<html>
<head>
    <title>Login</title>
    <meta charset="utf-8"
</head>
<body>
    <h1>Login</h1>

    <?php
        if (!empty($erros)):
            foreach ($erros as $erro):
                echo $erro;
            endforeach;
        endif;
    ?>
    <hr>
    <form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="POST">
        Login: <input type="text" name="login"><br>
        Senha: <input type="password" name="senha"><br>
        <button type="submit" name="btn-entrar">Entrar</button>
    </form>
</body>
</html>