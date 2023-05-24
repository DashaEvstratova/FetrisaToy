<template>
  <div>
    <ul>
      <li v-for="message in messages" :key="message.id">{{ message.text }}</li>
    </ul>
    <input type="text" v-model="newMessage">
    <button @click="sendMessage">Отправить</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      messages: [],
      newMessage: '',
    }
  },
  mounted() {
    this.$options.sockets.onmessage = (message) => {
      this.messages.push(JSON.parse(message.data))
    }
  },
  methods: {
    sendMessage() {
      this.$socket.send(JSON.stringify({ message: this.newMessage }))
      this.newMessage = ''
    },
  },
}
</script>
