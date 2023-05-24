<template>
    <form @submit.prevent="connect">
        <b-input placeholder="ID заметки" v-model="noteId" />
        <button>Подключиться</button>
    </form>
    <hr>
    <form @submit.prevent="sendMessage">
        <b-input placeholder="Сообщение" v-model="message" />
        <button>Отправить</button>
    </form>

    <b>Сообщения</b>
    <pre>{{messages}}</pre>
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