Vue.component('sector', {
  data: function() {
    return {}
  },
  methods: {
    goBack: function() {
      router.go(-1)
    }
  },
  template: `
    <div>
      <el-page-header @back="goBack" content="小区配置信息查询"></el-page-header>
      <el-divider></el-divider>
    </div>
  `
})