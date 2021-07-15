let PG2 = document.getElementById('PG2')
console.log(bodyHeight+'px')
PG2.style.height = bodyHeight+'px'

let zr = document.getElementById('zr')
let jc = document.getElementById('jc')
let bt = document.getElementById('bt')

let photo1 = document.querySelector('.photo1')
let photo2 = document.querySelector('.photo2')
let photo3 = document.querySelector('.photo3')

zr.onclick = function (){
    document.querySelector('.js1').style.display = 'block'
    document.querySelector('.js2').style.display = 'none'
    document.querySelector('.js3').style.display = 'none'

    photo1.style.boxShadow = '0 0 5px gold'
    photo2.style.boxShadow = '0 0 0 transparent '
    photo3.style.boxShadow = '0 0 0 transparent '
}
jc.onclick = function (){
    document.querySelector('.js1').style.display = 'none'
    document.querySelector('.js2').style.display = 'block'
    document.querySelector('.js3').style.display = 'none'
    photo1.style.boxShadow = '0 0 0 transparent '
    photo2.style.boxShadow = '0 0 5px gold'
    photo3.style.boxShadow = '0 0 0 transparent '
}
bt.onclick = function (){
    document.querySelector('.js1').style.display = 'none'
    document.querySelector('.js2').style.display = 'none'
    document.querySelector('.js3').style.display = 'block'
    photo1.style.boxShadow = '0 0 0 transparent '
    photo2.style.boxShadow = '0 0 0 transparent'
    photo3.style.boxShadow = '0 0 5px gold'
}