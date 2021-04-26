Vue.component('welcome', {
  props: ['username'],
  template: `
    <h1>{{ username }}，欢迎使用系统</h1>
  `
})