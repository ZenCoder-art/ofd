import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
    {
        path: '/',
        name: 'home',
        component: HomeView
    },
    {
        path: '/testing-center',
        name: 'testing-center',
        component: () => import('../views/TestCenterView.vue')
    },
    {
        path: '/model-explanation',
        name: 'model-explanation',
        component: () => import('../views/ModelView.vue')
    },
    {
        path: '/api-docs',
        name: 'api-docs',
        component: () => import('../views/ApiDocsView.vue')
    },
    {
        path: '/feedback',
        name: 'feedback',
        component: () => import('../views/FeedbackView.vue')
    }
]

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes,
    scrollBehavior() {
        return { top: 0 }
    }
})

export default router