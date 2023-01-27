import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store/index.js'
import './assets/main.css'
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";
/* ServiceWorker for PWA */
import './registerServiceWorker';

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faCar, faPlus, faEdit, faParking } from '@fortawesome/free-solid-svg-icons'

/* add icons to the library */
library.add(faCar, faPlus, faEdit, faParking)

let app = createApp(App)
app.component('font-awesome-icon', FontAwesomeIcon)
app.use(store).use(router).mount('#app')
