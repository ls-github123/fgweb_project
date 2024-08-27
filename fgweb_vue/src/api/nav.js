import http from "../http";
import { reactive } from "vue";

const nav = reactive({
    header_nav_list: [], // 头部导航列表
    footer_nav_list: [], // 脚部导航列表
    get_header_nav() {
        // 获取头部导航菜单
        return http.get("home/heradnav/").then(response => {
            // console.log('头部导航请求成功.....')
            // console.log(response)
            this.header_nav_list = response.data;
        })
    },
    get_footer_nav() {
        // 获取脚部导航菜单
        return http.get("home/footernav/").then(response => {
            console.log('底部导航请求成功.....')
            console.log(response)
            this.footer_nav_list = response.data;
        })
    }
})

export default nav;