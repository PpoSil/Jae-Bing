<template>
  <!-- 전체 디브 -->
  <div id="main">
    <!-- 네브바 있는 헤더 -->
    <header>
      <nav class="nav fixed-top">
        <a href="/" class="home-btn font-weight-bold">
          <img class="main-Logo" src="./main.gif" alt="재빙" />
          JEABING
        </a>
        <div>
          <router-link :to="{ name: 'Signup' }" class="nav-margin">
            <button class="main-btn font-weight-bold">SignUp</button>
          </router-link>
          <router-link :to="{ name: 'Login' }" class="nav-margin">
            <button class="main-btn font-weight-bold">Login</button>
          </router-link>
        </div>
      </nav>
      <router-view @login="login = true" />
    </header>
    <div v-if="this.$route.path == '/'">
      <!-- 텍스트 박스 먹은 비디오 박스 -->
      <div class="video-box">
        <!-- 비디오 박스 -->
        <div class="jb-box">
          <div class="shadowcover"></div>
          <video muted autoplay loop>
            <source src="./Legend.mp4" type="video/mp4" />
            <strong>Your browser does not support the video tag.</strong>
          </video>
        </div>

        <!-- 비디오 내에 보이는 텍스트 박스 -->
        <div class="message-title jb-text">
          <p class="fw-bold">내가 찾던 재미</p>
          <p>보고 싶은 콘텐츠를 발견하세요!</p>
          <p>최신, 인기 TV프로그램, 영화</p>
          <p>해외시리즈, 파라마운트+ 오리지널 및 독점</p>
        </div>
      </div>
      <!-- 비디오 박스 끝 -->

      <!-- 이미지 슬라이드 디브 -->
      <div class="flow-scene-wrap">
        <div class="flow-scene-first">
          <!-- ul박스 -->
          <ul class="first-ul-1">
            <li class="first-li-1">
              <picture class="pic">
                <source
                  srcset="https://image.tving.com/upload/cms/caip/CAIP1500/P000643144.jpg/dims/resize/F_webp,1024"
                  type="image/webp"
                  class="src"
                />
                <img
                  class="load-img"
                  src="https://image.tving.com/upload/cms/caip/CAIP1500/P000643144.jpg/dims/resize/1024"
                  alt="유 퀴즈 온 더 블럭 포스터"
                />
              </picture>
            </li>
            <li class="first-li-1">
              <picture class="pic">
                <source
                  srcset="https://image.tving.com/upload/cms/caip/CAIP1500/P001706762.jpg/dims/resize/F_webp,1024"
                  type="image/webp"
                  class="src"
                />
                <img
                  class="load-img"
                  src="https://image.tving.com/upload/cms/caip/CAIP1500/P001706762.jpg/dims/resize/1024"
                  alt="장사천재 백사장 포스터"
                />
              </picture>
            </li>
            <li class="first-li-1">
              <picture class="pic">
                <source
                  srcset="https://image.tving.com/upload/cms/caip/CAIP1500/P001693843.jpg/dims/resize/F_webp,1024"
                  type="image/webp"
                  class="src"
                />
                <img
                  class="load-img"
                  src="https://image.tving.com/upload/cms/caip/CAIP1500/P001693843.jpg/dims/resize/1024"
                  alt="방과 후 전쟁활동 포스터"
                />
              </picture>
            </li>
            <li class="first-li-1">
              <picture class="pic">
                <source
                  srcset="https://image.tving.com/upload/cms/caip/CAIP1500/P001691763.jpg/dims/resize/F_webp,1024"
                  type="image/webp"
                  class="src"
                />
                <img
                  class="load-img"
                  src="https://image.tving.com/upload/cms/caip/CAIP1500/P001691763.jpg/dims/resize/1024"
                  alt="래빗홀 포스터"
                />
              </picture>
            </li>
            <li class="first-li-1">
              <picture class="pic">
                <source
                  srcset="https://image.tving.com/upload/cms/caip/CAIP1500/P001710496.jpg/dims/resize/F_webp,1024"
                  type="image/webp"
                  class="src"
                />
                <img
                  class="load-img"
                  src="https://image.tving.com/upload/cms/caip/CAIP1500/P001710496.jpg/dims/resize/1024"
                  alt="닥터 차정숙 포스터"
                />
              </picture>
            </li>
          </ul>
        </div>
        <!-- flow-scene-first div -->
      </div>
    </div>
    <!-- flow-scene-wrap div -->
  </div>
  <!-- main div -->
