<template>
  <div class="profile-container">
    <!-- 프로필 카드 -->
    <div class="profile-card">
      <strong><h1 class="mt-4 text-left">Profile</h1></strong>
      <div class="profile-div" v-if="profile">
        <h2 class="text-left my-3">
          <span class="username pr-2 pl-0">[ {{ profile.username }} ]</span>

          <!-- 팔로우 버튼 -->
          <span v-if="!isCurrentUser">
            <button
              style="color: #d67297; width: auto; height: auto"
              class="follow-btn"
              v-if="!isCurrentUser"
              @click="toggleFollow"
            >
              {{ isFollowing ? "Unfollow" : "Follow" }}
            </button>
          </span>

          <!-- 팔로워 수 -->
          <span style="font-size: 16px" class="follower"
            >Follower: {{ followersCount }}</span
          >

          <!-- 회원등급 -->
          <span style="font-size: 16px" class="grade"
            >Grade: {{ isAdmin ? "관리자" : "일반회원" }}</span
          >
        </h2>

        <!-- <p class="text-left">
          <strong>가입일:</strong> {{ formatDate(profile.date_joined) }}
        </p> -->
        <p
          style="color: #e8d1d9; font-size: 18px"
          class="text-left p-auto my-1"
        >
          Birth :{{ profile.date_of_birth }}
        </p>
        <p style="color: #e8d1d9; font-size: 18px" class="text-left">
          Email :{{ profile.email }}
        </p>
      </div>
    </div>
    <!-- 프로필 카드 끝 -->

    <div v-if="profile">
      <!-- <p><strong>회원코드:</strong> {{ profile.id }}</p> -->

      <!-- 전체적인 작성한 디브 -->
      <div class="created-div">
        <!-- 버튼 넣을 div 박스 -->
        <div class="btn-div mt-4">
          <!-- 게시글 -->
          <button
            style="font-size: 18px"
            class="created-btn"
            @click="selectedTab = 'posts'"
          >
            Created Posts
          </button>

          <!-- 리뷰 -->
          <button
            style="font-size: 18px"
            class="created-btn"
            @click="selectedTab = 'reviews'"
          >
            Created Review
          </button>

          <!-- 댓글 -->
          <button
            style="font-size: 18px"
            class="created-btn"
            @click="selectedTab = 'comments'"
          >
            Created Comments
          </button>
        </div>

        <!-- 작성한 게시글 테이블 -->
        <table
          class="created-table table table-hover"
          v-if="selectedTab === 'posts'"
        >
          <tr>
            <th>No.</th>
            <th>TITLE</th>
            <th>CONTENT</th>
            <th>DATE</th>
          </tr>
          <tr v-for="(post, idx) in posts" :key="idx">
            <th>{{ post.id }}</th>
            <th>{{ post.title }}</th>
            <th>{{ post.content }}</th>
            <th>
              {{ $moment(post.created_at).format("YYYY-MM-DD hh:mm:ss") }}
            </th>
          </tr>
        </table>

        <!-- 작성한 리뷰 테이블 -->
        <table
          class="created-table table table-hover"
          v-if="selectedTab === 'reviews'"
        >
          <tr>
            <th>No.</th>
            <th>MOIVE</th>
            <th>RATE</th>
            <th>CONTENT</th>
            <th>DATE</th>
          </tr>

          <tr v-for="review in reviews" :key="review.id">
            <th>{{ review.id }}</th>
            <th>{{ review.movie.title }}</th>
            <th>{{ review.rate }}</th>
            <th>{{ review.content }}</th>
            <th>
              {{ $moment(review.created_at).format("YYYY-MM-DD hh:mm:ss") }}
            </th>
          </tr>
        </table>

        <!-- 작성한 댓글 테이블 -->
        <table
          class="created-table table table-hover"
          v-if="selectedTab === 'comments'"
        >
          <tr>
            <th>No.</th>
            <th>POST NO.</th>
            <th>CONTENT</th>
            <th>DATE</th>
          </tr>
          <tr v-for="comment in comments" :key="comment.id">
            <th>{{ comment.id }}</th>
            <th>{{ comment.post }}</th>
            <th>{{ comment.content }}</th>
            <th>
              {{ $moment(comment.created_at).format("YYYY-MM-DD hh:mm:ss") }}
            </th>
          </tr>
        </table>
      </div>
    </div>
    <p v-else>Loading...</p>
  </div>
</template>

<script>
import axios from "axios";

