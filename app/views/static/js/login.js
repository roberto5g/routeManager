$(document).ready(function() {
  $('#loginForm').submit(function(e) {
    e.preventDefault();
    var username = $('#username').val();
    var password = $('#password').val();

    // Faça a validação do usuário e senha aqui

    // Exemplo de redirecionamento após o login
    window.location.href = '/home';
  });
});
