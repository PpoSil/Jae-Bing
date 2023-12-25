<template>
  <div class="post-detail-div">
    <div class="create-post-container">
      <div style="height: 100px"></div>
      <div class="htag">
        <h1 v-if="this.purpose == 'create'" style="margin-top: 20px">
          Create Post
        </h1>
        <h1 v-else-if="this.purpose == 'update'" class="my-3">Create Post</h1>
      </div>

      <div class="row justify-content-center">
        <form
          v-if="this.purpose == 'create'"
          v-on:submit.prevent="createPostForm"
        >
          <div class="post-form-group">
            <label for="title">Title : </label>
            <div>
              <input
                type="text"
                class="form-control create-form-control"
                id="title"
                v-model.trim="title"
                style="color: #e8d1d9"
              />
            </div>
          </div>

          <div class="post-form-group my-3">
            <label for="content">Content : </label>
            <textarea
              class="form-control create-form-control"
              id="content"
              v-model="content"
              style="color: #e8d1d9"
            ></textarea>
          </div>
          <button style="color: #d67297" class="submit-btn" type="submit">
            Submit
          </button>
        </form>

        <form v-if="this.purpose == 'update'" v-on:submit.prevent="updatePost">
          <div>
            <label for="title">Title: </label>
            <input type="text" id="title" v-model.trim="title" />
          </div>
          <div>
            <label for="content">Content: </label>
            <input type="text" id="content" v-model="content" />
          </div>
          <button type="submit-btn">Submit</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL;
import axios from "axios";

export default {
  name: "CreatePost",
  data: function () {
    return {
      posts: [],
      title: "",
      content: "",
      purpose: "",
      updateId: "",
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
    createPostForm: function () {
      const config = this.setToken();

      const postItem = {
        title: this.title,
        content: this.content,
      };
      axios
        .post(`${SERVER_URL}/community/post_create/`, postItem, config)
        .then((res) => {
          //console.log(res)
          this.$router.push({
            name: "PostDetail",
            params: {
              id: res.data.id,
            },
          });
        })
        .catch((err) => {
          console.log(err);
          alert("잘못된 정보를 입력했습니다.");
        });
    },
    updatePost: function () {
      const config = this.setToken();

      const postItem = {
        title: this.title,
        content: this.content,
        post_code: 1,
      };
      axios
        .put(
          `${SERVER_URL}/community/post_delete_update/${this.updateId}/`,
          postItem,
          config
        )
        .then((res) => {
          this.$router.push({
            name: "PostDetail",
            params: {
              id: res.data.id,
            },
          });
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  created: function () {
    this.purpose = this.$route.params.purpose;
    this.updateId = this.$route.params.id;
    this.title = this.$route.params.title;
    this.content = this.$route.params.content;
  },
  mounted() {
    window.scrollTo(0, 0);
  },
};
</script>

<style scoped>
.create-post-container {
  width: 100%;
  min-height: 85vh;
  color: #e8d1d9;
  font-size: 20px;

  background-image: url("postdetailback.png");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.submit-btn {
  width: 100%;
}

.create-form-control {
  /* background-color: #e8d1d986 !important; */
}

input,
textarea {
  padding: 10px;
  width: auto;
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

/* 왜 아웃라인 안 없어짐? + 배경 경계 맞추기 */
input:hover,
textarea:hover {
  border-color: #e8d1d9;
  outline: none;
}

input:focus,
textarea:focus,
input:active,
textarea:active {
  background-color: #0f264859;
  outline: none;
}
</style>
