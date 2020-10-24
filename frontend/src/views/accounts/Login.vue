<template>
  <div>
    <h1>로그인</h1>
    <div>
      <img :src="logo" alt="" class="mylogo">
      <b-container fluid class="pb-4 px-0">
        <b-row class="my-1 align-items-center">
          <b-col cols="4" class="pr-0 text-left">
            <label for="username" class="mb-0">아이디:</label>
          </b-col>
          <b-col cols="8" class="pl-0">
            <b-form-input v-model="loginData.username" id="username" type="text" placeholder="아이디를 입력하세요."></b-form-input>
          </b-col>
        </b-row>
        <b-row class="my-1 align-items-center">
          <b-col cols="4" class="pr-0 text-left">
            <label for="password" class="mb-0">비밀번호:</label>
          </b-col>
          <b-col cols="8" class="pl-0">
            <b-form-input v-model="loginData.password" @keyup.enter="login" id="password" type="password" placeholder="비밀번호를 입력하세요."></b-form-input>
          </b-col>
        </b-row>
      </b-container>
      <div>
        <b-button block @click="login" class="mybutton mb-2">로그인</b-button>
      </div>
      <div class="text-right">
        <!-- 아직 비밀번호 찾기 component 없음 -->
        <router-link :to="{ name: 'ResetPassword' }" class="d-inline mr-3 mytext">비밀번호 찾기</router-link>
        <!-- <p class="d-inline mr-3 mytext">비밀번호 찾기</p> -->
        <router-link :to="{ name: 'Signup' }" class="d-inline mytext">회원가입</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import logo from '@/assets/logo.png'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Login',
  data() {
    return {
      loginData: {
        username: null,
        password: null,
      },
      logo,
    }
  },
  props: {
    isLoggedIn: Boolean,
  },
  methods: {
    setCookie(token) {
      // 발급 받은 token을 쿠키에 저장
      this.$cookies.set('auth-token', token)
      this.$emit('login')
    },

    login() {
      console.log(SERVER_URL)
      axios.post(SERVER_URL + '/rest-auth/login/', this.loginData)
        .then(res => {
          this.setCookie(res.data.key)  // { key: 'asdfasdfasdf' }
          this.$router.push({ name: 'Home' })
        })
        .catch(err => {
        alert('아이디와 비밀번호를 확인해주세요')
        console.log(err.response.data)
        })
    },
  },
}
</script>

<style scoped>
  input[type=password] {
    font-family: Arial, Helvetica, sans-serif;
  }
  ::placeholder {
    font-family: 'Cafe24Oneprettynight';
  }
  .mybutton {
    background-color: #fa1e44;
    border: none;
  }
  .mylogo {
    height: 300px;
    margin-bottom: 20px;
  }
  .mytext {
    color: #084481;
  }
</style>