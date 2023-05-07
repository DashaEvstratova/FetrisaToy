<script>
import {MDBBtn, MDBIcon, MDBInput} from "mdb-vue-ui-kit";
import ProfilBar from "@/components/ProfilBar.vue";
import FooterMain from "@/components/FooterMain.vue";
import axios from 'axios';

export default {
    name: "BuketPage",
    components: {FooterMain, MDBInput, MDBBtn, MDBIcon, ProfilBar},
    data() {
        return {
            item: {},
            user: null,
            likes: [],
        }
    },
    mounted() {
        if (JSON.parse(localStorage.getItem('user'))
        ) {
            const userId = JSON.parse(localStorage.getItem('user')).user_id;
            this.getUserById(userId)
                .then(user => {
                    this.user = user;
                    this.fetchLikes();
                })
                .catch(error => {
                    console.error(error);
                });
        }
  },
    methods: {
        async getUserById(id) {
            const response = await fetch(`http://127.0.0.1:8000/users/`);
            const users = await response.json();
            const user = users.find(user => user.id === id);
            return user;
        },
        async redirectToBucket() {
            this.$router.push('/bucket');
        },
        async redirectToLike() {
            this.$router.push('/like');
        },
        async redirectToMenu() {
            this.$router.push('/menu');
        },
        async fetchLikes() {
            const user_id = this.user.id; // Замените на фактический ID пользователя
            axios
                .get(`http://127.0.0.1:8000/like/user/${user_id}/`)
                .then(response => {
                    this.likes = response.data;
                })
                .catch(error => {
                    console.error(error);
                });
        },
    }
}
</script>

<template>
    <h1 class="funny-title section-title">Fetrisa Toy</h1>
    <div class="container">
        <table id="maket">
            <tr>
                <td id="rightcol">
                    <button @click="redirectToMenu" type="button" class="btn btn-primary btn-circle">
                        <b-icon class="h1 mb-2" icon="menu-button-wide-fill" aria-hidden="true"></b-icon>
                    </button>
                </td>
                <td id="rightcol">
                    <template>
                        <MDBInput
                                v-model="search1"
                                inputGroup
                                :formOutline="false"
                                wrapperClass="mb-3"
                                placeholder="Search"
                                aria-label="Search"
                                aria-describedby="button-addon2"
                        >
                            <MDBBtn color="primary">
                                <MDBIcon icon="search"/>
                            </MDBBtn>
                        </MDBInput>
                    </template>
                </td>
                <td id="rightcol">
                    <ProfilBar :user="user"/>
                </td>
                <td id="rightcol">
                    <button @click="redirectToBucket" type="button" class="btn btn-primary btn-circle">
                        <b-icon class="h1 mb-2" icon="basket3-fill" aria-hidden="true"></b-icon>
                    </button>
                </td>
                <td id="rightcol">
                    <button type="button" @click="redirectToLike" class="btn btn-primary btn-circle">
                        <b-icon class="h1 mb-2" icon="suit-heart-fill" aria-hidden="true"></b-icon>
                    </button>
                </td>
            </tr>
        </table>
    </div>
<!--    <img :src="require(`../assets/1.jpeg`)" :alt="selectedImage">-->
    <b-card-group deck>
                    <div class="row" style="display: flex; justify-content: space-evenly;">
                        <b-card v-for="item in likes" :key="item.item.id"
                                :to="`/item/${item.item.id}`"
                                @click="$router.push(`/item/${item.item.id}`)"
                                :img-src="require(`../assets/${item.item.pictures[0].picture}`)"
                                :title="item.item.name"
                                img-alt="Изображение"
                                img-top
                                tag="article"
                                style="max-width: 20rem"
                                class="card-scale md-4 mb-4"
                        >
                            <b-card-title class='d-flex justify-content font-weight-bold'>{{ item.item.price }} ₽</b-card-title>
                            <b-card-text class="text-truncate d-flex justify-content" style="max-width: 300px;">
                                {{ item.item.description }}
                            </b-card-text>
                        </b-card>
                        </div>
                    </b-card-group>
<!--    </div>-->
  <FooterMain/>
</template>

<style scoped>
.card-scale {
  transition: transform 0.3s ease-out;
}

.card-scale:hover {
  transform: scale(1.05);
}
.product-card img {
  width: 100%;
}

.product-card h2 {
  font-size: 1.5rem;
  margin: 0.5rem 0;
}

.product-card p {
  margin: 0.5rem 0;
}

.btn-circle {
    height: 40px;
    text-align: center;
    white-space: normal; /* восстанавливаем свойству значение по умолчанию */
}

#maket {
    width: 110%; /* Ширина всей таблицы */
   }
   TD {
    vertical-align: top; /* Вертикальное выравнивание в ячейках */
    padding: 5px; /* Поля вокруг ячеек */
   }
   TD#leftcol {
    width: 200px; /* Ширина левой колонки */
   }
   TD#rightcol {
   }

@import "https://fonts.googleapis.com/css?family=Russo+One";

h1.funny-title {
    border-top: 5px solid #d3b7c8;
    border-bottom: 5px solid #d3b7c8;
    font-size: 70px;
    text-align: center;
    margin-top: 40px;
    margin-bottom: 5px;
    text-transform: capitalize;
    font-family: cursive;
    font-weight: 900;
    letter-spacing: 8px
}

@-webkit-keyframes move-background {
    0% {
        background-position: -300px 0
    }
    100% {
        background-position: 300px -300px
    }
}

@-moz-keyframes move-background {
    0% {
        background-position: -300px 0
    }
    100% {
        background-position: 300px -300px
    }
}

@keyframes move-background {
    0% {
        background-position: -300px 0
    }
    100% {
        background-position: 300px -300px
    }
}

.section-title {
    -webkit-animation-play-state: running;
    -moz-animation-play-state: running;
    animation-play-state: running;
    color: transparent;
    background: url(https://obninsksite.ru/assets/theme/images/blog/square.svg) no-repeat #d3b7c8;
    background-size: cover;
    -webkit-text-fill-color: transparent;
    -moz-text-fill-color: transparent;
    -webkit-background-clip: text;
    -moz-background-clip: text;
    background-clip: text;
    -webkit-animation: move-background 20s infinite linear alternate;
    -moz-animation: move-background 20s infinite linear alternate;
    animation: move-background 20s infinite linear alternate
}

.container {
    text-align: center;
    margin-top: 5%;
}

.form-container .form-horizontal .form-group label{
 font-size: 15px;
 font-weight: 600;
 text-transform: uppercase;
}

</style>