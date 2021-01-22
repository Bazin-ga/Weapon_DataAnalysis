<template>
  <!--为echarts准备一个具备大小的容器dom-->
  <div id="main" style="width: 1200px;height: 700px;"></div>
</template>
<script>
import echarts from 'echarts'
export default {
  name: '',
  data() {
    return {
      charts: '',
      opinionData: data [120, 200, 150, 80, 70, 110, 130]
    }
  },
  methods: {
    drawLine(id) {
      this.charts = echarts.init(document.getElementById(id))
      this.charts.setOption({
        title: {
          text: '实体类别统计',
          subtext: '主体客体一共有6种类型',
          left: 'center'
        },
        tooltip: {
          trigger: 'item',
          formatter: '{a} <br/>{b}: {c} ({d}%)'
        },
        legend: {
          orient: 'vertical',
          left: 10,
          data: ['学校', '人物', '电视综艺', '娱乐人物', '歌曲', '影视作品', '企业/品牌', '音乐专辑', '图书作品', 'Date', 'Text', '学科专业', 'Number', '机构', '行政区', '企业', '文学作品', '气候', '奖项', '城市', '国家', '历史人物', '地点', '景点', '作品', '语言']
        },
        series: [
          {
            name: '访问来源',
            type: 'pie',
            radius: ['50%', '70%'],
            avoidLabelOverlap: true,
            label: {
              show: true,
            },
            data: [
              {'value': 11334, 'name': '学校'},
              {'value': 295384, 'name': '人物'},
              {'value': 10416, 'name': '电视综艺'},
              {'value': 12507, 'name': '娱乐人物'},
              {'value': 51210, 'name': '歌曲'},
              {'value': 87706, 'name': '影视作品'},
              {'value': 923, 'name': '企业/品牌'},
              {'value': 7757, 'name': '音乐专辑'},
              {'value': 29818, 'name': '图书作品'},
              {'value': 20441, 'name': 'Date'},
              {'value': 13000, 'name': 'Text'},
              {'value': 43, 'name': '学科专业'},
              {'value': 5260, 'name': 'Number'},
              {'value': 20087, 'name': '机构'},
              {'value': 2220, 'name': '行政区'},
              {'value': 19559, 'name': '企业'},
              {'value': 2346, 'name': '文学作品'},
              {'value': 908, 'name': '气候'},
              {'value': 3404, 'name': '奖项'},
              {'value': 1183, 'name': '城市'},
              {'value': 11493, 'name': '国家'},
              {'value': 8305, 'name': '历史人物'},
              {'value': 4741, 'name': '地点'},
              {'value': 748, 'name': '景点'},
              {'value': 441, 'name': '作品'},
              {'value': 146, 'name': '语言'}
            ]
          }
        ]
      })
    }
  },
  //调用
  mounted() {
    this.$nextTick(function() {
      this.drawLine('main')
    })
  }
}
</script>
<style scoped>
* {
  margin: 0;
  padding: 0;
  list-style: none;
}
</style>