const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  name: "Profile",
  data() {
    return {
      profile: null,
      isAdmin: false,
      reviews: [], // 리뷰
      posts: [], // 게시글
      comments: [], // 댓글
      followersCount: 0, // 팔로워 수
      isFollowing: false,
      isCurrentUser: false,
      selectedTab: "posts",
      followtrial: 0,
    };
  },
  methods: {
    setToken() {
      const token = localStorage.getItem("jwt");

      const config = {
        headers: {
          Authorization: `JWT ${token}`,
        },
      };
      return config;
    },
    formatDate(date) {
      return this.$moment(date).format("YYYY-MM-DD");
    },
    toggleFollow() {
      const username = this.$route.params.username;
      const config = this.setToken();

      if (this.isFollowing) {
        axios
          .post(
            `${SERVER_URL}/accounts/profile/${username}/unfollow/`,
            {},
            config
          )
          .then((res) => {
            alert("언팔로우되었습니다."); // 알림 표시
            this.followtrial = 0;
          })
          .catch((err) => {
            console.log(err);
          });
        axios
          .get(`${SERVER_URL}/accounts/profile/${username}/followers/`)
          .then((res) => {
            this.followersCount = res.data.length - 1;
            // console.log(res.data, '어디 함 볼까1');
            // console.log(this.$store.state.login_user, '유저');
            // console.log(res.data.includes(this.$store.state.login_user));
            // this.followersCount = res.data.length; // 팔로워 수 설정
            console.log(res.data, "언팔로우");
            if (res.data.includes(this.$store.state.login_user)) {
              // console.log('있네');
              this.isFollowing = false;
            }
          })
          .catch((err) => {
            console.log(err);
          });
      } else {
        axios
          .post(
            `${SERVER_URL}/accounts/profile/${username}/follow/`,
            {},
            config
          )
          .then((res) => {
            // this.isFollowing = true;
            // console.log(res.data, '팔로우');
            // this.followersCount = res.data.followers_count;
            this.followtrial++;
            alert("팔로우되었습니다."); // 알림 표시
          })
          .catch((err) => {
            console.log(err);
          });
        axios
          .get(`${SERVER_URL}/accounts/profile/${username}/followers/`)
          .then((res) => {
            // console.log(res.data, '어디 함 볼까2');
            // console.log(this.$store.state.login_user, '유저');
            // console.log(res.data.includes(this.$store.state.login_user));
            console.log(this.followtrial, "몇번 눌렀니");
            console.log(res.data, "팔로우");
            this.followersCount = res.data.length + 1;
            if (res.data.includes(this.$store.state.login_user)) {
              // console.log('있네');
              this.isFollowing = true;
            }
            if (this.followtrial === 0) {
              this.isFollowing = true;
            }
          })
          .catch((err) => {
            console.log(err);
          });
      }
    },
  },
  created() {
    const currentusername = localStorage.getItem("username");
    const username = this.$route.params.username;
    axios
      .get(`${SERVER_URL}/accounts/profile/${username}/`)
      .then((res) => {
        this.profile = res.data;
        // this.followersCount = this.profile.followers_count; // 팔로워 수 설정
        this.isCurrentUser = this.profile.username === currentusername;
        // console.log(this.isCurrentUser);
      })
      .catch((err) => {
        console.log(err);
      });

    // 추가된 부분: 팔로워 수 가져오기
    axios
      .get(`${SERVER_URL}/accounts/profile/${username}/followers/`)
      .then((res) => {
        // console.log(res.data, '어디 함 볼까2');
        // console.log(this.$store.state.login_user, '유저');
        // console.log(res.data.includes(this.$store.state.login_user));
        this.followersCount = res.data.length;
        if (res.data.includes(this.$store.state.login_user)) {
          // console.log('있네');
          if (res.data.includes(this.$store.state.login_user)) {
            // console.log('있네');
            this.isFollowing = true;
          } else {
            this.isFollowing = false;
          }
        }
      })
      .catch((err) => {
        console.log(err);
      });

    axios
      .get(`${SERVER_URL}/movies/${username}/reviews/`)
      .then((res) => {
        this.reviews = res.data;
      })
      .catch((err) => {
        console.log(err);
      });
    axios
      .get(`${SERVER_URL}/community/${username}/posts/`)
      .then((res) => {
        this.posts = res.data;
      })
      .catch((err) => {
        console.log(err);
      });
    axios
      .get(`${SERVER_URL}/community/${username}/comments/`)
      .then((res) => {
        this.comments = res.data;
        console.log(this.comments);
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>

<style>
/* 전체적인 프로필 디브 */
.profile-container {
  color: #e8d1d9;
  min-height: 100vh;
  width: 100%;
  padding: 0 10%;
  background-image: url("profile.png");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  color: #e8d1d9;
}

/* 프로필 정보 */
.profile-div {
  border-style: dashed none;
  border-color: #e8d1d969;
  background-color: #101130b3;
}

/* 팔로우 버튼 */
.follow-btn {
  width: auto;
  height: auto;
  padding: 0px;
}

.follow-btn:focus {
  outline: none;
}

/* 작성한~ 버튼 디브 */
.btn-div {
  display: flex;
  justify-content: flex-start;
  /* margin-top: 20px; */
}

/* 작성한 게시글 */
.created-btn {
  width: auto;
  padding-left: 0px;
}

/* 버튼 클릭시 테두리 삭제 */
.created-btn:focus {
  outline: none;
}

/* 작성한~ 테이블 속성 */
.created-table {
  font-family: "NeoDunggeunmo";
  font-size: 20px;
  color: #e8d1d9 !important;
  border-style: dashed;
  /* border-color: #4c4d81b2; */
  border-color: #e8d1d969;
  background-color: #101130d1;
  /* margin: 2px; */
}

.created-div {
  padding: 0px 20px 20px 20px;
}

/* 프로필 카드 */
.profile-card {
  /* background-color: #101130; */
  color: white;
  padding: 20px 20px 0px;
}

/* 팔로워 속성 */
.follower {
  font-size: 16px;
}

/* 회원 등급 속성 */
.grade {
  font-size: 16px;
}

/* 유저 이름 속성 */
.username {
  padding-right: 8px;
  padding-left: 4px;
  margin: auto;
  font-size: 40px;
}

/* 테이블 요소 속성 */
th {
  padding: 2px !important;
}
</style>
