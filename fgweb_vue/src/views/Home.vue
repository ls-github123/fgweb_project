<template>
  <div class="home">
    <Header></Header>
    <div id="main">
      <Banner></Banner>
      <NewCourse></NewCourse>
    </div>
    <Footer></Footer>
  </div>
</template>

<script setup>
import Header from "../components/Header.vue"
import Footer from "../components/Footer.vue"
import Banner from "../components/Banner.vue"
import NewCourse from "../components/NewCourse.vue"

// // 测试CORS的跨域配置是否有问题
// import http from "../http";
// http.get("/home/test/").then(response=>{
//   console.log(response.data);
// })

</script>


<style scoped>

</style>