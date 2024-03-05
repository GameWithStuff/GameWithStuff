(async () => {
    const readline = require('readline')
    const rl = readline.createInterface(
        {
            input: process.stdin,
            output: process.stdout
        }
    )

    let num1 = Math.floor(Math.random() * 10 + 1)
    let num2 = Math.floor(Math.random() * 10 + 1)
    let Ans = num1 + num2

    function input(prompt) {
    
        return new Promise((resolve, reject) => {
            rl.question(prompt, (ans) => {
                resolve(ans);
                rl.close();
            });
        })
    }

    console.log(await input('Hi\n'))


})()