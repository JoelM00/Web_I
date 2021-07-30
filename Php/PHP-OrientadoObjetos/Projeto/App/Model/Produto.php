<?php

namespace App\Model;

class Produto {
    private $id, $nome, $descricao;

    public function getNome() {
        return $this->nome;
    }

    public function getDescricao() {
        return $this->descricao;
    }

    public function getId() {
        return $this->id;
    }

    public function setDescricao($descricao) {
        $this->descricao = $descricao;
    }

    public function setNome($nome) {
        $this->nome = $nome;
    }

    public function setId($id) {
        $this->id = $id;
    }

}