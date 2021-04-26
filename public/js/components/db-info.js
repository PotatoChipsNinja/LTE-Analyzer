Vue.component('db-info', {
  data: function() {
    return {
      loading: true,
      info: {},
      tableData: []
    }
  },
  mounted: function() {
    let that = this
    axios.get(host + "/admin/DBInfo").then((res) => {
      this.info = res.data
    }).catch((err) => {
      console.log(err)
      that.$message.error('与服务器连接出错')
    }).then(() => {
      that.loadTable()
    })
  },
  methods: {
    goBack: function() {
      router.go(-1)
    },
    loadTable: function() {
      this.loading = true
      let descMap = {
        host: "数据库地址",
        port: "数据库端口号",
        db: "数据库名",
        username: "数据库连接用户名",
        password: "数据库连接口令",
        interactiveTimeout: "交互式连接超时时间，单位：秒",
        waitTimeout: "非交互式连接超时时间，单位：秒",
        partition: "数据库表所在的物理分区",
        queryCacheSize: "数据库缓冲区大小"
      }
      for (let key in this.info) {
        this.tableData.push({item: key, description: descMap[key], value: this.info[key]})
      }
      this.loading = false
    }
  },
  template: `
    <div>
      <el-page-header @back="goBack" content="数据库信息"></el-page-header>
      <el-divider></el-divider>
      <el-table :data="tableData" v-loading="loading" stripe style="box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);">
        <el-table-column prop="item" label="项目"></el-table-column>
        <el-table-column prop="description" label="描述"></el-table-column>
        <el-table-column prop="value" label="值"></el-table-column>
      </el-table>
    </div>
  `
})