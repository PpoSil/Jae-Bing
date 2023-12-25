import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import VueMoment from 'vue-moment';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue';
import VModal from 'vue-js-modal';

Vue.use(BootstrapVue);
Vue.use(IconsPlugin);
Vue.use(VModal);

Vue.config.productionTip = false;
Vue.use(VueMoment);

const truncate = function (text, length, clamp) {
  clamp = clamp || '...';
  const node = document.createElement('div');
  node.innerHTML = text;
  const content = node.textContent;
  return content.length > length ? content.slice(0, length) + clamp : content;
};
Vue.filter('truncate', truncate);

const halfStar = function (rate) {
  return rate / 2;
};
Vue.filter('half', halfStar);

// 로그인 사용자 정보 가져오기
const username = localStorage.getItem('username');
const jwt = localStorage.getItem('jwt');
const login_user = Number(localStorage.getItem('login_user'));
const is_admin = JSON.parse(localStorage.getItem('is_admin'));
const user_movie = JSON.parse(localStorage.getItem('user_movie'));

if (username && jwt) {
  store.dispatch('login', { username, jwt, login_user, user_movie, is_admin });
}

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
