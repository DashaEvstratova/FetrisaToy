<script>
import {MDBBtn, MDBIcon, MDBInput} from "mdb-vue-ui-kit";
import ProfilBar from "@/components/ProfilBar.vue";
import FooterMain from "@/components/FooterMain.vue";

export default {
    name: "BuketPage",
    components: {FooterMain, MDBInput, MDBBtn, MDBIcon, ProfilBar},
    data() {
        return {
            item: {},
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
        async getUserById(id) {
            const response = await fetch(`http://127.0.0.1:8000/users/`);
            const users = await response.json();
            const user = users.find(user => user.id === id);
            return user;
        },
        redirectToBucket() {
            this.$router.push('/bucket');
        },
        redirectToLike() {
            this.$router.push('/like');
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

</style>