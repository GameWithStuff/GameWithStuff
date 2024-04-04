let screen = document.querySelector('.screen');
let txt = []
Array.from(document.querySelectorAll('.buttons button')).forEach((b) => {
    b.onclick = () => {
        // if (b.innerHTML === '(' ) {
        //     txt.push('\(')
        //     screen.innerHTML = txt.join('')
        //     return
        // }
        // if ( b.innerHTML === ')') {
        //     txt.push('\)')
        //     screen.innerHTML = txt.join('')
        //     return
        // }
        txt.push(b.innerHTML)
        screen.innerHTML = txt.join('')
    }
})
document.querySelector('.backspace').onclick = () => {
    txt.pop()
    screen.innerHTML = txt.join('')
}
document.querySelector('.ce').onclick = () => {
    txt = []
    screen.innerHTML = ''
}
document.querySelector('.equal').onclick = () => {

    try {
        console.log(txt.join(''))
        txt = eval(txt.join('').replace('^', '**'))
        // console.log('txt')
        if (!isNaN(txt)) {
            screen.innerHTML = txt.join('')
            txt = txt.toString().split('')
            if (!isFinite(txt)) {
                txt = []
                screen.innerHTML = 'Wayy too big'
            }
        }
        else {
            txt = []
            screen.innerHTML = 'Error'
        }
    }
    catch {
        txt = []
        screen.innerHTML = 'Error'
    }
}