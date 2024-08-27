<template>
  <el-form
    ref="ruleFormRef"
    :model="ruleForm"
    :rules="rules"
    label-width="120px"
    class="demo-ruleForm"
    :size="formSize"
    status-icon
  >
    <el-form-item label="名称" prop="name">
      <el-input v-model="ruleForm.name" />
    </el-form-item>
    <el-form-item label="描述" prop="description">
      <el-input v-model="ruleForm.description" />
    </el-form-item>
    <el-form-item label="选择项目" prop="region">
      <el-select v-model="ruleForm.project" placeholder="请选择">
        <el-option :label="i.name" :value="i.id"  v-for="i in options"/>
       
      </el-select>
    </el-form-item>
   

    
    <el-form-item>
      <el-button type="primary" @click="submitForm(ruleFormRef)"
        >Create</el-button
      >
      <el-button @click="resetForm(ruleFormRef)">Reset</el-button>
    </el-form-item>
  </el-form>
</template>

<script lang="ts" setup>
import http from "../../http";
import { reactive, ref,onMounted } from 'vue'
import type { FormInstance, FormRules } from 'element-plus'
import { oppositeOrderMap } from "element-plus/es/components/table-v2/src/constants";

const formSize = ref('default')
const ruleFormRef = ref<FormInstance>()
const ruleForm = reactive({
  name: '',
  project: '',
  description:'',

})

const rules = reactive<FormRules>({
  name: [
    {
      required: true,
      trigger: 'blur',
    }
  ]
})

const submitForm = async (formEl: FormInstance | undefined) => {
  if (!formEl) return
  await formEl.validate((valid, fields) => {
    if (valid) {
       //调用接口处理
       console.log(ruleForm)
       http.post('tasks/',ruleForm).then(res=>{

       })
    } else {
      console.log('error submit!', fields)
    }
  })
}

const resetForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return
  formEl.resetFields()
}

const options =ref([])

onMounted(()=>{
    // http.get('project/').then(res=>{
           // options.value=res.data.plist
    // })
    options.value=[{"id":1,'name':'教育平台'},{"id":2,'name':'医疗平台'}]
})
</script>
