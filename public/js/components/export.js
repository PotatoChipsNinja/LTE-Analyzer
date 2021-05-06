Vue.component('export', {
  data: function() {
    return {
      value: "",
      type: "",
      options: [
        { value: 1, label: "tbCell" },
        { value: 2, label: "tbKPI" },
        { value: 3, label: "tbPRB" },
        { value: 4, label: "tbPRBnew" },
        { value: 5, label: "tbMROData" }
      ],
      typeOptions: ["xlsx", "csv"]
    }
  },
  methods: {
    goBack: function() {
      router.go(-1)
    },
    confirm: function() {
      axios.get(host + "/data/export", {
        params: { table: this.value, type: this.type }
      }).then((res) => {
        window.open(res.data.url)
        this.$notify.info({
          title: '开始下载',
          message: '导出的数据表已开始下载'
        })
      }).catch((err) => {
        console.log(err)
        this.$message.error('与服务器连接出错')
      })
    }
  },
  template: `
    <div>
      <el-page-header @back="goBack" content="数据导出"></el-page-header>
      <el-divider></el-divider>

      <el-select v-model="value" placeholder="请选择要导出的数据表" style="margin-left: 20px; margin-top: 12px">
        <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value">
        </el-option>
      </el-select>

      <el-select v-model="type" placeholder="请选择要导出的文件格式" style="margin-top: 12px">
        <el-option v-for="item in typeOptions" :key="item" :label="item" :value="item">
        </el-option>
      </el-select>

      <el-button :disabled="value === '' || type === ''" style="margin-left: 10px; margin-top: 12px" @click="confirm" type="primary">导出</el-button>
    </div>
  `
})