<template>
  <b-container class="myhome d-flex justify-content-center align-items-center pb-5">
    <b-row>
      <b-col cols="12" md="6" offset-md="3">
        <img :src="image" class="myimage" alt="">
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import image from '@/assets/main_image.png'

export default {
  name: 'Home',
  data() {
    return {
      image,
    }
  }
}
</script>

<style scoped>
  .myhome {
    height: 100%;
  }
  .myimage {
    width: 100%;
  }
</style>