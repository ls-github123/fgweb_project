<template>
  <el-table :data="tableData" style="width: 100%">
    
    <el-table-column prop="name" label="角色名" width="120" />
    
    <el-table-column fixed="right" label="Operations" width="120">
      <template #default="scope">
        <el-button link type="primary" size="small" @click="handleClick"
          >Detail</el-button
        >
        <el-button link type="primary" size="small">Edit</el-button>
        <el-button link type="primary" size="small" @click="setres(scope.row.id)">资源配制</el-button>
      </template>
    </el-table-column>
  </el-table>


    <el-dialog
    v-model="dialogVisible"
    title="Tips"
    width="80%"
  >
    

<el-transfer v-model="value" :data="data" />

    <template #footer>
      <span class="dialog-footer">
        <el-button @click="dialogVisible = false">Cancel</el-button>
        <el-button type="primary" @click="addresource"
          >Confirm</el-button
        >
      </span>
    </template>
  </el-dialog>

</template>

<script lang="ts" setup>
import http from "../../http";
import {onMounted,ref} from 'vue'

const dialogVisible=ref(false)
const value=ref([])
const data = ref([])
const roleid = ref('')

const handleClick = () => {
  console.log('click')
}

const tableData = ref([])
onMounted(()=>{
    http.get('troles/').then(res=>{
        tableData.value = res.data.rlist
    })
})

const setres=(rid)=>{
    roleid.value = rid
    http.get('tresource/?roleid='+rid).then(res=>{
        data.value = res.data.allres
        value.value = res.data.checkedids
        dialogVisible.value=true
    })
    
}

const addresource=()=>{
    http.post('tresource/',{'roleid':roleid.value,'resids':value.value}).then(res=>{
        roleid.value=''
        dialogVisible.value=false
    })
}
</script>
