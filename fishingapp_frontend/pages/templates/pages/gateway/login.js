function onLoginClick() {
    const password = document.getElementById("password").value;
    const username = document.getElementById("username").value;

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 400) {
            alert("Username or password is incorrect")
        } else if (this.readyState == 4 && this.status == 200) { // Thisis the callback function
            const responseString = this.responseText;
            const resultObject = JSON.parse(responseString);
            const tokenString = resultObject.token;
            console.log(tokenString);
            localStorage.setItem('indoor_air_token', tokenString); // http://127.0.0.1:9000
            window.location.href = "/dashboard";
        }
    }

    xhttp.open("POST", "{{ BACKEND_API_SERVER_ADDRESS }}/api/login", true);
    xhttp.setRequestHeader("content-type", "application/x-www-form-urlencoded");
    xhttp.send("username="+username+"&password="+password);
}
