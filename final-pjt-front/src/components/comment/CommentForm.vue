<template>
  <div class="comment-div d-flex justify-content-start">
    <div>
      <form v-on:submit.prevent="createComment">
        <div class="row">
          <div class="col-3 d-flex align-items-center m-0 pr-0">
            <label style="font-size: 22px" for="content" class="m-0"
              >Comment:
            </label>
          </div>
          <div class="col-6 position-relative p-0">
            <input
              placeholder="Enter Comment"
              type="text"
              class="form-control"
              id="content"
              v-model="content"
            />
          </div>
          <div class="col-3 d-flex align-items-center">
            <button
              type="submit"
              class="comment-create-btn"
              style="color: #d67297"
            >
              Submit
            </button>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL;
import axios from "axios";

export default {
  name: "CommentForm",
  data: function () {
    return {
      content: "",
    };
  },
  props: {
    post: [Object, String],
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
    createComment: function () {
      const config = this.setToken();

      const commentItem = {
        content: this.content,
      };
      //console.log(this.post)
      const postId = this.post.id;
      axios
        .post(
          `${SERVER_URL}/community/${postId}/comment_create/`,
          commentItem,
          config
        )
        .then((res) => {
          //console.log(res)
          this.$store.state.comments.unshift(res.data);
          this.content = "";
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  created: function () {
    console.log("post타입은?" + typeof this.post);
    console.log(this.post);
  },
};
</script>

<style scoped>
.comment-container {
  width: 100%;
  max-width: 500px;
  margin: 0 auto;
}

input {
  width: 100%;
  border: dashed;
  border-color: #e8d1d969;
  border-radius: 10px;
  background-color: #0f264859;
  outline: none;
  color: #e8d1d9;
  margin-left: 13px;
}

input:focus {
  color: #e8d1d9;
  background-color: #0f264859 !important;
  border-color: #e8d1d9;
}

input:hover {
  border-color: #e8d1d9;
}

.comment-create-btn:focus {
  outline: none;
}
</style>
