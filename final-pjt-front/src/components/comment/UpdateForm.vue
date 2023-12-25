<template>
  <div class="container">
    <div class="row">
      <hr />
    </div>

    <form v-on:submit.prevent="updateComment">
      <div class="row">
        <div
          class="col-2 d-flex align-items-center justify-content-start p-0"
          id="updateDiv"
        >
          <label class="m-0" for="content" style="font-size: 20px"
            >Edit :
          </label>
        </div>
        <div class="col-7 d-flex align-items-center p-0">
          <input
            type="text"
            class="form-control"
            id="content"
            v-model="content"
          />
        </div>
        <div class="col-3 d-flex align-items-center p-0">
          <button
            class="p-0"
            style="font-size: 20px; color: #d67297"
            type="submit"
            @click="updateComment(post)"
          >
            Submit
          </button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL;
import axios from "axios";

export default {
  name: "UpdateForm",
  data: function () {
    return {
      content: "",
      comments: "",
    };
  },
  props: {
    updateCommentItem: [Object, String],
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
    updateComment: function () {
      const config = this.setToken();
      const updateItem = {
        ...this.updateCommentItem,
        post: this.post.id,
        content: this.content,
      };
      axios
        .put(
          `${SERVER_URL}/community/${this.post.id}/comment/${this.updateCommentItem.id}/`,
          updateItem,
          config
        )
        .then((res) => {
          console.log(res);
          this.$emit("trigger");
          const targetCommentIdx = this.comments.findIndex((comment) => {
            return comment.id === res.data.id;
          });
          this.$store.state.comments[targetCommentIdx].content = this.content;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  created: function () {
    this.content = this.updateCommentItem.content;
    this.comments = this.$store.state.comments;
  },
};
</script>

<style scoped>
#updatedDiv {
  display: inline;
}

form {
  display: inline;
}

input {
  border: dashed;
  border-color: #e8d1d969;
  border-radius: 10px;
  background-color: #0f264859;
  outline: none;
  color: #e8d1d9;
}

input:focus {
  color: #e8d1d9;
  background-color: #0f264859 !important;
  border-color: #e8d1d9;
  outline: none;
}

input:hover {
  border-color: #e8d1d9;
  outline: none;
}
</style>
