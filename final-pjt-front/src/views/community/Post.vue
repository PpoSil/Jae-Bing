<template>
  <div class="article">
    <div class="container">
      <div class="row">
        <div class="col-3 p-0">
          <h1 class="h1-tag mt-5 mt-2 text-left">Post</h1>
        </div>

        <div
          class="create-btn-div p-0 col-9 d-flex align-items-center justify-content-end align-items-end"
        >
          <button
            v-if="this.$store.state.login"
            @click="createPost()"
            class="create-btn btn float-right"
          >
            Create Post
          </button>
          <p v-else class="my-4 float-right">
            게시글 작성하려면 로그인하구 와!
          </p>
        </div>
      </div>

      <!-- 게시판 테이블 -->
      <div class="row">
        <table class="article-table table table-hover">
          <tr>
            <th>No</th>
            <th>Title</th>
            <th>Writer</th>
            <th>Create Date</th>
          </tr>
          <tr v-for="(post, idx) in posts" :key="idx">
            <th>{{ post.id }}</th>
            <th @click="postDetail(post)">{{ post.title }}</th>
            <th>{{ post.user.username }}</th>
            <th>
              {{ $moment(post.created_at).format("YYYY-MM-DD hh:mm:ss") }}
            </th>
          </tr>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL;
import axios from "axios";

export default {
  name: "Post",
  data: function () {
    return {
      posts: [],
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
    createPost: function () {
      this.$router.push({
        name: "CreatePost",
        params: {
          purpose: "create",
        },
      });
    },
    postDetail: function (post) {
      this.$router.push({
        name: "PostDetail",
        params: {
          id: post.id,
        },
      });
    },
  },
  created: function () {
    const config = this.setToken();
    axios
      .get(`${SERVER_URL}/community/`, config)
      .then((res) => {
        this.posts = res.data;
      })
      .catch((err) => {
        console.log(err);
      });
  },
  mounted() {
    window.scrollTo(0, 0);
  },
};
</script>

<style>
@font-face {
  font-family: "NeoDunggeunmoPro-Regular";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2302@1.0/NeoDunggeunmoPro-Regular.woff2")
    format("woff2");
  font-weight: normal;
  font-style: normal;
}

@font-face {
  font-family: "NeoDunggeunmo";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.3/NeoDunggeunmo.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}

.article-table {
  font-family: "NeoDunggeunmo";
  font-size: 20px;
  color: #e8d1d9 !important;
  border-style: dashed;
  /* border-color: #4c4d81b2; */
  border-color: #e8d1d969;
}

.create-btn-div {
  position: relative;
  /* height: 100%; */
}

.create-btn {
  font-size: 20px !important;
  font-family: "NeoDunggeunmoPro-Regular";
  color: #d67297 !important;
  width: auto;
  margin-top: auto;
}

.h1-tag {
  font-family: "NeoDunggeunmoPro-Regular";
  margin-left: auto;
  margin-right: auto;
}

@media (max-width: 768px) {
  .h1-tag {
    font-size: 35px; /* Adjust the font size as needed */
  }
}

.article {
  width: 100%;
  min-height: 100vh;
  background-image: url("postdetailback.png");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  /* backdrop-filter: blur(10px); */
  color: #e8d1d9;
}

.article-table {
  font-family: "NeoDunggeunmo";
  font-size: 20px;
  color: #e8d1d9 !important;
  border-style: dashed;
  /* border-color: #4c4d81b2; */
  border-color: #e8d1d969;
  background-color: #101130d1;
}
</style>
