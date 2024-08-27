import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from "./router";  // 在客户端项目的导包语法中，目录下的index.js的作用类似于python的__init__.py
import store from "./store"


createApp(App).use(router).use(store).mount('#app')
