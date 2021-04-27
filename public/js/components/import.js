Vue.component('import', {
  data: function() {
    return {
      value: "",
      options: [
        { value: 1, label: "tbCell" },
        { value: 2, label: "tbKPI" },
        { value: 3, label: "tbPRB" },
        { value: 4, label: "tbMROData" }
      ],
      active: 0,
      file: null,
      fileSelected: false,
      finished: false,
      progress: 0,
      ws: null
    }
  },
  computed: {
    enableNext: function() {
      return (this.active === 0 && this.value != "") || (this.active === 1 && this.fileSelected)
    }
  },
  methods: {
    goBack: function() {
      router.go(-1)
    },
    next: function() {
      this.active++
      if (this.active === 2) {
        let type = this.file.name.substr(this.file.name.lastIndexOf('.')+1)
        let that = this
        this.ws = new WebSocket(wsHost + "/data/import?table=" + this.value + "&type=" + type)
        this.ws.onopen = function() {
          that.ws.send(that.file.raw)
        }
        this.ws.onmessage = function(e) {
          if (e.data === "finish") {
            that.progress = 100
            that.finished = true
            that.active = 3
            that.$notify({
              title: '导入成功',
              message: '数据表已被成功导入数据库',
              type: 'success'
            })
            that.ws.onclose = function() {}
            that.ws.close()
          } else {
            that.progress = parseInt(e.data)
          }
        }
        this.ws.onerror = function(e) {
          console.log(e)
          that.$message.error('与服务器连接出错')
        }
        this.ws.onclose = function(e) {
          console.log(e)
          that.$message.error('与服务器连接出错')
        }
      }
    },
    change: function(file, fileList) {
      this.file = file
      this.fileSelected = true
    },
    clearFile: function() {
      this.file = {}
      this.fileSelected = false
    }
  },
  template: `
    <div>
      <el-page-header @back="goBack" content="数据导入"></el-page-header>
      <el-divider></el-divider>

      <el-row type="flex" justify="center" style="margin-top: 50px">
        <el-col style="width: 70%">
          <el-steps :active="active" finish-status="success" style="margin-bottom: 12px">
            <el-step title="选择数据表"></el-step>
            <el-step title="选择文件"></el-step>
            <el-step title="导入数据"></el-step>
          </el-steps>

          <el-select v-if="active === 0" v-model="value" placeholder="请选择数据表">
            <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value">
            </el-option>
          </el-select>

          <el-upload v-if="active === 1 && !fileSelected" :on-change="change" drag action="" :limit="1" :show-file-list="false" :auto-upload="false">
            <i class="el-icon-upload"></i>
            <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
          </el-upload>

          <el-input v-if="active === 1 && fileSelected" v-model="file.name" disabled style="width: 40%; margin-right: 12px">
            <template slot="prepend">已选择</template>
          </el-input>
          <el-button v-if="active === 1 && fileSelected" style="margin-top: 12px;" @click="clearFile">重新选择</el-button>

          <el-button v-if="active < 2" :disabled="!enableNext" style="margin-top: 12px;" @click="next" type="primary">下一步</el-button>

          <div v-if="active >= 2" style="margin-right: 3rem; margin-top: 20px">
            <h3 v-if="!finished" style="font-weight: 400; color: #1f2f3d"><i class="el-icon-loading"></i> 数据导入中，请耐心等待...</h3>
            <h3 v-if="finished" style="font-weight: 400; color: #1faf3d"><i class="el-icon-circle-check"></i> 数据导入完成！</h3>
            <el-progress :text-inside="true" :stroke-width="20" :percentage="progress" status="success"></el-progress>
          </div>
        </el-col>
      </el-row>
    </div>
  `
})