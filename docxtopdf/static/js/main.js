var fileinput  = document.getElementById("id_filename")
fileinput.addEventListener("change",uploadFile, )

function uploadFile(){
    file = fileinput.files[0]
    console.log(file.type)
}
