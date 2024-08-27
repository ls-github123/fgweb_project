<template>
  <div>
  
  </div>
</template>

<script setup>

import {onMounted,ref}  from "vue"
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()

onMounted(() => {
  const userid = route.query.userid
  const token = route.query.token
  localStorage.setItem('userid',userid)
  localStorage.setItem('token',token)
  router.replace('/user')
 
})


</script>

<style>

</style>