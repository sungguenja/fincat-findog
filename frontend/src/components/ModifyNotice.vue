<template>
  <div>
    <h1 class="mt-2 mb-3">글 수정</h1>
    <div class="form-group">
      <div class="d-flex justify-content-between mb-3">
        <img :src="notice.image_url" style="width: 50%;" />
        <div style="width: 45%;">
          <input type="text" class="form-control" placeholder="* 제목" v-model="notice.title" />
          <div class="d-flex flex-column">
            <input type="file" class="d-block my-3" @change="onFileChanged" />
            <b-button id="upload" class="mybutton1" style="width: 70px;" @click="onUpload">Upload!</b-button>
          </div>
        </div>
      </div>

      <input type="text" class="form-control" placeholder="종" v-model="notice.animal.kind" />
      <select
        name="species"
        id="species"
        class="form-control my-2"
        title="품종"
        v-model="notice.species.species"
      >
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
        v-model="notice.city.city"
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
        v-model="notice.borough.gu"
        style="width: 45%"
      >
        <option value="null">구</option>
        <option v-for="(boroughs,id) in gugun" :key="id" :value="boroughs.gu">{{boroughs.gu}}</option>
      </select>
      </div>
      <input type="text" class="form-control my-2" placeholder="이름" v-model="notice.name" />
      <select
        name="sex"
        id="sex"
        class="form-control"
        title="성별"
        v-model="notice.gender"
      >
        <option value="null">성별</option>
        <option value="Male">수컷</option>
        <option value="Female">암컷</option>
        <option value="Unknown">모름</option>
      </select>
      <input type="text" class="form-control my-2" placeholder="나이" v-model="notice.age" />
      <input type="text" class="form-control my-2" placeholder="발견 일시" v-model="notice.time" />
      <textarea type="text" class="form-control my-2" placeholder="내용" v-model="notice.content"></textarea>
    </div>
    <b-button block class="mybutton2 mb-3" @click="submit()">수정</b-button>
    <b-button block class="mb-4" @click="moveNoticeDetail()">취소</b-button>
    <b-modal ref="mymodal" hide-footer title="로딩 중" :no-close-on-backdrop="true">
      <h1>로딩 중</h1>
      <loading-circle style="width: 100%;"></loading-circle>
    </b-modal>
  </div>
</template>

<script>
const API_URL = process.env.VUE_APP_SERVER_URL;

import axios from "axios";
import { mapGetters } from "vuex";

import LoadingCircle from "./LoadingCircle.vue";

