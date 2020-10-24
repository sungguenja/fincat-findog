<template>
  <div>
    <h2>여행 중인 반려동물</h2>
    <hr />
    <div class="d-flex justify-content-between">
      <select
        name="city"
        id="city"
        class="form-control"
        title="시"
        v-model="selectedCity"
        @change="getArticles"
      >
        <option value="null">시</option>
        <!-- <option value="all">시</option>			 -->
        <option v-for="(citys,id) in sido" :key="id" :value="citys.city">{{citys.city}}</option>
      </select>
      <select
        name="borough"
        id="borough"
        class="form-control mx-4"
        title="구"
        v-model="selectedGu"
        @change="getArticles"
      >
        <option value="null">구</option>
        <!-- <option value="all">구</option> -->
        <option v-for="(boroughs,id) in gugun" :key="id" :value="boroughs.gu">{{boroughs.gu}}</option>
      </select>
      <select
        name="animal"
        id="animal"
        class="form-control"
        title="종"
        v-model="selectedKind"
        @change="getArticles"
      >
        <option value="null">종</option>
        <!-- <option value="all">종</option>			 -->
        <option v-for="(animal,id) in animals" :key="id" :value="animal.kind">{{animal.kind}}</option>
      </select>

      <!-- <button type="button" class="btn btn-primary" style="width:10%;display:inline-block; float:right;" >검색</button>				 -->
    </div>
    <p />
    <p></p>
    <table class="table table-striped table-bordered table-hover">
      <thead>
        <tr>
          <th style="width:25%;">시</th>
          <th style="width:25%;">구</th>
          <th style="width:25%;">종</th>
          <th style="width:25%;">제목</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="(notice,id) in notices"
          :key="id"
          
          @click="moveLostDetail(notice.id)"
        >
          <td>{{notice.city.city.slice(0, 2)}}</td>
          <td>{{notice.borough.gu.slice(0, 3)}}</td>
          <td>{{notice.animal.kind}}</td>
          <td>{{notice.title.slice(0, 5)}}</td>
        </tr>
      </tbody>
    </table>
    <p />
  </div>
</template>

<script>
// import sessionManager from "@/components/SessionManager.js";
const API_URL = process.env.VUE_APP_SERVER_URL;

import { mapGetters } from "vuex";
import axios from "axios";

export default {
  name: "Notice",
  data() {
    return {
      notices: [],
      key: "1",
      word: "",
      orderTitle: 0,
      id: "",

      s: "all",
      g: "all",

      title: "",
      animal: "",
      species: "",
      animal: "",
      city: "",
      borough: "",
      gu: "",
      citys: [],
      no: "",

      sido: [],
      gugun: [],
      animals: [],
      breeds: [],
      name: "",
      gender: "",
      age: "",
      time: "",
      img_path: "",
      content: "",
      selectedCity: null,
      selectedGu: null,
      selectedKind: null,
    };
  },
  components: {},
  computed: {
    // ...mapGetters(['userinfo', 'isLogin']),
  },
  created() {
    axios
      .get(`${API_URL}/articles/city/`)
      .then(({ data }) => {
        this.sido = data;
      })
      .catch((err) => {
        alert("정보를 받아올때 에러가 발생했습니다.");
        console.log(err);
      });

    axios
      .get(`${API_URL}/articles/borough/`)
      .then(({ data }) => {
        this.gugun = data;
      })
      .catch((err) => {
        alert("정보를 받아올때 에러가 발생했습니다.");
        console.log(err);
      });

    axios
      .get(`${API_URL}/articles/animal/`)
      .then(({ data }) => {
        this.animals = data;
      })
      .catch((err) => {
        alert("정보를 받아올때 에러가 발생했습니다.");
        console.log(err);
      });

    //   sessionManager(true, this.isLogin);
    axios
      .get(`${API_URL}/articles_lost/`)
      .then(({ data }) => {
        this.notices = data;
      })
      .catch((err) => {
        alert("정보를 받아올때 에러가 발생했습니다.");
        console.log(err);
      });
  },
  methods: {
    getArticles() {
      var city = (this.selectedCity == "null") ? null : this.selectedCity
      var borough = (this.selectedGu == "null") ? null : this.selectedGu
      var animal = (this.selectedKind == "null") ? null : this.selectedKind
      const data =  {
        'city': city,
        'borough': borough,
        'animal': animal
      }
      axios.post(`${API_URL}/articles_lost/search/`, data)
      .then((res) => {
        this.notices = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    moveLostDetail(id) {
      this.$router.push({ path: "/articles_lost/" + id });
    },
    keyWord(city, gu, kind) {
      console.log(city);
      console.log(gu);
      console.log(kind);
      console.log(this.selectedCity);
      console.log(this.selectedGu);
      console.log(this.selectedKind);

      if (
        city === this.selectedCity &&
        gu === this.selectedGu &&
        kind === this.selectedKind
      ) {
        return true;
      } else if (
        this.selectedCity == null &&
        this.selectedGu == null &&
        this.selectedKind == null
      ) {
        return true;
      }

      return false;
    },
  },
  filter: {},
};
</script>

<style scoped>
  
</style>