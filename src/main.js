import { createApp } from 'vue'

import App from './App.vue'

// BootStrap 5.3.3v
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

import FoodItem from './components/FoodItem.vue'
import TestItem from './components/TestItem.vue'

const app = createApp(App)
app.component('food-item', FoodItem)
app.component('test-item', TestItem)
app.mount("#app")

//createApp(App).mount('#app')
