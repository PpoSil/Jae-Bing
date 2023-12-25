<template>
  <div class="sign-img">
    <div class="container">
      <h1 class="my-4">Sign up</h1>

      <!-- 유저 네임 -->
      <div class="signup-form-group mt-4">
        <label for="username">USERNAME</label>
        <input
          placeholder="Enter Your USERNAME"
          type="text"
          class="form-control2"
          id="username"
          v-model="credentials.username"
        />
      </div>

      <!-- 비밀번호 -->
      <div class="signup-form-group mt-4">
        <label for="password mb-1">PASSWORD</label>
        <input
          placeholder="Enter Your PASSWORD"
          type="password"
          class="form-control2"
          id="password"
          v-model="credentials.password"
        />
      </div>

      <!-- 비밀번호 확인 -->
      <div class="signup-form-group mt-4">
        <label for="passwordConfirmation">CONFIRM PASSWORD</label>
        <input
          placeholder="Confirm PASSWORD"
          type="password"
          id="passwordConfirmation"
          v-model="credentials.passwordConfirmation"
          @keypress.enter="signup"
          class="form-control2"
        />
      </div>

      <!-- 이메일 -->
      <div class="signup-form-group mt-4">
        <label for="email">E-MAIL</label>
        <input
          placeholder="Enter Your E-MAIL"
          type="email"
          class="form-control2"
          id="email"
          v-model="credentials.email"
        />
        <small id="emailHelp" class="form-text text-muted"
          >We'll never share your email with anyone else.</small
        >
      </div>

      <!-- 생년월일 -->
      <div class="signup-form-group mt-4">
        <label for="date_of_birth">BIRTH</label>
        <input
          type="date"
          class="form-control2"
          id="date_of_birth"
          v-model="credentials.date_of_birth"
        />
      </div>

      <!-- 개인정보약관동의 박스 -->
      <div class="form-check">
        <div class="row">
          <div class="col-5 d-flex justify-content-end p-2">
            <input
              class="check-box m-0"
              type="checkbox"
              id="gridCheck"
              checked="true"
              v-model="agree"
              @click="agreePage"
            />
          </div>

          <div class="col-7 d-flex flex justify-content-right p-2">
            <label for="gridCheck">
              <p class="mt-1">개인정보 이용 약관에 동의합니다.</p>
            </label>
          </div>
        </div>
      </div>
      <br />

      <div class="signup-form-group font-1-2em">
        <button @click="signup" id="signupbtn"></button>
        <h5 class="m-0" style="color: #d67297">
          Do You Want To Start The Game?
        </h5>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  name: "Signup",
  data: function () {
    return {
      credentials: {
        username: "",
        password: "",
        email: "",
        date_of_birth: "",
      },
      agree: false,
    };
  },
  methods: {
    signup: function () {
      if (this.agree === true) {
        axios
          .post(`${SERVER_URL}/accounts/signup/`, this.credentials)
          .then(() => {
            this.$router.push({ name: "Login" });
            this.agree = false;
          })
          .catch((err) => {
            console.log(err);
            alert("회원가입 정보가 올바르지 않습니다.");
          });
      } else {
        alert("개인정보 이용 약관에 동의해야합니다.");
      }
    },
    agreePage: function () {
      alert(
        "① 선생님은 저희에 대해 언제든지 개인정보 열람,정정,삭제,처리정지 요구 수 있어요^^7. \n② 그러면 빠르게 지워드릴게요^^7 \n③ 사칭하면 혼나요 ^^7."
      );
    },
  },
  mounted() {
    window.scrollTo(0, 0);
  },
};
</script>

<style scoped>
.sign-img {
  background-image: url("loginpagefix2 (1).png");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}
.container {
  color: #d5b0c1;
}

.signup-form-group {
  font-size: 20px;
}

/*  */
input {
  padding: 10px;
  width: 200px;
  height: 40px;
  display: block;
  margin: 0 auto;
  border: dashed;
  border-color: #e8d1d969;
  border-radius: 15px;
  background-color: #0f264859;
  outline: none;
  color: #e8d1d9;
  font-size: 18px;
}

input:focus {
  padding: 10px;
  color: #e8d1d9;
  background-color: #0f264859 !important;
}

/* 회원가입 버튼 */
#signupbtn {
  font-size: 2em !important;
  width: 300px;
  height: 40px;
  margin-bottom: 0px;
  background-image: url("startbtn2.png");
  /* background-size: cover; */
  background-position: center;
  background-repeat: no-repeat;
  border: none;
  outline: none;
  cursor: pointer;
}

/* input 속성 */
.form-control2 {
  background-color: #e8d1d900;
}

/* 개인정보약관 */
.form-check-label {
}
/* 체크박스 */
.check-box {
  width: 25px !important;
  height: 25px;
}
</style>
