import './assets/main.css'
import 'vue-material-design-icons/styles.css';

import { createApp } from 'vue';
import { createPinia } from 'pinia'

import router from './routes';
import App from './App.vue';


const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
