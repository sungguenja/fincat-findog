<template>
  <div>
    <h1 class="mt-2 mb-3">발견 신고</h1>
    <div class="d-none d-md-block">
      <div class="form-group">
        <div class="d-flex justify-content-between mb-3">
          <img :src="image_url" style="width: 50%;" />
          <div style="width: 45%;">
            <input type="text" class="form-control" placeholder="* 제목" v-model="title" />
            <div class="d-flex flex-column">
              <input type="file" class="d-block my-3" @change="onFileChanged" />
              <b-button id="upload" class="mybutton1" style="width: 70px;" @click="onUpload">Upload!</b-button>
            </div>
          </div>
        </div>

        <input type="text" class="form-control" placeholder="종" v-model="selectedAnimal" />
        <select name="species" id="species" class="form-control my-2" title="품종" v-model="breed">
          <option value="null">품종</option>
          <option
            v-for="(onebreed,id) in this.breeds"
            :key="id"
            :value="onebreed.species"
          >{{onebreed.species}}</option>
        </select>
        <div class="d-flex justify-content-between my-2">
          <select
            name="city"
            id="city"
            class="form-control"
            title="시"
            v-model="selectedCity"
            style="width:45%;"
          >
            <option value="null">시</option>
            <option v-for="(citys,id) in sido" :key="id" :value="citys.city">{{citys.city}}</option>
          </select>
          <select
            name="borough"
            id="borough"
            class="form-control"
            title="구"
            v-model="selectedGu"
            style="width:45%;"
          >
            <option value="null">구</option>
            <option v-for="(boroughs,id) in gugun" :key="id" :value="boroughs.gu">{{boroughs.gu}}</option>
          </select>
        </div>
        <input type="text" class="form-control my-2" placeholder="이름" v-model="name" />
        <select
          name="sex"
          id="sex"
          class="form-control"
          title="성별"
          v-model="selectedGender"
        >
          <option value="null">성별</option>
          <option value="Male">수컷</option>
          <option value="Female">암컷</option>
          <option value="Unknown">모름</option>
        </select>
        <input type="text" class="form-control my-2" placeholder="나이" v-model="age" />
        <input type="text" class="form-control my-2" placeholder="발견 일시" v-model="time" />
        <textarea type="text" class="form-control my-2" placeholder="내용" v-model="content"></textarea>
      </div>
      <b-button block class="mybutton2 mb-3" @click="submit()">등록</b-button>
      <b-button block class="mb-4" @click="moveNotice()">취소</b-button>
    </div>

    <div class="d-block d-md-none">
      <div class="form-group">
        <div class="d-flex justify-content-between mb-3">
          <img :src="image_url" style="width: 50%;" />
          <div style="width: 45%;">
            <input type="text" class="form-control" placeholder="* 제목" v-model="title" />
            <div class="d-flex flex-column">
              <input type="file" class="d-block my-3" @change="onFileChanged" />
              <b-button id="upload" class="mybutton1" style="width: 70px;" @click="onUpload">Upload!</b-button>
            </div>
          </div>
        </div>

        <input type="text" class="form-control" placeholder="종" v-model="selectedAnimal" />
        <select name="species" id="species" class="form-control my-2" title="품종" v-model="breed">
          <option value="null">품종</option>
          <option
            v-for="(onebreed,id) in this.breeds"
            :key="id"
            :value="onebreed.species"
          >{{onebreed.species}}</option>
        </select>
        <div class="d-flex justify-content-between my-2">
          <select
            name="city"
            id="city"
            class="form-control"
            title="시"
            v-model="selectedCity"
            style="width: 45%;"
          >
            <option value="null">시</option>
            <option v-for="(citys,id) in sido" :key="id" :value="citys.city">{{citys.city}}</option>
          </select>
          <select
            name="borough"
            id="borough"
            class="form-control"
            title="구"
            v-model="selectedGu"
            style="width: 45%;"
          >
            <option value="null">구</option>
            <option v-for="(boroughs,id) in gugun" :key="id" :value="boroughs.gu">{{boroughs.gu}}</option>
          </select>
        </div>
        <input type="text" class="form-control my-2" placeholder="이름" v-model="name" />
        <select
          name="sex"
          id="sex"
          class="form-control"
          title="성별"
          v-model="selectedGender"
        >
          <option value="null">성별</option>
          <option value="Male">수컷</option>
          <option value="Female">암컷</option>
          <option value="Unknown">모름</option>
        </select>
        <input type="text" class="form-control my-2" placeholder="나이" v-model="age" />
        <input type="text" class="form-control my-2" placeholder="발견 일시" v-model="time" />
        <textarea type="text" class="form-control my-2" placeholder="내용" v-model="content"></textarea>
      </div>
      <b-button block class="mybutton2 mb-3" @click="submit()">등록</b-button>
      <b-button block class="mb-4" @click="moveNotice()">취소</b-button>
    </div>
    <b-modal ref="mymodal" hide-footer title="로딩 중" :no-close-on-backdrop="true">
      <h1>로딩 중</h1>
      <loading-circle style="width: 100%;"></loading-circle>
    </b-modal>
  </div>
</template>

<script>
import axios from "axios";
import { mapGetters } from "vuex";
const API_URL = process.env.VUE_APP_SERVER_URL;
import LoadingCircle from "./LoadingCircle.vue";

