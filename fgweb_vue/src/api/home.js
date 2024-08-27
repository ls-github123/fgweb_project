import { reactive } from "vue";
import http from "../http";
const course = reactive({
    data: [], // 轮播广告列表
    get_course_list() {
        // 获取轮播广告列表
        return http.get("homeCourse/").then(response => {
            // this.data = response.data.clist;
            this.data = [{ "id": 1, 'name': '222' }]

        })
    }
})

export default course;