<script>
import axios from "axios";

export default {
  name: "LoginGitHubPage",
  data() {
    return {
      email: this.loginGitHub(),
      password: '',
    }
  },
  methods: {
    async loginGitHub() {
      const code = new URLSearchParams(window.location.search).get('code');
      const response = await axios.post('http://localhost:8000/auth_git_hub/', code);
      this.email = response.data.email
      if (this.email !== 'error') {
        this.password = response.data.password
        await axios.post('http://localhost:8000/auth/register/', {
          email: this.email,
          password: this.password,
        }).then(response => {
          // сохраняем данные пользователя в localStorage
          localStorage.setItem('user', JSON.stringify(response.data));
          this.$router.push('/menu');
        }).catch(error => {
          this.error = error.response.data;
        });
      }
    }
  }
}
</script>

<template>
<p>Регистрация пришло успешно!</p>
</template>

<style scoped>

</style>