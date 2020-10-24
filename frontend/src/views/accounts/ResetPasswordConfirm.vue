<template>
    <div>
    <h1>비밀번호 재설정</h1>
    <b-input-group class="my-2">
      <template v-slot:prepend>
        <b-input-group-text >비밀번호</b-input-group-text>
      </template>
      <b-form-input v-model="password" type="password" placeholder="비밀번호를 입력하세요."></b-form-input>
    </b-input-group>
    <b-input-group class="my-2">
      <template v-slot:prepend>
        <b-input-group-text >토큰</b-input-group-text>
      </template>
      <b-form-input v-model="token" @keyup.enter="submit" placeholder="토큰을 입력하세요."></b-form-input>
    </b-input-group>
    <button @click="submit" class="my-2 btn btn-outline-dark">제출</button>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL
export default {
    data() {
        return {
            password: '',
            tokne: '',
        }
    },
    methods: {
        submit() {
            const context = {
                password: this.password,
                token: this.token
            }
            axios.post(SERVER_URL + '/accounts/password_reset/confirm/', context)
            .then((res) => {
                alert("비밀번호가 변경되었습니다.")
                this.$router.push({ name: 'Login' })
            })
            .catch((err) => {
                console.log(err)
            })
        }
    }
}
</script>

<style>

</style>