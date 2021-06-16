Vue.component('c2i', {
  data: function() {
    return {
      result: [],
      search: ''
    }
  },
  mounted: function() {
    this.getTable()
  },
  methods: {
    goBack: function() {
      router.go(-1)
    },
    getTable: function() {
      axios.get(host + "/advanced/c2i").then((res) => {
        this.result = res.data.result
      }).catch((err) => {
        console.log(err)
        this.$message.error('与服务器连接出错')
      })
    }
  },
  template: `
    <div>
      <el-page-header @back="goBack" content="主邻小区 C2I 干扰分析"></el-page-header>
      <el-divider></el-divider>
      <el-table
        stripe
        :data="result.filter(data => !search || data.servingSector.includes(search) || data.interfereringSector.includes(search))"
        style="width: 100%; box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);"
      >
        <el-table-column>
          <template slot="header" slot-scope="scope">
            <el-input v-model="search" placeholder="筛选小区 ID" clearable />
          </template>
          <el-table-column
            prop="servingSector"
            label="主小区 ID"
            sortable
            align="center">
          </el-table-column>
          <el-table-column
            prop="interfereringSector"
            label="邻小区 ID"
            sortable
            align="center">
          </el-table-column>
        </el-table-column>
        <el-table-column
          prop="mean"
          label="主邻小区 RSRP 差值的均值"
          sortable
          align="center">
        </el-table-column>
        <el-table-column
          prop="std"
          label="主邻小区 RSRP 差值的标准差"
          sortable
          align="center">
        </el-table-column>
        <el-table-column
          prop="diff9"
          label="主邻小区 RSRP 差值小于 9 的概率"
          sortable
          align="center">
        </el-table-column>
        <el-table-column
          prop="abs6"
          label="主邻小区 RSRP 差值绝对值小于 6 的概率"
          sortable
          align="center">
        </el-table-column>
      </el-table>
    </div>
  `
})