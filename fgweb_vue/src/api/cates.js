import http from "../http";
import { reactive } from "vue";

const cates = reactive({
    cates_list: [], // 头部导航列表
    cc_list: {},
    course_list: [],
    c_list: [],
    cates_l: [],

    get_cate_nav() {
        // 获取头部导航菜单
        return http.get("ccates/").then(response => {
            this.cates_list = response.data.clist;

        })
    },

    get_course(cateid) {
        // 获取头部导航菜单
        return http.get("catescourses/?cateid=" + cateid).then(response => {
            this.cc_list = response.data.clist;
            this.course_list = response.data.cousers
        })
    },

    get_course_list(catesid, ind) {
        // 获取轮播广告列表
        return http.get("homeCourse/?catesid=" + catesid).then(response => {
            if (catesid) {
                this.c_list[ind]['courses'] = response.data.clist
            } else {
                this.c_list = response.data.clist;
            }

        })
    }
})

export default cates;