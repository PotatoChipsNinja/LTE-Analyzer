Vue.component('login', {
  props: ['logged'],
  data: function() {
    return {
      username: "",
      password: "",
      tab: "0"
    }
  },
  created: function() {
    if (this.logged) {
      router.push('/')
    }
  },
  methods: {
    login: function() {
      let that = this
      if (this.username === "") {
        this.$message.error('用户名不能为空')
      } else if (this.password === "") {
        this.$message.error('密码不能为空')
      } else {
        let type = this.tab == "0" ? "admin" : "user"
        let url = host + "/" + type + "/login"
        axios.post(url, new URLSearchParams({
          username: this.username,
          password: this.password
        })).then((res) => {
          if (res.data.success) {
            that.$notify({
              title: '登录成功',
              message: '欢迎回到 LTE 网络干扰分析系统',
              type: 'success'
            })
            localStorage.setItem("username", that.username)
            localStorage.setItem("type", type)
            that.$emit('login')
            router.push('/')
          } else {
            that.$message.error('用户名或密码错误')
          }
        }).catch((err) => {
          console.log(err)
          that.$message.error('与服务器连接出错')
        })
      }
    }
  },
  template: `
    <el-row type="flex" justify="center" style="margin-top: 5%;">
        <el-tabs type="border-card" style="text-align: center; width: 32%" v-model="tab" class="login">
          <el-tab-pane label="管理员登录" style="padding: 10px 30px;">
            <el-input placeholder="请输入用户名" v-model="username" clearable style="margin: 5px;">
              <template slot="prepend">用户名</template>
            </el-input>
            <el-input placeholder="请输入密码" v-model="password" show-password style="margin: 5px;">
              <template slot="prepend">密码</template>
            </el-input>
            <el-button type="primary" @click="login" style="margin: 5px;">登录</el-button>
          </el-tab-pane>
          <el-tab-pane label="普通用户登录" style="padding: 10px 30px;">
            <el-input placeholder="请输入用户名" v-model="username" clearable style="margin: 5px;">
              <template slot="prepend">用户名</template>
            </el-input>
            <el-input placeholder="请输入密码" v-model="password" show-password style="margin: 5px;">
              <template slot="prepend">密码</template>
            </el-input>
            <el-button type="primary" @click="login" style="margin: 5px;">登录</el-button>
          </el-tab-pane>
        </el-tabs>
    </el-row>
  `
})