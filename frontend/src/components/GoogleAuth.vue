<template>
  <div>
    <button @click="signIn">Sign In with Google</button>
  </div>
</template>

<script>
export default {
  methods: {
    async signIn() {
      this.$gAuth
        .signIn()
        .then(user => {
          // Обработка успешной авторизации
          console.log(user);
        })
        .catch(error => {
          // Обработка ошибки авторизации
          console.log(error);
        });
    }
  }
};
</script>
