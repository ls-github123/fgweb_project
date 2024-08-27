<template>
  <el-table :data="tableData" style="width: 100%">
    <el-table-column prop="name" label="Name" width="180" />
    <el-table-column fixed="right" label="Operations" min-width="120">
      <template #default="scope">
        <el-button link type="primary" size="small" @click="handleClick(scope.row.id)">
          资源配制
        </el-button>
        <el-button link type="primary" size="small">修改</el-button>
        <el-button link type="primary" size="small">删除</el-button>
      </template>
    </el-table-column>
  </el-table>

<el-dialog
    v-model="dialogVisible"
    title="Tips"
    width="500"
  >
    
<el-transfer v-model="value" :data="data" />

    <template #footer>
      <div class="dialog-footer">
        <el-button @click="dialogVisible = false">Cancel</el-button>
        <el-button type="primary" @click="setresource()">
          提交
        </el-button>
      </div>
    </template>
  </el-dialog>
</template>

<script lang="ts" setup>
import {onMounted,ref} from 'vue'
import http from "../../http";
const tableData = ref([])
const dialogVisible = ref(false)

//选中资源值的数据
const value=ref([])

const roleid=ref(0)

// interface Option {
//   id: number
//   name: string
// }
//左侧所有资源数据
const data=ref([])


const getrlist=()=>{
    // http.get('roles/').then(res=>{
    //     tableData.value = res.data.list
    // })
     tableData.value = [{"id":1,'name':'项目经理'},{"id":2,'name':'程序员'}]
}

const handleClick=(rid)=>{
  //保存roleid
  roleid.value = rid
  //获取全部资源以及此角色已经配制过的资源
  http.get('resource/?roleid='+roleid.value).then(res=>{
    data.value = res.data.reslist
    value.value = res.data.checkedids
    //显示穿梭框
    dialogVisible.value=true
   
  })
  
}

const setresource=()=>{
  http.post('resource/',{"roleid":roleid.value,'resid':value.value}).then(res=>{
    if(res.data.code == 200){
      dialogVisible.value=false
      roleid.value = 0
    }
  })
}

onMounted(()=>{
    getrlist()
})
</script>
