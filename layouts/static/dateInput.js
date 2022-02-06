let timeField = document.querySelector('.post_date')

function timeSet(){
    var now = new Date()
    var time = now.toLocaleString()
    time.replace(',', '')
    timeField.innerHTML = time

    setTimeout(timeSet, 1000)
}

timeSet()