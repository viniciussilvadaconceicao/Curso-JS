// exercicio de bom dia boa tarde e boa noite

var agora = new Date()//cria um objeto com a data e hora atual
var hora = agora.getHours()//pega a hora atual

console.log(`Agora são ${hora} Horas `)

if (hora < 12){
    console.log('Bom dia')

}else if (hora <= 18){
    console.log('Boa tarde')
}
else{
    console.log('Boa noite')
}