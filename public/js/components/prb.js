Vue.component('prb', {
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
      <el-page-header @back="goBack" content="PRB信息统计与查询"></el-page-header>
      <el-divider></el-divider>
    </div>
  `
})