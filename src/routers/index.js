import {createRouter, createWebHistory} from 'vue-router'

const routes = [
    {
        path: '/login',
        name: 'login',
        component: () => import('@/views/login/login')
    },
    {
        path: '/register',
        component: ()=>import('@/views/register/register')
    },
    {
        path: '/reader',
        component:()=>import('@/views/reader/reader')
    }
]

const history = createWebHistory()
const router = createRouter({
    history, // 路由模式
    routes,
})
export default router