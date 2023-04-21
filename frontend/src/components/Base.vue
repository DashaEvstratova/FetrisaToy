<template>
    <div>
        <b-card no-body>
            <b-tabs card>
                <b-tab title="Tab 1" active>
                    <b-card-text>Tab contents 1</b-card-text>
                </b-tab>
                <b-tab title="Tab 2">
                    <b-card-text>Tab contents 2</b-card-text>
                </b-tab>
            </b-tabs>
        </b-card>
    </div>
</template>

<script>

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
export default {
  name: "main_frame",
  data() {
    return {
    }
  },
    compatConfig:{MODE: 3}
}
</script>

<style scoped>

</style>