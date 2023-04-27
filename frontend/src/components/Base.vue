<template>
    <div>
        <div>
            <b-tabs content-class="mt-3" justified>
                <b-tab title="Для мастериц" active>
                    <br>
                    <br>
                </b-tab>
                <b-tab title="Для покупателей">
                    <br>
                    <br>
                    <b-card-group deck>
                    <div class="row" style="display: flex; justify-content: space-evenly;">
                        <b-card v-for="item in items" :key="item"
                                :to="`/item/${item.id}`"
                                :img-src="item.picture"
                                :title="item.item.name"
                                img-alt="Изображение"
                                img-top
                                tag="article"
                                style="max-width: 20rem"
                                class="card-scale md-4 mb-4"
                        >
                            <b-card-title class='d-flex justify-content font-weight-bold'>{{ item.item.price }} ₽</b-card-title>
                            <b-card-text class="text-truncate d-flex justify-content" style="max-width: 300px;">
                                {{ item.item.description }}
                            </b-card-text>
                        </b-card>
                        </div>
                    </b-card-group>
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
                const response = await fetch("http://127.0.0.1:8000/items/");
                this.items = await response.json();
            } catch (error) {
                this.error = "Произошла ошибка при запросе данных, попробуйте еще раз"
            }
        },
    }
}
</script>

<style scoped>
.card-scale {
  transition: transform 0.3s ease-out;
}

.card-scale:hover {
  transform: scale(1.05);
}
</style>