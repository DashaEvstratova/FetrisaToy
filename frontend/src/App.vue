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
      <router-view/>
</template>
<script>

export default {
    name: 'App',
    components: {
    }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
