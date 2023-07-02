const loginForm = document.getElementById('login-form')
const baseEndpoint = "http://localhost:800/api"
if (loginForm){
    loginForm.addEventListener('submit', handleLogin)
}

function handleLogin(event){
    console.log(event)
    event.preventDefault()
    const loginEndpoint = `${baseEndpoint}/token/`
    let loginFormData = new FormData(loginForm)
    let loginObjectData = Object.fromEntries(loginFormData)
    let bodyStr = JSON.stringify(loginObjectData)
    console.log(loginObjectData, bodyStr)
    const options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: bodyStr
    }
    fetch(loginEndpoint, options)
    .then(response=>{
        return response.json()
    })
    .then(handleAuthData)
    .catch(err => {
        console.log('err', err)
    })
}

function handleAuthData(authData) {
    localStorage.setItem('access', authData.access)
    localStorage.setItem('refresh', authData.refresh)
}
