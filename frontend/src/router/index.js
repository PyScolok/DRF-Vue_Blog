import Vue from 'vue'
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import Single from '../views/Single.vue';

Vue.use(VueRouter);

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
    },
    {
        path: '/:slug',
        name: 'Single',
        component: Single,
        props: true,
    }
]

const router = new VueRouter({
    mode: 'history',
    routes: routes,
})

export default router