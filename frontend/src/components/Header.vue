<template>
  <b-nav fill class="myheader d-flex justify-content-center align-items-center">
    <b-nav-item :to="{ name: 'Home' }">
      <img class="mylogo mb-0" :src="HeaderLogo" alt="header-logo">
    </b-nav-item>
  </b-nav>
</template>

<script>
import HeaderLogo from '@/assets/header-logo.png'

export default {
  name: 'Header',
  data() {
    return {
      HeaderLogo,
    }
  }
}
</script>

<style scoped>
  .myheader {
    background-color: #FEC925;
    position: fixed;
    top: 0;
    width: 100%;
    height: 50px;
    z-index: 1;
  }
  .mylogo {
    height: 40px;
  }
</style>