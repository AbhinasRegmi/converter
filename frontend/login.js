let login = document.getElementById("login");

//check if the url has access_token and refresh_tokens
let current_url = new URL(window.location.href);
let search_params = new URLSearchParams(current_url.search);

if(search_params.has("access_token") & search_params.has("refresh_token")){

    const access_token = search_params.get("access_token");
    const refresh_token = search_params.get("refresh_token");

    // set the cookies and redirec to main page
    setCookie("access_token", access_token)
    setCookie("refresh_token", refresh_token)

    document.location.href = "http://localhost:5500/frontend/index.html"
}


function setCookie(cookieName, cookieValue){

    const date = new Date();
    date.setTime(date.getTime() + (15 * 24 * 60 * 60 * 1000));
    const expires = "expires=" + date.toUTCString();
    document.cookie = cookieName + "=" + cookieValue + ";" + expires + ";path=/";
}



function onLogin(){
    const route = "http://localhost:8000/api/v1/auth/login/google?referer=http://localhost:5500/frontend/login.html";

    window.location.href = route;
}
