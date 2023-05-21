<script>
import {MDBBtn, MDBIcon, MDBInput} from "mdb-vue-ui-kit";
import ProfilBar from "@/components/ProfilBar.vue";
import FooterMain from "@/components/FooterMain.vue";

export default {
    name: "DeliveryPage",
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
        <h2>Доставка</h2>
        <br>
        <p class="text-justify">
            Доставка - один из ключевых аспектов онлайн-шопинга, который играет важную роль в удовлетворении
            потребностей
            клиентов. В современном мире, где комфорт и удобство имеют первостепенное значение, доставка товаров из
            онлайн-магазинов стала неотъемлемой частью нашей повседневной жизни. В этом тексте мы рассмотрим важность и
            преимущества доставки из онлайн-магазина, а также различные аспекты этого процесса.
        </p>
        <p class="text-justify">
            Одним из главных преимуществ покупок в онлайн-магазинах является возможность получить товар прямо у порога
            своего дома. Вместо того чтобы тратить время на посещение физического магазина, клиенты могут просто выбрать
            нужный товар в онлайн-каталоге, оформить заказ и ждать доставки. Это особенно удобно для занятых людей,
            которые не могут выделить время на поход по магазинам.
        </p>
        <p class="text-justify">
            Доставка из онлайн-магазина также предлагает широкий спектр вариантов и гибкость. Клиенты могут выбрать
            удобный для них способ доставки, будь то обычная почта, курьерская служба или пункт самовывоза. Это
            позволяет каждому клиенту выбрать опцию, соответствующую его индивидуальным предпочтениям и требованиям.
        </p>
        <p class="text-justify">
            Быстрая доставка - еще одно преимущество онлайн-магазинов. В современном мире, где все движется быстро и
            мгновенно, клиенты ожидают получить свои заказы в кратчайшие сроки. Многие онлайн-магазины предлагают
            экспресс-доставку, которая позволяет клиентам получить товар уже на следующий день после оформления заказа.
            Благодаря сотрудничеству с курьерскими службами и оптимизации логистических процессов, онлайн-магазины
            способны обеспечить быструю доставку своим клиентам.
        </p>
        <p class="text-justify">
            Кроме того, доставка из онлайн-магазина обычно сопровождается возможностью отслеживания статуса заказа в
            реальном времени. Клиенты могут проверить, находится ли их товар на складе, был ли он отправлен, находится
            ли в пути или уже прибыл в пункт назначения. Это создает прозрачность и доверие между клиентом и магазином,
            позволяя клиентам быть в курсе процесса доставки.
        </p>
        <p class="text-justify">
            Безопасность также является важным аспектом доставки из онлайн-магазина. Курьерские службы обеспечивают
            надежную упаковку и защиту товаров во время транспортировки, чтобы предотвратить повреждения или утрату.
            Кроме того, многие онлайн-магазины предлагают защиту покупателя и возможность возврата товара в случае
            неудовлетворенности или повреждения.
        </p>
        <p class="text-justify">
            Однако, важно отметить, что доставка из онлайн-магазина может иметь и некоторые ограничения. Например, в
            отдаленные регионы или за пределы страны доставка может занять больше времени или быть недоступной. Также
            стоит учесть возможные задержки в доставке, связанные с погодными условиями, праздниками или высоким спросом
            на товар.
        </p>
        <p class="text-justify">
            В заключение, доставка из онлайн-магазина является удобным, быстрым и гибким способом получения товаров. Она
            предлагает широкий выбор опций доставки, позволяет отслеживать статус заказа и обеспечивает безопасность
            товаров. Онлайн-магазины стремятся удовлетворить потребности своих клиентов и постоянно совершенствуют свои
            службы доставки, чтобы обеспечить удобство и удовлетворение каждого клиента.
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