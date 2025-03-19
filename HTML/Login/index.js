function hideReg() {
    const divs = document.getElementById('register');
    if (divs.style.visibility === "visible") {
        divs.style.visibility = "hidden";
        div = document.getElementById('login');
        div.style.visibility = "visible";
    } 
    else {
        divs.style.visibility = "visible";
    }
}

function hideLog() {
    const divs = document.getElementById('login');
    if (divs.style.visibility === "visible") {
        divs.style.visibility = "hidden";
        div = document.getElementById('register');
        div.style.visibility = "visible";
    } 
    else {
        divs.style.visibility = "visible";
    }
}

function LogIn()
{
    var username = document.getElementById('logname').value
    var password = document.getElementById('logpass').value
    const passw =  /^[A-Za-z]\w{7,14}$/;
    if(password.value.match(passw)) 
    { 
        alert('Correct, try another...')
        return true;
    }
    else
    { 
        alert('Wrong...!')
        return false;
    }
}