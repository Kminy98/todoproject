window.onload = () => {
console.log("실행")

}

async function handleSignin(){
    const email = document.getElementById("email").value
    const password = document.getElementById("password").value

    const response = await fetch('http://127.0.0.1:8000/user/signup/', {
        headers:{
            'content-type':'application/json',
        },
        method:'POST',
        body: JSON.stringify({
            "email":email,
            "password":password
        })
    })
}

async function handleLogin(){
    console.log("눌림")
    const email = document.getElementById("email").value
    const password = document.getElementById("password").value

    const response = await fetch('http://127.0.0.1:8000/user/api/token/', {
        headers:{
            'content-type':'application/json',
        },
        method:'POST',
        body: JSON.stringify({
            "email":email,
            "password":password
        })
    })

    const response_json = await response.json()

    localStorage.setItem("access", response_json.access);
    localStorage.setItem("refresh", response_json.refresh);

    const base64Url = response_json.access.split('.')[1];
    const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    const jsonPayload = decodeURIComponent(atob(base64).split('').map(function (c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));

    localStorage.setItem("payload", jsonPayload);
}


async function handleMock(){
    const email = document.getElementById("email").value
    const password = document.getElementById("password").value

    const response = await fetch('http://127.0.0.1:8000/user/mock/', {
        headers:{
            "Authorization":"Beater " + localStorage.getItem("access")
        },
        method:'GET',
    })
}