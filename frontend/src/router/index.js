import Vue from 'vue'
import VueRouter from 'vue-router';
import HomePage from '../views/HomePage.vue';
import SinglePost from '../views/SinglePost.vue';
import PostsByTag from '../views/PostsByTag.vue';
import PostsByCategory from '../views/PostsByCategory.vue';
import AboutPage from '../views/AboutPage.vue';
import ContactPage from '../views/ContactPage.vue';

Vue.use(VueRouter);

const routes = [
    {
        path: '/',
        name: 'HomePage',
        component: HomePage,
    },
    {
        path: '/about',
        name: 'AboutPage',
        component: AboutPage,
    },
    {
        path: '/contacts',
        name: 'ContactPage',
        component: ContactPage
    },
    {
        path: '/:slug',
        name: 'Single',
        component: SinglePost,
        props: true,
    },
    {
        path: '/tag/:slug',
        name: 'PostsByTag',
        component: PostsByTag, 
        props: true,
    },
    {
        path: '/category/:slug',
        name: 'PostsByCategory',
        component: PostsByCategory,
        props: true,
    },
]

const router = new VueRouter({
    mode: 'history',
    routes: routes,
})

export default router