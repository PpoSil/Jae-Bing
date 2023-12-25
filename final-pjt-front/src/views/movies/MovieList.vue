<template>
  <div class="movie-main">
    <div style="max-width: 370px; margin-left: auto; margin-right: 5%">
      <h1 class="font-do my-3"></h1>
      <b-row class="d-flex justify-content-end">
        <div class="mainvideo" style="margin-left: 500px">
          <div class="video-overlay"></div>
          <video muted autoplay loop>
            <source src="./Movie002.mp4" type="video/mp4" />
            <strong>Your browser does not support the video tag.</strong>
          </video>
        </div>
      </b-row>

      <b-row class="find">
        <b-col class="d-flex justify-content-end">
          <b-carousel
            id="carousel-1"
            v-model="slide"
            :interval="2000"
            controls
            indicators
            background="#101130;"
            style="text-shadow: 1px 1px 2px #333"
            @sliding-start="onSlideStart"
            @sliding-end="onSlideEnd"
            ref="carouselRef"
            fade
          >
            <b-carousel-slide
              v-for="(movie, idx) in ordered"
              :key="idx"
              img-blank-color="dark"
              img-height="480"
              style="width: auto"
            >
              <template #img>
                <div
                  class="popluar-text"
                  style="
                    background-color: #10113000;
                    color: #e8d1d9;
                    font-size: 30px;
                  "
                >
                  Movie Hit
                </div>
                <div
                  style="
                    display: flex;
                    justify-content: flex-end;
                    background-color: #e8d1d900;
                  "
                  class="slide-card-div"
                >
                  <img
                    class="d-block img-fluid"
                    :src="`https://image.tmdb.org/t/p/w185${movie.poster_path}`"
                    alt="image slot"
                    style="max-height: 480px; margin: 0px 10px 10px"
                  />
                </div>
              </template>
            </b-carousel-slide>
          </b-carousel>
        </b-col>
      </b-row>
    </div>

    <!-- 장르 선택 버튼 -->
    <div>
      <div class="d-flex justify-content-end">
        <b-dropdown class="mt-3" id="genreBtn" :text="search || '장르 선택'">
          <b-dropdown-item
            class="genreBtn-item"
            v-for="(genre, index) in genres"
            :key="index"
            @click="searchByGenre(genre)"
          >
            {{ genre }}
          </b-dropdown-item>
        </b-dropdown>
      </div>
    </div>

    <!-- 추천한 장르 토대로 랜덤 4개 추천 -->
    <div class="movie-container" v-if="login && recommend_list.length > 0">
      <h1 class="font-do my-3">Movie Recommendations For You!</h1>
      <div class="row d-flex justify-content-center">
        <MovieListItem
          v-for="(movie, idx) in recommend_list"
          :key="idx"
          :movie="movie"
          class="col-2 p-0"
        />
      </div>
    </div>

    <!-- 장르 선택시 나타나는 리스트 -->
    <div class="caro-movie">
      <h1 v-if="movies.length" class="font-do my-5">{{ search }} List</h1>
      <carousel class="custom-carousel" :perPage="8">
        <slide v-for="(movie, idx) in movies" :key="idx">
          <MovieListItem :movie="movie" class="pick" :search="search" />
        </slide>
      </carousel>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";

import MovieListItem from "@/components/movie/MovieListItem";
import { Carousel, Slide } from "vue-carousel";

