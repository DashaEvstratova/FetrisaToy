<script>
import axios from 'axios'

export default {
    name: "ItemPage",
    data() {
        return {
            item: {}
        }
    },
    mounted() {
        this.getItemById(this.$route.params.id)
            .then(item => {
                this.item = item

            })
    },
    methods: {
        async getItemById(id) {
            return axios.get(`http://127.0.0.1:8000/items/${id}/`)
                .then(response => {
                    return response.data
                })
                .catch(error => {
                    // Обработка ошибки
                    console.log(error)
                })
        }
    }
}
</script>

<template>
<p>{{ item }}</p>
</template>


<style scoped>

</style>