function getname() {
    x = document.getElementById('name').value;
    document.getElementById('nameresult').innerHTML =x
}
function getcode() {
    x = document.getElementById('code').value;
    document.getElementById('coderesult').innerHTML =x 
}
function getdate() {
    x = document.getElementById('date').value;
    document.getElementById('dateresult').innerHTML ='유효기간 : ' + x.substring(0, 4) +'년 ' + x.substring(4, 6)+'월 '+x.substring(6, 8)+'일';
}


function gettheme(event) {
    document.getElementById('themeresult').innerText = event.target.value;
}
