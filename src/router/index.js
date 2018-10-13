import Vue from 'vue'
import Router from 'vue-router'
import firebase from 'firebase'
import db from '@/firebase/init.js'
import store from '@/store/store.js'
import login from '@/components/login'
import editprofile from '@/components/edit-profile'
import profile from '@/components/profile'
import home from '@/components/home'
import dashboard from '@/components/dashboard'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/login',
      name: 'login',
      component: login
    },
    {
      path: '/editprofile',
      name: 'editprofile',
      component: editprofile,
      meta:{
        requiresAuth: true
      }
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: dashboard,
      meta:{
        requiresAuth: true
      }
    },
    {
      path: '/profile/:uname',
      name: 'profile',
      component: profile
    },
    {
      path: '/',
      name: 'home',
      component: home
    }
  ]
})

router.beforeEach((to,from,next) => {
  if (to.matched.some(rec => rec.meta.requiresAuth)) {
    let user = store.state.user
    if (user) {
      next()
    }
    else {
      next({name:'login'})
      }
    }
    else {
      next()
  }
})

export default router
