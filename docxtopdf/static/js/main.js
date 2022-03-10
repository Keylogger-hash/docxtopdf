var fileinput  = document.getElementById("id_filename")
form = document.getElementById("id_filename")
console.log(form)
fileinput.addEventListener("change",uploadFile, )

function uploadFile(){
    file = fileinput.files[0]
    console.log(file.type)
}
