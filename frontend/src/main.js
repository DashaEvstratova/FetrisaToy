import {createApp} from 'vue'
import { createRouter, createWebHistory } from "vue-router"
import App from './App.vue'
import AuthPage from "@/pages/AuthPage";
import { BootstrapVue, IconsPlugin, ModalPlugin } from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

const routeInfos = [
    {
        path : "/auth",
        component : AuthPage
    },
]

const router = createRouter({
    history : createWebHistory(),
    routes : routeInfos
})

const app=createApp(App)
app.use(BootstrapVue)
app.use(IconsPlugin)
app.use(ModalPlugin)

app.use(router).mount('#app')