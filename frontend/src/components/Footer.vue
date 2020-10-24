<template>
  <b-nav justified class="myfooter pt-1 align-items-center">
    <!-- 1. 게시물 리스트 (default) -->
    <b-nav-item @click="changeState(1), moveTab('LostNotice')">
      <b-icon-list-ul
        v-if="tabNumber == 1"
        class="myactiveicon"
      ></b-icon-list-ul>
      <b-icon-list-task v-else class="myicon"></b-icon-list-task>
    </b-nav-item>
    <!-- 2. 검색 -->
    <b-nav-item @click="changeState(2), moveTab('Notice')">
      <!-- <b-nav-item @click="changeState(2), moveTab('IndexSearch')"> -->
      <b-icon-search v-if="tabNumber == 2" class="myactiveicon"></b-icon-search>
      <b-icon-search v-else class="myicon"></b-icon-search>
    </b-nav-item>
    <!-- 3. 게시물 작성 -->
    <b-nav-item-dropdown
      size="lg"
      variant="link"
      toggle-class="text-decoration-none"
      no-caret
      @click="changeState(3)"
    >
      <template v-slot:button-content @click="changeState(3)">
        <b-icon-plus-circle-fill
          v-if="tabNumber == 3"
          class="myactiveicon"
        ></b-icon-plus-circle-fill>
        <b-icon-plus-circle v-else class="myicon"></b-icon-plus-circle>
      </template>
      <b-dropdown-item-btn @click="movelost(), changeState(3)"
        >주인으로 작성</b-dropdown-item-btn
      >
      <b-dropdown-item-btn @click="movefind(), changeState(3)"
        >발견자로 작성</b-dropdown-item-btn
      >
    </b-nav-item-dropdown>
    <!-- 4. 보호소 리스트 -->
    <b-nav-item @click="changeState(4), moveTab('OpenApi')">
      <b-icon-house-fill
        v-if="tabNumber == 4"
        class="myactiveicon"
      ></b-icon-house-fill>
      <b-icon-house v-else class="myicon"></b-icon-house>
    </b-nav-item>
    <!-- 5. 내 프로필 or 로그인 (회원가입) -->
    <b-nav-item v-if="isLoggedIn" @click="changeState(5), moveTab('MyProfile')">
      <b-icon-person-circle
        v-if="tabNumber == 5"
        class="myactiveicon"
      ></b-icon-person-circle>
      <b-icon-person-circle v-else class="myicon"></b-icon-person-circle>
    </b-nav-item>
    <b-nav-item v-if="!isLoggedIn" @click="changeState(5), moveTab('Login')">
      <b-icon-person-circle
        v-if="tabNumber == 5"
        class="myactiveicon"
      ></b-icon-person-circle>
      <b-icon-person-circle v-else class="myicon"></b-icon-person-circle>
    </b-nav-item>
  </b-nav>
</template>

<script>
export default {
  name: "Footer",
  data() {
    return {
      tabNumber: null,
    };
  },
  props: {
    isLoggedIn: Boolean,
  },
  methods: {
    // 탭을 클릭하면 해당 탭을 활성화
    changeState(tabNumber) {
      // sessionStorage.setItem('tab_num', tabNumber);
      this.tabNumber = tabNumber;
    },
    moveTab(name) {
      this.$router.push({ name: name });
    },
    movelost(){
      this.$router.push({path: "/articles_lost/create"});
    },
    movefind(){
      this.$router.push({path: "/articles_find/create"});
    }
  },
  mounted() {},
  created() {
    var para = document.location.href.split("/");
    if (para[para.length - 1] == "articles_find") {
      this.tabNumber = 1;
    } else if (para[para.length - 1] == "articles_lost") {
      this.tabNumber = 2;
    } else if (para[para.length - 1] == "create") {
      this.tabNumber = 3;
    } else if (para[para.length - 1] == "shelter") {
      this.tabNumber = 4;
    } else if (
      para[para.length - 1] == "login" ||
      para[para.length - 1] == "myprofile"
    ) {
      this.tabNumber = 5;
    } else {
      this.tabNumber = null;
    }
  },
};
</script>

<style scoped>
.myfooter {
  background-color: #fec925;
  position: fixed;
  bottom: 0;
  width: 100%;
  height: 50px;
  z-index: 1;
}
.myactiveicon {
  color: #084481;
}
.myicon {
  color: gray;
}
</style>