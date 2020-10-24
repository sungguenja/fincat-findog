<template>
  <div>
    <h1>비밀번호 수정</h1>
    <b-input-group>
      <template v-slot:prepend>
        <b-input-group-text >비밀번호</b-input-group-text>
      </template>
      <b-form-input v-model="password_1" type="password" placeholder="비밀번호를 입력하세요."></b-form-input>
    </b-input-group>
    <b-input-group>
      <template v-slot:prepend>
        <b-input-group-text >비밀번호 확인</b-input-group-text>
      </template>
      <b-form-input v-model="password_2" @keyup.enter="submit" type="password" placeholder="비밀번호를 확인해주세요."></b-form-input>
    </b-input-group>
    <button @click="submit">제출</button>
  </div>
</template>

<script>
import Axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL
export default {
  data() {
    return {
      password_1: '',
      password_2: ''
    }
  },
  methods: {
    submit() {
      if (this.password_1 != this.password_2) {
        alert('패스워드와 패스워드 확인문자가 맞질 않습니다.')
        return false
      }
      const token = this.$cookies.get('auth-token')
      Axios({
        method: 'POST',
        url: `${SERVER_URL}/rest-auth/password/change/`,
        headers:{
          'Authorization':`Token ${token}`
        },
        data: {
          "new_password1": this.password_1,
          "new_password2": this.password_2
        }
      })
      .then(res => {
        alert('수정성공')
        console.log(res)
        this.$router.push({name:'MyProfile'})
      })
      .catch(err => {
        alert(err.detail)
      })
    }
  }
}
</script>

<style>
  input[type=password] {
    font-family: Arial, Helvetica, sans-serif;
  }
  ::placeholder {
    font-family: 'Cafe24Oneprettynight';
  }
</style>