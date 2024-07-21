function adicionar() {
    let numero = document.getElementById('numero').value;
    let selnum = document.getElementById('selnum');
    
    if (numero === '') {
        alert('Por favor, digite um número!');
    } else if (numero < 1 || numero > 100) {
        alert('Por favor, digite um número entre 1 e 100!');
    } else {
        let optionExists = false;
        
        for (let i = 0; i < selnum.options.length; i++) {
            if (numero === selnum.options[i].value) {
                optionExists = true;
                break;
            }
        }
        
        if (optionExists) {
            alert('Número já adicionado!');
        } else {
            let item = document.createElement('option');
            item.text = `Valor ${numero} adicionado.`;
            item.value = numero; // Add this line to set the value of the option
            selnum.appendChild(item);
        }
    }
}
