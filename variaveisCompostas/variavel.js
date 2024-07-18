let num = [5, 2, 1, 4, 3]
num[5] = 6// Adiciona um elemento na posição que eu quiser
num.push(7)// Adiciona um elemento no final do array
num.sort()// Ordena os elementos do array
console.log(`${num.length} elementos`)// Mostra o tamanho do array
console.log(`eles são ${num}`)

for (let pos=0; pos<num.length; pos++){
    console.log(num[pos])
}