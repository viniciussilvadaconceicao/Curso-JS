function contar(){
    var inicio = document.getElementById('txtinicio')
    var fim = document.getElementById('txtfim')
    var passo = document.getElementById('txtpasso')
    var rsp = document.getElementById('rsp')
    
    for (var cont = Number(inicio.value); cont <= Number(fim.value); cont += Number(passo.value)){
        if (inicio.value == '' || fim.value == '' || passo.value == ''){
            alert('Preencha todos os campos!')
            rsp.innerHTML = 'Impossível contar!'
            return; 

        } else if (passo.value <= 0){
            alert('Passo inválido! Considerando passo 1')
            passo.value = 1
            return;
        } else {
            rsp.innerHTML += `${cont}<br>` // Adiciona uma quebra de linha após cada valor
        }
    }
}

