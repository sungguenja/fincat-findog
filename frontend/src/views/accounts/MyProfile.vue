<template>
  <div>
    <div>
      <h1>{{user.username}}님 페이지</h1>
    </div>
    <div class="d-flex justify-content-between mt-4 mb-3">
      <b-button @click="modifyPassword" class="mybutton1 mr-2">비밀번호 수정</b-button>
      <b-button @click="modifyProfile" class="mybutton2 ml-2">정보 수정</b-button>
    </div>
    <div class="d-flex justify-content-between mb-5">
      <b-button @click="logout" class="mybutton3 mr-2">로그아웃</b-button>
      <b-button v-b-modal.modal-prevent-closing class="mybutton4 ml-2">탈퇴하기</b-button>
    </div>
    <b-modal id="modal-prevent-closing" modal-class="mymodal" hide-footer>
      <template v-slot:modal-title>
        탈퇴 확인창
      </template>
      <div class="d-block text-center">
        <h3>탈퇴하시려면</h3>
        <h3>'탈퇴하겠습니다'</h3>
        <h3>라고 입력해주세요</h3>
        <b-form @submit.prevent="deleteAccount" class="my-3">
          <b-form-input v-model="text" placeholder="탈퇴하겠습니다"></b-form-input>
          <b-button class="my-3" block type="submit" variant="danger">탈퇴합니다</b-button>
        </b-form>
      </div>
      <b-button class="my-3" block @click="$bvModal.hide('modal-prevent-closing')">취소</b-button>
    </b-modal>
    <div class="d-block my-3" style="overflow: hidden;">
      <div class="d-none d-md-inline" style="float: left; width:45%;">
        <h2 class="mb-3">여행 간 우리 아이들</h2>
        <b-container>
          <b-list-group>
            <b-row>
              <b-col cols="3" class="p-0"><b-list-group-item class="px-1">제목</b-list-group-item></b-col>
              <b-col cols="3" class="p-0"><b-list-group-item class="px-1">종 (품종)</b-list-group-item></b-col>
              <b-col cols="6" class="p-0"><b-list-group-item class="px-1">내용 요약</b-list-group-item></b-col>
            </b-row>
            <b-row v-for="item in losts" :key="item.id">
              <b-col cols="3" class="p-0 grow"><b-list-group-item route :to="{ name: 'LostDetail', params: {pk:item.id} }" class="px-1">{{item.title}}</b-list-group-item></b-col>
              <b-col cols="3" class="p-0 grow"><b-list-group-item v-b-popover.bottomright="item.species.species" class="px-1">{{item.animal.kind}}</b-list-group-item></b-col>
              <b-col cols="6" class="p-0 grow"><b-list-group-item route :to="{ name: 'LostDetail', params: {pk:item.id} }" class="px-1">{{item.content}}</b-list-group-item></b-col>
            </b-row>
          </b-list-group>
        </b-container>
      </div>
      <div class="d-none d-md-inline" style="float: right; width: 45%;">
        <h2 class="mb-3">내가 찾은 아이들</h2>
        <b-container>
          <b-list-group>
            <b-row>
              <b-col cols="3" class="p-0"><b-list-group-item class="px-1">제목</b-list-group-item></b-col>
              <b-col cols="3" class="p-0"><b-list-group-item class="px-1">종 (품종)</b-list-group-item></b-col>
              <b-col cols="6" class="p-0"><b-list-group-item class="px-1">내용 요약</b-list-group-item></b-col>
            </b-row>
            <b-row v-for="item in finds" :key="item.id">
              <b-col cols="3" class="p-0 grow"><b-list-group-item route :to="{ name: 'Detail', params: {pk:item.id} }" class="px-1">{{item.title}}</b-list-group-item></b-col>
              <b-col cols="3" class="p-0 grow"><b-list-group-item v-b-popover.bottomright="item.species.species" class="px-1">{{item.animal.kind}}</b-list-group-item></b-col>
              <b-col cols="6" class="p-0 grow"><b-list-group-item route :to="{ name: 'Detail', params: {pk:item.id} }" class="px-1">{{item.content}}</b-list-group-item></b-col>
            </b-row>
          </b-list-group>
        </b-container>
      </div>
      <div class="d-block d-md-none">
        <h2 class="mb-3">여행 간 우리 아이들</h2>
        <b-container>
          <b-list-group>
            <b-row>
              <b-col cols="3" class="p-0"><b-list-group-item class="px-1">제목</b-list-group-item></b-col>
              <b-col cols="3" class="p-0"><b-list-group-item class="px-1">종 (품종)</b-list-group-item></b-col>
              <b-col cols="6" class="p-0"><b-list-group-item class="px-1">내용 요약</b-list-group-item></b-col>
            </b-row>
            <b-row v-for="item in finds" :key="item.id">
              <b-col cols="3" class="p-0 grow"><b-list-group-item route :to="{ name: 'LostDetail', params: {pk:item.id} }" class="px-1">{{item.title}}</b-list-group-item></b-col>
              <b-col cols="3" class="p-0 grow"><b-list-group-item v-b-popover.bottomright="item.species.species" class="px-1">{{item.animal.kind}}</b-list-group-item></b-col>
              <b-col cols="6" class="p-0 grow"><b-list-group-item route :to="{ name: 'LostDetail', params: {pk:item.id} }" class="px-1">{{item.content}}</b-list-group-item></b-col>
            </b-row>
          </b-list-group>
        </b-container>
        <h2 class="mt-5 mb-3">내가 찾은 아이들</h2>
        <b-container>
          <b-list-group>
            <b-row>
              <b-col cols="3" class="p-0"><b-list-group-item class="px-1">제목</b-list-group-item></b-col>
              <b-col cols="3" class="p-0"><b-list-group-item class="px-1">종 (품종)</b-list-group-item></b-col>
              <b-col cols="6" class="p-0"><b-list-group-item class="px-1">내용 요약</b-list-group-item></b-col>
            </b-row>
            <b-row v-for="item in losts" :key="item.id">
              <b-col cols="3" class="p-0 grow"><b-list-group-item route :to="{ name: 'Detail', params: {pk:item.id} }" class="px-1">{{item.title}}</b-list-group-item></b-col>
              <b-col cols="3" class="p-0 grow"><b-list-group-item v-b-popover.bottomright="item.species.species" class="px-1">{{item.animal.kind}}</b-list-group-item></b-col>
              <b-col cols="6" class="p-0 grow"><b-list-group-item route :to="{ name: 'Detail', params: {pk:item.id} }" class="px-1">{{item.content}}</b-list-group-item></b-col>
            </b-row>
          </b-list-group>
        </b-container>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  data() {
    return {
      user: {},
      text: null,
      finds: [],
      losts: [],
    }
  },
  methods: {
    logout() {
      this.$emit('logout')
    },

    modifyProfile() {
      this.$router.push({name:'ModifyProfile'})
    },

    modifyPassword() {
      this.$router.push({name:'ModifyPassword'})
    },

    deleteAccount() {
      const token = this.$cookies.get('auth-token')
      if (this.text != '탈퇴하겠습니다') {
        alert('입력하신 문구가 틀렸습니다')
        return false
      }
      axios({
        method: 'DELETE',
        url: `${SERVER_URL}/accounts/delete/`,
        headers:{
          'Authorization':`Token ${token}`
        }
      })
        .then(res => {
          alert('탈퇴가 완료되었습니다. \n 여행 간 반려동물이 돌아오셨기를 바랍니다')
          console.log(res)
        })
        .catch(err => {
          alert('에러가 발생했습니다 \n 확인해주세요')
          console.log(err)
        })
      this.logout()
    }
  },
  created() {
    const token = this.$cookies.get('auth-token')
    axios({
      method: "GET",
      url: `${SERVER_URL}/rest-auth/user`,
      headers: {
        'Authorization':`Token ${token}`,
      }})
      .then(res => {this.user = res.data})
      .catch(err => {console.log(err)})

    axios({
      method: "GET",
      url: `${SERVER_URL}/articles/myarticles/`,
      headers: {
        'Authorization':`Token ${token}`
      }
    })
      .then(res => {
        this.finds = res.data.articles_find
        this.losts = res.data.articles_lost
      })
      .catch(err => {
        console.log(err)
      })
  },
}
</script>

<style scoped>
  .grow { 
  transition: all .2s ease-in-out; 
  }
  .grow:hover { 
  transform: scale(1.05); 
  }
  .mybutton1 {
    width: 50%;
    background-color: #478BD1;
    border: none;
  }
  .mybutton2 {
    width: 50%;
    background-color: #084481;
    border: none;
  }
  .mybutton3 {
    width: 50%;
    background-color: #FF6A6A;
    border: none;
  }
  .mybutton4 {
    width: 50%;
    background-color: #FA1E44;
    border: none;
  }
  ::v-deep .mymodal {
    font-family: 'Cafe24Oneprettynight';
  }
  .popover {
    font-family: 'Cafe24Oneprettynight';
    font-weight: bold;
  }
</style>