//aula 1 //

document.querySelector('h1.content-head__title').innerText='Vinicius é a grande promessa no mundo da programação'

document.querySelector('h2.content-head__subtitle').innerText=
'nascido em duque de caxias, Rio dejaneiro e criado na cidade de Deus e Saquarema, ele se esforça para ser o top 1 do Rio de janeiro '

 
//operadores lógicos
// && (e) || (ou) ! (não)
var n1 = 5
var n2 = 8
true && true // true pois os dois são verdadeiros
true && false // false pois um é verdadeiro e o outro falso
false && true // false pois um é verdadeiro e o outro falso
true || true // true pois um é verdadeiro
true || false // true pois um é verdadeiro
false || true // true pois um é verdadeiro
n1 <= n2 || n2 / 2 == 2 // no primeiro caso verdadeiro , no segundo falso , o resultado é verdadeiro pois o || aceita verdadeiro se um dos dois for verdadeiro
n1 > n2 && n1 % 2 == 0 // no primeiro caso falso , no segundo verdadeiro , o resultado é falso pois o && so aceita verdadeiro se os dois forem verdadeiros
//var idade = 27
var  estado  ='RJ'
var salario = 2800
var sexo = 'M'

idade >= 15 && idade <= 20 // a idade está entre 15 e 20 anos
estado == 'RJ' || estado == 'SP' // o estado é RJ ou SP
salario > 2000 && sexo != 'F' // o salário é maior que 2000 e o sexo é diferente de feminino

//ternario 
teste ? 'verdadeiro' : 'falso' // teste é verdadeiro ou falso sempre nessa ordem
teste ? 'aprovado' : 'reprovado'
var media = 5
media >= 7 ? 'aprovado' : 'reprovado'

var x = 8
var rsp = x % 2 == 0 ? 'par' : 'impar' // se o resto da divisão por 2 for 0 é par , se não é impar
var idade = 27
var resp = idade >= 18 ? 'MAIOR DE IDADE' : 'MENOR DE IDADE' // se a idade for maior ou igual a 18 é maior de idade , se não é menor de idade