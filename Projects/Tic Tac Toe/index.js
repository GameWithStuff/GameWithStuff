let currentTurn = 'X'
let Buttons = Array.from(document.querySelectorAll('.TicTacToe button'))
let a1 = document.querySelector('#a1')
let a2 = document.querySelector('#a2')
let a3 = document.querySelector('#a3')
let b1 = document.querySelector('#b1')
let b2 = document.querySelector('#b2')
let b3 = document.querySelector('#b3')
let c1 = document.querySelector('#c1')
let c2 = document.querySelector('#c2')
let c3 = document.querySelector('#c3')
function Place(e) {
    if (e.target.innerText == '') {

        e.target.innerText = currentTurn
        if (currentTurn === 'X') {
            currentTurn = 'O'
        }
        else {
            currentTurn = 'X'
        }
    }
    if (a1.innerHTML == a2.innerHTML && a2.innerHTML == a3.innerHTML && a1.innerHTML != '') {
        console.log('if')
        document.querySelector('.winner').innerText = e.target.innerText

        Buttons.forEach((button) => {
            button.onclick = () => { }
        })


    }
    else if (b1.innerHTML == b2.innerHTML && b2.innerHTML == b3.innerHTML && b1.innerHTML != '') {
        document.querySelector('.winner').innerText = e.target.innerText
        Buttons.forEach((button) => {
            button.onclick = () => { }
        })


    }
    else if (c1.innerHTML == c2.innerHTML && c2.innerHTML == c3.innerHTML && c1.innerHTML != '') {
        document.querySelector('.winner').innerText = e.target.innerText
        Buttons.forEach((button) => {
            button.onclick = () => { }
        })


    }
    else if (a1.innerHTML == b1.innerHTML && b1.innerHTML == c1.innerHTML && a1.innerHTML != '') {
        document.querySelector('.winner').innerText = e.target.innerText
        Buttons.forEach((button) => {
            button.onclick = () => { }
        })


    }
    else if (a2.innerHTML == b2.innerHTML && b2.innerHTML == c2.innerHTML && a2.innerHTML != '') {
        document.querySelector('.winner').innerText = e.target.innerText
        Buttons.forEach((button) => {
            button.onclick = () => { }
        })


    }
    else if (a3.innerHTML == b3.innerHTML && b3.innerHTML == c3.innerHTML && a3.innerHTML != '') {
        document.querySelector('.winner').innerText = e.target.innerText
        Buttons.forEach((button) => {
            button.onclick = () => { }
        })


    }
    else if (a1.innerHTML == b2.innerHTML && b2.innerHTML == c3.innerHTML && a1.innerHTML != '') {
        document.querySelector('.winner').innerText = e.target.innerText
        Buttons.forEach((button) => {
            button.onclick = () => { }
        })


    }
    else if (c1.innerHTML == b2.innerHTML && b2.innerHTML == a3.innerHTML && c1.innerHTML != '') {
        document.querySelector('.winner').innerText = e.target.innerText
        Buttons.forEach((button) => {
            button.onclick = () => { }
        })


    }
    else if(!(Buttons.map((button) => button.innerHTML == '')).includes(true)) {
        document.querySelector('.winner').innerText = 'No one'
        Buttons.forEach((button) => {
            button.onclick = () => { }
        })
    }



}

Buttons.forEach((button) => {
    button.onclick = Place
})
