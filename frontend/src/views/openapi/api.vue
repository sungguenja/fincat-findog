<template>
  <div>
    <div class="d-none d-md-block">
      검색 시작 날 : <input type="date" v-model="bgnde">
      검색 끝 날 : <input type="date" v-model="endde">
      지역구 : 
      <select v-model="org_cd">
        <option value="null">선택하세요</option>
        <option value="3220000">강남구</option>
        <option value="3240000">강동구</option>
        <option value="3080000">강북구</option>
        <option value="3150000">강서구</option>
        <option value="3200000">관악구</option>
        <option value="3040000">광진구</option>
        <option value="3160000">구로구</option>
        <option value="3170000">금천구</option>
        <option value="3100000">노원구</option>
        <option value="3090000">도봉구</option>
        <option value="3050000">동대문구</option>
        <option value="3190000">동작구</option>
        <option value="3130000">마포구</option>
        <option value="3120000">서대문구</option>
        <option value="3210000">서초구</option>
        <option value="3030000">성동구</option>
        <option value="3070000">성북구</option>
        <option value="3230000">송파구</option>
        <option value="3140000">양천구</option>
        <option value="3180000">영등포구</option>
        <option value="3020000">용산구</option>
        <option value="3110000">은평구</option>
        <option value="3000000">종로구</option>
        <option value="3010000">중구</option>
        <option value="3060000">중랑구</option>
      </select>
    </div>
    <div class="my-2 d-none d-md-block">
      중성화 여부 : 
      <select v-model="neuter_yn">
        <option value="null">모름</option>
        <option value="Y">했음</option>
        <option value="N">안했음</option>
      </select>
      동물 종류 : 
      <select v-model="upkind">
        <option value="417000">개</option>
        <option value="422400">고양이</option>
        <option value="429900">기타</option>
      </select>
    </div>
    <b-container class="d-block d-md-none">
      <b-row>
        <p class="col-12 my-1">검색 시작 날 : <input type="date" v-model="bgnde"></p>
        <p class="col-12 my-1">검색 끝 날 : <input type="date" v-model="endde"></p>
        <p class="col-12 my-1">지역구 : 
          <select v-model="org_cd">
            <option value="null">선택하세요</option>
            <option value="3220000">강남구</option>
            <option value="3240000">강동구</option>
            <option value="3080000">강북구</option>
            <option value="3150000">강서구</option>
            <option value="3200000">관악구</option>
            <option value="3040000">광진구</option>
            <option value="3160000">구로구</option>
            <option value="3170000">금천구</option>
            <option value="3100000">노원구</option>
            <option value="3090000">도봉구</option>
            <option value="3050000">동대문구</option>
            <option value="3190000">동작구</option>
            <option value="3130000">마포구</option>
            <option value="3120000">서대문구</option>
            <option value="3210000">서초구</option>
            <option value="3030000">성동구</option>
            <option value="3070000">성북구</option>
            <option value="3230000">송파구</option>
            <option value="3140000">양천구</option>
            <option value="3180000">영등포구</option>
            <option value="3020000">용산구</option>
            <option value="3110000">은평구</option>
            <option value="3000000">종로구</option>
            <option value="3010000">중구</option>
            <option value="3060000">중랑구</option>
          </select></p>
          <p class="col-12 my-1">중성화 여부 : 
            <select v-model="neuter_yn">
              <option value="null">모름</option>
              <option value="Y">했음</option>
              <option value="N">안했음</option>
            </select></p>
          <p class="col-12 my-1">동물 종류 : 
            <select v-model="upkind">
              <option value="417000">개</option>
              <option value="422400">고양이</option>
              <option value="429900">기타</option>
            </select>
          </p>
      </b-row>
    </b-container>
    <button @click="NewSearch" class="my-2 btn btn-primary">검색</button>
    <div v-show="IsSearch" class="my-2">
      <button v-show="pageNo != 1" @click="GoBefore" class="btn btn-light mx-5">이전</button>
      <button v-show="CanGoForward" @click="GoForward" class="btn btn-dark mx-5">다음</button>
    </div>
    <Card v-for="animal in SearchData" :key="animal.desertionno" v-bind:animal="animal" class="my-3"></Card>
    <div v-show="IsSearch" class="my-2">
      <button v-show="pageNo != 1" @click="GoBefore" class="btn btn-light mx-5">이전</button>
      <button v-show="CanGoForward" @click="GoForward" class="btn btn-dark mx-5">다음</button>
    </div>
  </div>
</template>

<script>
import Axios from 'axios'
import Card from '../../components/api_card'
const API_KEY = process.env.VUE_APP_OPEN_API_KEY
const API_URL = process.env.VUE_APP_SERVER_URL
export default {
  data() {
    return {
      bgnde: null,
      endde: null,
      upkind: null,
      upr_cd: 6110000,
      org_cd: null,
      neuter_yn: null,
      pageNo:1,
      numOfRows:20,
      IsSearch:false,
      SearchData:[],
      CanGoForward: true,
      TotalCount: 0
    }
  },
  methods: {
    search() {
      var url = 'http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/abandonmentPublic?'
      if (this.bgnde != null) {
        url = url + 'bgnde' + '=' + this.bgnde.replace(/-/g,'') +'&'
      }
      if (this.endde != null) {
        url = url + 'endde' + '=' + this.endde.replace(/-/g,'') +'&'
      }
      if (this.upkind != null) {
        url = url + 'upkind' + '=' + this.upkind +'&'
      }
      if (this.upr_cd != null) {
        url = url + 'upr_cd' + '=' + this.upr_cd +'&'
      }
      if (this.org_cd != null) {
        url = url + 'org_cd' + '=' + this.org_cd +'&'
      }
      if (this.neuter_yn != null) {
        url = url + 'neuter_yn' + '=' + this.neuter_yn +'&'
      }
      if (this.pageNo != null) {
        url = url + 'pageNo' + '=' + this.pageNo +'&'
      }
      if (this.numOfRows != null) {
        url = url + 'numOfRows' + '=' + this.numOfRows +'&'
      }
      if (API_KEY != null) {
        url = url + 'ServiceKey=' + API_KEY
      }
      Axios({
        method:'POST',
        url: `${API_URL}/articles/search_api/`,
        data:{'url':url}
        }
      )
      .then(res => {
        this.SearchData = res.data.animals
        this.TotalCount = res.data.cnt
        this.IsSearch = true
        if (this.SearchData.length<20) {this.CanGoForward = false}
        else {this.CanGoForward = true}
      })
      .catch(err => {
        console.log(err)
        console.log('실패')
      })
    },
    GoBefore() {
      this.pageNo -= 1
      this.search()
    },
    GoForward() {
      this.pageNo += 1
      this.search()
    },
    NewSearch() {
      this.pageNo = 1
      this.search()
    }
  },
  components: {
    Card
  }
}
</script>

<style>

</style>