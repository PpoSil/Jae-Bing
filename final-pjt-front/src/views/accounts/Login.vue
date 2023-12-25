<template>
  <div class="login-div">
    <div class="container">
      <div class="row">
        <div class="col-6 welcome-div">
          <h1 class="m-3">Welcome</h1>
          <h2>To The New Game :)</h2>
        </div>
      </div>

      <div class="row">
        <div class="col-6 d-flex justify-content-center" id="rightline">
          <div class="mb-3 mt-5" style="max-width: 18rem">
            <div class="card-body">
              <div class="input-group-lg">
                <h3>ID</h3>
                <input
                  type="text"
                  placeholder="Enter Your ID!"
                  id="username"
                  class="form-control1"
                  v-model="credentials.username"
                />
              </div>
              <br />
              <br />
              <div class="input-group-lg">
                <h3>PASSWORD</h3>
                <input
                  placeholder="Enter Your PASSWORD!"
                  type="password"
                  id="password"
                  class="form-control1"
                  v-model="credentials.password"
                  @keypress.enter="login"
                />
              </div>
              <br />
              <button
                @click="login"
                class="login-btn btn mt-3 font-1-5em btn-block"
              >
                <img
                  src="./startbtn2.png"
                  alt="웅 이미지"
                  class="login-image"
                />
              </button>
            </div>
          </div>
        </div>

        <div class="col-6 d-flex align-items-center justify-content-center">
          <div>
            <h3 class="signup-ment ml-4 mb-0">Want a new game?</h3>
            <div class="emptydiv"></div>
            <router-link class="signup-a" :to="{ name: 'Signup' }">
              <img
                src="./signup-btn.png"
                alt="가입 이미지"
                class="signup-image"
              />
            </router-link>
            <div class="emptydiv"></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  name: "Login",
  data: function () {
    return {
      credentials: {
        username: "",
        password: "",
      },
    };
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem("jwt");

      const config = {
        headers: {
          Authorization: `JWT ${token}`,
        },
      };
      return config;
    },

    login: function () {
      axios
        .post(`${SERVER_URL}/accounts/api-token-auth/`, this.credentials)
        .then((res) => {
          // console.log(res)
          localStorage.setItem("jwt", res.data.token);
          this.$emit("login");
          this.$store.state.login = true;

          // console.log(res)
          const config = this.setToken();
          axios
            .get(`${SERVER_URL}/accounts/user/`, config)
            .then((res) => {
              // console.log(res.data)
              const id = res.data;
              this.$store.state.login_user = id;
              this.$store.state.username = this.credentials.username;
              localStorage.setItem(
                "user_movie",
                JSON.stringify(this.$store.state.user_movie)
              );
              localStorage.setItem("username", this.credentials.username);
              localStorage.setItem("login_user", id);
              this.$store.dispatch("recommendMovie", id);
              this.$store.dispatch("getMovie");
              // console.log(this.$store.state.login_user)
            })
            .catch((err) => {
              console.log(err);
            });

          axios
            .post(`${SERVER_URL}/accounts/is-admin/`, this.credentials)
            .then((res) => {
              this.$store.dispatch("isAdmin", res.data);
              localStorage.setItem("is_admin", res.data);
            })
            .catch((err) => {
              console.log(err);
            });
          this.$store.state.username = this.credentials.username;
          if (this.flag) {
            this.$router.push({
              name: "AdminManagement",
            });
          } else {
            this.$router.push({
              name: "MovieList",
            });
          }
        })
        .catch((err) => {
          console.log(err);
          alert("로그인 정보가 일치하지 않습니다.");
        });
    },
  },
  mounted() {
    window.scrollTo(0, 0);
    const token = localStorage.getItem("jwt");
    if (token) {
      const config = this.setToken();

      // 토큰 검증 및 사용자 정보 요청
      axios
        .get(`${SERVER_URL}/accounts/user/`, config)
        .then((res) => {
          const id = res.data;
          this.$store.state.login_user = id;
          this.$store.state.username = this.credentials.username;
          localStorage.setItem("username", this.credentials.username);
          localStorage.setItem("login_user", id);
          this.$store.dispatch("recommendMovie", id);

          // 로그인 상태를 설정
          this.$store.state.login = true;
        })
        .catch((err) => {
          console.log(err);

          // 토큰 검증 실패 시 로그인 상태를 false로 설정
          this.$store.state.login = false;
        });
    } else {
      // 토큰이 없는 경우 로그인 상태를 false로 설정
      this.$store.state.login = false;
    }
  },
};
</script>

<style scoped>
.login-div {
  background-image: url("loginpagefix2 (1).png");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.container {
  color: #e8d1d9;
  min-height: 90vh;
  background-color: #e8d1d900;
}

.welcome-div {
  margin-top: 90px;
}

/* input 속성 */
.form-control1 {
  padding: 10px;
  width: 100%;
  height: 40px;
  border: dashed;
  border-radius: 15px;
  border-color: #e8d1d969;
  outline: none;
  background-color: #0f264859;
  color: #e8d1d9;
  font-size: 20px;
}

/* input 클릭시 */
.form-control1:focus {
  padding: 10px;
  color: #e8d1d9;
}

#rightline {
  border-right: dashed #e8d1d969;
}

.emptydiv {
  height: 50px;
}

.signup-ment {
  text-decoration: none;
  font-size: 50px;
}

.signup-a {
  display: inline-block;
  color: #e8d1d9;
  font-size: 20px;
  position: relative;
}

.signup-image {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: auto;
  height: auto;
  /* Add any additional styles for the image */
}

.login-btn {
  color: #e8d1d9;
  font-size: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.login-image {
  margin-right: 10px;
  width: auto;
  height: auto;
  /* Add any additional styles for the image */
}
</style>
