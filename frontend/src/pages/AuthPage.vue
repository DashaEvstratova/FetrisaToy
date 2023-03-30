<template>
  <div class='form'>
    <form method="post">
      <div class="container">
        <h1>Регистрация</h1>
        <hr>
        <br>
        <label for="email"><b>Email: </b></label>{{ ' ' }}
        <input name="email" type="text" v-model="email"/>
        <br>
        <br>
        <label for="psw"><b>Пароль: </b></label> {{ ' ' }}
        <input name="psw" type="password" v-model="psw"/>
        <br>
        <br>
        <label for="psw-repeat"><b>Повторите пароль: </b></label> {{ ' ' }}
        <input name="psw_repeat" type="password" v-model="psw_repeat"/>
        <br>
        <br>
        <button type="submit" class="registerbtn">Регистрация</button>
      </div>
      <br>
      <div class="container signin">
        <p>У вас уже есть аккаунт?<a href="/menu/login/"> Войти</a>.</p>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: "AuthPage",
  data() {
    return {
      email: '',
      psw: '',
      psw_repeat: ''
    }
  },
}
</script>

<style scoped>

.form {
  background: #fcecde;
  font-family: 'Nunito', sans-serif;
  width: 500px;
  padding: 40px;
  border-radius: 10px;
  margin: 30px auto 15px;
  box-shadow: 14px 14px 20px #cbced1, -14px -14px 20px white;
}

.form-container .form-horizontal .form-group label {
  font-size: 15px;
  font-weight: 600;
  text-transform: uppercase;
}

button {
  color: #000;
  background-color: #ffe3ca;
  font-size: 15px;
  font-weight: bold;
  text-transform: uppercase;
  width: 100%;
  padding: 18px 79px 15px;
  border-radius: 25px;
  box-shadow: 6px 6px 6px #c9c8c8, -6px -6px 6px #ffffff;
  border: none;
  transition: all 0.5s ease 0s;
}

button:hover,
button:focus {
  color: #000000;
  letter-spacing: 4px;
  box-shadow: none;
  outline: none;
}

form {
  height: 10px;
  padding: 20px;
  display: inline-block;
  transition: all 0.3s ease 0s;
  outline: none;
  color: #000000;
}
</style>