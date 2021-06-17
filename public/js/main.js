const host = "http://localhost:3000/api"
const wsHost = "ws://localhost:3000/api"

const routes = [
  { path: '/', component: Vue.component('welcome') },
  { path: '/login', component: Vue.component('login') },
  { path: '/admin/user', component: Vue.component('user') },
  { path: '/admin/db-info', component: Vue.component('db-info') },
  { path: '/admin/db-setting', component: Vue.component('db-setting') },
  { path: '/admin/db-index', component: Vue.component('db-index') },
  { path: '/data/import', component: Vue.component('import') },
  { path: '/data/export', component: Vue.component('export') },
  { path: '/query/sector', component: Vue.component('sector') },
  { path: '/query/eNodeB', component: Vue.component('eNodeB') },
  { path: '/query/kpi', component: Vue.component('kpi') },
  { path: '/query/prb', component: Vue.component('prb') },
  { path: '/advanced/c2i', component: Vue.component('c2i') },
  { path: '/advanced/c2i3', component: Vue.component('c2i3') },
  { path: '/advanced/louvain', component: Vue.component('louvain') },
  { path: '/user/passwd', component: Vue.component('passwd') }
]

const router = new VueRouter({
  mode: 'history',
  routes: routes
})

const app = new Vue({
  el: '#app',
  router: router,
  data: {
    logged: false,
    username: "",
    isAdmin: false
  },
  created: function() {
    this.login()
  },
  methods: {
    login: function() {
      if (localStorage.getItem("username") === null) {
        if (router.currentRoute.path != '/login') {
          router.push('/login')
        }
      } else {
        this.logged = true
        this.username = localStorage.getItem("username")
        this.isAdmin = localStorage.getItem("type") === "admin"
      }
    },
    logout: function() {
      localStorage.removeItem("username")
      localStorage.removeItem("type")
      this.logged = false
      this.username = ""
      this.isAdmin = false
      router.push('/login')
    }
  }
})