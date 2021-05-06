Vue.component('welcome', {
  props: ['username'],
  template: `
    <el-row type="flex" justify="center" style="top: 20%">
      <el-col :span="12">
        <el-card shadow="always" style="text-align: center">
          <el-row type="flex" justify="center" style="font-size: 6rem">
            <el-col style="height: 8rem; width: 8rem">
              <img src="/assets/bupt_logo.png" style="height: 80%; width: 80%; margin: 10%">
            </el-col>
            <el-divider direction="vertical"></el-divider>
            <el-col style="height: 8rem; width: 8rem">
              <i class="el-icon-s-marketing" style="font-size: 8rem; color: #CD5555"></i>
            </el-col>
          </el-row>
          <h1>{{ username }}，欢迎使用 LTE 网络干扰分析系统</h1>
          <a href="https://github.com/PotatoChipsNinja/TLE-Analyzer" target="_blank">
            <el-button icon="el-icon-takeaway-box" href="https://baidu.com">项目仓库</el-button>
          </a>
          <a href="mailto:shiyuhui2000@bupt.edu.cn" target="_blank">
            <el-button icon="el-icon-message">联系作者</el-button>
          </a>
        </el-card>
      </el-col>
    </el-row>
  `
})