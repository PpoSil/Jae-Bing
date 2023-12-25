<template>
  <div>
    <!-- <b-card
        v-if="!movie.poster_path.includes('#')"
        :img-src="`https://image.tmdb.org/t/p/w185${movie.poster_path}`"
        img-alt="Image"
        class="card-img my-2"
        @click="showDetail"></b-card>

      <b-card
        v-else
        img-src="https://image.tmdb.org/t/p/w185/g3gpHLUuQLGI9gRmfraSQCN1TYk.jpg"
        img-alt="Image"
        img-top
        class="my-2"
        @click="showDetail">
      </b-card> -->

    <div class="carocard" v-if="!movie.poster_path.includes('#')">
      <img class="movielistitem m-0" :src="`https://image.tmdb.org/t/p/w185${movie.poster_path}`" @click="showDetail" />
    </div>
    <div class="carocard" v-else>
      <img
        class="movielistitem"
        src="https://image.tmdb.org/t/p/w185/g3gpHLUuQLGI9gRmfraSQCN1TYk.jpg"
        @click="showDetail"
      />
    </div>

    <!-- 영화눌렀을때 이게 보이게 한다 -->
    <b-modal class="font-fixel" hide-footer v-model="show" size="xl" title="Movie Information" style="color: #e8d1d9">
      <div class="modal-content">
        <!-- ... -->
      </div>
      <!-- 영화디테일 부분 -->
      <div class="detail-box">
        <div
          class="modal-backdrop"
          :style="`background-image: url(https://image.tmdb.org/t/p/original${movie.backdrop_path})`"
        ></div>

        <div class="detail-content">
          <div class="trailer">
            <iframe
              id="player"
              type="text/html"
              width="400"
              height="225"
              :src="`http://www.youtube.com/embed/${trailerVideoId}?autoplay=1&mute=1&controls=0&cc_load_policy=1`"
              frameborder="0"
              allowfullscreen
            ></iframe>
          </div>

          <!-- Poster -->
          <div class="poster">
            <img
              :src="`https://image.tmdb.org/t/p/w185${movie.poster_path}`"
              alt="movie poster"
              v-if="!movie.poster_path.includes('#')"
            />
            <img src="https://image.tmdb.org/t/p/w185/g3gpHLUuQLGI9gRmfraSQCN1TYk.jpg" alt="movie poster" v-else />
          </div>

          <div
            class="details text-right px-2 mb-2"
            style="
              background: linear-gradient(#10113000, #10113050, #10113071, #10113071, #10113071, #10113050, #10113000);
              color: #e8d1d9;
              margin-left: 290px;
              margin-top: 50px;
              text-align: right;
            "
          >
            <!-- Title -->
            <h4 class="font-fixel mt-4">[ {{ movie.title }} ]</h4>

            <!-- Release Date -->
            <h5 class="font-fixel">Release Date: {{ movie.release_date }}</h5>

            <!-- Vote Average -->
            <h5 class="font-fixel">Vote Average: {{ movie.vote_average }}</h5>

            <!-- Adult Rating -->
            <h5 class="font-fixel" v-if="movie.adult">19세 관람가</h5>

            <!-- Overview -->
            <h5 class="font-fixel mb-2" style="text-align: left">{{ movie.overview | truncate(200, '...') }}</h5>
          </div>
        </div>
      </div>
      <br />

      <!-- 리뷰 부분 -->
      <div v-if="is_admin === false && login === true" :class="{ appear: showForm }">
        <h2 class="font-fixel" style="color: #e8d1d9">Create Review</h2>
        <div id="reviewForm">
          <!-- 리뷰 별점 부분 -->
          <div>
            <label for="rate" class="font-fixel float-left">Rate : </label>
            <p style="width: 5px; height: 5px; margin-left: 5px" class="font-fixel float-left">{{ selected_rate }}</p>
            <input type="range" min="1" max="10" step="1" v-model="selected_rate" class="justify-content-center ml-3" />
            <!-- <select id="rate" v-model="selected_rate" class="ml-1">
              <option v-for="(n, idx) in rate_options" :key="idx">{{ n }}</option>
            </select> -->

            <!-- 여기하는 중 -->
            <!-- 별점 박스 -->
            <b-input-group>
              <b-form-rating
                size="lg"
                id="rate"
                v-model="selected_rate"
                color="#e8d1d9;"
                stars="10"
                style="background-color: #10113000; border: dashed; border-color: #e8d1d969"
              ></b-form-rating>
              <b-input-group-append>
                <b-input-group-text
                  class="justify-content-center m-0 font-fixel"
                  style="
                    min-width: 3em;
                    background-color: #10113000;
                    border-style: dashed none;
                    border-color: #e8d1d969;
                    border-width: 3px;
                  "
                >
                  {{ selected_rate }}
                </b-input-group-text>
                <b-input-group-prepend>
                  <b-button
                    style="background-color: #10113000; border: dashed; border-color: #e8d1d969"
                    class="movie-detail-btn font-fixel"
                    @click="selected_rate = null"
                    >Clear</b-button
                  >
                </b-input-group-prepend>
              </b-input-group-append>
            </b-input-group>
          </div>

          <!-- 이 영화를 추천합니다 -->
          <div class="mt-3" style="color: #e8d1d9; display: flex; align-items: center">
            <label for="like" class="mr-2 font-fixel" style="font-size: 20px">Recommend</label>
            <label for="like" class="mr-2 font-fixel" id="recommend-label" style="font-size: 20px">This Movie.</label>
            <b-form-checkbox
              style="width: 20px; height: auto; margin-bottom: 8px; background-color: #10113000"
              id="like"
              checked="true"
              v-model="like"
              inline
            ></b-form-checkbox>
          </div>
          <!-- 감상평 인풋 -->
          <div class="input-group">
            <label for="content"></label>
            <textarea
              class="font-fixel form-control my-3"
              aria-label="With textarea"
              id="content"
              cols="60"
              rows="5"
              v-model.trim="content"
              placeholder="Please Leave A Comment."
              style="
                border: dashed #e8d1d969;
                border-radius: 10px;
                background-color: #10113000;
                color: #e8d1d9;
                padding: 15px;
              "
            ></textarea>
          </div>

          <!-- 리뷰 댓글 수정, 삭제 버튼  -->
          <div>
            <div class="d-flex justify-content-center">
              <button
                :class="{ appear: showAdd }"
                class="movie-detail-btn font-fixel mr-1 ml-1"
                @click="addReview(movie)"
              >
                Submit
              </button>
              <button @click="hideDetail" :class="{ appear: showAdd }" class="movie-detail-btn font-fixel mr-1 ml-1">
                Cancel
              </button>
              <button
                :class="{ appear: !showAdd }"
                class="movie-detail-btn font-fixel mr-1 ml-1"
                @click="updateReview(movie)"
              >
                Edit
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- 리뷰목록 -->
      <h2 style="color: #e8d1d9" class="font-fixel">Review List</h2>
      <hr style="border: dashed #e8d1d9; border-width: 2px; border-spacing: 10px" />
      <ul class="px-3">
        <li v-for="(review, idx) in reviews" :key="idx">
          <div v-if="review.movie.id == movie.id || review.id == movie.id">
            <div class="row review-dottedline mt-5">
              <div class="col-3" id="review-rank">
                <!-- 리뷰 별점 부분 -->
                <div>
                  <b-form-rating
                    style="width: auto; background-color: #10113000"
                    color="#DE5078"
                    inline
                    size="sm"
                    :value="review.rate | half()"
                    readonly
                    no-border
                  >
                  </b-form-rating>
                </div>
              </div>

              <div
                class="col-6 font-fixel"
                id="review-content"
                style="word-break: break-all; color: #e8d1d9; font-size: 20px"
              >
                <!-- 리뷰 내용 부분 -->
                <p>{{ review.content }}</p>
                <p>Writer : {{ review.user.username }} | {{ $moment(review.created_at).format('YYYY-MM-DD') }}</p>
              </div>

              <div
                class="col-3 font-fixel d-flex justify-content-end"
                id="review-button"
                v-if="review.user.id == login_user"
              >
                <!-- 리뷰 수정, 삭제 버튼 -->
                <button
                  style="font-size: 20px"
                  @click="updateReady(review)"
                  :class="{ appear: showAdd }"
                  class="movie-detail-btn mr-1 ml-1"
                >
                  Edit
                </button>
                <button
                  style="font-size: 20px"
                  @click="deleteReview(movie)"
                  :class="{ appear: showAdd }"
                  class="movie-detail-btn mr-1 ml-1"
                >
                  Delete
                </button>
              </div>
            </div>
          </div>
        </li>
      </ul>
    </b-modal>
  </div>
</template>

<script>
const SERVER_URL = process.env.VUE_APP_SERVER_URL;
import Vue from 'vue';
// import VueYoutube from 'vue-youtube';
import axios from 'axios';
import _ from 'lodash';
import { mapState } from 'vuex';
// Vue.use(VueYoutube);

export default {
  name: 'MovieListItem',
  props: {
    movie: Object,
  },
  // components: {
  //   'vue-youtube': VueYoutube,
  // },
  data: function () {
    return {
      selected_rate: null,
      like: false,
      content: null,
      show: false,
      showForm: false,
      showAdd: false,
      reviewId: null,
      rate_options: _.range(0, 11),
      variants: ['light', 'dark'],
      showTrailer: false,
      trailerVideoId: '',
      // playerVars: {
      //   autoplay: 1,
      //   controls: 1,
      // },
      reviews: [],
    };
  },
  methods: {
    showDetail: function () {
      // console.log('얘두');
      // console.log(this.review_list);
      this.show = true;
      const API_Key = 'AIzaSyA6w5yAn6ZwQBz_uR-iJfDl8Mj1PJ_8QtE';
      const movieTitle = this.movie.title;
      const query = 'official trailer' + movieTitle;
      this.avgRate = this.movie.rate;

      const apiUrl = `https://www.googleapis.com/youtube/v3/search?key=${API_Key}&q=${query}&part=snippet&type=video`;
      axios
        .get(`${SERVER_URL}/movies/${this.movie.id}/reviews/`)
        .then((res) => {
          // console.log(res.data, 'data');
          this.reviews = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
      axios
        .get(apiUrl)
        .then((response) => {
          const videos = response.data;
          console.log(response.request.status);
          if (response.request.status === 200) {
            // 필터링된 예고편 영상 가져오기
            this.trailerVideoId = videos.items[0].id.videoId;
            console.log(this.trailerVideoId);
          } else {
            console.log('예고편이 없습니다.');
          }
        })
        .catch((error) => {
          console.error('API 요청 중 오류 발생:', error);
        });
    },

    handlePlaying() {
      console.log('Video is playing');
    },
    hideDetail: function () {
      this.show = false;
    },
    setToken: function () {
      const token = localStorage.getItem('jwt');

      const config = {
        headers: {
          Authorization: `JWT ${token}`,
        },
      };
      return config;
    },
    addReview: function (movie) {
      const config = this.setToken();
      const reviewInfo = {
        content: this.content,
        rate: this.selected_rate,
        like: this.like,
      };
      axios
        .post(`${SERVER_URL}/movies/${movie.id}/review/`, reviewInfo, config)
        .then((res) => {
          // console.log(res.data)
          const reviewerInfo = {
            movie_id: this.movie.id,
            reviewer_id: res.data.user.id,
          };
          this.$store.state.review_list.unshift(res.data);
          let acount = 0;
          for (const review of this.review_list) {
            if (review.movie.id == this.movie.id) {
              acount++;
            }
          }
          console.log('리뷰수:', acount);
          this.total[this.movie.id] += this.selected_rate;
          console.log('총점수:', this.total[this.movie.id]);
          this.$store.state.movie_list[this.movie.id - 1].rate = this.total[this.movie.id] / acount;
          console.log('평균:', this.$store.state.movie_list[this.movie.id - 1].rate);
          if (this.like) {
            this.$store.state.movie_list[this.movie.id - 1].vote_count += 1;
          }
          this.$store.dispatch('checkReviewer', reviewerInfo);
          this.$store.dispatch('recommendMovie');
          this.content = null;
          this.selected_rate = null;
          this.like = false;
          this.showForm = true;
          this.showDetail();
        })
        .catch((err) => {
          console.log(err);
        });
    },
    deleteReview: function (movie) {
      const config = this.setToken();
      if (confirm('이 리뷰를 삭제하겠습니까?')) {
        axios
          .delete(`${SERVER_URL}/movies/${movie.id}/review/update/`, config)
          .then((res) => {
            console.log(res);
            const idx1 = this.review_list.findIndex((review) => {
              return review.id === movie.id;
            });
            this.$store.state.review_list.splice(idx1, 1);
            let dcount = 0;
            for (const review of this.review_list) {
              if (review.movie.id === this.movie.id) {
                dcount++;
              }
            }
            if (dcount <= 0) {
              dcount = 1;
            }
            console.log('리뷰수:', dcount);

            const idx2 = this.user_movie[this.login_user].findIndex((user) => {
              return user.id === movie.id;
            });
            this.$store.state.user_movie[this.login_user].splice(idx2, 1);

            this.total[this.movie.id] -= res.data.rate;
            console.log('총점수:', this.total[this.movie.id]);

            this.$store.state.movie_list[this.movie.id - 1].rate = this.total[this.movie.id] / dcount;
            console.log('평균', this.$store.state.movie_list[this.movie.id - 1].rate);

            if (res.data.like) {
              this.$store.state.movie_list[this.movie.id - 1].vote_count -= 1;
            }

            this.showForm = false;
            this.showAdd = false;
            this.showDetail();
          })
          .catch((err) => {
            console.log(err);
          });
        axios
          .get(`${SERVER_URL}/movies/${this.movie.id}/reviews/`)
          .then((res) => {
            // console.log(res.data, 'data');
            this.reviews = res.data;
          })
          .catch((err) => {
            console.log(err);
          });
      }
    },
    updateReady: function (review) {
      this.content = review.content;
      this.like = review.like;
      this.selected_rate = review.rate;
      this.showForm = false;
      this.showAdd = true;
      this.reviewId = review.id;
    },

    updateReview: function (movie) {
      const config = this.setToken();
      const reviewInfo = {
        id: this.reviewId,
        user: this.login_user,
        movie: movie.id,
        content: this.content,
        rate: this.selected_rate,
        like: this.like,
      };
      axios
        .put(`${SERVER_URL}/movies/${movie.id}/review/update/`, reviewInfo, config)
        .then((res) => {
          this.content = null;
          this.like = false;
          this.selected_rate = null;
          this.showForm = true;
          this.showAdd = false;
          this.reviewId = null;
          console.log(res);
          const idx = this.review_list.findIndex((review) => {
            return review.id === res.data.id;
          });
          this.total[this.movie.id] -= this.$store.state.review_list[idx].rate;
          this.$store.state.review_list[idx].content = res.data.content;
          this.$store.state.review_list[idx].rate = res.data.rate;

          if (this.$store.state.review_list[idx].like) {
            if (res.data.like === false) {
              this.$store.state.movie_list[this.movie.id - 1].vote_count -= 1;
            }
          } else {
            if (res.data.like === true) {
              this.$store.state.movie_list[this.movie.id - 1].vote_count += 1;
            }
          }

          this.$store.state.review_list[idx].like = res.data.like;

          let ucount = 0;
          for (const review of this.review_list) {
            if (review.movie.id === this.movie.id) {
              ucount++;
            }
          }
          console.log('리뷰수:', ucount);

          this.total[this.movie.id] += res.data.rate;
          console.log('총점수:', this.total[this.movie.id]);

          this.$store.state.movie_list[this.movie.id - 1].rate = this.total[this.movie.id] / ucount;
          console.log('평균', this.$store.state.movie_list[this.movie.id - 1].rate);
          this.showDetail();
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  created: function () {
    if (this.user_movie[this.login_user] && this.user_movie[this.login_user].includes(this.movie.id)) {
      this.showForm = true;
      console.log(this.showForm, '보여줘');
    }
    this.avgRate = this.movie.rate;
  },
  computed: {
    ...mapState(['login', 'login_user', 'is_admin', 'user_movie', 'movie_list', 'review_list', 'total']),
  },
};
</script>

<style scoped>
@font-face {
  font-family: 'NeoDunggeunmoPro-Regular';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2302@1.0/NeoDunggeunmoPro-Regular.woff2')
    format('woff2');
  font-weight: normal;
  font-style: normal;
}

/* 픽셀체 */
.font-fixel {
  font-family: 'NeoDunggeunmoPro-Regular';
  color: #e8d1d9;
}
/* 디테일부분 모든 버튼 */
.movie-detail-btn:hover {
  color: #e293af;
  outline: none;
}
.movie-detail-btn:active,
.movie-detail-btn:focus {
  color: #e293af;
  outline: none;
}

.card-img {
  height: auto !important;
}

.appear {
  display: none;
}

.detail-box {
  position: relative;
  height: 500px;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}

.detail-content {
  /* position: relative;
  z-index: 1;
  display: flex;
  height: 100%; */
  position: absolute;
  top: 50%;
  left: 0;
  right: 0;
  transform: translateY(-50%);
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  z-index: 2;
}
.modal-backdrop {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.6);
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  z-index: 0 !important;
  filter: blur(3px);
}

.poster {
  flex: 0 0 300px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 20px;
}

.poster img {
  width: 100%;
  height: 120%;
  border-radius: 4px;
}

.details {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  align-self: flex-end;
  position: absolute;
}

.modal-xl {
  max-width: 1000px;
}
/* .trailer-container {
  position: relative;
  padding-bottom: 56.25%;
  overflow: hidden;
  max-width: 100%;
  flex-grow: 1;
}
.trailer-container embed {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
} */

.appear {
  display: none;
}

.review-dottedline {
  border-bottom: dashed #e8d1d9;
}

.card {
  background-color: #826592 !important;
  border: none !important;
}

.img-top {
  border-bottom-left-radius: 0;
  border-bottom-right-radius: 0;
}

iframe {
  pointer-events: none;
}

.trailer {
  position: absolute;
  top: 20px; /* Adjust the top position as needed */
  right: 20px; /* Adjust the right position as needed */
  width: 400px !important; /* Adjust the width as needed */
  height: 225px !important; /* Adjust the height as needed */
  object-fit: cover;
  z-index: 1;
}

.movielistitem {
  width: auto;
  height: auto;
}
.carocard {
  width: 200px !important;
}

/deep/ .modal > .modal-dialog > .modal-content {
  background: #1c1e4900;
  border: none;
}
/deep/ .close,
/deep/ .modal > .modal-dialog > .modal-content > .modal-header > .modal-title > .close,
/deep/ .modal > .modal-dialog > .modal-content > .modal-header {
  color: #e8d1d9 !important;
  font-family: 'NeoDunggeunmoPro-Regular';
}
/deep/ .modal {
  background: linear-gradient(#101130, #1c1e4900, #1c1e4900, #101130);
}

input,
range {
  accent-color: #e8d1d9;
}

/* select {
  border: dashed 1.5px;
  background-color: #1c1e49;
  border-radius: 5px;
  color:#e8d1d9;
} */

.input-group-prepend button {
  background-color: #1c1e49;
  width: auto;
  height: auto;
}
</style>
