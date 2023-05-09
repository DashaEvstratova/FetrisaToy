import { createRouter, createWebHistory } from "vue-router"
import App from './App.vue'
import Vue, { createApp} from '@vue/compat';
import AuthPage from "@/pages/AuthPage";
import LoginPage from "@/pages/LoginPage.vue";
import MainPage from "@/pages/MainPage.vue";
import ItemPage from "@/pages/ItemPage.vue"
import LikePage from "@/pages/LikePage.vue";
import BuketPage from '@/pages/BuketPage.vue'
import {BootstrapVue, BootstrapVueIcons} from "bootstrap-vue";
import PayPage from "@/pages/PayPage.vue";
import ProfilePage from "@/pages/ProfilePage.vue";

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
    },
    {
        path:"/menu",
        component: MainPage
    },
    {
        path: '/item/:id',
        name: 'ItemPage',
        component: ItemPage,
    },
    {
        path:'/bucket',
        component: BuketPage
    },
    {
        path:'/like',
        component: LikePage
    },
    {
        path:'/pay',
        component: PayPage
    },
    {
        path:'/profile',
        component: ProfilePage
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