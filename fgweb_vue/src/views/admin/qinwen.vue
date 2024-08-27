<template>
  <div class="common-layout">
    <el-container>
      <el-aside width="400px">
       <el-button type="primary" @click="addcate">新建</el-button>
       <el-row>
       <el-col  :span="12">
       <el-input v-model="title" placeholder="Please input" />
       </el-col>
       <el-col  :span="12">
        <el-button type="primary">新建</el-button>
       </el-col>
       </el-row>
        <el-row>
        <ul>
    
        <li v-for="j in historylist" @click="getcates(j.id)">{{j.name}} </li>
        
        </ul>
        </el-row>

      </el-aside>
      <el-main>
      <el-row>
      <el-col>
      <div v-for="i in meslist">
      <p>问题：{{i.name}}</p>
      <p>答案：{{i.answer}}</p>
      </div>
      
      
      </el-col>
      </el-row>

      <el-row>
      <el-col>上传文件</el-col>
      </el-row>

      <el-row>
      <el-col>
        <el-input v-model="content" type="textarea" />
        <el-button type="primary" @click="onSubmit">提交</el-button>
      </el-col>
      </el-row>
      
      </el-main>
    </el-container>
  </div>
</template>
<script lang="ts" setup>
import { ref,reactive,onMounted } from 'vue'
import http from "../../http";

// do not use same name with ref

const title=ref('')
const content=ref('')
const meslist=ref([])
const historylist = ref([])
const cid = ref(0)


onMounted(()=>{
  http.get('questions/?userid=1').then(res=>{
    historylist.value = res.data.hlist
  })
})

const getcates=(cateid)=>{
  cid.value = cateid
  http.get('catesques/?cid='+cateid).then(res=>{
      meslist.value=res.data.reslist
  })
}

const addcate=()=>{
  http.post('catesques/',{"userid":1}).then(res=>{
    cid.value = res.data.cid
    meslist.value=[]
  })
}


const onSubmit = () => {
  // {"code":200,'answer':'sdfsdf','cid':cid,'name':name}
    http.post('questions/',{'userid':1,'qustion':content.value,'cid':cid.value}).then(res=>{
        if(res.data.code == 200){
            meslist.value.push({"name":content.value,'answer':res.data.answer})
           
            if(res.data.name){
             
              historylist.value.unshift({"name":res.data.name,"id":res.data.cid})
            }
            cid.value = res.data.cid
        }
       
        
        
    })
    // meslist.value.push({"q":"sdfsdfdsf?",'a':"aaaaasdfdsfsd","id":'1'})
    // historylist.value.unshift = {"q":"sdfsdfdsf?","id":'1'}
    

//    http.post('/',{'content':content.value}).then(res=>{
//       meslist.value.push({"q":content.value,'a':res.data.mes})
//    })
}
</script>
