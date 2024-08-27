<template>
  <el-form :model="form" label-width="auto" style="max-width: 600px">
    <el-form-item label="姓名">
      <el-input v-model="form.name" />
    </el-form-item>
     <el-form-item label="年龄">
      <el-input v-model="form.age" />
    </el-form-item>
    
    <el-form-item>
      <el-button type="primary" @click="onSubmit">添加</el-button>
      <el-button>取消</el-button>
    </el-form-item>
  </el-form>
</template>

<script lang="ts" setup>
import { reactive } from 'vue'

// do not use same name with ref
const form = reactive({
  name: '',
  age:''
})

const onSubmit = () => {
 
}
</script>

