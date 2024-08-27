<template>
  <div class="player">
    <div id="player"></div>
    <div class="chapter-list">
      <h2>{{course.info.name}}</h2>
      <el-tree
        v-if="course.lesson_list.length>0"
        highlight-current
        class="filter-tree"
        :data="course.lesson_list"
        :props="course.defaultProps"
        default-expand-all
        node-key="id"
        @node-click="node_click"
        >
      </el-tree>
    </div>
  </div>
</template>

<script setup>
import {onMounted, watch} from "vue"
import http from "../http"
import "../utils/player"
import course from "../api/course";
import {useRoute} from "vue-router";
import settings from "../settings";

const route = useRoute();

// 获取路由参数[课程ID]
course.course_id = route.params.course;
let token = sessionStorage.access_token || localStorage.access_token;

// 获取当前课程的学习进度与课程基本信息
course.get_user_course(token).then(response=>{
  if(course.lesson_link){
    // 页面刷新完成，ajax获取当前课程的学习进度以后，自动播放
    polyv( course.lesson_link);
  }
})
course.get_course().then(response=>{

  let ret = [];
  let chapter_item = {}
  for(let chapter of course.chapter_list){
    chapter_item = {
      id: 'chapter-'+chapter.id,
      label: `第${chapter.orders}章. ${chapter.name}`,
      children: [],
    }

    if(chapter.get_lesson_list.length>0){
      for(let lesson of chapter.get_lesson_list){
        chapter_item.children.push({
          id: 'lesson-'+lesson.id,
          label: `${chapter.orders}.${lesson.orders} ${lesson.name}`,
          lesson: lesson
        })
      }
    }
    ret.push(chapter_item)
  }

  course.lesson_list = ret;

});

const node_click = data=>{
  if(!data.lesson){
    // 如果点击的树形菜单，不是课时，则不需要往下切换课时
    return ;
  }
  // 切换播放的课时内容
  course.current_lesson = data.lesson.id;

  // 先删除原来的播放器
  course.player?.destroy(); // 如果course.player为True，则调用course.player.destroy();// 新建一个播放器
  console.log(data.lesson.lesson_link)
  // 播放新的课时
  polyv(data.lesson.lesson_link);
  // 设置自动播放
  course.player.j2s_resumeVideo();
}



let polyv = (vid)=>{
  let token = sessionStorage.access_token || localStorage.access_token;
  // 1. 到数据库中查询用户购买的课程，是否有当前章节

  // 2. 到数据库中查询当前用户购买的课程是否在有效期内
  course.player = polyvPlayer({
    wrap: '#player',
    width: document.documentElement.clientWidth - 300, // 页面宽度
    height: document.documentElement.clientHeight,     // 页面高度
    forceH5: true,
    vid: vid,
    code: "root", // 一般是用户昵称
    // 视频加密播放的配置
    playsafe(vid, next){ // 向后端发送请求获取加密的token
      http.get(`courses/polyv/token/`, {
        params: {
          vid,
        },
        headers: {
          "Authorization": "Bearer " + token,
        }
      }).then(response=>{
        // 获取播放视频的token令牌
        next(response.data);
      })
    }
  });

  // 获取课时播放进度
  course.get_lesson_study_time(course.current_lesson, token).then(response=>{
    // 设置播放进度
    course.player.on('s2j_onPlayerInitOver',(e)=>{
      course.player.j2s_seekVideo(response.data);
    });
  })

  let video = document.querySelector(".pv-video")
  // 监听是否是否播放中[记录学习进度]
  video.ontimeupdate = ()=>{
    // console.log("播放进度: ", video.currentTime);
    // 每隔几秒，发送一次ajax到服务端更新学习进度和课时进度
    let time = parseInt(video.currentTime);
    if(time % settings.seed_time === 0){
      console.log(`每隔${settings.seed_time}秒打印执行`);
      if(course.current_time < time){
          // 监听当前课时的播放时间
          course.current_time = time;
      }
    }
  }
}

onMounted(()=>{
  // 页面初始化完成以后，自动生成播放器[默认播放]
  // 监听当前浏览器窗口的大小是否发生变化，让播放器随着窗口变化大小
  window.onresize = ()=>{
    document.querySelector(".pv-video-player").style.width = `${document.documentElement.clientWidth - 300}px`;
    document.querySelector(".pv-video-player").style.height = `${document.documentElement.clientHeight}px`;
  }
})


watch(
    ()=>course.current_time,
    ()=>{
        let token = sessionStorage.access_token || localStorage.access_token;
        let lesson = course.current_lesson
        course.update_lesson_study_time(lesson, course.current_time, token).then(response=>{
        console.log(response.data)
      })
    }
)


</script>

<style scoped>
/* 这里的标签样式只在当前组件生效 */
.chapter-list{
  position: absolute;
  top: 0;
  right: 0;
  width: 300px;
  background-color: #ccc;
}
.chapter-list h2 {
  height: 40px;
  line-height: 40px;
  text-indent: 1rem;
}
</style>

<style>
/* 这里的标签样式不仅在当前组件生效 */
.player{
  background-color: #333;
}
.player .el-tree-node__content:hover,
.player .el-tree-node__content:active,
.player .el-tree-node:focus>.el-tree-node__content,
.player .el-tree--highlight-current .el-tree-node.is-current>.el-tree-node__content{
  background-color: #FF9900;
  color: #fff;
}
.player .el-tree{
  background-color: #333;
  color: #fff;
}
</style>