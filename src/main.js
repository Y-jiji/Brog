import { createApp } from 'vue'
import App from './App.vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import router from './routers/index'
import axios from 'axios'

axios.defaults.withCredentials = true;
const instance = axios.create({
    baseURL:""
})
const app = createApp(App)
//app.config.unwrapInjectedRef = true
app.use(router)
app.use(ElementPlus)
app.config.globalProperties.$axios = instance
app.mount('#app')