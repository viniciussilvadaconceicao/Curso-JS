function geratabela(){
    var valor = document.getElementById('valor')
    var inicio = 1
    var final = 10 
    var passo = 1
    var rsp = document.getElementById('rsp')
    for (var cont = inicio; cont <= final; cont += passo){
        rsp.innerHTML += `${valor.value} x ${cont} = ${valor.value * cont} <br>`
    }
}