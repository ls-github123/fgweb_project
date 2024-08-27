<template>
  <div>
 
 <el-row>
    <el-col :span="24">
    <el-input v-model="cname" style="width: 240px" placeholder="Please input" />
    <el-button @click="getlist">搜索</el-button>

    
    <el-button @click="changesort('id')">默认</el-button>
    <el-button @click="changesort('create_time')">时间</el-button>
    </el-col>
  </el-row>

  <el-row>
    <el-col :span="24">
    <ul>
    <li v-for="i in catelist">{{i.name}}</li>
    </ul>
    </el-col>
  </el-row>

  <el-row>
    <el-col :span="24">
    <el-table :data="tableData" style="width: 100%">
    <el-table-column prop="name" label="Date" width="180" />
    <el-table-column prop="descrip" label="Name" width="180" />
    <el-table-column prop="price" label="Address" />
  </el-table>
    </el-col>
  </el-row>
  
  <div class="example-pagination-block">
    <div class="example-demonstration">When you have few pages</div>
    <el-pagination layout="prev, pager, next" :total="total" :page-size="1" @current-change="handleCurrentChange"/>
  </div>

  </div>
</template>

<script lang="ts" setup>
import { ref,onMounted } from 'vue'
import http from '../../http'
const cname = ref('')
const catelist = ref([])
const tableData = ref([])
const total=ref(0)
const page = ref(1)
const sorted=ref('id')



const getlist=()=>{
    http.get('clist/?cname='+cname.value+"&page="+page.value+"&sorted="+sorted.value).then(res=>{
        catelist.value = res.data.clist
        tableData.value = res.data.blist
        total.value = res.data.total
    })
}

const changesort=(value)=>{
    sorted.value = value
    getlist()
}

const handleCurrentChange = (val: number) => {
  console.log(`current page: ${val}`)
  page.value = val
  getlist()
}


onMounted(()=>{
    getlist()
})
</script>

<style>

</style>