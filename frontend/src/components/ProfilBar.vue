<template>
  <div>
    <b-dropdown variant="primary">
      <template #button-content>
        <b-icon icon="person-fill" aria-hidden="true"></b-icon>
      </template>
        <div v-if="user">
         <b-icon icon="person-fill" aria-hidden="true"></b-icon>
           {{user.email}}
            <br>
      <b-dropdown-item-button @click="goToProfilePage">Профиль</b-dropdown-item-button>
      <b-dropdown-divider></b-dropdown-divider>
          <b-dropdown-item-button @click="goToChatPage">Чатик</b-dropdown-item-button>
      <b-dropdown-divider></b-dropdown-divider>
      <b-dropdown-item-button variant="danger" @click="logout">
        Выйти
      </b-dropdown-item-button>
        </div>
        <div v-else>
            <b-dropdown-divider></b-dropdown-divider>
      <a href="http://localhost:8080/login/"><b-dropdown-item-button>Войти</b-dropdown-item-button></a>
        </div>
    </b-dropdown>
  </div>
</template>

<script>
export default {
    name: "ProfilBar",
    props: {
        user: {
            type: Object,
            required: true,
        },
    },
    data() {
        return {
            active: 'home',
            activeSidebar: false
        }
    },
    methods: {
        async logout() {
            // удаляем данные пользователя
            localStorage.removeItem('user');
            location.reload();
        },
        async goToProfilePage() {
            this.$router.push('/profile');
        },
        async goToChatPage(){
          this.$router.push('/notifications');
        }
    }
}
</script>

<style scoped>

</style>