<template>
    <div>
        <div>
            <b-tabs content-class="mt-3" justified>
                <b-tab title="Для мастериц" active>
                    <br>
                    <br>
                </b-tab>
                <p>{{items}}</p>
                <b-tab title="Для покупателей">
                    <br>
                    <br>
                    <div v-for="item in items" :key="item">
                    <b-card
                        img-src=''
                        img-alt="Изображение"
                        img-top
                        tag="article"
                        style="max-width: 20rem"
                        class="mb-2"
                    >
                        <b-card-header>{{item.item.name}}</b-card-header>
                        <b-card-body class='d-flex justify-content'>{{ item.item.price }} ₽</b-card-body>
                        <b-card-text class="text-truncate d-flex justify-content" style="max-width: 300px;">
                            {{ item.item.description }}
                        </b-card-text>
                        <b-button href="#" variant="primary">Иди куда-нибудь</b-button>
                    </b-card>
                    </div>
                </b-tab>
            </b-tabs>
        </div>
    </div>
</template>

<script>
export default {
  name: "TabContent",

    data(){
        return {
            items:this.load_items()
        }
    },
    methods: {
        async load_items() {
            try {
                const response = await fetch("http://127.0.0.1:8000/picturer/");
                this.items = await response.json();
            } catch (error) {
                this.error = "Произошла ошибка при запросе данных, попробуйте еще раз"
            }
        },
    }
}
</script>

<style scoped>
</style>