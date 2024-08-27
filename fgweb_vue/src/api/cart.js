import {reactive} from "vue";
import http from "../http";
import store from "../store";
import router from "../router";

const cart = reactive({
  course_list: [],  // 购物车中的商品列表
  total_price: 0,  // 购物车中的商品总价格
  selected_course_total: 0, // 购物车中被勾选商品的数量
  checked: false,  // 购物车中是否全选商品了
  add(course_id, token){
      // 添加商品到购物车
      return http.post("/cart/cart/", {
            course_id: course_id
        }, {
            // 因为当前课程端添加课程商品到购物车必须登录，所以接口操作时必须发送jwt
            headers: {
                Authorization: "Bearer " + token,
            }
        })
  },
  list(token){
    // 购物车商品列表
    return http.get("/cart/cart/", {
      headers:{
          Authorization: "Bearer " + token,
      }
    }).then(response=>{
      console.log('购物车列表请求成功');
      console.log(response);
      if(response.data.cart){
        this.course_list = response.data.cart;
        this.calc();
      }else{
        ElMessage.error("当前购物车没有任何商品，请购物后再继续操作！");
        router.push("/");
      }
      return response
    })
  },
  calc(){
    // 计算当前购物车中的商品总价格和勾选商品的总数
    let total_price = 0;  // 临时设置一个变量用于累计总价格
      let select_total = 0; // 临时设置一个变量用于累计勾选商品的数量
      this.course_list.forEach(course=>{
        // 累计当前购物车中有多少商品课程被勾选了。
        if(course.selected){

          // 统计当前课程的总价格
          if(course.discount.price !== undefined){
            // 当课程有优惠价格
            total_price+=parseFloat(course.discount.price);
          }else{
            // 当课程没有优惠价格
            total_price+=parseFloat(course.price);
          }

          select_total+=1;
        }
      })
      this.total_price = total_price;
      this.selected_course_total = select_total;
      this.checked = this.selected_course_total === this.course_list.length;
  },
  select(course_id, selected, token){
    // 切换商品课程的勾选状态
    return http.patch("/cart/cart/", {
      course_id: course_id,
      selected: selected,
    }, {
        // 因为当前课程端添加课程商品到购物车必须登录，所以接口操作时必须发送jwt
        headers: {
            Authorization: "Bearer " + token,
        }
    }).then(response=>{
      // 重新计算被勾选的商品数量
      this.calc();
    })

  },
  select_all(selected, token) {
    // 切换购物车对应商品课程的全选状态
    return http.put("/cart/cart/", {
      selected,
    },{
      headers:{
        Authorization: "Bearer " + token,
      }
    }).then(response=>{
      this.calc();
    })
  },
  delete_course(key, token){
    // 从购物车中删除商品课程
    let course_id = this.course_list[key].id;
    return http.delete("/cart/cart/", {
      params:{
        course_id,  // course_id: course_id,的简写
      },
      headers:{
        Authorization: "Bearer " + token,
      }
    }).then(response=>{
      this.course_list.splice(key, 1);
      // 通知vuex更新购物车中商品总数
      store.commit("set_cart_total", this.course_list.length);
      this.calc();
    })
  },
})

export default cart;