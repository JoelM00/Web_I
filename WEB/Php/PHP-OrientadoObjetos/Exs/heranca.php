<?php

class Veiculo {
    private $modelo;
    public $cor;
    public $ano;

    protected function andar() {
        echo "Andou!<br>";
    }

    public function parar() {
        echo "Parou!<br>";
    }

    public function getModelo() {
        return $this->modelo;
    }

    public function setModelo($modelo) {
        $this->modelo = $modelo;
    }

}


class Carro extends Veiculo {
    public function limpaBrisa() {
        echo "limpador ligado!<br>";
        $this->andar();
    }
}

class Moto extends Veiculo {
    public function darGrau() {
        echo "a dar grau!<br>";
    }
}

$mota = new Moto();
//$mota->setModelo("Yamaha");
$mota->cor = "vermelho";
$mota->ano = 2000;

$mota->parar();
$mota->darGrau();

$carro = new Carro();
$carro->cor = "Amarelo";
$carro->setModelo("Lamborghini");
$carro->ano = 2000;

$carro->limpaBrisa();
//$carro->andar();

