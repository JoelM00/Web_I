/*
var p = document.createElement("p");
p.innerHTML = "Ola, pessoal!";

var img = document.createElement("img");
img.src = "js.png";

document.getElementById("conteudo").appendChild(p);
document.getElementById("conteudo").appendChild(img);

document.getElementById("conteudo").removeChild(img);
*/
/*
console.log(
    document.body.childNodes
)

var lista = document.body.childNodes;
alert(lista[5].childNodes[3].childNodes[0].nodeValue);

console.log(
    document.getElementById("ilheus").parentNode.parentNode
)
*/

/*
document.getElementById("btn-set").addEventListener("click",function() {
    document.getElementById("title").setAttribute("class","red");
})

document.getElementById("btn-remove").addEventListener("click",function(){
    document.getElementById("title").removeAttribute("class");
})

document.getElementById("btn-get").addEventListener("click",function(){
    var value = document.getElementById("title").getAttribute("class");
    document.getElementById("paragrafo").innerHTML = value;
})
*/
/*

var titulo = document.querySelector("h1");
var texto = document.createTextNode("Um qualquer texto");

titulo.appendChild(texto);

titulo.textContent = "Um novo texto";
*/

/*
var lista = document.getElementsByTagName("ul")[0];
var itens = lista.children;

var novoItem = document.createElement("li")
novoItem.textContent = "Suco de laranja";

lista.insertBefore(novoItem,itens[1]);

var lista2 = document.getElementsByTagName("ul")[1];
var itens = lista2.children;
var novoItem2 = document.createElement("li");
novoItem2.textContent = "Margarina";

lista2.replaceChild(novoItem2,itens[2]);

console.log(lista2);
*/
/*
//Array
var frutas = ["ananas","maca"];

//Object
var carro = new Object();
carro.ano = 2000;
carro.marca = "BMW";
carro.potencia = 300;
carro.cor = "red";

alert(typeof(carro.ano));

//function
var soma = function(a,b) {
    return a+b;
}

alert(typeof(soma));
*/
/*
let meuArray = ["Ola, mundo!",
                123,
                3.42342,
                {ano: 2000,marca: "BMW",serie: "M4"},
                ["sony","xperia","1","iii"],
            ];

console.log(meuArray[4][3])
*/
/*
let pessoa = {
    nome: "Joel Martins",
    idade: 21,
    altura: 1.78,
    feliz: true,
    pets: ['kika','mimi','gato'],
    carros: {
        camaro: {
            placa: "123456",
            cor: "verde",
        },
        mustang: {
            placa: "543221",
            cor: "vermelho",
        }
    },
    andar: function(distancia){
        alert(pessoa.nome+" andou "+distancia+" kms")
    }
}

pessoa.andar(1234213);
console.log(pessoa.carros.mustang.cor)
*/

/*
let paises = document.getElementsByClassName("pais")

for(let i=0; i<paises.length; i++) {
    console.log(paises[i].innerHTML)
} 

var i = 0;
while(i < paises.length) {
    console.log(paises[i].innerHTML);
    i++;
}
*/
/*
let fruta = {
    nome: "Maca",
    preco: 2.4,
    unidade: 1,
}

let aparelhos = ['SmarTV','smartPhone','smartSony'];

for(let valor in fruta) {
    console.log(valor);
}

for(let valor of aparelhos){
    console.log(valor);
}
*/
/*
function soma(x,y) {
    return x+y;
}

document.getElementById("resultado").innerHTML = soma(3,4);
*/
/*
var nome = prompt("Diga o seu nome:");
alert(nome);
*/
/*
var conf = confirm("Tem certeza que deseja excluir esse item?");
alert(conf);
*/