function adicionar(){
    let num = document.getElementById('numero')
    let lista = document.getElementById('selnum')
    num = num.value

    if (num == ''){
        alert('Por favor, digite um número!')

    } else if (num < 1 || num> 100){
        window.alert('por favor digite um numero entre 1 e 100!')

    }else{
        let opicaoexistente = false

        for (let cont = 0 ; cont < lista.options.length; cont++){
            if (num == lista.options[cont].value){
                opicaoexistente == true
                break
            }
        }
        
        if (opicaoexistente){
            alert('Numero já adicionado!')
        }
        
        else{
            let item = document.createElement('option')
            item.text= `Valor ${num} adicionado.`
            item.value = num
            lista.appendChild(item)
        }
    }
}