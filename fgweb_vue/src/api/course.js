import {reactive} from "vue";
import http from "../http";
const course = reactive({
    direction_list: [],    // 学习方向列表
    category_list: [],     // 课程分类列表
    course_list: [],     // 课程信息列表
    current_direction: 0,  // 当前选中的学习方向，0表示所有方向
    current_category: 0,  // 当前选中的课程分类，0表示不限分类
    ordering: "",          // 课程排序条件

    page: 1,               // 当前页码，默认为1
    size: 8,               // 当前页数据量
    count: 0,              // 课程信息列表的数量
    has_perv: false,       // 是否有上一页
    has_next: false,       // 是否有下一页

    course_discount_timer: null,           // 课程列表相关数据的定时器
    text: "",              // 搜索框字段
    hot_word_list: [],    // 热搜词列表


    course_id: null,  // 课程ID
    info: {           // 课程详情信息
      teacher:{},     // 课程相关的老师信息
      discount:{      // 课程相关的折扣信息
        type: ""
      }
    },
    tabIndex: 2,      // 课程详情页中默认展示的课程信息的选项卡
    timer: null,      // 课程详情页的相关数据的定时器
    chapter_list: [], // 课程章节列表

    get_course_direction(){
      // 获取学习方向信息
      return http.get(`/course/diretion/`).then(response=>{
        this.direction_list = response.data;
      })
    },
    get_course_category () {
      // 获取课程分类信息
      return http.get(`/course/category/${this.current_direction}/`,).then(response=>{
        // console.log('课程分类信息请求成功..........');
        // console.log(response);
        this.category_list = response.data;
      }).catch((err) => {
        // console.log('课程分类信息请求失败------');
        // console.log(err);
      });
    },
    get_course_list () {
      // 获取课程列表
      let params = {
        page: this.page,
        size: this.size,
      }
      if(this.ordering){
        params.ordering = this.ordering;
      }
     return http.get(`/course/course/${this.current_direction}/${this.current_category}/`,{
       params,
     }).then(response=>{
        console.log('课程信息请求成功....');
        console.log(response);
        // 当前页的数据列表
        // 需要修改
        // TODO
        this.course_list = response.data.results;
        // 总数据量
        course.count = response.data.count
        // 是否有上一页和下一页
        course.has_perv = !!response.data.previous; // !!2个非表示把数据转换成布尔值
        course.has_next = !!response.data.next;
        // 开始活动倒计时
        this.start_timer();
     }).catch((err) => {
        console.log('课程信息请求失败了....');
        console.log(err);
     });
    },
    start_timer() {
      // 课程相关的优惠活动倒计时
      // clearInterval(this.course_discount_timer);
      // this.course_discount_timer = setInterval(() => {
      //       this.course_list.forEach((course) => {
      //           // js的对象和python里面的字典/列表一样， 是属于引用类型的。所以修改了成员的值也会影响自身的。
      //           if (course.discount.expire !== undefined && course.discount.expire > 0) {
      //               // 时间不断自减
      //               course.discount.expire--
      //           }
      //       })
      //   }, 1000);
    },
    search_course() {
        // 课程搜索
        let params = {
            page: 1,
            size: this.size,
            text: this.text,
        }
        if (this.ordering) {
            params['ordering'] = this.ordering
        }
        return http.get(`/courses/search`, {
            params,
        }).then(response=>{
        // 当前页的数据列表
        this.course_list = response.data.results;
        this.course_list.forEach(course=>{
          console.log(course);
          course.discount = JSON.parse(course.discount)
        })
        // 总数据量
        course.count = response.data.count
        // 是否有上一页和下一页
        course.has_perv = !!response.data.previous; // !!2个非表示把数据转换成布尔值
        course.has_next = !!response.data.next;
        // 开始活动倒计时
        this.start_timer();
        // 更新搜索关键字
        this.get_hot_word();
     })
    },
    get_hot_word(){
        // 课程热搜关键字
        return http.get("/courses/search/hot_word/").then(response=>{
          this.hot_word_list = response.data
        })
    },
    get_course(){
      // 获取课程详情
      return http.get(`/course/coursdetail/${this.course_id}/`).then(response=>{
        console.log('获取课程详情.....成功');
        console.log(response);
        this.info = response.data;
        
        // console.log(this.info.students);

        // 获取课程章节
        this.get_course_chapters();
      })
    },
    get_course_chapters(){
        // 获取指定课程的章节列表
        // 章节中附带课程列表
        return http.get(`/course/${this.course_id}/chapters/`).then(response=>{
          this.chapter_list = response.data;
          console.log('获取课程章节成功.....');
          console.log(response);
        }).catch((err)=>{
          console.log('获取课程章节失败.....');
          console.log(err);
        })
    }
})

export default course;