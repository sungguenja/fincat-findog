import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

import Login from '@/views/accounts/Login.vue'
import Signup from '@/views/accounts/Signup.vue'
import MyProfile from '../views/accounts/MyProfile.vue'
import ModifyProfile from '../views/accounts/ModifyProfile.vue'
import ModifyPassword from '../views/accounts/ModifyPassword.vue'


import OpenApi from '../views/openapi/api.vue'

import Notice from "@/components/Notice.vue"
import LostNotice from "@/components/LostNotice.vue"

import WriteNotice from "@/components/WriteNotice.vue"
import LostWriteNotice from "@/components/LostWriteNotice.vue"

import Detail from "@/components/Detail.vue"
import LostDetail from "@/components/LostDetail.vue"

import ModifyNotice from "@/components/ModifyNotice.vue"
import ResetPassword from "../views/accounts/ResetPassword.vue"
import ResetPasswordConfirm from "../views/accounts/ResetPasswordConfirm.vue"





// error 페이지
import ErrorPage from "../views/Error.vue"

import LostModifyNotice from "@/components/LostModifyNotice.vue"

import Selectnotice from "@/components/Selectnotice.vue"



Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: "/accounts/myprofile",
    name: "MyProfile",
    component: MyProfile
  },
  {
    path: "/accounts/modify",
    name: "ModifyProfile",
    component: ModifyProfile
  },
  {
    path: "/accounts/modifypassword",
    name: "ModifyPassword",
    component: ModifyPassword
  },
  {
    path: "/accounts/resetpassword",
    name: "ResetPassword",
    component: ResetPassword
  },
  {
    path: "/accounts/resetpasswordconfirm",
    name: "ResetPasswordConfirm",
    component: ResetPasswordConfirm
  },
  {
    path: "/articles_find",
    name: "Notice",
    component: Notice
  },
  {
    path: "/articles_lost",
    name: "LostNotice",
    component: LostNotice
  },

  {
    path: "/articles_find/create",
    name: "WriteNotice",
    component: WriteNotice
  },
  {
    path: "/articles_lost/create",
    name: "LostWriteNotice",
    component: LostWriteNotice
  },

  {
    path: "/articles_find/:pk",
    name: "Detail",
    component: Detail
  },
  {
    path: "/articles_lost/:pk",
    name: "LostDetail",
    component: LostDetail
  },

  {
    path: "/articles_find/update/:pk",
    name: "ModifyNotice",
    component: ModifyNotice
  },
  {
    path: "/articles_lost/update/:pk",
    name: "LostModifyNotice",
    component: LostModifyNotice
  },
  {
    path: '/shelter',
    name: 'OpenApi',
    component: OpenApi
  },
  {
    path: '/selectnotice',
    name: 'Selectnotice',
    component: Selectnotice
  },
  {
    path: '*',
    name: 'ErrorPage',
    component: ErrorPage
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  const publicPages = ['Home', 'Login', 'Signup', 'ResetPassword', 'ResetPasswordConfirm', 'Notice', 'LostNotice', 'OpenApi', 'Selectnotice', 'ErrorPage']  // Login 안해도 됨
  const authPages = ['Login', 'Signup',]  // Login 되어있으면 안됨
  const loginRequiredPages = ['MyProfile', 'ModifyProfile', 'ModifyPassword', 'WriteNotice', 'LostWriteNotice', 'Detail', 'LostDetail', 'ModifyNotice', 'LostModifyNotice',]

  const authRequired = !publicPages.includes(to.name)  // 로그인 해야 함.
  const unauthRequired = authPages.includes(to.name)  // 로그인 해서는 안됨
  const loginRequired = loginRequiredPages.includes(to.name)
  const isLoggedIn = !!Vue.$cookies.isKey('auth-token')

  if (unauthRequired && isLoggedIn) {
    next("/");
  }
  if (loginRequired && !isLoggedIn) {
    alert('로그인이 필요합니다.')
    next({ name: "Login" })
  }
  authRequired && !isLoggedIn ? next({ name: "Login" }) : next();
});
export default router
