
let main = async () => {
    let mergedPDF = await PDFLib.PDFDocument.create()

    document.querySelector('.merge').onclick = async (event) => {
        try {
            
            let title = document.querySelector('.title').value
            title = (title.substr(-4)).toLowerCase() !== '.pdf' ? title + '.pdf' : title
            event.target.disabled = true
            let input = document.querySelector('.files')
            let files = Array.from(input.files)


            let fileDataArray = []

            let fileToData = async (file) => {
                return file.arrayBuffer()
            }

            for (let file of files) {
                fileDataArray.push(await fileToData(file))
            }

            for (let fileData of fileDataArray) {
                const pdf = await PDFLib.PDFDocument.load(fileData)
                    .then(pdf => pdf)

                console.log(pdf)

                const copiedPages = await mergedPDF.copyPages(pdf
                    , pdf.getPageIndices()
                )


                copiedPages.forEach((page) => mergedPDF.addPage(page))

            }

            let mergedPDFFile = await mergedPDF.save()

            let PDFBlob = new Blob([mergedPDFFile], { type: 'application/pdf' })

            let BlobURL = URL.createObjectURL(PDFBlob).toString()

            let link = document.createElement('a')

            link.href = BlobURL

            link.download = title
        
            link.click()

            event.target.disabled = false

            
            
        }
        catch {
            alert('Error : corrupted or invalid PDF File')
        }
        finally { 
            location.href = location.href
        }
    }
}

main()
