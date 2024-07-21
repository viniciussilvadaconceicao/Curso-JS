function adicionar() {
    let num = document.getElementById('numero').value;
    let lista = document.getElementById('selnum');
    
    if (num === '') {
        alert('Por favor, digite um número!');
    } else if (num < 1 || num > 100) {
        alert('Por favor, digite um número entre 1 e 100!');
    } else {
        let opcaoExistente = false;
        
        for (let i = 0; i < lista.options.length; i++) {
            if (num === lista.options[i].value) {
                opcaoExistente = true;
                break;
            }
        }
        
        if (opcaoExistente) {
            alert('Número já adicionado!');
        } else {
            let item = document.createElement('option');
            item.text = `Valor ${num} adicionado.`;
            item.value = num; 
            lista.appendChild(item);
        }
    }
}

function finalizar(){
    let lista = document.getElementById('selnum');
    let rsp = document.getElementById('rsp');
    let total = lista.length;
    let soma = 0;
    let maior = 0;
    let menor = Number(lista[0].value)
    if (total === 0){
        alert('Adicione valores antes de finalizar!');
    } else if(total === 1){
        alert('Adicione mais valores antes de finalizar!');
    } else {
        for(let i = 0; i < total; i++){
            soma += Number(lista[i].value);
            
            if (Number(lista[i].value) > maior){
                maior = Number(lista[i].value);
            }
            
            if (Number(lista[i].value) < menor){
                menor = Number(lista[i].value);
            }
        }
        
        rsp.innerHTML = '';
        rsp.innerHTML += `<p>Ao todo, temos ${total} números cadastrados.</p>`;
        rsp.innerHTML += `<p>O maior valor informado foi ${maior}.</p>`;
        rsp.innerHTML += `<p>O menor valor informado foi ${menor}.</p>`;
        rsp.innerHTML += `<p>Somando todos os valores, temos ${soma}.</p>`;
        rsp.innerHTML += `<p>A média dos valores digitados é ${soma/total}.</p>`;
    }
}