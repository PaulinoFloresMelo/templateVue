import { createWebHistory, createRouter } from 'vue-router';

// crear objeto rutas de vue router -- objeto VR

const Home = () => import ('../views/Home.vue')
const About = () => import ('../views/About.vue')
const Cosmos = () => import ('../views/Cosmos.vue')
const Prueba = () => import ('../views/Prueba.vue')

const routes = [
    { path: '/', component: Home },
    { path: '/about', component: About },
    { path: '/cosmos', component: Cosmos },
    { path: '/prueba', component: Prueba },
  ]

// instancia de vue
const router = createRouter({
    history: createWebHistory(),
    routes,
  });

export default router;