</template>

<script>
export default {
  mounted() {
    var originalID, cloneID; //인터벌 포인터
    //롤링 배너 복제본 생성
    let roller = document.querySelector('.flow-scene-first');
    roller.id = 'roller1';

    let clone = roller.cloneNode(true);
    clone.id = 'roller2';
    document.querySelector('.flow-scene-wrap').appendChild(clone); //부착

    //원본, 복제본 배너 위치 지정
    document.querySelector('#roller1').style.left = '0px';
    document.querySelector('#roller2').style.left = document.querySelector('.flow-scene-first ul').offsetWidth + 'px';

    //클래스 할당
    roller.classList.add('original');
    clone.classList.add('clone');

    //인터벌 메서드로 애니메이션 생성
    let rollerWidth = document.querySelector('.flow-scene-first ul').offsetWidth; //회전 배너 너비값
    let betweenDistance = 1; //이동 크기 - 정수여야 함

    //롤링 시작
    function startRoller() {
      originalID = window.setInterval(
        betweenRollCallback,
        parseInt(1000 / 100),
        betweenDistance,
        document.querySelector('#roller1')
      );
      cloneID = window.setInterval(
        betweenRollCallback,
        parseInt(1000 / 100),
        betweenDistance,
        document.querySelector('#roller2')
      );
    }

    // 정지 안쓰려면 아래 주석하심 됩니다? 안호구씨 그리고 위에 변수 지워주고 originalID, cloneID 이거 두개
    //롤링 정지
    function stopRoller() {
      clearInterval(originalID);
      clearInterval(cloneID);
    }

    //마우스 호버시 롤링이 멈추었다 벗어나면 다시 롤링이 되도록 처리
    document.getElementById('roller1').addEventListener('mouseover', () => {
      stopRoller();
    });
    document.getElementById('roller2').addEventListener('mouseover', () => {
      stopRoller();
    });
    document.getElementById('roller1').addEventListener('mouseout', () => {
      startRoller();
    });
    document.getElementById('roller2').addEventListener('mouseout', () => {
      startRoller();
    });

    //인터벌 애니메이션 함수(공용)
    function betweenRollCallback(d, roller) {
      let left = parseInt(roller.style.left);
      roller.style.left = left - d + 'px'; //이동
      //조건부 위치 리셋
      if (rollerWidth + (left - d) <= 0) {
        roller.style.left = rollerWidth + 'px';
      }
    }

    startRoller(); //롤링 초기화
  },
};
</script>

<style>
@font-face {
  font-family: 'DungGeunMo';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_six@1.2/DungGeunMo.woff') format('woff');
  font-weight: normal;
  font-style: normal;
}

@font-face {
  font-family: 'EF_watermelonSalad';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2210-EF@1.0/EF_watermelonSalad.woff2') format('woff2');
  font-weight: normal;
  font-style: normal;
}

