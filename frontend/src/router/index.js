import Vue from 'vue'
import VueRouter from 'vue-router'
import Sign from '../views/Sign.vue'
import Dashboard from '../views/Dashboard.vue'
import Reader from '../views/Reader.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Sign',
    component: Sign
  },
  {
    path: '/dashboard',
    name: "DashBoard",
    component: Dashboard
  },
  {
    path: '/reader',
    name: "Reader",
    component: Reader
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
  ,
  {
    path: '/reader',
    name: 'Reader',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Reader.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
