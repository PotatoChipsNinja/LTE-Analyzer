Vue.component('kpi', {
  data: function() {
    return {
      sectorOptions: [],
      attrOptions: [],
      sectorValue: "",
      attrValue: "",
      dateValue: "",
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
  mounted: function() {
    this.getCandidate()
  },
  methods: {
    goBack: function() {
      router.go(-1)
    },
    getCandidate: function() {
      for (let i = 5; i <= 6; i++) {
        axios.get(host + "/query/candidate", {
          params: { key: i }
        }).then((res) => {
          if (i == 5) {
            this.sectorOptions = res.data.candidate
          } else {
            this.attrOptions = res.data.candidate
          }
        }).catch((err) => {
          console.log(err)
          this.$message.error('与服务器连接出错')
        })
      }
    },
    confirm: function() {
      axios.get(host + "/query/kpi", {
        params: {
          name: this.sectorValue,
          start: this.dateValue[0].getDate(),
          end: this.dateValue[1].getDate(),
          attribute: this.attrValue
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
      for (let i = this.dateValue[0].getDate(); i <= this.dateValue[1].getDate(); i++) {
        xAxisData.push(i + "日")
      }
      this.chartOption = {
        title: {
          text: this.attrValue + " 随时间变化图",
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
          type: 'value'
        },
        series: [{
            name: this.attrValue,
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
      <el-page-header @back="goBack" content="小区 KPI 指标信息查询"></el-page-header>
      <el-divider></el-divider>

      <el-select v-model="sectorValue" filterable placeholder="请输入或选择小区名称" style="width: 12rem">
        <el-option v-for="item in sectorOptions" :key="item" :label="item" :value="item">
        </el-option>
      </el-select>

      <el-select v-model="attrValue" filterable placeholder="请输入或选择属性" style="width: 10rem">
        <el-option v-for="item in attrOptions" :key="item" :label="item" :value="item">
        </el-option>
      </el-select>

      <el-date-picker v-model="dateValue" :default-value="new Date('2020-07-17')" :picker-options="pickerOptions" type="daterange" range-separator="至" start-placeholder="开始日期" end-placeholder="结束日期">
      </el-date-picker>

      <el-button :disabled="sectorValue === '' || attrValue === '' || !dateValue" @click="confirm" type="primary">查询</el-button>
      <el-button :disabled="result.length === 0" @click="save" type="primary" style="margin-left: 0">保存数据</el-button>

      <div ref="chart" style="height: 22rem; width: 32rem; margin-top: 30px"></div>
    </div>
  `
})