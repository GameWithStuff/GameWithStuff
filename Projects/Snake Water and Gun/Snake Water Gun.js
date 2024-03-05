alert('Now you are playing snake water gun with a computer and this is gonna be fair')
const computer = ['Snake', 'Water', 'Gun'][Math.floor(Math.random() * 3)]
let user = prompt("Enter S W or G")
while(user != 'S' && user != 'G' && user != 'W'){
    user = prompt("Enter S W or G")

}
{
    let obj = {
        S : 'Snake',
        W : 'Water',
        G : 'Gun',
        s : 'Snake',
        w : 'Water',
        g : 'Gun'
    }
    user = obj[user]
}
alert(
    (user === 'Snake' && computer === 'Water') ||
    (user === 'Water' && computer === 'Gun') ||
    (user === 'Gun' && computer === 'Snake') ?
    "Congrats You Won"
    : 
    user === computer ?
    "We tied as we picked the same thing"
    : "I won and you lost,so better luck next time"
)
alert(`and by the way, I picked ${computer} and you picked ${user} `)
