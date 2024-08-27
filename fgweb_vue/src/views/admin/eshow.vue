<template>
    <div id="show" style="width:600px;height:200px;"></div>
</template>
<script lang="ts" setup>
import {onMounted,ref} from "vue"
import * as echarts from 'echarts';

const datalist=ref([])
const countlist = ref([])

const initecharts=()=>{
    
    var chartDom = document.getElementById('show');
    var myChart = echarts.init(chartDom);
    var option;

    option = {
    xAxis: {
        type: 'category',
        data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    },
    yAxis: {
        type: 'value'
    },
    series: [
        {
        data: [150, 230, 224, 218, 135, 147, 260],
        type: 'line'
        }
    ]
    };

    option && myChart.setOption(option);
}

// const getdata=()=>{
//     http.get('').then(res=>{
//         datalist.value = res.data.datalist
//         countlist.value = res.data.countlist
//         initecharts()
//     })
// }
onMounted(()=>{
    // getdata()
    initecharts()
})

</script>