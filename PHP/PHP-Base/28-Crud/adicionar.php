<?php
//Header
include 'includes/header.php';
?>

<div class="row">
    <div class="col s12 m6 push-m3">
        <h3 class="light">Novo Cliente</h3>

        <form action="Php-Action/create.php" method="POST">
            <div class="input-field col s12">
                <input type="text" name="nome" id="nome">
                <label for="nome">Nome</label>
            </div>
            <div class="input-field col s12">
                <input type="text" name="sobrenome" id="sobrenome">
                <label for="sobrenome">SobreNome</label>
            </div>
            <div class="input-field col s12">
                <input type="email" name="email" id="email">
                <label for="email">Email</label>
            </div>
            <div class="input-field col s12">
                <input type="text" name="idade" id="idade">
                <label for="idade">Idade</label>
            </div>
            <button type="submit" name="btn-registar" class="btn">Registar</button>
            <a href="index.php" class="btn green">Listar</a>
        </form>

    </div>
</div>

<?php
//Footer
include 'includes/footer.php';
?>