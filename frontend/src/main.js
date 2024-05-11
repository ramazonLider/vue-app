import './assets/main.css';
import './assets/phoenix';
import './assets/anchor';
import './assets/bootstrap';
import './assets/dayjs';
import axios from "axios";


import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

const app = createApp(App)

axios.defaults.baseURL = "http://127.0.0.1:8000/api/"

app.use(createPinia())
app.use(router)

app.mount('#app')

