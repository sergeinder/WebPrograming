(async function () {
    const url = "http://localhost:8000/auth/me";
    response = await fetch(url, {
        method: 'GET',
        credentials: 'include',}
    )
    let element = document.getElementById("menuright");
    if (response.ok) {
      var A1 = document.createElement('a');
      A1.setAttribute('id', 'youfavorite');
      A1.innerText = "Favorite";
      A1.setAttribute('href', "http://localhost:8000/pages/favourite/fav");
      element.appendChild(A1);
    var A2 = document.createElement('a');
    A2.setAttribute('id', 'logout');
    A2.innerText = "Logout";
    element.appendChild(A2);
    const buttonlo = document.getElementById('logout');
    buttonlo.addEventListener('click', async function(){
    const url = "http://localhost:8000/auth/logout";
    await  fetch(url, {
      method: 'POST',
      credentials: 'include',}
    )
    window.location.href = "/pages/main"
  } )
    }else{
        var A1 = document.createElement('a');
        A1.setAttribute('href', "http://localhost:8000/pages/login");
        A1.setAttribute('id', 'login');
        A1.innerText = "Login";
        var A2 = document.createElement('a');
        A2.setAttribute('href', "http://localhost:8000/pages/register");
        A1.setAttribute('id', 'register');
        A2.innerText = "Register";
        element.appendChild(A1);
        element.appendChild(A2);
    }
  }())