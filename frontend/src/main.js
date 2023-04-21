import {createApp} from 'vue'
import { createRouter, createWebHistory } from "vue-router"
import App from './App.vue'
import AuthPage from "@/pages/AuthPage";
import LoginPage from "@/pages/LoginPage.vue";


const routeInfos = [
    {
        path : "/auth",
        component : AuthPage
    },
    {
        path:"/login",
        component: LoginPage
    }
]

const router = createRouter({
    history : createWebHistory(),
    routes : routeInfos
})

const app = createApp(App)

app.use(router).mount('#app')