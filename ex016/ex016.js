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
            rsp.innerHTML += `${cont} \u{1F449}`// Adiciona uma quebra de linha após cada valor
        }// Adiciona uma bandeira de chegada após a contagem 
    }rsp.innerHTML += '\u{1F3C1}'// Adiciona uma bandeira de chegada após a contagem
}

/*https://www.unicode.org/emoji/charts/full-emoji-list.html* site dos emoji para javaScrip 
para inserir o emogi \u{aqui o codigo do emoji} */