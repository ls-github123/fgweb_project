<template>
  <div>
    <div class="bg000" v-for="i,ind in cates.c_list" :key="ind">
      <div class="container-types new-course">
        <h3 class="types-title justify-content_flex-start">{{i.name}}
          <ul class="menu">
            <li 
                v-for="item,index in i.cates" :key="index" @click="selectTab(item,ind)"
            >
              <a>{{ item.name }}</a>
            </li>
          </ul>
        </h3>
        <div class="list clearfix show"  v-for="c,cindex in i.courses" :key="cindex">
          <a class="item" >
            <div class="img"
                style="background-image: url('https://img1.sycdn.imooc.com/szimg/65e07b1108d30cc005400304.jpg')">
            </div>
            <div class="title ellipsis2">{{c.name}}</div>
            <div class="difficulty">中级 · 172人报名 </div>
            <div class="bottom clearfix">
              <span class="price l red bold">￥499.00</span>
            </div>
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import {reactive} from "vue"
import cates from "../api/cates";

// tab
// const tablist = reactive([])

cates.get_course_list(0,0)

// let nowTab = reactive(tablist[0])
const selectTab=(item,ind) =>{
  state.current_menu = item.id
  cates.get_course_list(item.id,ind)
  // nowTab = item
}
const state = reactive({
  current_menu: 1,
})
</script>

<style scoped>
.bg000 {
  box-shadow: 0 2px 4px 0 rgba(7, 17, 27, 0.06);
}

.container-types {
  width: 1152px;
  margin-left: auto;
  margin-right: auto;
  padding: 32px 0;
}

.container-types.new-course .types-title {
  background-image: url('/src/assets/img/title-bg3.png');
}

.container-types .types-title {
  height: 36px;
  background: no-repeat left center / auto 29px;
  padding-left: 180px;
  margin-bottom: 30px;
  display: -webkit-box;
  display: -ms-flexbox;
  display: -webkit-flex;
  display: flex;
  -webkit-box-align: center;
  -ms-flex-align: center;
  -webkit-align-items: center;
  align-items: center;
}

.menu {
  user-select: none;
}
.container-types.new-course .list.show {
  display: block;
}
.clearfix:after {
    content: '\0020';
    display: block;
    height: 0;
    clear: both;
    visibility: hidden;
}
.menu li {
  position: relative;
  padding: 0 14px;
  margin: 0;
  float: left;
  font-size: 14px;
  line-height: 30px;
  cursor: pointer;
  color: #545C63;
  transition: all .2s;
}
.container-types .types-title .menu li:hover a{
  color: #E02020;
}
.container-types .types-title .menu li.curr a{
  color: #E02020;
  font-weight: bold;
}
.container-types .types-title .menu li.curr:after {
  content: '';
  position: absolute;
  left: 50%;
  bottom: 0;
  margin-left: -0.7em;
  width: 1.4em;
  height: 2px;
  border-radius: 100px;
  background-color: #E76060;
}
.item{
  position: relative;
  width: 270px;
  height: 272px;
  margin: 0 24px 24px 0;
  background: #FFFFFF;
  box-shadow: 0 6px 10px 0 rgba(95, 101, 105, 0.15);
  border-radius: 8px;
  float: left;
  transition: all .2s;
}
.container-types.new-course .list .item .img{
  height: 152px;
  background-size: 100%;
  margin-bottom: 8px;
  border-radius: 8px;
}
.container-types.new-course .list .item .title{
  color: #545C63;
  line-height: 20px;
  height: 40px;
  margin-bottom: 8px;
  padding: 0 8px;
}
.container-types.new-course .list .item .title.ellipsis2{
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
}
.container-types.new-course .list .item .difficulty{
  display: block;
  color: #9199A1;
  font-size: 12px;
  margin-bottom: 8px;
  padding: 0 8px;
}
.container-types.new-course .list .item .bottom{
    font-size: 12px;
    color: #9199A1;
    line-height: 18px;
    padding: 0 8px;
    margin-bottom: 18px;
}
.container-types.new-course .list .item .bottom .red{
    color: #F01414;
}
.container-types.new-course .list .item .bottom .price{
  line-height: 20px;
  margin-right: 2px;
}
</style>