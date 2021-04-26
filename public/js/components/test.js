Vue.component('button-counter', {
  data: function () {
    return {
      count: 0
    }
  },
  template: '<el-button type="primary" v-on:click="count++">You clicked me {{ count }} times.</el-button>'
})

Vue.component('data-table', {
  data: function () {
    const item = {
        date: '2016-05-02',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      }
    return { tableData: Array(20).fill(item) }
  },
  template: `
    <el-table :data="tableData">
      <el-table-column prop="date" label="日期" width="140">
      </el-table-column>
      <el-table-column prop="name" label="姓名" width="120">
      </el-table-column>
      <el-table-column prop="address" label="地址">
      </el-table-column>
    </el-table>
  `
})

Vue.component('read-file', {
  data: function () {
    return {
      fileList: [],
      isOk: false
    }
  },
  /*
  computed: {
    fileList: function() {
      return this.$refs.upload.uploadFiles
    },
    isok: function() {
      if (this.$refs.upload) {
        console.log(this.$refs.upload.uploadFiles)
        return false
      } else {
        return true
      }
      
      //return false
    }
  },
  */
  methods: {
    onChange(file, fileList) {
      this.fileList = fileList
      this.isOk = (fileList.length == 1)
    },
    mysubmit() {
      let reader = new FileReader()
      reader.onload = function() {
        console.log(reader.result)
        //console.log("done")
      }
      reader.readAsText(this.fileList[0].raw)
    }
  },
  template: `
  <div>
    <el-upload action="" drag multiple :auto-upload="false" ref="upload" :on-change="onChange" :on-remove="onChange">
      <i class="el-icon-upload"></i>
      <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
      <div class="el-upload__tip" slot="tip">只能上传jpg/png文件，且不超过500kb</div>
    </el-upload>

    <el-button @click="mysubmit" :disabled="!isOk">默认按钮</el-button>
  </div>
  `
})