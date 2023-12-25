<template>
  <div>
    <div
      class="mt-4"
      style="border-style: dashed none; border-color: #e8d1d969; width: 439px"
    >
      <span style="font-size: 35px; padding: 0px 10px 0px 0px"
        >Comment List</span
      >
      <span style="font-size: 20px">Comment Count : {{ comments.length }}</span>
    </div>
    <div v-for="(comment, idx) in comments" :key="idx" class="media px-0">
      <div class="media-body" style="border-bottom: dashed #e8d1d969">
        <h4 class="mt-0">
          [ {{ comment.user.username }} ] {{ comment.content }}
        </h4>
        <p class="m-0">
          Create:
          {{ $moment(comment.created_at).format("YYYY-MM-DD hh:mm:ss") }}
        </p>
        |
        <p class="ml-0">
          Edit Date :
          {{ $moment(comment.created_at).format("YYYY-MM-DD hh:mm:ss") }}
        </p>

        <div v-if="updateTrigger === comment.id">
          <UpdateForm
            :updateCommentItem="updateCommentItem"
            :post="post"
            @trigger="changeTrigger"
          />
        </div>
        <div>
          <!--작성자와 접속자가 같다면, 수정/삭제 버튼 활성화-->
          <!--단, 관리자의 경우 삭제 버튼 활성화 -->
          <button
            style="color: #d67297"
            class="comment-btn pl-0"
            v-if="comment.user.id == login_user && updateTrigger === false"
            @click="updatePostForm(comment)"
          >
            Edit
          </button>

          <button
            style="color: #d67297"
            class="comment-btn"
            v-if="is_admin && updateTrigger === false"
            @click="deleteComment(comment)"
          >
            Delete
          </button>

          <button
            style="color: #d67297"
            class="comment-btn"
            v-else-if="comment.user.id == login_user && updateTrigger === false"
            @click="deleteComment(comment)"
          >
            Delete
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL;
import axios from "axios";
import UpdateForm from "@/components/comment/UpdateForm";

import { mapState } from "vuex";

export default {
  name: "CommentList",
  components: {
    UpdateForm,
  },
  data: function () {
    return {
      updateTrigger: false,
      updateCommentItem: "",
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

    deleteComment: function (comment) {
      const config = this.setToken();
      axios
        .delete(
          `${SERVER_URL}/community/${this.post.id}/comment/${comment.id}/`,
          config
        )
        .then((res) => {
          const targetCommentIdx = this.comments.findIndex((comment) => {
            return comment.id === res.data.id;
          });
          this.$store.state.comments.splice(targetCommentIdx, 1);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    updatePostForm: function (comment) {
      this.updateTrigger = comment.id;
      this.updateCommentItem = comment;
    },
    changeTrigger: function () {
      this.updateTrigger = false;
    },
  },
  created: function () {
    // if (login) {
    //   this.username = this.$store.state.username
    //   this.login = this.$store.state.login
    // }
  },
  computed: {
    ...mapState(["login", "login_user", "username", "is_admin", "comments"]),
  },
};
</script>

<style scoped>
div > p {
  display: inline;
  margin: 10px 5px;
}

/* 댓글 수정 삭제 버튼 */
.comment-btn {
  width: auto;
  margin: 0px;
  font-size: 18px;
  /* padding: 0px; */
  /* border: dashed #e8d1d969;
  border-radius: 5px; */
}

.comment-btn:active,
.comment-btn:focus {
  outline: none;
}
</style>
