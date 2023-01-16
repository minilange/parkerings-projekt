import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import LoginView from '../views/LoginView.vue'
import ParkView from '../views/ParkView.vue'
import NewParkingView from '../views/NewParkingView.vue'
import AreaView from '../views/AreaView.vue'
import NotFound from '../views/NotFoundView.vue'
import RegisterView from '../views/RegisterView.vue'
import CarRegisterView from '../views/CarRegisterView.vue'
import ProfileView from '../views/ProfileView.vue'
import AdminView from '../views/AdminView.vue'
// import store from '../store/index.js'

function isLoggedIn() {
  // if(!Object.keys(store.state.user).length == 0){
  //   return true
  // }else{
  //   return false
  // }

  return true;
}
function isAdmin() {
  /* Commented out for test purposes!  */
  // if(!Object.keys(store.state.user).length == 0){
  //   return true
  // }else{
  //   return false
  // }

  return true;
}

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/about',
    name: 'about',
    component: AboutView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/park',
    name: 'park',
    component: ParkView
  },
  {
    path: '/new-parking',
    name: 'newparking',
    component: NewParkingView
  },
  {
    path: '/areas',
    name: 'areas',
    component: AreaView
  },
  {
    path: '/register',
    name: 'registers',
    component: RegisterView
  },
  {
    path: '/register-car',
    name: 'carregister',
    component: CarRegisterView
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView,
    beforeEnter: [isLoggedIn]
  },
  {
    path: '/admin',
    name: 'admin',
    component: AdminView,
    beforeEnter: [isAdmin] 
  },
  {
    path: "/:catchAll(.*)",
    component: NotFound,
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
