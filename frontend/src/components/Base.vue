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
                    <b-card
                            img-src="https://sun9-57.userapi.com/impg/rypwy6KP-GuW2TYSrRo-g7jHeshxBISsv-OL_g/ER3WehheW2s.jpg?size=1080x1068&quality=95&sign=02d3b92aecd6aa3c098af70c1a162655&type=album"
                            img-alt="Изображение"
                            img-top
                            tag="article"
                              style="max-width: 20rem"
                            class="mb-2"
                        ><p style="align:'left'">800 ₽</p>
                            <b-button href="#" variant="primary">Иди куда-нибудь</b-button>
                        </b-card>
                </b-tab>
            </b-tabs>
        </div>
    </div>
</template>

<script>
export default {
  name: "TabContent",
  data() {
    return {
    }
  },
}
</script>

<style scoped>
</style>