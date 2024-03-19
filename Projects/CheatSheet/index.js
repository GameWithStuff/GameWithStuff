let getArr = () => {
    if (!!localStorage.getItem('arr') == false) {
        localStorage.setItem('arr', '[]')
        return []
    }
    return JSON.parse(localStorage.getItem('arr'))
}

let setArr = item => {
    localStorage.setItem('arr', JSON.stringify(item))
}

let init = () => {
    Array.from(document.querySelectorAll('.copy')).forEach((copy) => {
        copy.onclick = e => {
            console.log(e.target)
            console.log(e.target.parentElement)
            console.log(e.target.parentElement.parentElement)
            console.log(e.target.parentElement.parentElement.firstElementChild)
            console.log(e.target.parentElement.parentElement.firstElementChild.value)
            navigator.clipboard.writeText(e.target.parentElement.parentElement.firstElementChild.value)
        }
    })
    Array.from(document.querySelectorAll('textarea')).forEach(ta => {
        ta.onchange = e => {
            let arr = []
            let headings = Array.from(document.querySelectorAll('.heading'))
            let codes = Array.from(document.querySelectorAll('.code'))
            for (let i in document.querySelectorAll('.card')) {
                let obj = {
                    heading: headings[i].value,
                    code: codes[i].value,
                }
            }
            setArr(arr)
            arr.push(obj)
        }
        console.log(getArr())
    })
}
init()

let createCard = () => {
    let card = document.createElement('div')
    card.className = 'card'
    card.innerHTML = `<textarea class="heading"></textarea><div class="codeAndCopy"><textarea class="code"></textarea><button class="copy"><img src="https://png.pngtree.com/png-vector/20190329/ourmid/pngtree-vector-copy-icon-png-image_889395.jpg"alt=""></button>`
    return card

}