export default {
  name: "ModifyNotice",
  data() {
    return {
      notice: {},
      selectedFile: null,
      temp: "",

      breed: "",
      find_pk: "",
      //   kind: '',

      sido: [],
      gugun: [],
      //   animals: [],
      breeds: [],
      citys: [],
      gu: "",

      title: "",
      animal: "",
      species: "",
      city: "",
      borough: "",
      name: "",
      gender: "",
      age: "",
      time: "",
      image_url: "",
      content: "",
      selectedCity: null,
      selectedGu: null,
      selectedGender: null,
      loading: false,
    };
  },
  components: {
    LoadingCircle,
  },
  computed: {
    // ...mapGetters(['isLogin']),
  },
  created() {
    // var animal= '';
    const token = this.$cookies.get("auth-token");
    console.log(token);
    axios({
      method: "GET",
      url: `${API_URL}/articles_find/update/` + this.$route.params.pk,

      headers: {
        Authorization: `Token ${token}`,
      },
    })
      .then((res) => {
        this.notice = res.data;
        console.log(res.data.id);
        this.find_pk = res.data.id;
        if (this.notice.animal.kind == "고양이") {
          axios
            .get(`${API_URL}/articles/species/1`)
            .then((respon) => {
              console.log(respon.data);
              this.breeds = respon.data;
              console.log(this.breeds);
              //   this.notice.species.species=this.temp;
              console.log(this.breed);
            })

            .catch((erroo) => {
              console.log(erroo);
              alert("정보를 받아올때 에러가 발생했습니다.");

              // this.$refs['mymodal'].hide()
            });
        } else {
          axios
            .get(`${API_URL}/articles/species/2`)
            .then((respon) => {
              console.log(respon.data);
              this.breeds = respon.data;
              console.log(this.breeds);
              //   this.notice.species.species=this.temp;
              console.log(this.breed);
            })

            .catch((erroo) => {
              console.log(erroo);
              alert("정보를 받아올때 에러가 발생했습니다.");

              // this.$refs['mymodal'].hide()
            });
        }
      })
      .catch((err) => {
        console.log(err);
        alert("정보를 받아올때 에러가 발생했습니다.");
      });

    axios
      .get(`${API_URL}/articles/city/`)
      .then(({ data }) => {
        this.sido = data;
      })
      .catch((err) => {
        console.log(err);
        alert("정보를 받아올때 에러가 발생했습니다.");
      });

    axios
      .get(`${API_URL}/articles/borough/`)
      .then(({ data }) => {
        this.gugun = data;
      })
      .catch((err) => {
        console.log(err);
        alert("정보를 받아올때 에러가 발생했습니다.");
      });
  },
  methods: {
    submit() {
      const token = this.$cookies.get("auth-token");
      console.log(token);
      // console.log()
      console.log(this.notice.animal.kind);
      console.log(this.notice.species.species);
      console.log(this.notice.city.city);
      console.log(this.notice.borough.gu);
      console.log(this.notice.title);
      console.log(this.notice.name);
      console.log(this.notice.content);
      console.log(this.notice.gender);
      console.log(this.notice.age);
      console.log(this.notice.time);
      console.log(this.notice.image_url);

      axios({
        method: "PUT",
        url: `${API_URL}/articles_find/update/` + this.find_pk + "/",
        data: {
          animal: this.notice.animal.kind,
          species: this.notice.species.species,
          city: this.notice.city.city,
          borough: this.notice.borough.gu,
          title: this.notice.title,
          name: this.notice.name,
          content: this.notice.content,
          gender: this.notice.gender,
          age: this.notice.age,
          time: this.notice.time,
          image_url: this.notice.image_url,

          //   "animal": {
          //         "kind": this.notice.animal.kind
          //   },
          //   "species": {
          //         "animal": {
          //         "kind": this.notice.animal.kind
          //         },
          //         "species": this.notice.species.species
          //     },
          //     "city": {
          //         "city": this.notice.city.city
          //     },
          //     "borough": {
          //         "city": {
          //         "city": this.notice.city.city
          //         },
          //         "gu": this.notice.borough.gu
          //     },
          //     "title": this.notice.title,
          //     "name": this.notice.name,
          //     "content": this.notice.content,
          //     "gender": this.notice.gender,
          //     "age": this.notice.age,
          //     "time": this.notice.time,
          //     "image_url": this.notice.image_url
        },
        headers: {
          Authorization: `Token ${token}`,
        },
      })
        .then(({ data }) => {
          console.log(data);
          console.log(data.id);
          // if (data == 'success'){
          this.$router.push({ path: `/articles_find/${this.find_pk}` });
          // }
        })
        .catch((err) => {
          alert(
            "수정할때 에러가 발생했습니다. \n 입력값을 다시 한번 확인해주세요!"
          );
          console.log(err);
        });
    },
    moveNoticeDetail() {
      this.$router.push({ path: `/articles_find/${this.pk}` });
    },

    onFileChanged(event) {
      this.selectedFile = event.target.files[0];
      console.log(this.selectedFile);
    },
    onUpload() {
      // document.getElementById('myModal').modal({'show' : true});
      // document.getElementById('myModal').modal('show');
      // this.loading=true;
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

              this.notice.animal.kind = respon.data.animal;
              this.temp = respon.data.breed;

              if (this.notice.animal.kind === "cat") {
                this.notice.animal.kind = "고양이";

                axios
                  .get(`${API_URL}/articles/species/1`)
                  .then((respon) => {
                    console.log(respon.data);
                    this.breeds = respon.data;
                    console.log(this.breeds);
                    this.notice.species.species = this.temp;
                    console.log(this.breed);
                  })

                  .catch((erroo) => {
                    console.log(erroo);
                    this.$refs["mymodal"].hide();
                  });
              } else if (this.notice.animal.kind === "dog") {
                this.notice.animal.kind = "강아지";

                axios
                  .get(`${API_URL}/articles/species/2`)
                  .then((respon) => {
                    console.log(respon.data);
                    this.breeds = respon.data;
                    console.log(this.breeds);
                    this.notice.species.species = this.temp;
                    console.log(this.breed);
                  })

                  .catch((erroo) => {
                    console.log(erroo);
                    this.$refs["mymodal"].hide();
                  });
              }
              // this.notice.species.species = respon.data.breed;
              this.pk = respon.data.pk;
              this.notice.image_url =
                `${API_URL}/media/` + respon.data.img_path;
              // document.getElementById("animal").value = animal;
              // this.loading=false;
              this.$refs["mymodal"].hide();

              // document.getElementById(myModal).modal('hide');
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
      // axios.get('http://localhost:8000/animal/tf/1/')
      //     .then(res => console.log(res))
    },

    // submit() {
    //     axios.put("http://localhost:8080/posts/modify", {
    //       gongjino: this.$route.params.no,
    //       title: this.notice.title,
    //       content: this.notice.content
    //     }).then(() => {

    //     }).finally(() => {
    //         this.moveNoticeDetail();
    //     });
    // },
    // moveNoticeDetail(){
    //     this.$router.push({path: "/articles_find/"+this.$route.params.pk});
    // }
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