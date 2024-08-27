import {reactive} from "vue";
import http from "../http";
const banner = reactive({
  data: [],  // 轮播广告列表
  get_banner_list(){
    // 获取轮播广告列表
    return http.get("home/banner/").then(response=>{
      console.log('轮播图数据请求成功.....');
      console.log(response);
      this.data = response.data;
    })
  }
})

export default banner;