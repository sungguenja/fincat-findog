<template>
  <div>
    <h1>회원가입</h1>
    <div>
      <b-container fluid class="py-4 px-0">
        <b-row class="my-1 align-items-center">
          <b-col cols="4" class="pr-0 text-left">
            <label for="username" class="mb-0">아이디:</label>
          </b-col>
          <b-col cols="8" class="pl-0">
            <b-form-input v-model="signupData.username" id="username" type="text" placeholder="아이디를 입력하세요."></b-form-input>
          </b-col>
        </b-row>
        <b-row class="my-1 align-items-center">
          <b-col cols="4" class="pr-0 text-left">
            <label for="password1" class="mb-0">비밀번호:</label>
          </b-col>
          <b-col cols="8" class="pl-0">
            <b-form-input v-model="signupData.password1" id="password1" type="password" placeholder="비밀번호를 입력하세요."></b-form-input>
          </b-col>
        </b-row>
        <b-row class="my-1 align-items-center">
          <b-col cols="4" class="pr-0 text-left">
            <label for="password2" class="mb-0">비밀번호 확인:</label>
          </b-col>
          <b-col cols="8" class="pl-0">
            <b-form-input v-model="signupData.password2" id="password2" type="password" placeholder="비밀번호를 다시 입력하세요."></b-form-input>
          </b-col>
        </b-row>
        <b-row class="my-1 align-items-center">
          <b-col cols="4" class="pr-0 text-left">
            <label for="email" class="mb-0">이메일:</label>
          </b-col>
          <b-col cols="8" class="pl-0">
            <b-form-input v-model="signupData.email" id="email" type="email" placeholder="이메일을 입력하세요."></b-form-input>
          </b-col>
        </b-row>
        <b-row class="my-1 align-items-center">
          <b-col cols="4" class="pr-0 text-left">
            <label for="nickname" class="mb-0">닉네임:</label>
          </b-col>
          <b-col cols="8" class="pl-0">
            <b-form-input v-model="signupData.nickname" id="nickname" type="text" placeholder="닉네임을 입력하세요."></b-form-input>
          </b-col>
        </b-row>
        <b-row class="my-1 align-items-center">
          <b-col cols="4" class="pr-0 text-left">
            <label for="phone" class="mb-0">연락처:</label>
          </b-col>
          <b-col cols="8" class="pl-0">
            <b-form-input v-model="signupData.phone_number" id="phone" type="tel" placeholder="연락처를 입력하세요."></b-form-input>
          </b-col>
        </b-row>
      </b-container>
      <div>
        <b-button block @click="signup" class="mybutton mb-2">회원가입</b-button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Signup',
  data() {
    return {
      signupData: {
        username: null,
        password1: null,
        password2: null,
        email: null,
        nickname: null,
        phone_number: null,
      }
    }
  },
  props: {
    isLoggedIn: Boolean,
  },
  methods: {
    setCookie(token) {
      // 발급 받은 token을 쿠키에 저장
      this.$cookies.set('auth-token', token)
      this.$emit('signup')
    },

    signup() {
      axios.post(SERVER_URL + '/rest-auth/signup/', this.signupData)
        .then(res => {
          this.setCookie(res.data.key)  // { key: 'asdfasdfasdf' }
          this.$router.push({ name: 'Home' })
        })
        .catch(err => console.log(err.response.data))
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
</style>