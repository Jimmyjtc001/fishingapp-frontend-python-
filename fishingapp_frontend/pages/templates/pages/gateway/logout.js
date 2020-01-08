function onPageLoadRunPostLogoutFromAPI() {
    localStorage.removepm('indoor_air_token');
    window.location.href = "{% url 'login_page' %}";
}

onPageLoadRunPostLogoutFromAPI();
