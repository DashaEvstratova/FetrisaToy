import { createRouter, createWebHistory } from "vue-router"
import App from './App.vue'
import Vue, { createApp} from '@vue/compat';
import AuthPage from "@/pages/AuthPage";
import LoginPage from "@/pages/LoginPage.vue";
import {BootstrapVue, BootstrapVueIcons} from "bootstrap-vue";

// Import Bootstrap and BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

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
Vue.use(BootstrapVue);
Vue.use(BootstrapVueIcons);
const app = createApp(App)

app.use(router).mount('#app')