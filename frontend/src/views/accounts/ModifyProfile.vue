<template>
  <div>
    <h1>수정 페이지</h1>
    <b-input-group class="my-2">
      <template v-slot:prepend>
        <b-input-group-text>이름</b-input-group-text>
      </template>
      <b-form-input v-model="user.username" @keyup.enter="submit"></b-form-input>
    </b-input-group>
    <b-input-group class="my-2">
      <template v-slot:prepend>
        <b-input-group-text>닉네임</b-input-group-text>
      </template>
      <b-form-input v-model="user.nickname" @keyup.enter="submit"></b-form-input>
    </b-input-group>
    <b-input-group class="my-2">
      <template v-slot:prepend>
        <b-input-group-text>연락처</b-input-group-text>
      </template>
      <b-form-input v-model="user.phone_number" @keyup.enter="submit"></b-form-input>
    </b-input-group>
    <button @click="submit" class="my-2 btn btn-success">제출</button>
  </div>
</template>

<script>
import Axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL
export default {
  data() {
    return {
      user: {}
    }
  },
  created() {
    const token = this.$cookies.get('auth-token')
    Axios({
      method:"GET",
      url:`${SERVER_URL}/rest-auth/user`,
      headers:{
        'Authorization':`Token ${token}`,
      }})
    .then(res => {
        this.user = res.data
        })
    .catch(err => {console.log(err)})
  },
  methods: {
    submit() {
      const token = this.$cookies.get('auth-token')
      Axios({
        method: 'PUT',
        url: `${SERVER_URL}/rest-auth/user/`,
        headers:{
          'Authorization':`Token ${token}`
        },
        data: {
          "username": this.user.username,
          "email": this.user.email,
          "nickname": this.user.nickname,
          "phone_number": this.user.phone_number,
          "password": this.user.password
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

</style>