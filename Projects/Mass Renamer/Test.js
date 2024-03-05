const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

rl.question(
    'Hi\n',
    (Input) => console.log(Input)
)