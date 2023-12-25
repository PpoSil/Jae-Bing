<template>
  <div class="search-container">
    <div class="mb-5">
      <label for="search" class="mx-3" style="color: #e8d1d9; font-size: 30px">Search: </label>
      <input
        placeholder="Enter Movie Name"
        type="text"
        id="search"
        style="
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
        "
        v-model.trim="search"
        @keypress.enter="searchMovie"
      />
    </div>

    <div class="row" v-if="movies.length">
      <div class="col-3 h-50 w-100 my-3" v-for="(movie, idx) in movies" :key="idx">
        <div class="card" style="background-color: #101130; border: dashed #e8d1d969; border-radius: 10px">
          <img class="card-img-top m-0" :src="movie.poster_path" :alt="movie.title" />
          <div class="card-body">
            <h5 style="color: #e8d1d9">{{ movie.title }}</h5>
            <!-- <button @click="addMovie(movie)" class="btn btn-pink">이 영화 추가</button> -->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// const SERVER_URL = process.env.VUE_APP_SERVER_URL;
const SEARCH_URL = process.env.VUE_APP_SEARCH_URL;
const API_KEY = process.env.VUE_APP_API_KEY;

import axios from 'axios';

export default {
  name: 'MovieSearch',
  data: function () {
    return {
      search: null,
      movies: [],
      img_url: 'http://image.tmdb.org/t/p/w185',
    };
  },
  methods: {
    searchMovie: function () {
      if (this.search) {
        this.movies = [];
        axios
          .get(`${SEARCH_URL}=${API_KEY}&language=ko-KR&query=${this.search}&page=1&include_adult=false`)
          .then((res) => {
            for (const movie of res.data.results) {
              // console.log(movie)
              const temp = {
                movie_no: movie.id,
                title: movie.title,
                release_date: movie.release_date,
                poster_path: this.img_url + movie.poster_path,
                overview: movie.overview,
                genres: movie.genre_ids,
              };
              if (movie.poster_path === null) {
                temp.poster_path = '';
              }
              // console.log(temp)
              this.movies.push(temp);
            }
          })
          .catch((err) => {
            console.log(err);
          });
        this.search = null;
      }
    },
  },
  mounted() {
    window.scrollTo(0, 0);
  },
};
</script>

<style scoped>
.card-img-top {
  width: 100%;
  height: 30vw;
  object-fit: cover;
}
.search-container {
  min-height: 100vh;
  width: 100%;
  padding: 0 10%;
  background-image: url('@/moviemain.png');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

/* 왜 이벤트들이 안 먹지..? */
input:hover {
  border-color: #e8d1d9;
}

input:active {
  background-color: #e8d1d9;
}

input:focus {
  background-color: #e8d1d9;
}
</style>
