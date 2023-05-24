<template>
      <div class="col-md-4 offset-md-4">
        <div class="form-container">
            <div class="form-icon"><i class="fa fa-user"></i></div>
                <div class="form-group">
                    <hr>
                    <br>
    <form @submit.prevent="connect">
        <b-input class="small-input" placeholder="ID игрушки" v-model="noteId" size="10" />
      <br>
        <button>Подключиться</button>
    </form>
    <hr>
    <form @submit.prevent="sendMessage">
        <b-input class="small-input" placeholder="Сообщение" v-model="message" size="20" />
      <br>
        <button>Отправить</button>
    </form>
<br>
    <b>Сообщения</b>
                  <br>
    <pre>{{messages}}</pre>
                </div>
        </div>
      </div>
</template>

<script>
import {initNotifications} from "@/services/notifications";

export default {
    name: "TestView",
    data() {
        return {
            noteId: null,
            message: null,
            messages: ''
        };
    },
    methods: {
        connect() {
            this.send = initNotifications(this.noteId, (message) => {
                this.messages += message.message + "\n";
            })
        },
        sendMessage() {
            this.send({message: this.message});
            this.message = null;
        }
    }
}
</script>
<style>
.small-input {
    width: 150px;
}
</style>