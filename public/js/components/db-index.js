Vue.component('db-index', {
  data: function() {
    return {
      indexList: [],
      loading: true,
      dialogVisible: false,
      form: {
        table: "",
        name: "",
        key: []
      },
      addLoading: false,
      options: [
        {
          value: 'tbcell',
          label: 'tbCell'
        },
        {
          value: 'tbprb',
          label: 'tbPRB'
        },
        {
          value: 'tbkpi',
          label: 'tbKPI'
        }
      ],
      keys: {
        'tbcell': ['CITY', 'SECTOR_ID', 'SECTOR_NAME', 'ENODEBID', 'ENODEB_NAME', 'EARFCN', 'PCI', 'PSS', 'SSS', 'TAC', 'VENDOR', 'LONGITUDE', 'LATITUDE', 'STYLE', 'AZIMUTH', 'HEIGHT', 'ELECTTILT', 'MECHTILT', 'TOTLETILT'],
        'tbprb': ['起始时间', '网元或基站名称', '小区描述', '小区名称'],
        'tbkpi': ['起始时间', '网元或基站名称', '小区', '小区名称', 'RRC连接建立完成次数', 'RRC连接请求次数', 'RRC建立成功率qf', 'E_RAB建立成功总次数', 'E_RAB建立尝试总次数', 'E_RAB建立成功率2', 'eNodeB触发的E_RAB异常释放总次数', '小区切换出E_RAB异常释放总次数', 'E_RAB掉线率', '无线接通率ay']
      }
    }
  },
  mounted: function() {
    this.loadList()
  },
  methods: {
    goBack: function() {
      router.go(-1)
    },
    loadList: function() {
      this.loading = true
      let that = this
      axios.get(host + "/index/getIndex").then((res) => {
        that.indexList = res.data.indexes
      }).catch((err) => {
        console.log(err)
        that.$message.error('与服务器连接出错')
      }).then(() => {
        that.loading = false
      })
    },
    del: function(row) {
      let that = this
      this.$confirm('此操作将永久删除该索引, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.loading = true
        axios.post(host + "/index/removeIndex", new URLSearchParams({
          table: row.table,
          name: row.name
        })).then((res) => {
          if (res.data.success) {
            that.$message({
              type: 'success',
              message: '删除成功!'
            })
          } else {
            that.$message.error('删除失败!')
          }
        }).catch((err) => {
          console.log(err)
          that.$message.error('与服务器连接出错')
        }).then(() => {
          that.loadList()
        })
      }).catch(() => {})
    },
    add: function() {
      if (this.form.table === "") {
        this.$message.error('请选择表名')
      } else if (this.form.name === "") {
        this.$message.error('索引名不能为空')
      } else if (this.form.key.length === 0) {
        this.$message.error('请选择键')
      } else {
        this.addLoading = true
        let that = this
        axios.post(host + "/index/addIndex", new URLSearchParams({
          table: that.form.table,
          name: that.form.name,
          key: that.form.key.join()
        })).then((res) => {
          if (res.data.success) {
            that.$message({
              type: 'success',
              message: '索引创建成功!'
            })
          } else {
            that.$message.error('索引创建失败!')
          }
        }).catch((err) => {
          console.log(err)
          that.$message.error('与服务器连接出错')
        }).then(() => {
          that.addLoading = false
          that.dialogVisible = false
          that.loadList()
        })
      }
    },
    clear: function() {
      this.form.table = ""
      this.form.name = ""
      this.form.key = []
    }
  },
  template: `
    <div>
      <el-page-header @back="goBack" content="索引管理"></el-page-header>
      <el-divider></el-divider>
      <el-button type="primary" icon="el-icon-plus" size="medium" @click="dialogVisible = true">新增索引</el-button>
      <el-button type="primary" icon="el-icon-refresh-right" size="medium" @click="loadList">刷新列表</el-button>

      <el-table :data="indexList" v-loading="loading" style="margin-top: 10px; box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);">
        <el-table-column label="表名" prop="table"></el-table-column>
        <el-table-column label="索引名" prop="name"></el-table-column>
        <el-table-column label="键">
          <template slot-scope="scope">
            <el-tag size="medium" v-for="(k, i) in scope.row.key.split(',')" :key="i" style="margin-right: 2px;">{{ k }}</el-tag>
          </template>
        </el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button size="mini" type="danger" @click="del(scope.row)">删除索引</el-button>
          </template>
        </el-table-column>
      </el-table>

      <el-dialog title="新增索引" :visible.sync="dialogVisible" @close="clear" width="40%">
        <el-form :model="form">
          <el-form-item label="表名" label-width="5rem">
            <el-select v-model="form.table" placeholder="请选择" @change="form.key = []">
              <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="索引名" label-width="5rem">
            <el-input v-model="form.name" clearable></el-input>
          </el-form-item>
          <el-form-item label="键" label-width="5rem">
            <el-select v-model="form.key" multiple placeholder="请选择">
              <el-option
                v-for="item in keys[form.table]"
                :key="item"
                :label="item"
                :value="item">
              </el-option>
            </el-select>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogVisible = false">取消</el-button>
          <el-button type="primary" @click="add" :loading="addLoading">确定</el-button>
        </div>
      </el-dialog>
    </div>
  `
})