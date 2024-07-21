function adicionar(){
    let numero = document.getElementById('numero').value;
    let selnum = document.getElementById('selnum');
    if (numero === ''){
        alert('Por favor, digite um número!');
    } else if(numero < 1 || numero > 100){
        alert('Por favor, digite um número entre 1 e 100!');
    } else {
        let item = document.createElement('option');
        item.innerHTML = `Valor ${numero} adicionado.`;
        selnum.appendChild(item);
    }
}