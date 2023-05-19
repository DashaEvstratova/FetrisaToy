<script>
import {MDBBtn, MDBIcon, MDBInput} from "mdb-vue-ui-kit";
import ProfilBar from "@/components/ProfilBar.vue";
import FooterMain from "@/components/FooterMain.vue";

export default {
    name: "BuketPage",
    components: {FooterMain, MDBInput, MDBBtn, MDBIcon, ProfilBar},
    data() {
        return {
            user: null,
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
    <div class="beautiful-text">
        <h2>Оплата</h2>
        <br>
        <p class="text-justify">
            Оплата является важной частью онлайн-покупок. С развитием электронной коммерции появилось множество удобных
            способов оплаты, которые предлагают покупателям гибкость и безопасность. В этом тексте я расскажу о
            различных способах оплаты в онлайн-магазинах.
        </p>
        <p class="text-justify">
            Одним из наиболее популярных способов оплаты является использование банковских карт. Это удобный и быстрый
            способ совершать покупки. Покупатель просто вводит данные своей карты (номер карты, срок действия, CVV-код)
            на защищенной странице платежного шлюза, и сумма покупки автоматически списывается с его счета. Большинство
            онлайн-магазинов принимают к оплате кредитные и дебетовые карты различных платежных систем, таких как Visa,
            Mastercard, American Express и другие.
        </p>
        <p class="text-justify">
            Другим распространенным способом оплаты является использование электронных платежных систем. Эти системы
            позволяют пользователям создавать аккаунты и связывать их с банковскими картами или счетами. Популярные
            платежные системы, такие как PayPal, Alipay, Apple Pay и Google Pay, предоставляют безопасные и удобные
            способы оплаты в онлайн-магазинах. Покупатели могут совершать платежи, просто вводя логин и пароль своего
            аккаунта, без необходимости каждый раз вводить данные карты.
        </p>
        <p class="text-justify">
            Также некоторые онлайн-магазины предлагают оплату при доставке (COD - Cash on Delivery). При этом покупатель
            может оплатить товар наличными при получении его от курьера. Этот способ оплаты особенно популярен в
            регионах, где у пользователей могут быть определенные опасения по поводу безопасности онлайн-платежей.
        </p>
        <p class="text-justify">
            Некоторые магазины предлагают альтернативные методы оплаты, такие как банковский перевод, чеки, электронные
            валюты и криптовалюты. Эти способы могут быть особенно удобными для международных покупателей или для тех,
            кто предпочитает не использовать банковские карты.
        </p>
        <p class="text-justify">
            Онлайн-магазины также обеспечивают безопасность платежей, используя различные меры защиты. SSL-шифрование
            обеспечивает конфиденциальность передаваемых данных, а многие магазины требуют двухфакторную аутентификацию
            для подтверждения платежей.
        </p>
        <p class="text-justify">
            Важно отметить, что каждый онлайн-магазин может поддерживать разные способы оплаты, и доступные варианты
            могут различаться в зависимости от географического положения покупателя. Поэтому перед оформлением покупки
            рекомендуется ознакомиться с предлагаемыми способами оплаты на сайте магазина.
        </p>
        <p class="text-justify">
            В заключение, онлайн-магазины предлагают множество удобных и безопасных способов оплаты. От использования
            банковских карт и электронных платежных систем до оплаты при доставке и альтернативных методов, покупатели
            могут выбирать наиболее удобный для них вариант. Важно помнить, что при совершении покупок онлайн следует
            обеспечить безопасность своих платежных данных и выбирать надежные магазины с хорошей репутацией.
        </p>
    </div>
    <FooterMain/>
</template>

<style scoped>
.beautiful-text {
    font-family: Arial, sans-serif;
    font-size: 18px;
    line-height: 1.5;
    color: #333;
    background-color: rgba(245, 245, 245, 0.27);
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    text-align: justify;
    margin-bottom: 60px;
    margin-left: 100px;
    margin-right: 100px;
    margin-top: 30px;
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