/* 도화지 배경 */
html {
  /* background-color: #0F2648; */
  background: linear-gradient(45deg, #e8d1d9, #3c537f, #101130);
}

/* 바디 배경 */
body {
  padding: 0px;
  margin: 0px;
}

.main-Logo {
  width: 70px;
  height: auto;
  margin: 0px;
}

/* 비디오 박스 */
.jb-box {
  width: 100%;
  height: 800px;
  overflow: hidden;
  margin: 0px auto;
  position: absolute;
}

/* 비디오 */
video {
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 0.45;
}

.shadowcover {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(transparent, transparent, transparent, #070512) !important;
  z-index: 10;
  pointer-events: none;
}

/* 텍스트 박스 */
.jb-text {
  position: absolute;
  top: 20%;
  width: 100%;
}

/* 텍스트 박스 내 텍스트 속성 */
.jb-text p {
  margin-top: -24px;
  text-align: center;
  font-size: 40px;
  color: #e8d1d9;
}

/* 전체 페이지 속성 */
#main {
  font-family: 'DungGeunMo';
  background-color: #101130;
  /* background: linear-gradient(45deg, #E8D1D9, #3C537F, #0f2648); */
  color: #e8d1d9;
  text-align: center;
}

/* 버튼들있는 네브바 */
.nav {
  color: #e8d1d9;
  display: flex;
  justify-content: space-between;
  font-size: 20px;
}

/* 홈 버튼 속성 */
.home-btn {
  text-decoration-line: none;
  padding: 8px;
  color: #e8d1d9;
  background-color: #10113000;
  width: 70px;
  height: 40px;
}

/* 홈 버튼에 마우스 올렸을 때 */
.home-btn:hover {
  text-decoration-line: none;
  color: #d5b0c1;
  outline: none;
}

/* 홈 버튼 클릭시 */
.home-btn:active {
  text-decoration-line: none;
  border: #d5b0c1;
  outline: none;
}

/* 회원가입, 로그인 버튼 */
.main-btn {
  font-size: 25px;
  width: auto;
  height: auto;
  margin-right: 8px;
}

.main-btn:active {
  text-decoration-line: none;
  border: #d5b0c1;
  outline: none;
}

/* 로그인, 회원가입 버튼 속성 */
button {
  margin: 15px;
  background-color: #10113000;
  /* border-color: #E8D1D9;; */
  color: #e8d1d9;
  width: 70px;
  height: 40px;
}

/* 버튼 클릭시 색변경 */
button:hover {
  color: #d5b0c1;
}

/* 여기 다시 건들기 */
a:active {
  color: #d5b0c1;
  text-decoration: none;
}

/* 각 태그들 점 없애기 */
dl,
li,
ol,
ul {
  list-style: none;
}

/* 슬라이드 이미지 속성 */
img {
  border-radius: 5px;
  width: 350px;
  height: 200px;
  margin: 10px;
}

.flow-scene-wrap {
  position: relative;
  overflow: hidden;
  height: 800px;
  z-index: 5;
}

.flow-scene-first {
  position: absolute;
  top: 50%;
}

.flow-scene-first > ul {
  margin: 0;
  list-style: none;
  padding: 9px 0;
  display: flex;
  flex-flow: row nowrap;
  align-items: center;
}

.first-ul-1 {
  height: 200px;
  bottom: 100%;
  position: relative;
}

.flow-scene-second ul {
  display: flex;
  /* width: 300%; */
  animation: slidein 6s infinite linear;
  animation-timing-function: linear;
}

@keyframes slidein1 {
  0% {
    transform: translateX(30%);
  }
  50% {
    transform: translateX(-70%);
  }
  50.01% {
    transform: translateX(70%);
  }
  100% {
    transform: translateX(30%);
  }
}

@keyframes slidein2 {
  0% {
    transform: translateX(0%);
  }
  100% {
    transform: translateX(-200%);
  }
}

/* 애니메이션 */
.roller.original {
  animation: 33s linear 0s infinite normal forwards running rollingleft1;
}
.roller.clone {
  animation: 33s linear 0s infinite normal none running rollingleft2;
}
@keyframes rollingleft1 {
  /* 원본용 */
  0% {
    transform: translateX(0);
  }
  50% {
    transform: translateX(-100%);
  }
  50.01% {
    transform: translateX(100%);
  }
  100% {
    transform: translateX(0);
  }
}

/* 클론용 */
/* @keyframes rollingleft2 {
  0% {
    transform: translateX(0);
  }
  100% {
    transform: translateX(-200%);
  }
} */

footer {
  width: 100%;
  height: 150px;
}
</style>
