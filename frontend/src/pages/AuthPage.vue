<template>
    <br>
    <br>
    <div class="col-md-4 offset-md-4">
        <div class="form-container">
            <div class="form-icon"><i class="fa fa-user"></i></div>
            <h3 class="title">Регистрация</h3>
            <form class="form-horizontal">
                <div class="form-group">
                    <hr>
                    <br>
                    <p>{{ msg }}</p>
                    <br>
                    <label for="email"><b>Email: </b></label>{{ ' ' }}
                    <input class="form-control" @change="get_email" name="email" type="text" v-model="email"/>
                    <br>
                    <br>
                    <label for="psw"><b>Пароль: </b></label> {{ ' ' }}
                    <input class="form-control" @change="get_psw" name="psw" type="password" v-model="psw"/>
                    <br>
                    <br>
                    <label for="psw-repeat"><b>Повторите пароль: </b></label> {{ ' ' }}
                    <input class="form-control" @change="get_psw_rep" name="psw_repeat" type="password" v-model="psw_repeat"/>
                    <br>
                    <br>
                    <br>
                    <button type="submit" v-on:click.prevent="sub" class="btn btn-default">Регистрация</button>
                </div>
                <br>
                <div class="container signin">
                    <p>У вас уже есть аккаунт?<a href="/menu/login/"> Войти</a>.</p>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
export default {
    name: "AuthPage",
    data() {
        return {
            msg: '',
            email: '',
            psw: '',
            psw_repeat: '',
            date: {}
        }
    },
    methods: {
        async get_email(event) {
            event.stopImmediatePropagation();
            const text = event.target.value;
            this.date['email'] = text
            console.log(this.date)
        },
        async get_psw(event) {
            event.stopImmediatePropagation();
            const text = event.target.value;
            this.date['psw'] = text
            console.log(this.date)
        },
        async get_psw_rep(event) {
            event.stopImmediatePropagation();
            const text = event.target.value;
            this.date['psw_repeat'] = text
            console.log(this.date)
        },
        sub: function(){
            if (!this.psw_repeat.length) {
                    this.msg = 'Введите повторно пароль'
                }
                if (!this.psw.length) {
                    this.msg = "Введите пароль"
                }
                if (!this.email.length) {
                    this.msg = 'Введите email'
                }
                if (!(this.psw === this.psw_repeat)) {
                    this.msg = 'Введенные пароли не совпадают'
                }
        }
    }
}
</script>

<style scoped>
.form-container{
 background: #FAE8DC;
 font-family: 'Nunito', sans-serif;
 padding: 40px;
 border-radius: 20px;
 box-shadow: 14px 14px 20px #E6B493, -14px -14px 20px #ffffff;
}

.form-container .form-icon{
 color: #d39a74;
 font-size: 55px;
 text-align: center;
 line-height: 100px;
 width: 100px;
 height:100px;
 margin: 0 auto 15px;
 border-radius: 50px;
 box-shadow: 7px 7px 10px #d3a688, -7px -7px 10px #ffffff;
}

.form-container .title{
 color: #d39a74;
 font-size: 25px;
 font-weight: 700;
 text-transform: uppercase;
 letter-spacing: 1px;
 text-align: center;
 margin: 0 0 20px;
}

.form-container .form-horizontal .form-group{ margin: 0 0 25px 0; }

.form-container .form-horizontal .form-group label{
 font-size: 15px;
 font-weight: 600;
 text-transform: uppercase;
}

.form-container .form-horizontal .form-control{
 color: #333;
 background: #ffffff;
 font-size: 15px;
 height: 50px;
 padding: 20px;
 letter-spacing: 1px;
 border: none;
 border-radius: 50px;
 box-shadow: inset 6px 6px 6px #ffffff, inset -6px -6px 6px #f3dbcc;
 display: inline-block;
 transition: all 0.3s ease 0s;
}

.form-container .form-horizontal .form-control:focus{
 box-shadow: inset 6px 6px 6px #ffffff, inset -6px -6px 6px #d3a688;
 outline: none;
}

.form-container .form-horizontal .form-control::placeholder{
 color: #ffffff;
 font-size: 14px;
}

.form-container .form-horizontal .btn{
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

.form-container .form-horizontal .btn:hover,
.form-container .form-horizontal .btn:focus{
 color: #000000;
 letter-spacing: 3px;
 box-shadow: none;
 outline: none;
}
</style>