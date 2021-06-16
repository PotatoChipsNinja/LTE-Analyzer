Vue.component('c2i3', {
  data: function() {
    return {
      result: [],
      search: '',
      x: 50,
      loading: false
    }
  },
  methods: {
    goBack: function() {
      router.go(-1)
    },
    confirm: function() {
      this.result = []
      this.search = ''
      this.loading = true
      axios.get(host + "/advanced/c2i3", {
        params: {
          x: this.x / 100
        }
      }).then((res) => {
        this.result = res.data.result
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
      <el-page-header @back="goBack" content="重叠覆盖干扰小区三元组分析"></el-page-header>
      <el-divider></el-divider>

      <el-row type="flex" align="middle" style="margin: 5px 0">
        <el-tag style="width: 5rem; text-align: center">阈值 x</el-tag>
        <el-slider
          v-model="x"
          show-input
          style="width: 24rem; margin-left: 10px"
        >
        </el-slider>
        <el-button style="margin-left: 10px" @click="confirm" type="primary" :loading="loading">分析</el-button>
      </el-row>

      <el-table
        stripe
        :data="result.filter(data => !search || data[0].includes(search) || data[1].includes(search) || data[2].includes(search))"
        style="width: 100%; box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);"
      >
        <el-table-column>
          <template slot="header" slot-scope="scope">
            <el-input v-model="search" placeholder="筛选小区 ID" clearable />
          </template>
          <el-table-column
            prop="0"
            label="小区一 ID"
            sortable
            align="center">
          </el-table-column>
          <el-table-column
            prop="1"
            label="小区二 ID"
            sortable
            align="center">
          </el-table-column>
          <el-table-column
            prop="2"
            label="小区三 ID"
            sortable
            align="center">
          </el-table-column>
        </el-table-column>
      </el-table>
    </div>
  `
})