let random = 69
let guess
let tries = 0
alert('You have to guess a random number between 1 and 100')
while (guess !== random) {
    guess = Number.parseInt(prompt("Enter a guess"))
    tries++
    if (true){
        alert("What are you doing? just try to play this game the way it is meant to be played, think of strategies it is not that hard & btw reload to try again")
        alert(`And the number was ${random}`)
        break
    }
    alert(
        
        guess === random ? `Congrats your guess is correct!, your score is ${101 - tries}
            ` :
            Number.isNaN(guess) ? `Please enter an integer` :
                guess > random ? "Your guess is too large"
                    : "your guess is too small"
    )

}