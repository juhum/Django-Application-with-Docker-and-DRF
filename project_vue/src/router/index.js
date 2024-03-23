import { createRouter, createWebHistory } from 'vue-router'
import store from '../store/index.js'
import HomeView from '../views/HomeView.vue'
import TaskView from '../views/TaskView'
import CategoryView from '../views/CategoryView'
import SignUpView from '../views/SignUpView'
import LoginView from '../views/LoginView'
import NotFoundView from '../views/NotFoundView'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/tasks',
    name: 'tasks',
    component: TaskView
  },
  {
    path: '/categories',
    name: 'categories',
    component: CategoryView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignUpView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/404',
    name: 'notfound',
    component: NotFoundView
  },
  {
    path: '/:pathMatch(.*)*',
    redirect: { name: 'notfound' }
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})


router.beforeEach((to, from, next) => {
  const isAuthenticated = localStorage.getItem("token");

  if (to.name === 'login' || to.name === 'signup') {
    if (isAuthenticated) {
      next('/');
    } else {
      next();
    }
  } else {
    next();
  }
});


export default router