export default {
  name: "MovieList",
  data: function () {
    return {
      slide: 0,
      sliding: null,
      search: "",
      i: 0,
      j: false,
      search: "액션",
      genres: [
        "액션",
        "모험",
        "애니메이션",
        "코미디",
        "범죄",
        "다큐멘터리",
        "드라마",
        "가족",
        "판타지",
        "역사",
        "공포",
        "음악",
        "미스터리",
        "로맨스",
        "SF",
        "TV 영화",
        "스릴러",
        "전쟁",
        "웨스턴",
      ],
    };
  },
  components: {
    MovieListItem,
    Carousel,
    Slide,
  },
  methods: {
    movieDetail: function (movie) {
      this.$router.push({
        name: "MovieDetail",
        params: {
          movie: movie,
        },
      });
    },
    searchByGenre(genre) {
      // console.log('찾을게~');
      this.search = genre;
      // console.log(this.search);
      // console.log(genre);
    },
    onSlideStart() {
      this.sliding = true;
    },
    onSlideEnd() {
      this.sliding = false;
    },
  },
  created: function () {
    this.i = 0;
    if (this.login === true && this.is_admin == false) {
      this.$store.dispatch("recommendMovie");
      console.log("실행");
    }
  },
  computed: {
    ...mapState([
      "login",
      "login_user",
      "is_admin",
      "movie_list",
      "ordered_movie_list",
      "recommend_list",
    ]),
    movies: function () {
      return this.movie_list.filter((movie) => {
        const genreNames = movie.genre_ids.map((id) => id.name);
        // console.log(movie.movie_no);
        // console.log(genreNames.includes(this.search));
        // console.log(movie.genre_ids.map((id) => id.name));
        // console.log(movie.genre_ids.some((id) => id.name));
        if (movie.movie_no && genreNames.includes(this.search)) {
          return movie;
        }
      });
    },
    ordered: function () {
      return this.ordered_movie_list.filter((movie) => {
        this.i++;
        if (this.i <= 8) {
          return movie;
        }
      });
    },
  },
  mounted() {
    window.scrollTo(0, 0);
    if (this.login === true && this.is_admin === false) {
      this.$store.dispatch("recommendMovie");
    }
  },
};
</script>

<style>
.carousel-caption {
  position: absolute;
  right: 15%;
  bottom: 20px;
  left: 25%;
  z-index: 10;
  padding-top: 20px;
  padding-bottom: 20px;
  color: #e8d1d9 !important;
}

/* .carousel-caption h3 {
  background-color: #101130a2 !important;
  border-radius: 20px;
  font-size: 20px;
  vertical-align: top;
} */

h1 {
  color: #e8d1d9;
}

/* 캐러셀 카드 박스 */
.slide-card-div {
  background-color: #e8d1d9;
  /* padding-bottom: 50px; */
}

/* 장르 선택 버튼 */
#genreBtn button {
  width: auto;
  height: auto;
  color: #e8d1d9;
  background-color: rgba(0, 0, 0, 0);
  border-color: rgba(0, 0, 0, 0);
  margin-right: 100px;
  font-size: 20px;
}

/* 장르 선택시 나타나는 드롭다운 메뉴 박스 */
#genreBtn ul {
  margin-right: 75px;
  background-color: #101130e8 !important;
  border: dashed #e8d1d9de;
  border-radius: 10px;
  outline: none;
}

/* 장르 선택시 나타나는 드롭다운 메뉴 박스 아이템 */
#genreBtn ul a {
  color: #e8d1d9 !important;
}

/* 장르 선택시 나타나는 드롭다운 메뉴 박스 아이템 버튼 올려놨을 때 */
#genreBtn ul a:hover {
  background-color: #e8d1d941;
}

/* 장르 선택 옆 세모 버튼 */
#genreBtn__BV_toggle_.dropdown-toggle::after {
  padding: 1px;
}

.genreDropdown {
  background-color: #e8d1d9;
}

.movie-container {
  margin: initial;
}
#genreDropdown {
  background-color: #e8d1d9;
}

.btn-secondary {
  background-color: #e8d1d9;
}
.custom-carousel .carousel-item {
  margin-right: 10px !important; /* 우측 간격 조정 */
  margin-left: 10px !important; /* 좌측 간격 조정 */
}
.pick {
  width: 200px;
}
.VueCarousel-slide {
  width: 300px !important;
  display: flex !important;
  justify-content: center !important;
}
video {
  display: flex !important;
  justify-content: end !important;
}

.movie-container {
  position: relative;
  z-index: 20;
}

.video-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(#0e0f2c, transparent, transparent, #020106);
  z-index: 10;
  pointer-events: none;
}

.caro-movie {
  position: relative;
  z-index: 15;
}

.mainvideo {
  width: 100%;
  height: 800px;
  overflow: hidden;
  margin: 0px auto;
  position: absolute;
}
.find {
  position: relative;
  z-index: 30;
}
</style>
