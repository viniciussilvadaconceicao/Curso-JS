function Verificar(){
    var agora = new Date()
    var hora = agora.getHours()
    var resp = window.document.getElementById('resp')
    var fot = window.document.getElementById('fot')
    

    if(hora >= 0 && hora < 12){
        fot.innerHTML = '<img id="imagem" src="imagem/manha.jpg" alt="foto do dia"></img>'
        resp.innerHTML = `Agora são ${hora} horas. Bom dia!`
        document.body.style.background = 'yellow'
        document.body.style.color = 'black'
        
    }
    else if(hora >= 12 && hora < 18){
        fot.innerHTML = ' <img src="imagem/tarde.jpg" alt="foto da tarde"></img>'
        resp.innerHTML = `Agora são ${hora} horas. Boa tarde!`
        document.body.style.background = ' rgb(248, 132, 65)'
        document.body.style.color = 'black'
    }
    else{
        fot.innerHTML = '<img src="imagem/noite.jpg" alt="foto da noite"></img></img>'
        resp.innerHTML = `Agora são ${hora} horas. Boa noite!`
        document.body.style.background = 'rgb(39, 27, 55)'
        document.body.style.color = 'white'
    }
}