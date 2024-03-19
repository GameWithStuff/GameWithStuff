const readline = require('readline')
const fs = require('fs')
const path = require('path')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

let input = async (question) => {
    return await new Promise((resolve, reject) => {
        rl.question((question + '\n'), (answer) => {
            resolve(answer)
            rl.close()
        })
    })

}

(async () => {
    console.log('Welcome to this mass renamer!')
    while (true) {

        let directory = await input('Please enter the path to the directory.')
        let filesInDirectory = []
        let selectedFiles = []
        fs.readdirSync(directory, (err, files) => {
            if (err) {
                filesInDirectory = null
            }
        })
        if (filesInDirectory === null) {
            console.log('Error: Unable to read the contents of the directory.')
            continue
        }
        else if (filesInDirectory.length === 0) {
            console.log('No Files found in directory.')
            continue
        }
        else {
            let ext = input('Please enter the file extension of the files you want to be renamed. (leave blank if you want all files to be renamed)')
            let newName = input('Please enter the new name for the selected file without the extension.')
            let ans = null
            do {
                ans = (input(` Do you want all ${ext} files in the ${directory} to be renamed to ${newName +
                    ext === '' ? ' + their original extension' : ('.' + ext)

                    } (y/n)`)).toLowerCase()
                ans = {
                    y: true,
                    n: false
                }[ans]
            }
            while (![true, false].includes(ans))
            if (!ans) {
                console.log('Session ended without Renaming anything.')
                continue
            }
            else {
                if (ext === '') {
                    selectedFiles = filesInDirectory
                }
                else {
                    let numberOfFile = 0
                    ext = '.' + ext
                    let getFileName = () => {
                        return newName + numberOfFile === 0 ? '' : `(${numberOfFile})` + ext
                    }
                    selectedFiles = filesInDirectory.filter(file => path.extname(file) === ext)
                    console.log('Processing... Please wait...')

                    selectedFiles.forEach(file => {
                        file.renameSync(file,getFileName())
                    })
                }
            }


        }



    }

})()
