<template>
  <div id="app">
    <!-- <div id="nav">
      <router-link to="/blogarticle">list</router-link>
    </div> -->
    <Header class="sticky-top"/>
    <router-view :isLoggedIn="isLoggedIn" @login="login" @signup="signup" @logout="logout" class="py-5 my-3 mybody"/>
    <Footer id="foot" :isLoggedIn="isLoggedIn"/>
  </div>
</template>

<script>
import axios from 'axios'
// axios.post(URL, BODY, HEADER)

// import BlogArticle from './components/BlogArticle.vue'
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'App',
  data() {
    return {
      isLoggedIn: false,
      scrolled: 0,
    }
  },
  components:{
    // BlogArticle,
    Header,
    Footer,
  },
  methods: {
    signup() {
      // login 상태를 true로 변경
      this.isLoggedIn = true
    },

    login() {
      // login 상태를 true로 변경
      this.isLoggedIn = true
    },
    
    logout() {
      // 삭제할 token 값을 담아서 backend로 요청을 보내야 함
      const config = {
        headers: {
          'Authorization': `Token ${this.$cookies.get('auth-token')}`
        }
      }
      
      axios.post(SERVER_URL + '/rest-auth/logout/', null, config)
        .then(res => {
          this.$cookies.remove('auth-token')
          this.isLoggedIn = false
          this.$router.push({ name: 'Home' })
        })
        .catch(err => console.log(err.reponse.data))
    },

    detectWindowScrollY() {
      var now = this.scrolled
      this.scrolled = window.scrollY
      var foot = document.getElementById('foot')
      if (now-this.scrolled<0) {foot.className='nav myfooter pt-1 align-items-center nav-justified m-fadeOut'}
      else if (now-this.scrolled>0) {foot.className='nav myfooter pt-1 align-items-center nav-justified m-fadeIn'}
    }
  },
  mounted() {
    // cookie에 auth-token이 있는지 체크
    this.isLoggedIn = this.$cookies.isKey('auth-token')
    window.addEventListener('scroll', this.detectWindowScrollY)
  },
  beforeDestory() {
    window.removeEventListener('scroll', this.detectWindowScrollY)
  }
}
</script>

<style scoped>
  #app {
    font-family: 'Cafe24Oneprettynight';
    text-align: center;
    height: 100%;
    /* background-color: #fefbf0; */
  }
  .mybody{
    width: 80%;
    margin: 0 auto;
    font-weight: bold;
  }
  #nav {
    padding: 30px;
  }

  #nav a {
    font-weight: bold;
    color: #2c3e50;
  }

  #nav a.router-link-exact-active {
    color: #42b983;
  }

  .m-fadeOut {
    visibility: hidden;
    opacity: 0;
    transition: visibility 0s linear 300ms, opacity 300ms;
  }

  .m-fadeIn {
    visibility: visible;
    opacity: 1;
    transition: visibility 0s linear 0s, opacity 300ms;
  }
</style>
