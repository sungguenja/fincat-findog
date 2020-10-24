<template>
  <div>
    <h2>찾을 수 없거나</h2>
    <h2>원인 모를 에러가</h2>
    <h2>발견되었습니다.</h2>
    <img :src="logo" alt="" class="mylogo">
    <div>
      <b-button block @click="goToMain" class="mybutton mb-2">메인페이지로 가기</b-button>
    </div>
  </div>
</template>

<script>
import logo from '@/assets/logo.png'

export default {
  name: 'Error',
  data() {
    return {
      logo,
    }
  },
  methods: {
    goToMain() {
      this.$router.push({ name: 'Home' })
    }
  }
}
</script>

<style scoped>
  .mylogo {
    height: 300px;
    margin-bottom: 20px;
  }
  .mybutton {
    background-color: #fa1e44;
    border: none;
  }
</style>