function geratabela(){
    var valor = document.getElementById('valor')
    var inicio = 1
    var final = 10 
    var passo = 1
    var rsp = document.getElementById('rsp')
    for (var cont = inicio; cont <= final; cont += passo){
        if (valor.value == ''){
            alert('Digite um valor na caixa de texto')
            rsp.innerHTML = 'Impossível gerar a tabuada!'
            return;
        } else if(valor.value <= 0){
            alert('digite valores positivos')
            rsp.innerHTML = 'Impossível gerar a tabuada com numeros negativos!'
        } else if (valor.value > 0){
            rsp.innerHTML += `${valor.value} X ${cont} = ${valor.value * cont} <br>`
        }
    }
}