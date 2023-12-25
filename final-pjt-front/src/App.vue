<template>
  <div id="app">
    <div class="main-img">
      <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
        integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2"
        crossorigin="anonymous"
      />
      <link
        rel="stylesheet"
        href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"
        integrity="sha512-..."
        crossorigin="anonymous"
      />

      <div id="nav" class="main-nav" v-if="this.$route.path !== '/'">
        <b-navbar toggleable="lg">
          <b-navbar-toggle target="navbar-nav-collapse hambuger">
            <i class="fas fa-bars"></i>
          </b-navbar-toggle>

          <b-navbar-brand href="/movies" class="font-weight-bold">
            <img class="Logo" src="./Logo.gif" alt="" />
          </b-navbar-brand>

          <b-collapse id="navbar-nav-collapse" is-nav>
            <b-navbar-nav>
              <!-- Remove the dropdown and its items -->
              <b-nav-item>
                <router-link :to="{ name: 'Post' }">Community</router-link>
              </b-nav-item>

              <b-nav-item-dropdown
                v-if="$store.state.login && this.$route.path !== '/login'"
                :text="username"
              >
                <b-dropdown-item class="dropdown-back">
                  <router-link
                    class="drop-item-btn"
                    :to="{ name: 'Profile', params: { username: username } }"
                    >Profile</router-link
                  >
                </b-dropdown-item>

                <b-dropdown-item>
                  <router-link @click.native="logout" to="#" class="nav-margin">
                    <button class="drop-item-btn font-weight-bold p-0">
                      Logout
                    </button>
                  </router-link>
                </b-dropdown-item>
              </b-nav-item-dropdown>

              <template v-if="$store.state.is_admin === true">
                <b-nav-item>
                  <router-link :to="{ name: 'ManageMovie' }" class="nav-margin">
                    <span class="badge badge-pill badge-warning">영화관리</span>
                  </router-link>
                </b-nav-item>

                <b-nav-item>
                  <router-link
                    :to="{ name: 'AdminManagement' }"
                    class="nav-margin"
                  >
                    <span class="badge badge-pill badge-warning">회원관리</span>
                  </router-link>
                </b-nav-item>
              </template>
            </b-navbar-nav>

            <b-navbar-nav class="ml-auto">
              <template v-if="$store.state.login">
                <b-nav-item>
                  <button
                    @click="triggerSearch"
                    class="font-weight-bold search-btn p-0 mr-3"
                  >
                    Search
                  </button>
                </b-nav-item>
                <!-- <p class="user font-weight-bold text-truncate">{{ username }}</p> -->
              </template>

              <template v-else>
                <b-nav-item>
                  <router-link :to="{ name: 'Signup' }" class="nav-margin">
                    <button class="nav-btn font-weight-bold">Signup</button>
                  </router-link>
                </b-nav-item>

                <b-nav-item>
                  <router-link :to="{ name: 'Login' }" class="nav-margin">
                    <button class="nav-btn font-weight-bold">Login</button>
                  </router-link>
                </b-nav-item>
              </template>
            </b-navbar-nav>
          </b-collapse>
        </b-navbar>
      </div>

      <router-view @login="login = true" />

      <!-- 푸터 -->
      <div class="jumbotron" id="footerjumbo">
        <div class="container">
          <div class="row">
            <div class="col-3 ms-5">
              <img
                src="./Logo.gif"
                style="width: 70px; height: auto"
                alt="Logo"
              />
              <h4>JAEBING</h4>
            </div>
            <div class="col-3 ms-5 my-3">
              <h6>대표이사 : 나야나</h6>
              <h6>주소 : 경북 구미시 3공단3로 302</h6>
              <h6>통신신고번호 : 어이쿠 깜빡했네</h6>
            </div>
            <div class="col-3 ms-5 my-3">
              <h6>이용약관 * 법적고지</h6>
              <h6>개인정보처리방침</h6>
              <h6>이메일무단수집거부</h6>
            </div>
            <div class="col-3 ms-5 my-3">
              <span class="clickable" style="color: #d44c7f" @click="openModal"
                >*전화문의*</span
              >
              <div class="modal" :class="{ 'is-active': showModal }">
                <div class="modal-background" @click="closeModal"></div>
                <div class="modal-image">
                  <img
                    class="moonhee"
                    src="./Untitled.png"
                    alt="전화문의 이미지"
                  />
                </div>
                <button
                  class="modal-shutdown is-large"
                  @click="closeModal"
                ></button>
              </div>
              <h6>고객지원</h6>
              <h6>블로그</h6>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// const SERVER_URL = process.env.VUE_APP_SERVER_URL

import { mapState } from "vuex";
// import axios from 'axios'

