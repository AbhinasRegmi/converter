//first check if there is access_token and refresh_token present
let access_token = getCookie("access_token");
let refresh_token = getCookie("refresh_token");


// if not tokens present redirect to login page
if( !access_token | !refresh_token ){
    window.location.href = "http://localhost:5500/frontend/login.html";
}

//check validity of access_token and refresh_token
verifyTokens(access_token, refresh_token)

//if valid route to upload page

//if access_token expired then use refresh token to get new access_token

//if invalid or expired route to login page

function getCookie(cookieName){
    const name = cookieName + "=";
    const decodedCookie = decodeURIComponent(document.cookie);
    const cookieArray = decodedCookie.split(';');
    for (let i = 0; i < cookieArray.length; i++) {
        let cookie = cookieArray[i];
        while (cookie.charAt(0) === ' ') {
        cookie = cookie.substring(1);
        }
        if (cookie.indexOf(name) === 0) {
        return cookie.substring(name.length, cookie.length);
        }
    }
    return "";
}

function verifyTokens(access, refresh){

    let post_url = "http://localhost:8000/api/v1/auth/verify-tokens"
    let data = {
        "access_token": access,
        "refresh_token": refresh,
        "token_type": "Bearer"
    }

    fetch(post_url,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data)
        }
    ).then(
        response => response.json()
    )
    .then(
        (data) => {
        
        if(data['detail']){
            window.location.href = "http://localhost:5500/frontend/login.html";
        }
    })
}


const form = document.querySelector('input[type="file"]');

form.addEventListener('submit', async (event) => {
    event.preventDefault(); // Prevent default form submission

    const url = 'http://localhost:8001/api/v1/upload-using-fileupload';
    let formData = new FormData();
    formData.append('file', form.files[0])

    try {
      const response = await fetch(url, {
        method: 'POST',
        body: formData
      });

      if (response.ok) {
        console.log('Video uploaded successfully');
      } else {
        console.error('Error uploading:', response.statusText);
      }
    } catch (error) {
      console.error('Error uploading video:', error.message);
    }
  });
