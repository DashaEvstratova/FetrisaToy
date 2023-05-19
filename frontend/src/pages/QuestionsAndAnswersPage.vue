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
        <h2>Вопросы и ответы</h2>
        <br>
        <p class="text-justify">
            Добро пожаловать в раздел "Вопросы и ответы" нашего онлайн-магазина! Здесь вы найдете ответы на самые часто
            задаваемые вопросы от наших клиентов. Мы стремимся предоставить вам всю необходимую информацию, чтобы
            сделать ваше покупательское путешествие приятным и безопасным.
        </p>
        <p class="text-justify">
            Как оформить заказ?
            Чтобы сделать заказ, просто выберите интересующий вас товар, добавьте его в корзину и перейдите к оформлению
            заказа. Заполните необходимые данные, выберите предпочитаемый способ доставки и оплаты, и завершите
            оформление заказа. Мы сделаем все возможное, чтобы ваш заказ был обработан и доставлен вам в кратчайшие
            сроки.
        </p>
        <p class="text-justify">
            Каковы способы оплаты?
            Мы принимаем различные способы оплаты, включая банковские карты, электронные платежные системы и оплату при
            доставке (COD). Выберите наиболее удобный для вас способ оплаты при оформлении заказа.
        </p>
        <p class="text-justify">
            Каковы сроки доставки?
            Сроки доставки могут различаться в зависимости от вашего местоположения и выбранного способа доставки.
            Обычно мы стараемся доставить заказ в течение нескольких рабочих дней. Подробную информацию о сроках
            доставки можно найти на странице доставки или при оформлении заказа.
        </p>
        <p class="text-justify">
            Как отследить мой заказ?
            После обработки и отправки заказа мы предоставим вам номер отслеживания, который вы сможете использовать для
            отслеживания статуса доставки вашего заказа. Вы сможете проверить его на нашем веб-сайте или на сайте службы
            доставки.
        </p>
        <p class="text-justify">
            Что делать, если у меня возникли проблемы с заказом?
            Мы всегда стремимся обеспечить наивысший уровень обслуживания, но если у вас возникли какие-либо проблемы с
            заказом, не стесняйтесь обращаться к нашей службе поддержки клиентов. Мы готовы помочь вам решить любые
            вопросы и проблемы.
        </p>
        <p class="text-justify">
            Могу ли я вернуть или обменять товар?
            Мы принимаем возвраты и обмены в соответствии с нашей политикой возврата. Если вы не полностью удовлетворены
            приобретенным товаром, свяжитесь с нами в течение определенного срока после получения заказа, и мы поможем
            вам с возвратом или обменом товара.
        </p>
        <p class="text-justify">
            Как связаться с нашей командой поддержки?
            Мы всегда готовы ответить на ваши вопросы и предоставить помощь. Вы можете связаться с нашей командой
            поддержки клиентов по электронной почте, телефону или через форму обратной связи на нашем веб-сайте.
        </p>
        <p class="text-justify">
            Мы надеемся, что эта секция "Вопросы и ответы" поможет вам получить все необходимые ответы и сделать ваше
            покупательское путешествие удобным и безопасным. Если у вас возникли дополнительные вопросы, не стесняйтесь
            обращаться к нам. Благодарим вас за выбор нашего онлайн-магазина!
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