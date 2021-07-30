<?php

namespace App\Model;

use PDO;

class ProdutoDAO {
    public function create(Produto $p) {
        $sql = "insert into produtos (nome,descricao) values ('?,?')";

        $stmt = Conexao::getConn()->prepare($sql);
        $stmt->bindValue(1,$p->getNome());
        $stmt->bindValue(2,$p->getDescricao());

        $stmt->execute();
    }

    public function read() {
        $sql = "select * from produtos";

        $stmt = Conexao::getConn()->prepare($sql);
        $stmt->execute();

        if ($stmt->rowCount() > 0):
            $resultado = $stmt->fetchAll(PDO::FETCH_ASSOC);
            return $resultado;
        else:

        endif;
    }

    public function update(Produto $p) {

    }

    public function delete($id) {

    }
}