export default {
  name: "WriteNotice",
  data() {
    return {
      //   title: '',
      //   content: '',
      selectedFile: null,
      breed: "",
      pk: "",
      temp: "",

      sido: [],
      cats: [],
      dogs: [],
      gugun: [],
      manwoman: [],
      animals: [],
      breeds: [],
      citys: [],
      species: [],
      gu: "",
      sex: "",

      title: "",
      animal: "",
      species: "",
      city: "",
      borough: "",
      name: "",
      gender: "",
      age: "",
      time: "",
      image_url: "https://ifh.cc/g/cwCkSw.png",
      content: "",
      selectedCity: null,
      selectedGu: null,
      selectedGender: null,
      // selectedChip:null,
      selectedAnimal: "",
      selectedSpecies: null,
      // selectedGender:null,
      loading: false,
    };
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

    // axios.get(`${API_URL}/articles/species/1`)
    //                       .then(respon =>{
    //                         console.log(respon.data);
    //                         this.cats=respon.data; });

    // axios.get(`${API_URL}/articles/species/2`)
    //                       .then(respon =>{
    //                         console.log(respon.data);
    //                         this.dogs=respon.data; });

    // axios.get(`${API_URL}/articles/borough/`).then(({data}) =>{
    //     this.gugun = data;
    // }).catch((err) => {
    //           alert('정보를 받아올때 에러가 발생했습니다.')
    //           console.log(err)
    // });

    axios
      .get(`${API_URL}/articles/animal/`)
      .then(({ data }) => {
        this.animals = data;
      })
      .catch((err) => {
        alert("정보를 받아올때 에러가 발생했습니다.");
        console.log(err);
      });

    // axios.get(`${API_URL}/articles/species/${this.selectedSpecies}`+"/").then(({data}) =>{
    //     this.breeds = data;
    // })
  },

  components: {
    LoadingCircle,
  },
  computed: {
    // ...mapGetters(['isLogin']),
  },
  methods: {
    submit() {
      const token = this.$cookies.get("auth-token");
      console.log(token);
      console.log();
      axios({
        method: "POST",
        url: `${API_URL}/articles_find/create/`,
        data: {
          animal: this.selectedAnimal,
          species: this.breed,
          city: this.selectedCity,
          borough: this.selectedGu,
          title: this.title,
          name: this.name,
          content: this.content,
          gender: this.selectedGender,
          // chip: this.selectedChip,
          age: this.age,
          time: this.time,
          image_url: this.image_url,
        },
        headers: {
          Authorization: `Token ${token}`,
        },
      })
        .then(({ data }) => {
          console.log(data);
          console.log(data.id);
          // if (data == 'success'){
          this.$router.push({ path: `/articles_find/${data.id}` }); //리스트 전체목록
          // }
        })
        .catch((err) => {
          console.log(err);
          alert("입력오류가 발생했습니다. \n 다시한번 확인해주세요!");
        });
    },
    moveNotice() {
      this.$router.push({ path: "/articles_find/" });
    },

    onFileChanged(event) {
      this.selectedFile = event.target.files[0];
      console.log(this.selectedFile);
    },
    onUpload() {
      // document.getElementById('myModal').modal({'show' : true});
      // document.getElementById('myModal').modal('show');
      var Form = new FormData();
      Form.append("picture", this.selectedFile);
      this.$refs["mymodal"].show();
      axios({
        method: "POST",
        url: `${API_URL}/imageapi/images/`,
        data: Form,
        headers: { "Content-type": "multipart/form-data" },
      })
        .then((res) => {
          axios
            .get(`${API_URL}/animal/tf/${res.data.pk}`)
            .then((respon) => {
              console.log(respon.data);
              console.log(respon.data.breed);
              this.selectedAnimal = respon.data.animal;
              console.log(this.selectedAnimal);
              this.temp = respon.data.breed;

              if (this.selectedAnimal === "cat") {
                this.selectedAnimal = "고양이";
                // this.selectedSpecies = respon.data.breed;

                axios
                  .get(`${API_URL}/articles/species/1`)
                  .then((respon) => {
                    console.log(respon.data);
                    this.breeds = respon.data;
                    console.log(this.breeds);
                    this.breed = this.temp;
                    console.log(this.breed);
                  })

                  .catch((erroo) => {
                    console.log(erroo);
                    this.$refs["mymodal"].hide();
                  });
              } else if (this.selectedAnimal === "dog") {
                this.selectedAnimal = "강아지";
                // this.selectedSpecies = respon.data.breed;

                // axios.get(`${API_URL}/articles/species/2`)
                // .then(respon =>{
                //   return new Promise(() =>{
                //     console.log(respon.data);
                //   this.breeds=respon.data;
                //   console.log(this.breeds)
                //   })

                axios
                  .get(`${API_URL}/articles/species/2`)
                  .then((respon) => {
                    console.log(respon.data);
                    this.breeds = respon.data;
                    console.log(this.breeds);
                    this.breed = this.temp;
                  })

                  .catch((erroo) => {
                    console.log(erroo);
                    this.$refs["mymodal"].hide();
                  });
              }
              // this.breed = respon.data.breed;
              console.log(this.breed);
              this.pk = respon.data.pk;
              this.image_url = `${API_URL}/media/` + respon.data.img_path;
              // document.getElementById("animal").value = animal;
              // document.getElementById(myModal).modal('hide');
              this.$refs["mymodal"].hide();

              // axios.get(`${API_URL}/articles/sqpecies`)
            })
            .catch((erroo) => {
              console.log(erroo);
              this.$refs["mymodal"].hide();
            });
        })
        .catch((err) => {
          console.log(err);
          this.$refs["mymodal"].hide();
        });
      // axios.get('${API_URL}/animal/tf/1/')
      //     .then(res => console.log(res))
    },
  },
};
</script>

<style scoped>
.mybutton1 {
  background-color: #084481;
  border: none;
}
.mybutton2 {
  background-color: #fa1e44;
  border: none;
}
</style>