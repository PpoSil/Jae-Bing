<template>
  <div class="post-detail-container">
    <div class="row justify-content-center">
      <div class="post-detail">
        <div>
          <h1 class="my-5">View Article Details</h1>
        </div>

        <button class="post-detail-btn heart-btn" @click="toggleLikePost">
          <span v-if="isPostLiked"
            ><img class="heart-img" src="./fullheart.png" alt=""
          /></span>
          <span v-else
            ><img class="heart-img" src="./emptyheart.png" alt=""
          /></span>
        </button>
        <span class="likes-span" style="font-size: 20px"
          >Likes : {{ likesCount }}</span
        >

        <div
          class="col media text-justify"
          style="width: 100%; word-break: break-all"
        >
          <div
            class="col media text-justify p-0"
            style="width: 100%; word-break: break-all"
          >
            <p style="font-size: 28px; margin: 0px">
              Writer :
              <router-link
                class="router-user"
                :to="{ name: 'Profile', params: { username: postUsername } }"
              >
                [ {{ postUsername }} ]</router-link
              >
            </p>
            <!-- 제목-->
            <h2 class="mt-0" style="display: flex; align-items: center">
              <span class="p-0">Title : [ {{ post.title }} ]</span>
            </h2>
          </div>

          <div
            style="
              width: 100%;
              height: 100%;
              border-style: dashed none;
              border-color: #e8d1d969;
            "
          >
            <!-- 작성자 -->

            <!-- 내용 -->
            <div style="font-size: 25px">
              <span style="display: block" class="pb-3 px-0">Content</span>
              <span style="display: block" class="p-0">{{ post.content }}</span>
            </div>

            <div>
              <!-- 작성일, 수정일 -->
              <span style="text-align: right; display: block">
                <span style="display: inline-block; text-align: left">
                  Create :
                  {{ $moment(post.created_at).format("YYYY-MM-DD hh:mm:ss") }}
                </span>
                |
                <span style="display: inline-block; text-align: left">
                  Current Edit Date :
                  {{ $moment(post.updated_at).format("YYYY-MM-DD hh:mm:ss") }}
                </span>
              </span>
            </div>
          </div>

          <div class="detail-btns">
            <button
              style="color: #d67297"
              class="modify-btn post-detail-btn mr-3"
              v-if="postUsername === this.$store.state.username"
              @click="updatePostForm(post)"
            >
              Edit
            </button>

            <!-- 관리자 글 삭제 버튼 -->
            <button
              class="modify-btn-admin post-detail-btn mr-3"
              v-if="this.$store.state.is_admin"
              @click="deletePost(post)"
            >
              Delete
            </button>

            <!-- 유저 글 삭제 버튼 -->
            <button
              style="color: #d67297"
              v-else-if="postUsername === this.$store.state.username"
              @click="deletePost(post)"
              class="delete-post-btn post-detail-btn mr-3"
            >
              Delete
            </button>
            <!-- 목록으로 가기 버튼 -->
            <button
              style="color: #d67297"
              @click="backToPost"
              class="postpage-btn"
            >
              Go To List
            </button>
          </div>

          <div class="comment-div">
            <!-- 댓글 -->
            <div class="create-comment-btn mt-5">
              <CommentForm v-if="this.$store.state.login" :post="post" />
              <p v-else>댓글을 작성하려면 로그인이 필요합니다.</p>
            </div>

            <CommentList :post="post" />
          </div>
        </div>
      </div>
    </div>

    <!-- create-comment-btn 끝 -->
  </div>
</template>

<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL;
import axios from "axios";

import CommentList from "@/components/comment/CommentList";
import CommentForm from "@/components/comment/CommentForm";

export default {
  name: "PostDetail",
  components: {
    CommentList,
    CommentForm,
  },
  data() {
    return {
      post: "",
      postUsername: "",
      postItem: "",
      all_comments: "",
      images: {
        logo: require("@/assets/images/logo.png"),
        flamingo: require("@/assets/images/flamingo.png"),
      },
      isPostLiked: false,
      likesCount: 0,
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
    backToPost() {
      this.$router.push({
        name: "Post",
      });
    },
    deletePost(post) {
      const config = this.setToken();
      axios
        .delete(
          `${SERVER_URL}/community/post_delete_update/${post.id}/`,
          config
        )
        .then(() => {
          this.$router.push({
            name: "Post",
          });
        })
        .catch((err) => {
          console.log(err);
        });
    },
    updatePostForm(post) {
      const postItem = {
        id: post.id,
        purpose: "update",
        title: post.title,
        content: post.content,
      };
      this.$router.push({
        name: "CreatePost",
        params: postItem,
      });
    },
    getAllComment() {
      axios
        .get(`${SERVER_URL}/community/${this.postItem}/comments/`)
        .then((res) => {
          if (res.data) {
            this.$store.state.comments = res.data;
            this.all_comments = this.$store.state.comments;
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
    toggleLikePost() {
      const config = this.setToken();
      axios
        .post(`${SERVER_URL}/community/posts/${this.post.id}/like/`, {}, config)
        .then((res) => {
          this.isPostLiked = res.data.liked;
          this.likesCount = res.data.likes_count;
          this.getLikesCount();
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getLikesCount() {
      const config = this.setToken();
      axios
        .get(`${SERVER_URL}/community/posts/${this.post.id}/like/`, config)
        .then((res) => {
          console.log(res.data.liked);
          console.log(res.data.likes_count);
          this.isPostLiked = res.data.liked;
          this.likesCount = res.data.likes_count;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  created() {
    this.postItem = this.$route.params.id;
    axios
      .get(`${SERVER_URL}/community/${this.postItem}/`)
      .then((res) => {
        this.post = res.data;
        this.postUsername = this.post.user.username;
        this.getLikesCount();
      })
      .catch((err) => {
        console.log(err);
      });

    this.getAllComment();
  },
  mounted() {
    window.scrollTo(0, 0);
  },
};
</script>

<style>
.post-detail-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  color: #e8d1d9;
  /* margin: 0px 20px; */
  min-height: 90vh;
  background-image: url("postdetailback.png");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.post-detail {
  width: 800px;
}

/* 미디어박스 세로정렬 */
.media {
  display: flex;
  flex-direction: column;
  /* border: dashed #e8d1d969;
  border-radius: 20px; */
  padding: 20px;
}

.likes-span {
  font-size: 15px;
}

/* 좋아요 버튼 */
.heart-btn:hover,
.heart-btn:active,
.heart-btn:focus {
  outline: none;
}

/* 좋아요 버튼 이미지 */
.heart-img {
  width: 45px !important;
  height: 40px !important;
}

.btn-div {
  justify-content: flex-end;
}

.detail-btns {
  font-size: 22px;
  color: #e4afc1 !important;
}

.post-detail-btn,
.create-comment-btn {
  padding: 0px;
  margin: 0px;
}

.postpage-btn {
  width: auto;
}

.post-detail-dates {
  display: flex;
  justify-content: flex-end;
}

.router-user {
  color: #e8d1d9;
}

.router-user:hover {
  text-decoration-line: none;
  color: #e8d1d9;
}

.comment-div {
  width: 100%;
  height: 100%;
}

/* 버튼 클릭시 아웃라인 삭제 */
.modify-btn:active,
.modify-btn-admin:active,
.delete-post-btn:active,
.postpage-btn:active {
  outline: none;
}

.delete-post-btn:focus {
  outline: none;
}
</style>
