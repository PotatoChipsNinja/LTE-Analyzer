Vue.component('user', {
  data: function() {
    return {
      userList: [],
      loading: true,
      dialogVisible: false,
      form: {
        username: "",
        password: "",
        repeat: ""
      },
      addLoading: false
    }
  },
  mounted: function() {
    this.loadList()
  },
  methods: {
    loadList: function() {
      this.loading = true
      let that = this
      axios.get(host + "/admin/userList").then((res) => {
        that.userList = res.data.users
      }).catch((err) => {
        console.log(err)
        that.$message.error('与服务器连接出错')
      }).then(() => {
        that.loading = false
      })
    },
    del: function(row) {
      let that = this
      this.$confirm('此操作将永久删除该用户, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.loading = true
        axios.post(host + "/admin/removeUser", new URLSearchParams({
          username: row.username
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
      if (this.form.username === "") {
        this.$message.error('用户名不能为空')
      } else if (this.form.password != this.form.repeat) {
        this.$message.error('两次输入的密码不一致')
      } else if (this.form.password === "") {
        this.$message.error('密码不能为空')
      } else {
        this.addLoading = true
        let that = this
        axios.post(host + "/admin/createUser", new URLSearchParams({
          username: that.form.username,
          password: that.form.password
        })).then((res) => {
          if (res.data.success) {
            that.$message({
              type: 'success',
              message: '用户创建成功!'
            })
          } else {
            that.$message.error('用户创建失败!')
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
      this.form.username = ""
      this.form.password = ""
      this.form.repeat = ""
    },
    goBack: function() {
      router.go(-1)
    }
  },
  template: `
    <div>
      <el-page-header @back="goBack" content="用户管理"></el-page-header>
      <el-divider></el-divider>
      <el-button type="primary" icon="el-icon-plus" size="medium" @click="dialogVisible = true">新增普通用户</el-button>
      <el-button type="primary" icon="el-icon-refresh-right" size="medium" @click="loadList">刷新列表</el-button>

      <el-table :data="userList" v-loading="loading" style="margin-top: 10px; box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);">
        <el-table-column label="创建日期">
          <template slot-scope="scope">
            <i class="el-icon-time"></i>
            <span style="margin-left: 10px">{{ scope.row.time }}</span>
          </template>
        </el-table-column>
        <el-table-column label="用户名">
          <template slot-scope="scope">
            <el-tag size="medium">{{ scope.row.username }}</el-tag>
          </template>
        </el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button size="mini" type="danger" @click="del(scope.row)">删除用户</el-button>
          </template>
        </el-table-column>
      </el-table>

      <el-dialog title="新增普通用户" :visible.sync="dialogVisible" @close="clear" width="40%">
        <el-form :model="form">
          <el-form-item label="用户名" label-width="5rem">
            <el-input v-model="form.username" clearable></el-input>
          </el-form-item>
          <el-form-item label="密码" label-width="5rem">
            <el-input v-model="form.password" show-password></el-input>
          </el-form-item>
          <el-form-item label="重复密码" label-width="5rem">
            <el-input v-model="form.repeat" show-password></el-input>
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