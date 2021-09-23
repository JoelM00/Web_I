<html>
<body>

<?php
    if(isset($_POST['enviar-formulario'])):
        //Array de erros
        $erros = array();

        //Limpeza de alguns carateres errados (tipo espacos)
        $nome = filter_input(INPUT_POST,'nome',FILTER_SANITIZE_SPECIAL_CHARS);

        $idade = filter_input(INPUT_POST,'idade',FILTER_SANITIZE_NUMBER_INT);

        $email = filter_input(INPUT_POST,'email',FILTER_SANITIZE_EMAIL);

        $url = filter_input(INPUT_POST,'url',FILTER_SANITIZE_URL);

        //Validacoes
        if(!$idade = filter_input(INPUT_POST,'idade',FILTER_VALIDATE_INT)):
            $erros[] = "Idade tem de ser um inteiro";
        endif;

        if(!$email = filter_input(INPUT_POST,'email',FILTER_VALIDATE_EMAIL)):
            $erros[] = "Email invalido";
        endif;

        if(!filter_var($url,FILTER_VALIDATE_URL)):
            $erros[] = "Url tem de ser uma URL";
        endif;

        //Exibir as mensagens
        if(!empty($erros)):
            foreach ($erros as $erro):
                echo "<li> $erro </li>";
            endforeach;
        else:
            echo "Os dados estao CORRETOS.";
        endif;
    endif;
?>

<form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="POST">
    Nome: <input type="text" name="nome"><br>
    Idade: <input type="text" name="idade"><br>
    Email: <input type="email" name="email"><br>
    URL: <input type="text" name="url"><br>
    <button type="submit" name="enviar-formulario">Enviar</button><br>
</form>

</body>
</html>