export default {
  name: "App",
  data: function () {
    return {
      login: false,
      images: {
        logo: require("@/assets/images/logo.png"),
        flamingo: require("@/assets/images/flamingo.png"),
      },
      hideAdd: true,
      showModal: false,
    };
  },
  methods: {
    openModal() {
      this.showModal = true;
    },
    closeModal() {
      this.showModal = false;
    },
    logout: function () {
      localStorage.removeItem("jwt");
      localStorage.removeItem("username");
      localStorage.removeItem("login_user");
      localStorage.removeItem("is_admin");
      localStorage.removeItem("user_movie");
      this.login = false;
      this.$store.state.login = false;
      this.$store.state.is_admin = false;
      this.$store.state.login_user = "";
      this.$store.state.username = null;
      this.$router.push({
        name: "Main",
      });
    },
    triggerSearch: function () {
      this.$router.push({ name: "MovieSearch" });
    },
  },
  created: function () {
    // 로그인
    const token = localStorage.getItem("jwt");

    if (this.$route.path !== "/") {
      console.log("입구컷");
      if (token) {
        this.login = true;
      }
      console.log("1번 발동");
      this.$store.dispatch("getMovie");
      if (this.$store.state.ordered_movie_list.length == 0) {
        // 영화 목록이 비어있는 경우에만 getMovie 액션 호출
        console.log("비었는데요?");
      }
      if (this.$route.path !== "/movies") {
        console.log("2번 발동");
        this.$router.push({ name: "MovieList" });
      }
    }
  },
  computed: {
    ...mapState(["is_admin", "username"]),
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Do+Hyeon&family=Jua&family=Nanum+Gothic&family=Poor+Story&family=Slabo+27px&display=swap");

@font-face {
  font-family: "NeoDunggeunmoPro-Regular";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2302@1.0/NeoDunggeunmoPro-Regular.woff2")
    format("woff2");
  font-weight: normal;
  font-style: normal;
}

/* 전체 div */
#app {
  font-family: "NeoDunggeunmoPro-Regular";
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: black;
  background: #101130;
  min-height: 100vh;
}

.main-img {
  background-image: url("moviemain.png");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

/* 로고 이미지 */
.Logo {
  width: 70px;
  height: auto;
  margin: 0px;
}

/* 햄버거 버튼 */
.navbar-toggler {
  color: #e8d1d9;
  border-color: #e8d1d9;
  padding: 8px; /* 햄버거 버튼 패딩을 8px로 수정 */
}

/* 햄버거 버튼, 텍스트 */
.navbar-toggler .fa-bars {
  margin-right: 4px; /* 햄버거 아이콘과 텍스트 사이의 우측 마진을 4px로 설정 */
}

/* 네브바의 a링크들 */
#nav a {
  font-size: 25px;
  font-weight: bold;
  color: #e8d1d9;
  text-decoration-line: none;
  /* background: linear-gradient(45deg, #E8D1D9, #3C537F, #0f2648); */
  /* color: #2c3e50; */
}

/* 네브바 버튼 클릭시 */
.nav-btn:focus {
  outline: none;
}

.hambuger:focus {
  outline: none;
}

#nav a.router-link-exact-active {
  /* color: #D44C7F; */
  color: #e8d1d9;
}

/* 푸터 */
#footerjumbo {
  min-height: 10vh;
  margin-bottom: 0rem;
}

/* 추가 */

/* community Mypage 네브바 속성 */
span {
  color: #e8d1d9;
  padding: 8px;
}

/* 네브바 속성 */
.navbar {
  font-size: 25px;
  background-color: #0f264800;
  padding: 8px; /* 기본 패딩을 8px로 수정 */
}

/* 네브바 토글 속성 */
.collapse {
  color: #e8d1d9;
  border-color: #e8d1d9;
}

/* 네브바 클릭시 나오는 item 속성 */
.drop-item {
  color: #3c537f;
  padding: 8px; /* 아이템 간격 조정 */
}

/* signup login 속성 */
button {
  color: #e8d1d9;
  background-color: #0f2648;
  border-color: #0f264800;
  padding: 4px 8px; /* 버튼 패딩을 상하 4px, 좌우 8px로 수정 */
}

.dropdown-toggle::after {
  color: #e8d1d9;
  margin: -5px;
}

/* 로그아웃 버튼 */
.logout {
  border-color: #0f264800;
  background-color: #0f264800;
  padding: 8px;
}

/* 검색 버튼 아웃라인 없이 */
.search-btn:focus {
  outline: none;
}

/* 유저 이름 */
.user {
  color: #e8d1d9;
  padding: 8px 8px 8px 0; /* 상단, 우측, 하단 패딩은 8px, 좌측 패딩은 0으로 수정 */
  margin: 10px 0; /* 상단 및 하단 마진은 10px로 수정 */
  white-space: nowrap; /* 텍스트가 넘칠 경우 줄바꿈 방지 */
  overflow: hidden; /* 텍스트가 넘칠 경우 가림 처리 */
  text-overflow: ellipsis; /* 가림 처리된 텍스트에 대해 ...으로 표시 */
}

.appear {
  display: none;
}

.jumbotron {
  background: linear-gradient(180deg, #070512, #101130);
  flex-grow: 1; /* Add this line */
  padding: 30px 20px 20px !important;
  color: #e8d1d9;
}

.fa-bars {
  color: #e8d1d9;
}

.dropdown-menu {
  background-color: #3c537f50 !important;
  margin: 0px !important;
  padding: 0px !important;
  border-radius: 5px !important;
}

.dropdown-menu:active {
  outline: none;
}

.dropdown-menu:focus {
}

.drop-item-btn:hover {
  color: #f5a6c1 !important;
}

.drop-item-btn:focus {
  outline: none;
}

.dropdown-item {
  text-align: center !important;
}
.modal {
  display: none;
}
.modal.is-active {
  display: flex;
  align-items: center;
  justify-content: center;
}
.modal-behind {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background-color: rgba(0, 0, 0, 0.5);
}
.moonhee {
  width: 800px !important;
  height: 782px !important;
}
.modal-shutdown {
  position: absolute;
  top: 10px;
  right: 10px;
}
</style>
