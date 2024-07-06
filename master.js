var x,am,count;
ddval = ['Free','Special','VIP','Vehicle pooja2','Vehicle pooja4']
price = [0,50,100,100,200]
function updater() {
    x = document.getElementById('services').value
    count = document.getElementById('nodev').value
    am = price[ddval.indexOf(x)]
    document.getElementById('amount').innerHTML = am*count;
    document.getElementById('type').innerHTML = document.getElementById('services').value;
    document.getElementById('name').innerHTML = document.getElementById('rname').value;
    document.getElementById('phno').innerHTML = document.getElementById('rphno').value;
    document.getElementById('nod').innerHTML = count
    document.getElementById('totam').innerHTML = am*count;
}

function reset(){
    document.getElementById('rname').value = ""
    document.getElementById('rphno').value = ""
    document.getElementById('nodev').value = ""    
    document.getElementById('amount').innerHTML = ""
}