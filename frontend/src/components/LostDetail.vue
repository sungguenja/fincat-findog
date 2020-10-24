<template>
  <div>
    <table class="table table-striped table-bordered table-hover mt-3">
      <thead>
        <tr>
          <th>제목</th>
          <th>{{notice.title}}</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td colspan="2"><img :src="notice.image_url" style="width:80%;"/></td>
        </tr>
        <tr>
          <td>전화번호</td>
          <td style="white-space:pre;">{{notice.user.phone_number}}</td>
        </tr>
        <tr>
          <td>시</td>
          <td style="white-space:pre;">{{notice.city.city}}</td>
        </tr>
        <tr>
          <td>구</td>
          <td style="white-space:pre;">{{notice.borough.gu}}</td>
        </tr>
        <tr>
          <td>시간</td>
          <td style="white-space:pre;">{{notice.time}}</td>
        </tr>
        <tr>
          <td>종</td>
          <td style="white-space:pre;">{{notice.animal.kind}}</td>
        </tr>
        <tr>
          <td>품종</td>
          <td style="white-space:pre;">{{notice.species.species}}</td>
        </tr>
        <tr>
          <td>이름</td>
          <td style="white-space:pre;">{{notice.name}}</td>
        </tr>
        <tr>
          <td>성별</td>
          <td style="white-space:pre;">{{notice.gender}}</td>
        </tr>
        <tr>
          <td>칩 여부</td>
          <td style="white-space:pre;">{{notice.chip}}</td>
        </tr>
        <tr>
          <td>나이</td>
          <td style="white-space:pre;">{{notice.age}}</td>
        </tr>
        <tr>
          <td>내용</td>
          <td style="white-space:pre;">{{notice.content}}</td>
        </tr>
      </tbody>
    </table>

    <b-button  v-if="notice.user.username == user.username" class="mybutton1" @click="moveLostNoticeModify()">수정</b-button>
    <b-button  v-if="notice.user.username == user.username" class="mybutton2 mx-3" @click="moveLostNoticeDelete()">삭제</b-button>
    <b-button class="border-0" @click="moveLostNotice()">목록으로</b-button>

    <div class="d-flex justify-content-between">
      <h4 class="my-3 text-left">댓글 <b-icon-chat-text></b-icon-chat-text></h4>
      <b-button size="sm" class="mybutton1 my-3" @click="mdAddCmtOpen()">작성하기</b-button>
    </div>

      <b-list-group flush class="text-left">
        <b-list-group-item v-for="(onecomment,id) in notice.comments" :key="id" class="px-3">
          <b-row>
            <b-col cols="7" class="px-0"><p class="m-0">{{ onecomment.content }}</p></b-col>
            <b-col cols="3" class="text-right px-0"><p class="m-0">{{ onecomment.user.username }}</p></b-col>
            <b-col cols="2" class="text-right px-0">
              <b-icon-pencil v-if="onecomment.user.username == user.username" class="mr-1" @click="mdModCmtOpen(onecomment.id)"></b-icon-pencil>
              <b-icon-trash v-if="onecomment.user.username == user.username" @click="delCmt(onecomment.id)"></b-icon-trash>
            </b-col>
          </b-row>
        </b-list-group-item>
      </b-list-group>

    <b-modal ref="mdAddCmt" hide-footer title="댓글 작성">
      <b-form @submit="addCmt">
        <b-form-group label="댓글" label-for="f-a-c-content">
          <b-form-textarea
            id="f-a-c-content"
            v-model="comment"
            placeholder="댓글을 입력해주세요 (100자 이내)"
            :rows="10"
            :max-rows="20"
          ></b-form-textarea>
        </b-form-group>

        <b-btn type="submit" variant="primary" class="float-right">댓글 쓰기</b-btn>
      </b-form>
    </b-modal>

    <b-modal ref="mdModCmt" hide-footer title="댓글 수정하기">
      <b-form @submit="modCmt">
        <b-form-group label="댓글" label-for="f-m-c-ontent">
          <b-form-textarea
            id="f-m-c-ontent"
            v-model="commenter.content"
            placeholder="댓글을 입력해주세요 (100자 이내)"
            :rows="10"
            :max-rows="20"
          ></b-form-textarea>
        </b-form-group>

        <b-btn type="submit" variant="warning" class="float-right">댓글 수정</b-btn>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import CommentForm from "./CommentForm.vue";
