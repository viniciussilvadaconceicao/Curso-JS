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
