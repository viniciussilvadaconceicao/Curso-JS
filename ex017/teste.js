function tabuada(){
    var valor = 7;
    var inicio = 1;
    var final = 10;
    var passo = 1;
    for (var cont = inicio; cont <= final; cont += passo){
         console.log(`${valor} x ${cont} = ${valor * cont} `);
    }
}
tabuada()