import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './assets/main.css'
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";
/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faCar, faPlus } from '@fortawesome/free-solid-svg-icons'

/* add icons to the library */
library.add(faCar, faPlus)

createApp(App).component('font-awesome-icon', FontAwesomeIcon).use(router).mount('#app')
