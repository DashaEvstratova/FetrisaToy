<template>
  <div>
    <b-dropdown variant="primary">
      <template #button-content>
        <b-icon icon="person-fill" aria-hidden="true"></b-icon>
      </template>
<!--      <b-dropdown-item-button>-->
<!--         <b-icon icon="brush-fill" aria-hidden="true"></b-icon>-->
<!--         Фильтр <span class="sr-only">(Click to unlock)</span>-->
<!--      </b-dropdown-item-button>-->
<!--      <b-dropdown-divider></b-dropdown-divider>-->
      <a href="http://localhost:8080/login/"><b-dropdown-item-button>Войти</b-dropdown-item-button></a>
<!--      <b-dropdown-item-button>Some other action</b-dropdown-item-button>-->
<!--      <b-dropdown-divider></b-dropdown-divider>-->
<!--      <b-dropdown-item-button variant="danger">-->
<!--        <b-icon icon="trash-fill" aria-hidden="true"></b-icon>-->
<!--        Delete-->
<!--      </b-dropdown-item-button>-->
    </b-dropdown>
  </div>
</template>

<script>
export default {
    name: "ProfilBar",
    data() {
        return {
            active: 'home',
            activeSidebar: false
        }
    }
}
</script>

<style scoped>

</style>