import CommentList from "./CommentList.vue";
const API_URL = process.env.VUE_APP_SERVER_URL;

// import sessionManager from "@/components/SessionManager.js";
import { mapGetters } from "vuex";
import axios from "axios";

export default {
  name: "Detail",
  data() {
    return {
      onecomment: {},
      cmt_id: "",
      comments: [],
      commenters: [],
      commenter: {},

      notice: {},
      datas: {},
      id: "",
      comment: "",
      title: "",
      kind: "",
      animal: "",
      species: "",
      city: "",
      gu: "",
      borough: "",
      name: "",
      gender: "",
      age: "",
      time: "",
      image_url: this.image_url,
      content: "",
      user: {},

    };
  },
  components: {
    CommentList,
    CommentForm,
  },
  computed: {
    // ...mapGetters(['userinfo', 'isLogin']),
  },
  created() {
    const token = this.$cookies.get("auth-token");
    console.log(token);

    axios({
      method: "GET",
      url: `${API_URL}/articles_lost/` + this.$route.params.pk + "/",

      headers: {
        Authorization: `Token ${token}`,
      },
    })
      .then(({ data }) => {
        console.log(data);
        console.log(data.comments);
        this.notice = data;
        // console.log(data.id)
        // this.find_pk=data.id
        // this.commenters=notice.comments
      })
      .catch((err) => {
        console.log(err);
        alert("정보를 받아올때 에러가 발생했습니다.");
      });

      axios({
        method:"GET",
        url:`${API_URL}/rest-auth/user`,
        headers:{
            'Authorization':`Token ${token}`,
        }})
        .then(res => {
            this.user = res.data
            })
        .catch(err => {
            console.log(err)
            alert("정보를 받아올때 에러가 발생했습니다.");
        });
  },
  methods: {
    swalSuccess(msg) {
      return this.$swal({
        icon: "success",
        title: "성공",
        text: msg,
        timer: 2000,
      });
    },
    swalError(msg) {
      return this.$swal({
        icon: "error",
        title: "에러",
        text: msg,
        timer: 2000,
      });
    },
    addCmt(evt) {
      evt.preventDefault();

      const token = this.$cookies.get("auth-token");
      console.log(token);

      axios({
        method: "POST",
        url:
          `${API_URL}/articles_lost/comment/create/` +
          this.$route.params.pk +
          "/",
        data: {
          content: this.comment,
        },
        headers: {
          Authorization: `Token ${token}`,
        },
      })
        .then(({ data }) => {
          console.log(data);
          console.log(data.comments);
          this.comments = data.comments;
          console.log(this.comments);
          // this.datas=data;
          // console.log(this.datas)
          return this.swalSuccess("댓글 추가 완료");

          // if (data == 'success'){
          //   this.$router.push({path: `/articles_find/${data.id}`}); //리스트 전체목록
          // }
        })
        .then(() => {
          this.$refs.mdAddCmt.hide();
          location.reload();

          // this.$router.push({path: '/articles_lost/'});
          // location.reload();
          // this.$router.push({path: `/articles_find/`+this.$route.params.pk});
          // const path = `/articles_find/`+this.$route.params.pk
          // if ($route.path !== path) this.$route.push(path)
        })
        .catch((err) => {
          this.swalError(err.message);
        });
    },
    mdAddCmtOpen() {
      // this.formCmt.bd_id = v._id;
      // this.formCmt._id = '';
      // this.formCmt.id = '';
      // this.formCmt.content = '';
      this.$refs.mdAddCmt.show();
    },

    modCmt(evt) {
      evt.preventDefault();

      this.$swal({
        title: "댓글 수정",
        dangerMode: true,
        buttons: {
          cancel: {
            text: "취소",
            visible: false,
          },
          confirm: {
            text: "수정",
          },
        },
      })
        .then((res) => {
          if (!res) throw new Error("");

          const token = this.$cookies.get("auth-token");
          console.log(token);
          console.log(333);
          console.log(this.commenter.id);
          axios({
            method: "PUT",
            url:
              `${API_URL}/articles_lost/comment/update/` +
              this.$route.params.pk +
              "/" +
              this.commenter.id +
              "/",
            data: {
              content: this.commenter.content,
            },
            headers: {
              Authorization: `Token ${token}`,
            },
          })
            .then((res) => {
              console.log(res.data);
            })
            .catch((err) => {
              console.log(err);
              alert("수정할때 에러가 발생했습니다.");
            });
        })
        .then((res) => {
          // if (!res.data.success) throw new Error(res.data.msg);
          return this.swalSuccess("댓글 수정 완료");
        })
        .then(() => {
          this.$refs.mdModCmt.hide();
          location.reload();

          // this.$router.push({path:'/articles_lost/'});
          // this.refresh();
        })
        .catch((err) => {
          if (err.message) this.swalError(err.message);
          // else this.swalWarning('댓글 수정 취소');
        });
    },

    mdModCmtOpen(cmt_id) {
      // this.formCmt.bd_id = v._id;
      // this.formCmt._id = v._id;
      // this.formCmt.id = v.id;
      // this.formCmt.content = v.content;
      const token = this.$cookies.get("auth-token");
      console.log(token);

      axios({
        method: "GET",
        url:
          `${API_URL}/articles_lost/comment/update/` +
          this.$route.params.pk +
          "/" +
          cmt_id +
          "/",

        headers: {
          Authorization: `Token ${token}`,
        },
      })
        .then((res) => {
          console.log(res.data);
          this.commenter = res.data;
          console.log(res.data.id);
          this.find_pk = res.data.id;
        })
        .catch((err) => {
          console.log(err);
          alert("정보를 받아올때 에러가 발생했습니다.");
        });

      this.$refs.mdModCmt.show();
    },
    moveLostNotice() {
      this.$router.push({ path: "/articles_lost/" });
    },
    moveLostNoticeModify() {
      this.$router.push({
        path: "/articles_lost/update/" + this.$route.params.pk,
      });
    },
    moveLostNoticeDelete() {
      const token = this.$cookies.get("auth-token");
      console.log(token);
      console.log();
      axios({
        method: "DELETE",
        url: `${API_URL}/articles_lost/delete/` + this.$route.params.pk,
        headers: {
          Authorization: `Token ${token}`,
        },
      })
        .then(() => {
          this.moveLostNotice();
        })
        .catch((err) => {
          console.log(err);
          alert("삭제 에러가 발생했습니다.");
        });
    },
    delCmt(cmt_id) {
      this.$swal({
        title: "댓글 삭제",
        dangerMode: true,
        buttons: {
          cancel: {
            text: "취소",
            visible: true,
          },
          confirm: {
            text: "삭제",
          },
        },
      })
        .then((res) => {
          // if (!res) throw new Error('');
          const token = this.$cookies.get("auth-token");
          console.log(token);
          console.log(333);
          console.log(this.commenter.id);
          axios({
            method: "DELETE",
            url:
              `${API_URL}/articles_lost/comment/delete/` +
              this.$route.params.pk +
              "/" +
              cmt_id +
              "/",

            headers: {
              Authorization: `Token ${token}`,
            },
          })
            .then((res) => {
              console.log(res.data);
            })
            .catch((err) => {
              console.log(err);
            });
        })
        .then((res) => {
          // if (!res.data.success) throw new Error(res.data.msg);
          return this.swalSuccess("댓글 삭제 완료");
        })
        .then(() => {
          this.$refs.mdModCmt.hide();
          location.reload();

          // this.$router.push({path:'/articles_lost/'});
          // this.refresh();
        })
        .catch((err) => {
          if (err.message) this.swalError(err.message);
          // else this.swalWarning('댓글 수정 취소');
        });
    },

    // onCommentSubmit(comment) {

    // },
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