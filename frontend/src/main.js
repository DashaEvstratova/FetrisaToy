import {createApp} from 'vue'
import { createRouter, createWebHistory } from "vue-router"
import App from './App.vue'
import AuthPage from "@/pages/AuthPage";

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

createApp(App).use(router).mount('#app')