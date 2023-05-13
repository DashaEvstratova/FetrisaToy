
<template>
  <div>
            <div class="col-md-6 offset-md-3">
        <div class="form-container">
    <h1>Сброс пароля</h1>
            <hr>
            <br>
    <form @submit.prevent="resetPassword" class="form-horizontal">
        <label for="email"><b>Новый пароль: </b></label>{{ ' ' }}
      <input class="form-control" type="password" v-model="password" placeholder="New Password" required>
        <br>
        <br>
        <label for="email"><b>Повторите пароль: </b></label>{{ ' ' }}
      <input class="form-control" type="password" v-model="confirmPassword" placeholder="Confirm Password" required>
        <br>
        <br>
      <button class="btn btn-default" type="submit">Сброс пароля</button>
    </form>
  </div>
            </div>
  </div>
</template>

<script>

import axios from "axios";

export default {
  data() {
    return {
      password: '',
      confirmPassword: ''
    }
  },
    methods: {
    async resetPassword() {
      if (this.password !== this.confirmPassword) {
        alert('Пароли не совпадают');
        return;
      }
      const token = this.$route.params.token;
       const formData = new FormData();
            formData.append('token', token);
            formData.append('password', this.password);

        try {
            await axios.post(`http://127.0.0.1:8000/reset-password-api/`,
                formData);
            this.$router.push('/menu');
        } catch (error) {
            alert('Произошла ошибка');
            console.error(error);
        }
    }
  }
};
</script>


<style scoped>
.form-container{
 background: #FAE8DC;
 font-family: 'Nunito', sans-serif;
 padding: 40px;
 border-radius: 20px;
 box-shadow: 14px 14px 20px #E6B493, -14px -14px 20px #ffffff;
}

.form-container .form-icon{
 color: #d39a74;
 font-size: 55px;
 text-align: center;
 line-height: 100px;
 width: 100px;
 height:100px;
 margin: 0 auto 15px;
 border-radius: 50px;
 box-shadow: 7px 7px 10px #d3a688, -7px -7px 10px #ffffff;
}

.form-container .title{
 color: #d39a74;
 font-size: 25px;
 font-weight: 700;
 text-transform: uppercase;
 letter-spacing: 1px;
 text-align: center;
 margin: 0 0 20px;
}

.form-container .form-horizontal .form-group{ margin: 0 0 25px 0; }

.form-container .form-horizontal .form-group label{
 font-size: 15px;
 font-weight: 600;
 text-transform: uppercase;
}

.form-container .form-horizontal .form-control{
 color: #333;
 background: #ffffff;
 font-size: 15px;
 height: 50px;
 padding: 20px;
 letter-spacing: 1px;
 border: none;
 border-radius: 50px;
 box-shadow: inset 6px 6px 6px #ffffff, inset -6px -6px 6px #f3dbcc;
 display: inline-block;
 transition: all 0.3s ease 0s;
}

.form-container .form-horizontal .form-control:focus{
 box-shadow: inset 6px 6px 6px #ffffff, inset -6px -6px 6px #d3a688;
 outline: none;
}

.form-container .form-horizontal .form-control::placeholder{
 color: #ffffff;
 font-size: 14px;
}

.form-container .form-horizontal .btn{
 color: #000;
 background-color: #ffffff;
 font-size: 15px;
 font-weight: bold;
 text-transform: uppercase;
 width: 100%;
 padding: 12px 15px 11px;
 border-radius: 20px;
 box-shadow: 6px 6px 6px #d3a688, -6px -6px 6px #ffffff;
 border: none;
 transition: all 0.5s ease 0s;
}

.form-container .form-horizontal .btn:hover,
.form-container .form-horizontal .btn:focus{
 color: #000000;
 letter-spacing: 3px;
 box-shadow: none;
 outline: none;
}
</style>