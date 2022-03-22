
document.addEventListener('DOMContentLoaded', (event)=>{
    main()
})
function main() {
    let fileid = window.location.href.split('/')[4]
    let url = `/processing/${fileid}/`
    let app = document.querySelector("#app")
    fetch(url).then(r=>r.json()).then((data)=>{
        if (data.ready === true){
            filepathpdf = data.filepathpdf
            app.innerHTML = `<iframe id="idframe" width="100%" height="100%" src="${filepathpdf}"></iframe> `
        } else {
            app.innerHTML = `<p > <img style="display: block;margin-left: auto;margin-right: auto;width: 50%;" src="/static/images/14972.gif"</p>`
            setTimeout(main,1000)
        }
    })
}