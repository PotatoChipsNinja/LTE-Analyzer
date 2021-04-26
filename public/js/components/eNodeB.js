Vue.component('eNodeB', {
  data: function() {
    return {
      type: "eNodeB ID",
      options: [],
      value: "",
      result: {},
      loading: false,
      tableData: []
    }
  },
  mounted: function() {
    this.getCandidate()
  },
  methods: {
    goBack: function() {
      router.go(-1)
    },
    getCandidate: function() {
      axios.get(host + "/query/candidate", {
        params: { key: this.type === "eNodeB ID" ? 3 : 4 }
      }).then((res) => {
        this.options = res.data.candidate
      }).catch((err) => {
        console.log(err)
        this.$message.error('与服务器连接出错')
      })
    },
    change: function() {
      this.value = ""
      this.getCandidate()
    },
    confirm: function() {
      this.loading = true
      let params
      if (this.type === "eNodeB ID") {
        params = { eNodeBID: this.value }
      } else {
        params = { eNodeBName: this.value }
      }
      axios.get(host + "/query/eNodeB", {
        params: params
      }).then((res) => {
        this.result = res.data.result
      }).catch((err) => {
        console.log(err)
        this.$message.error('与服务器连接出错')
      }).then(() => {
        this.tableData = []
        for (let key in this.result) {
          this.tableData.push({item: key, value: this.result[key]})
        }
        this.loading = false
      })
    },
    save: function() {
      let blob = new Blob([JSON.stringify(this.result)], {type: "text/plain;charset=utf-8"})
      saveAs(blob, "result.txt")
    }
  },
  template: `
    <div>
      <el-page-header @back="goBack" content="基站 eNodeB 信息查询"></el-page-header>
      <el-divider></el-divider>

      <el-radio-group v-model="type" @change="change">
        <el-radio-button label="eNodeB ID"></el-radio-button>
        <el-radio-button label="eNodeB 名称"></el-radio-button>
      </el-radio-group>

      <el-select v-model="value" filterable :placeholder="'请输入或选择 ' + type" style="margin-left: 10px">
        <el-option v-for="item in options" :key="item" :label="item" :value="item">
        </el-option>
      </el-select>

      <el-button :disabled="value === ''" style="margin-left: 10px" @click="confirm" type="primary">查询</el-button>
      <el-button :disabled="tableData.length === 0" style="margin-left: 10px" @click="save" type="primary">保存</el-button>

      <el-table :data="tableData" v-loading="loading" style="margin-top: 20px; box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);">
        <el-table-column prop="item" label="键"></el-table-column>
        <el-table-column prop="value" label="值"></el-table-column>
      </el-table>
    </div>
  `
})