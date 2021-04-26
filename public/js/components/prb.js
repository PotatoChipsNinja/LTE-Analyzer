Vue.component('prb', {
  data: function() {
    return {
      sectorOptions: [],
      prbOptions: Array.from({length: 100}, (v, k) => k),
      sectorValue: "",
      prbValue: "",
      startDate: null,
      startTime: null,
      endDate: null,
      endTime: null,
      pickerOptions: {
        disabledDate: function(date) {
          return !(date.getFullYear() == 2020
            && date.getMonth() == 6
            && date.getDate() >= 17
            && date.getDate() <= 19)
        }
      },
      result: [],
      chart: null,
      chartOption: {}
    }
  },
  computed: {
    timeValid: function() {
      if (this.startDate && this.startTime && this.endDate && this.endTime) {
        if (this.startDate.getDate() < this.endDate.getDate()) {
          return true
        } else if (this.startDate.getDate() == this.endDate.getDate()) {
          return parseInt(this.startTime.substr(0, 2)) <= parseInt(this.endTime.substr(0, 2))
        }
      }
      return false
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
        params: { key: 7 }
      }).then((res) => {
        this.sectorOptions = res.data.candidate
      }).catch((err) => {
        console.log(err)
        this.$message.error('与服务器连接出错')
      })
    },
    confirm: function() {
      axios.get(host + "/query/prb", {
        params: {
          name: this.sectorValue,
          start: "" + this.startDate.getDate() + "-" + this.startTime.substr(0, 2),
          end: "" + this.endDate.getDate() + "-" + this.endTime.substr(0, 2),
          prb: this.prbValue
        }
      }).then((res) => {
        this.result = res.data.value
        this.updateChart()
        this.draw()
      }).catch((err) => {
        console.log(err)
        this.$message.error('与服务器连接出错')
      })
    },
    save: function() {
      let blob = new Blob([JSON.stringify(this.result)], {type: "text/plain;charset=utf-8"})
      saveAs(blob, "result.txt")
    },
    updateChart: function() {
      let xAxisData = []
      let date = this.startDate.getDate()
      let hour = parseInt(this.startTime.substr(0, 2))
      while (date < this.endDate.getDate() || (date == this.endDate.getDate() && hour <= parseInt(this.endTime.substr(0, 2)))) {
        xAxisData.push(date + "日" + hour + "时")
        if (hour == 23) {
          date++
          hour = 0
        } else {
          hour++
        }
      }
      this.chartOption = {
        title: {
          text: "第 " + this.prbValue + " 个 PRB 上检测到的干扰噪声随时间变化图",
          x: 'center'
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'cross',
            crossStyle: {
              color: '#999'
            }
          }
        },
        toolbox: {
          feature: {
            magicType: {show: true, type: ['line', 'bar']},
            saveAsImage: {show: true}
          }
        },
        xAxis: [
          {
            type: 'category',
            data: xAxisData,
            axisPointer: {
              type: 'shadow'
            }
          }
        ],
        yAxis: {
          type: 'value',
          min: -120,
          max: -90,
          axisLabel: {
            formatter: '{value} dBm'
          }
        },
        series: [{
            name: '干扰噪声',
            type: 'bar',
            data: this.result
        }]
      }
    },
    draw: function() {
      this.chart = echarts.init(this.$refs.chart)
      this.chart.setOption(this.chartOption)
    }
  },
  template: `
    <div>
      <el-page-header @back="goBack" content="PRB 信息统计与查询"></el-page-header>
      <el-divider></el-divider>

      <el-row style="margin: 5px 0">
        <el-tag style="width: 5rem; text-align: center">小区名称</el-tag>
        <el-select v-model="sectorValue" filterable placeholder="请输入或选择小区名称" style="width: 12rem">
          <el-option v-for="item in sectorOptions" :key="item" :label="item" :value="item">
          </el-option>
        </el-select>
      </el-row>

      <el-row style="margin: 5px 0">
        <el-tag style="width: 5rem; text-align: center">PRB 序号</el-tag>
        <el-select v-model="prbValue" filterable placeholder="请输入或选择 PRB 序号" style="width: 12.5rem">
          <el-option v-for="item in prbOptions" :key="item" :label="item" :value="item">
          </el-option>
        </el-select>
      </el-row>

      <el-row style="margin: 5px 0">
        <el-tag style="width: 5rem; text-align: center">起始时间</el-tag>
        <el-date-picker v-model="startDate" placeholder="请选择开始日期" :default-value="new Date('2020-07-17')" :picker-options="pickerOptions" type="date" style="width: 10rem">
        </el-date-picker>
        <el-time-select v-model="startTime" placeholder="请选择开始时间" :picker-options="{start:'00:00',step:'01:00',end:'24:00'}" style="width: 10rem">
        </el-time-select>
      </el-row>

      <el-row style="margin: 5px 0">
        <el-tag style="width: 5rem; text-align: center">结束时间</el-tag>
        <el-date-picker v-model="endDate" placeholder="请选择结束日期" :default-value="new Date('2020-07-17')" :picker-options="pickerOptions" type="date" style="width: 10rem">
        </el-date-picker>
        <el-time-select v-model="endTime" placeholder="请选择结束时间" :picker-options="{start:'00:00',step:'01:00',end:'24:00'}" style="width: 10rem">
        </el-time-select>
      </el-row>

      <el-button :disabled="sectorValue === '' || prbValue === '' || !timeValid" @click="confirm" type="primary">查询</el-button>
      <el-button :disabled="result.length === 0" @click="save" type="primary" style="margin-left: 0">保存数据</el-button>

      <div ref="chart" style="height: 22rem; margin-top: 30px"></div>
    </div>
  `
})