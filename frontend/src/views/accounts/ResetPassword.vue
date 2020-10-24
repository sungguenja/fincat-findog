<template>
    <div>
    <h1>비밀번호 찾기</h1>
    <b-input-group>
      <template v-slot:prepend>
        <b-input-group-text >이메일</b-input-group-text>
      </template>
      <b-form-input v-model="email" @keyup.enter="submit" placeholder="이메일을 입력하세요."></b-form-input>
    </b-input-group>
    <button @click="submit" class="btn btn-dark my-2">제출</button>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL
export default {
    data() {
        return {
            email: '',
        }
    },
    methods: {
        submit() {
            const context= {
                'email': this.email
            }
            axios.post(SERVER_URL + '/accounts/password_reset/', context)
            .then((res) => {
                console.log(res.data)
                alert("메일이 발송되었습니다")
                this.$router.push({ name: 'ResetPasswordConfirm' })
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