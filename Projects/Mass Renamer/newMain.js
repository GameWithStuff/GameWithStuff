
const readline = require('readline')
const fs = require('fs')
const path = require('path')



function input(prompt) {
    return new Promise((resolve, reject) => {
        const rl = readline.createInterface(
            {
                input: process.stdin,
                output: process.stdout
            }
        )
        rl.question(prompt, (ans) => {
            resolve(ans.trim());
            rl.close();
        });
    })
}
// Main Function
let main = async () => {

    console.log('Welcome to this mass renamer!')


    let directory = await input('Please enter the path to the directory.\n')//Selected Directory

    
    let filesInDirectory = fs.readdirSync(directory, {})// Files in the Directory : ['name.ext1', 'name2.ext2' ...]
    
    directory = directory[directory.length - 1] === '\\' ? directory : (directory + '\\')

    let targetedExtension
    do {
        targetedExtension = await input('Please enter the extension of the files you want to rename.\n')
    }
    while (!targetedExtension)
    targetedExtension = targetedExtension[0] === '.' ? targetedExtension : ('.' + targetedExtension)

    let newName = await input('Please enter the new name of the files you want to rename. (Don\'t include the extension)\n')

    let pathToFilesInDirectory = filesInDirectory.map(file => directory + file) // acts as oldPath



    let selectedFiles = pathToFilesInDirectory.filter(file => file.endsWith(targetedExtension))// Path to Files That Should be renamed
    let newNamesArray = []
    

    for (let i in selectedFiles) {
        if (i == 0) {
            newNamesArray.push(directory + newName + targetedExtension) 
        }
        else {
            newNamesArray.push(`${directory}${newName}(${i})${targetedExtension}`)
        }
    }

    for (let i in selectedFiles) { 
        fs.renameSync(selectedFiles[i], newNamesArray[i])
    }

    console.log('Done!!')





}

main()