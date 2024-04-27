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
      element.appendChild(A1);
      const buttonfp = document.getElementById('youfavorite');
      buttonfp.addEventListener('click', async function(){
      let data = await  response.json()
      console.log(data['id'])
      const url1 = "/pages/favourite/" + data['id']
      window.location.href = url1
    } )
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