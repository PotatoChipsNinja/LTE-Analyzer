Vue.component('louvain', {
  data: function() {
    return {
      x: 20.0,
      img: '',
      loading: false
    }
  },
  methods: {
    goBack: function() {
      router.go(-1)
    },
    confirm: function() {
      this.img = ''
      this.loading = true
      axios.get(host + "/advanced/louvain", {
        params: {
          x: this.x
        }
      }).then((res) => {
        this.img = res.data.img
      }).catch((err) => {
        console.log(err)
        this.$message.error('与服务器连接出错')
      }).then(() => {
        this.loading = false
      })
    }
  },
  template: `
    <div>
      <el-page-header @back="goBack" content="网络干扰结构分析"></el-page-header>
      <el-divider></el-divider>

      <el-row type="flex" align="middle" style="margin: 5px 0">
        <el-tag style="width: 8rem; text-align: center">边权最小显示阈值</el-tag>
        <el-input-number v-model="x" :precision="2" :step="1" :min="0" style="margin-left: 10px"></el-input-number>
        <el-button style="margin-left: 10px" @click="confirm" type="primary" :loading="loading">分析</el-button>
      </el-row>

      <el-image v-show="img" :src="img"></el-image>
    </div>
  `
})