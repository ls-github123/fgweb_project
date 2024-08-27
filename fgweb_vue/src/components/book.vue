<template>
<div>

<el-table :data="tableData" style="width: 100%">
    <el-table-column prop="date" label="Date" width="180" />
    <el-table-column prop="name" label="Name" width="180" />
    <el-table-column prop="address" label="Address" />
  </el-table>

  <div class="example-pagination-block">
    <div class="example-demonstration">When you have few pages</div>
    <el-pagination layout="prev, pager, next" :total="total" />
  </div>

</div>
  
</template>

<script lang="ts" setup>
import http from "../http";

import {onMounted,ref} from 'vue'
const tableData = ref([])
const total=ref(0)

const getmes=()=>{
    http.post('').then(res=>{
        tableData.value=res.data.list
        total.value=res.data.total
    })
}
onMounted(() => {
    getmes()
})

</script>
