<script>
import {MDBBtn, MDBIcon, MDBInput} from "mdb-vue-ui-kit";
import ProfilBar from "@/components/ProfilBar.vue";
import FooterMain from "@/components/FooterMain.vue";
// import axios from "axios";

export default {
    name: "ProfilPage",
    components: {FooterMain, MDBInput, MDBBtn, MDBIcon, ProfilBar},
    data() {
        return {
            user: null,
            email: '',
            name: '',
            surname: '',
            patronymic: '',
            city:'',
            street:'',
            house:'',
            corps:'',
            apartment:'',
            phone_number:'',
            data_of_birthday:'',
            avatar:''
        }
    },
    mounted() {
        if (JSON.parse(localStorage.getItem('user'))
        ) {
            const userId = JSON.parse(localStorage.getItem('user')).user_id;
            this.getUserById(userId)
                .then(user => {
                    this.user = user;
                    this.email = user.email;
                    this.name = user.name;
                    this.surname = user.surname;
                    this.patronymic = user.patronymic;
                    this.city = user.city;
                    this.street = user.street;
                    this.house = user.house;
                    this.corps = user.corps;
                    this.apartment = user.apartment;
                    this.phone_number = user.phone_number;
                    this.data_of_birthday = user.data_of_birthday;
                    this.avatar = user.avatar
                })
                .catch(error => {
                    console.error(error);
                });
        }
    },
    methods: {
        handleAvatarClick() {
            this.$refs.fileInput.click();
        },
        handleFileChange(event) {
            const file = event.target.files[0];
            const reader = new FileReader();

            reader.onload = () => {
                // Преобразование содержимого файла в base64-кодировку
                const base64Data = reader.result;
                this.avatar = base64Data;
            };

            reader.readAsDataURL(file);
        },
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
                    <button type="button" @click="redirectToLike" class="btn btn-primary btn-circle">
                        <b-icon class="h1 mb-2" icon="suit-heart-fill" aria-hidden="true"></b-icon>
                    </button>
                </td>
            </tr>
        </table>
    </div>
    <br>
    <br>
    <div class="center-container">
        <div class="mb-2">
            <div class="avatar-container" @click="handleAvatarClick">
                <b-avatar size="10rem" :src="avatar"></b-avatar>
                <input type="file" ref="fileInput" style="display: none" @change="handleFileChange">
            </div>
        </div>
    </div>
    <br>
    <hr>
    <br>
    <div class="center-cont">
    <div class="input-container">
        <label for="name">Email:</label>
        <b-form-input v-model="email" type="email" placeholder="Введите ваш email"></b-form-input>
    </div>
    </div>
    <br>
    <div class="center-cont">
    <div class="input-container">
        <label for="name">Имя:</label>
        <b-form-input v-model="name" placeholder="Введите ваше имя"></b-form-input>
    </div>
    </div>
    <br>
     <div class="center-cont">
    <div class="input-container">
        <label for="name">Фамилия:</label>
        <b-form-input v-model="surname" placeholder="Введите вашу фамилию"></b-form-input>
    </div>
    </div>
    <br>
    <div class="center-cont">
        <div class="input-container">
            <label for="name">Отчество:</label>
            <b-form-input v-model="patronymic" placeholder="Введите ваше отчество"></b-form-input>
        </div>
    </div>
    <br>
    <hr>
    <div class="center-cont">
        <div class="input-container">
            <label for="name"> Номер телефона:</label>
            <b-form-input v-model="phone_number" placeholder="Введите номер телефона"></b-form-input>
        </div>
    </div>
    <br>
    <div class="center-cont">
        <div class="input-container">
            <label for="name"> Дата рождения:</label>
            <b-form-input v-model="data_of_birthday" type='date'></b-form-input>
        </div>
    </div>
    <br>
    <hr>
    <div class="center-cont">
        <div class="input-container">
            <label for="name">Город:</label>
            <b-form-input v-model="city" placeholder="Введите город доставки"></b-form-input>
        </div>
    </div>
    <br>
    <div class="center-cont">
        <div class="input-container">
            <label for="name">Улица:</label>
            <b-form-input v-model="street" placeholder="Введите улицу доставки"></b-form-input>
        </div>
    </div>
    <br>
    <div class="center-cont">
        <div class="input-container">
            <label for="name">Дом:</label>
            <b-form-input v-model="house" placeholder="Введите номер дом"></b-form-input>
        </div>
    </div>
    <br>
    <div class="center-cont">
        <div class="input-container">
            <label for="name">Корпус (если есть):</label>
            <b-form-input v-model="corps" placeholder="Введите номер корпуса"></b-form-input>
        </div>
    </div>
    <br>
    <div class="center-cont">
        <div class="input-container">
            <label for="name"> Квартира:</label>
            <b-form-input v-model="apartment" placeholder="Введите номер квартиры"></b-form-input>
        </div>
    </div>
    <br>
    <a href="">Сбросить пароль</a>
    <br>
    <br>
    <FooterMain/>
</template>

<style scoped>
.input-container {
    display: flex;
    align-items: center;
    max-width: 100%;
}

.center-container {
    display: flex;
    justify-content: center;
    align-items: center;

}

.center-cont {
    display: flex;
    justify-content: center;
    align-items: center;
}

.input-container label {
    margin-right: 1rem;
}

.avatar-container {
    background-color: #d5d4d4;
    width: 10rem;
    height: 10rem;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
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