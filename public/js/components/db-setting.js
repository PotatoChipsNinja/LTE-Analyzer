Vue.component('db-setting', {
  data: function() {
    return {
      interactiveTimeout: 0,
      waitTimeout: 0,
      queryCacheSize: "",
      loadingTimeout: false,
      loadingCache: false
    }
  },
  mounted: function() {
    this.loadSetting()
  },
  methods: {
    goBack: function() {
      router.go(-1)
    },
    loadSetting: function() {
      axios.get(host + "/admin/DBInfo").then((res) => {
        this.interactiveTimeout = res.data.interactiveTimeout
        this.waitTimeout = res.data.waitTimeout
        this.queryCacheSize = res.data.queryCacheSize
      }).catch((err) => {
        console.log(err)
        this.$message.error('与服务器连接出错')
      })
    },
    setTimeout: function() {
      this.loadingTimeout = true
      axios.post(host + "/admin/setTimeout", new URLSearchParams({
        interactiveTimeout: this.interactiveTimeout,
        waitTimeout: this.waitTimeout
      })).then((res) => {
        if (res.data.success) {
          this.$message({
            type: 'success',
            message: '修改成功!'
          })
        } else {
          this.$message.error('修改失败!')
        }
      }).catch((err) => {
        console.log(err)
        this.$message.error('与服务器连接出错')
      }).then(() => {
        this.loadingTimeout = false
        this.loadSetting()
      })
    },
    setCache: function() {
      this.loadingCache = true
      axios.post(host + "/admin/setCache", new URLSearchParams({
        queryCacheSize: this.queryCacheSize
      })).then((res) => {
        if (res.data.success) {
          this.$message({
            type: 'success',
            message: '修改成功!'
          })
        } else {
          this.$message.error('修改失败!')
        }
      }).catch((err) => {
        console.log(err)
        this.$message.error('与服务器连接出错')
      }).then(() => {
        this.loadingCache = false
        this.loadSetting()
      })
    }
  },
  template: `
    <div>
      <el-page-header @back="goBack" content="数据库设置"></el-page-header>
      <el-divider></el-divider>

      <el-card class="box-card timeout" style="width: 50%; margin: 30px" shadow="hover">
        <div slot="header" class="clearfix">
          <span>数据库连接超时时间</span>
          <el-button type="primary" icon="el-icon-s-promotion" @click="setTimeout" :loading="loadingTimeout" style="float: right; margin-top: -5px; padding: 10px 12px">应用</el-button>
        </div>
        <el-input v-model="interactiveTimeout" style="margin: 5px;">
          <template slot="prepend">交互式连接超时时间</template>
          <template slot="append">秒</template>
        </el-input>
        <el-input v-model="waitTimeout" style="margin: 5px;">
          <template slot="prepend">非交互式连接超时时间</template>
          <template slot="append">秒</template>
        </el-input>
      </el-card>

      <el-card class="box-card" style="width: 50%; margin: 30px" shadow="hover">
        <div slot="header" class="clearfix">
          <span>数据库缓冲区大小</span>
          <el-button type="primary" icon="el-icon-s-promotion" @click="setCache" :loading="loadingCache" style="float: right; margin-top: -5px; padding: 10px 12px">应用</el-button>
        </div>
        <el-input v-model="queryCacheSize" style="margin: 5px;">
          <template slot="prepend">数据库缓冲区大小</template>
        </el-input>
      </el-card>
    </div>
  `
})