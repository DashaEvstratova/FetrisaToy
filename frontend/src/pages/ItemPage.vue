<script>
import axios from 'axios'
import {MDBBtn, MDBIcon, MDBInput} from "mdb-vue-ui-kit";
import ProfilBar from "@/components/ProfilBar.vue";

export default {
    name: "ItemPage",
    components: {MDBInput, MDBBtn, MDBIcon, ProfilBar},
    data() {
        return {
            item: {},
            value: 5,
            review: ' 20 отзывов',
            user: null,
        }
    },
    mounted() {
        this.getItemById(this.$route.params.id)
            .then(item => {
                this.item = item

            })
        if (JSON.parse(localStorage.getItem('user'))
        ) {
            const userId = JSON.parse(localStorage.getItem('user')).user_id;
            this.getUserById(userId)
                .then(user => {
                    this.user = user;
                })
                .catch(error => {
                    console.error(error);
                });
        }
    }
    ,
    methods: {
        async getItemById(id) {
            return axios.get(`http://127.0.0.1:8000/items/${id}/`)
                .then(response => {
                    return response.data
                })
                .catch(error => {
                    // Обработка ошибки
                    console.log(error)
                })
        },
        async getUserById(id) {
            const response = await fetch(`http://127.0.0.1:8000/users/`);
            const users = await response.json();
            const user = users.find(user => user.id === id);
            return user;
        },
        addToCart() {
            axios.post('http://127.0.0.1:8000/bucket/create/', {
                "user": this.user.id,
                "item": this.item.item.id
            })
                .catch(error => {
                    console.log(error);
                });
        },
        addToLike() {
            axios.post('http://127.0.0.1:8000/like/create/', {
                "user": this.user.id,
                "item": this.item.item.id
            })
                .catch(error => {
                    console.log(error);
                });
        }
    }
}
</script>
<template>
    <h1 class="funny-title section-title">Fetrisa Toy</h1>
    <div class="container">
        <table id="maket">
            <tr>
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
                    <button type="button" class="btn btn-primary btn-circle">
                        <b-icon class="h1 mb-2" icon="basket3-fill" aria-hidden="true"></b-icon>
                    </button>
                </td>
                <td id="rightcol">
                    <button type="button" class="btn btn-primary btn-circle">
                        <b-icon class="h1 mb-2" icon="suit-heart-fill" aria-hidden="true"></b-icon>
                    </button>
                </td>
            </tr>
        </table>
    </div>
    <div class="container">
        <div class="centered-block">
            <h2>{{ item?.item?.name }}</h2>
            <table>
                <tr>
                    <td>
            <div class="small-div" style="float: left;">
                <b-form-rating v-model="value" readonly show-value precision="2"></b-form-rating>
            </div>
                    </td>
                    <td style="text-align: center; vertical-align: middle;">
                        <a href="">{{review}}</a>
                    </td>
                </tr>
            </table>
            <table>
                <tr>
                    <td>
            <img :src="item.picture" alt="Product Image" class="product-image">
                    </td>
                    <td>
            <div class="text" style="width: 650px;">
                <p>Размер: {{ item?.item?.size }}</p>
                <p v-if="item?.item?.number">
                    Осталось: {{ item?.item?.number }}
                </p>
                <p v-else>
                    Нет в наличии
                </p>
                <p>{{ item?.item?.description }}</p>
            </div>
                    </td>
                    <td style="width: 700px;">
                        <div class="col-md-5" style="width: 300px">
                            <div class="form-container form-horizontal">
                                <div class="d-flex align-items-center justify-content-between">
                                    <h3>{{ item?.item?.price }} ₽</h3>
                                    <button @click="addToLike" type="button" class="btn btn-primary btn-circle" id="like">
                                        <b-icon class="h1 mb-2" icon="suit-heart-fill" aria-hidden="true"
                                                style="color: #d3b7c8;"></b-icon>
                                    </button>
                                </div>
                                <br>
                                <button @click="addToCart" type="submit" class="btn btn-default">Добавить в корзину</button>
                            </div>
                        </div>
                    </td>
                </tr>
            </table>
        </div>
    </div>
</template>


<style scoped>
#like {
    background-color: transparent;
    border-color: transparent;
    font-size: 2rem;
}
img.product-image {

    float: left;
    margin-right: 10px; /* отступ справа от картинки */
    border-radius: 10px; /* скругление углов */
  }

  .text {
    overflow: auto;
  }
.small-div {
  transform: scale(0.7);
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

.centered-block {
    display: inline-block;
    width: 110%;
    height: 110%;
    text-align: left;
    padding: 1rem;
}

.form-container{
 background: #FAE8DC;
 font-family: 'Nunito', sans-serif;
 padding: 40px;
 border-radius: 20px;
 box-shadow: 14px 14px 20px #E6B493, -14px -14px 20px #ffffff;
}

.form-container .form-horizontal .form-group label{
 font-size: 15px;
 font-weight: 600;
 text-transform: uppercase;
}

.btn-default{
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
</style>