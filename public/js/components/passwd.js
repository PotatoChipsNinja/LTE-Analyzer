Vue.component('passwd', {
  props: ['username', 'isAdmin'],
  data: function() {
    return {
      loading: false,
      oldPasswd: "",
      newPasswd: "",
      repeat: ""
    }
  },
  methods: {
    goBack: function() {
      router.go(-1)
    },
    passwd: function() {
      if (this.newPasswd != this.repeat) {
        this.$message.error('两次输入的密码不一致')
      } else if (this.newPasswd === "") {
        this.$message.error('密码不能为空')
      } else {
        this.loading = true
        let type = this.isAdmin ? "admin" : "user"
        let url = host + "/" + type + "/passwd"
        axios.post(url, new URLSearchParams({
          username: this.username,
          oldPasswd: this.oldPasswd,
          newPasswd: this.newPasswd
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
          this.loading = false
          this.oldPasswd = ""
          this.newPasswd = ""
          this.repeat = ""
        })
      }
    }
  },
  template: `
    <div>
      <el-page-header @back="goBack" content="修改密码"></el-page-header>
      <el-divider></el-divider>

      <el-card class="box-card passwd" style="width: 50%; margin: 30px" shadow="hover">
        <div slot="header" class="clearfix">
          <span>修改密码</span>
          <el-button type="primary" icon="el-icon-s-promotion" @click="passwd" :loading="loading" style="float: right; margin-top: -5px; padding: 10px 12px">应用</el-button>
        </div>
        <el-input placeholder="请输入当前密码" v-model="oldPasswd" show-password style="margin: 5px;">
          <template slot="prepend">原密码</template>
        </el-input>
        <el-input placeholder="请设置一个新密码" v-model="newPasswd" show-password style="margin: 5px;">
          <template slot="prepend">新密码</template>
        </el-input>
        <el-input placeholder="请再次输入新密码" v-model="repeat" show-password style="margin: 5px;">
          <template slot="prepend">重复新密码</template>
        </el-input>
      </el-card>
    </div>
  `
})