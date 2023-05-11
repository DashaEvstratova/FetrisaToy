<script>
import {MDBBtn, MDBIcon, MDBInput} from "mdb-vue-ui-kit";
import ProfilBar from "@/components/ProfilBar.vue";
import FooterMain from "@/components/FooterMain.vue";
import axios from "axios";

export default {
    name: "BuketPage",
    components: {FooterMain, MDBInput, MDBBtn, MDBIcon, ProfilBar},
    data() {
        return {
            items: {},
            user: null,
            summ: 0
        }
    },
    mounted() {
        if (JSON.parse(localStorage.getItem('user'))
        ) {
            const userId = JSON.parse(localStorage.getItem('user')).user_id;
            this.getUserById(userId)
                .then(user => {
                    this.user = user;
                    this.fetchBucketItems();
                })
                .catch(error => {
                    console.error(error);
                });
        }
    },
    methods: {
        async getSum() {
            for (let i = 0; i < this.items.length; i++) {
                this.summ += this.items[i].item.price * this.items[i].count;
            }
        },
        async getUserById(id) {
            const response = await fetch(`http://127.0.0.1:8000/users/`);
            const users = await response.json();
            const user = users.find(user => user.id === id);
            return user;
        },
        async fetchBucketItems() {
      axios
        .get(`http://127.0.0.1:8000/bucket/user/${this.user.id}/`)
        .then(response => {
          this.items = response.data;
          this.getSum();
        })
        .catch(error => {
          console.log(error);
        });
        },
        async redirectToBucket() {
            this.$router.push('/bucket');
        },
        async ToPay() {
            const items = this.items.map(item => {
                return {
                    id: item.item.id,
                    count: item.count
                };
            });
            const total = this.summ;
            axios.post('http://127.0.0.1:8000/create-order/', { items: items, total: total, user:this.user.id },
            { headers: { 'Content-Type': 'application/json' } })
                .then(response => {
                    // Обработка успешного создания заказа
                    console.log(response.data);
                    // Дополнительные действия, например, перенаправление на страницу успешного заказа
                })
                .catch(error => {
                    // Обработка ошибок
                    console.error(error);
                });
            this.$router.push('/pay');
        },
        async redirectToLike() {
            this.$router.push('/like');
        },
        async redirectToMenu() {
            this.$router.push('/menu');
        },
        async updateBucketItem(item_id, count) {
            try {
                await axios.put('http://127.0.0.1:8000/update-bucket-item/', {
                    user_id: this.user.id,
                    item_id: item_id,
                    count: count
                });
            } catch (error) {
                // Обработка ошибки
                console.error(error);
            }
        },
        removeItem(item) {
            const index = this.items.indexOf(item);
            if (index !== -1) {
                this.items.splice(index, 1);
                this.deleteItem(item);
            }
        },
        deleteItem(item) {
            console.log(item.id)
            axios
                .delete(`http://127.0.0.1:8000/remove-bucket-item/?user_id=${this.user.id}&item_id=${item.item.id}`)
                .then(() => {
                    console.log("Object deleted successfully");
                })
                .catch((error) => {
                    console.error(error);
                });
        },
        decrementCount(item) {
            item.count = Math.max(0, item.count - 1);
            this.summ -= item.item.price
            if (item.count === 0) {
                this.removeItem(item);
            }
            else {
                this.updateBucketItem(item.id, item.count)
            }
        },
        incrementCount(item) {
            item.count = Math.min(100, item.count + 1);
            this.updateBucketItem(item.item.id, item.count)
            this.summ += item.item.price
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
                    <button @click="redirectToLike" type="button" class="btn btn-primary btn-circle">
                        <b-icon class="h1 mb-2" icon="suit-heart-fill" aria-hidden="true"></b-icon>
                    </button>
                </td>
            </tr>
        </table>
    </div>
    <br>
    <br>
    <table style="width: 100%; table-layout: fixed;">
        <tr>
            <td style="width: 70%;">
                <div v-for="item in items" :key="item.item.id" class="card mb-5"
                     style="max-width: 540px; margin-top: 20px; margin-left: auto; margin-right: auto;">
                    <div class="row no-gutters">
                        <div class="col-md-4">
                            <img
                                :src="`${item.item.pictures[0].picture}`"
                                @click="$router.push(`/item/${item.item.id}`)"
                                class="card-img"
                                alt="Упс"
                                height="170"
                            >
                        </div>
                        <div class="col-md-8">
                            <div class="card-body">
                                <h5 class="card-title">{{ item.item.name }}</h5>
                                <div class="input-group quantity_goods text-truncate d-flex justify-content"
                                     style="max-width: 300px;">
                                    {{ item.item.description }}
                                </div>
                                <br>
                                <p class="card-text">
                                    <small class="text-muted">{{ item.item.price }} руб.</small>
                                </p>
                                <button type="button" @click="decrementCount(item)">-</button>
                                <input type="number" :min="0" :max="100" v-model="item.count" readonly class="raz">
                                <button type="button" @click="incrementCount(item)">+</button>
                            </div>
                        </div>
                    </div>
                </div>
            </td>
            <td style="width: 30%;">
                        <div class="col-md-5" style="width: 300px">
                            <div class="form-container form-horizontal">
                                <div class="d-flex align-items-center justify-content-between">
                                    <h3>Итого: {{ summ }} ₽</h3>
                                </div>
                                <br>
                                <button v-if='user' @click="ToPay" type="submit" class="btn btn-default">Перейти к оформлению
                                </button>
                            </div>
                        </div>
                    </td>
        </tr>
    </table>
    <FooterMain/>
</template>

<style scoped>
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