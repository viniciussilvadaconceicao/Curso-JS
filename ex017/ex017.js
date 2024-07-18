function geratabela() {
    var valor = document.getElementById('valor');
    var inicio = 1;
    var final = 10;
    var passo = 1;
    var tab = document.getElementById('seltab');
    var rsp = document.getElementById('rsp')

    if (valor.value == '') {
        alert('Digite um valor!');
        return;
    } else {
        for (var cont = inicio; cont <= final; cont += passo) {
            var item = document.createElement('option');
            item.style.margin = '8px';
            item.style.padding = '8px';  
            rsp.innerHTML = `<strong>Tabuada de ${valor.value} gerada com sucesso!</strong>`;
            rsp.style.color = 'green';
            rsp.style.font = 'normal 20pt Arial'; 
            item.textContent = `${valor.value} x ${cont} = ${valor.value * cont}`;
            tab.appendChild(item);
        }
    }
}