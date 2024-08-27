import {reactive} from "vue";
import http from "../http";
import store from "../store";
import router from "../router";

const order = reactive({
  selected_course_list: [], // 购物车勾选商品列表
  total_price: 0,      // 勾选商品列表的总价格
  real_price: 0,       // 勾选商品列表的实付总价格
  discount_price: 0,   // 本次下单的优惠价格
  use_coupon: false,   // 用户是否使用优惠
  discount_type: 0,    // 0表示优惠券，1表示积分
  coupon_list:[],      // 用户拥有的可用优惠券列表
  select: -1,          // 当前用户选中的优惠券的下标
  credit: 0,           // 当前用户选择抵扣的积分
  fixed: true,         // 底部订单总价是否固定浮动
  pay_type: 0,         // 支付方式

  credit_to_money: 0,  // 积分兑换现金的比例
  has_credit: 0,       // 用户拥有的积分
  max_use_credit: 0,   // 最可以使用的积分数量

  show_success_page: true, // 是否显示成功提示的页面内容
  pay_time: undefined,     // 付款时间
  course_list: [],         // 已购买的课程列表

  loading: false,           // 显示订单支付的倒计时的遮罩层
  timeout: 15*60,           // 订单倒计时
  timer: null,              // 订单支付的定时器标志
  order_id: null,           // 当前订单ID

  order_status: -1,        // 个人中心的默认显示的订单状态选项，-1表示全部
  order_status_chioces:[], // 个人中心的订单支付状态选项
  page: 1,                 // 个人中心的订单列表对应的页码
  size: 5,                 // 个人中心的订单列表对应的单页数据量
  order_list:[],           // 个人中心的订单列表
  count: 0,                // 个人中心的订单列表的总数据量

  get_selected(token){
    // 获取购物车中的勾选商品列表
    return http.get("/cart/cartorder/", {
      headers:{
          Authorization: "Bearer " + token,
      }
    }).then(response=>{
      if(response.data.cart){
        this.selected_course_list = response.data.cart;
        this.calc_cart();
        this.get_coupon_list(token);
      }else{
        ElMessage.error("当前购物车没有任何商品，请购物后再继续操作！");
        router.push("/");
      }
      return response
    })
  },
  calc_cart(){
    // 计算本次下单的所有商品的相关价格
    let original_total_price = 0;  // 所有的课程的原价总价格
    let real_total_price = 0;      // 所有的课程的实付总价格
    let max_use_credit = 0;        // 所有的课程的累计可以最大兑换积分
    this.selected_course_list.forEach(course=>{
      original_total_price += course.price;
      max_use_credit += course.credit
      if(course.discount.price !== undefined){
        // 当课程有优惠价格
        real_total_price+=parseFloat(course.discount.price);
      }else{
        // 当课程没有优惠价格
        real_total_price+=parseFloat(course.price);
      }
    })
    this.total_price = original_total_price;
    this.real_price = real_total_price;
    this.max_use_credit = max_use_credit;
  },
  create_order(token){
    // 创建订单
    let data = {
      pay_type: this.pay_type,
      credit: this.credit,
      user_coupon_id: this.coupon_list[this.select]?.user_coupon_id
    }
    return http.post("order/orders/",data,{
        headers:{
            Authorization: "Bearer " + token,
        }
    }).then(response=>{
        // 从购物车商品总数里面扣减本次下单的商品数量
        store.commit("set_cart_total", store.state.cart_total - this.selected_course_list.length);
        ElMessage.success("下单成功！马上跳转到支付页面，请稍候~");
        this.order_id = response.data.id;
        this.timeout = response.data.timeout;
        this.get_pay_link(this.order_id);
        this.loading = true; // 显示支付倒计时
        clearInterval(this.timer);
        this.timer = setInterval(()=>{
           if(order.timeout > 1) {
             order.timeout = order.timeout - 1;
           }else{
             ElMessage.error("订单超时！如果您已经支付成功！请点击关闭当前弹窗！当前页面1.5秒后关闭！");
             clearInterval(this.timer);
             // 发送一个订单查询
             this.check_order_result().then(response=>{
                console.log(response);
                if(response.status === 201){
                  // 支付完成！
                  ElMessage.success("支付成功！马上跳转到个人中心页面，请稍候~");
                  // 1.5秒后关闭页面，跳转到用户中心的我的订单页面中
                  setTimeout(()=>{
                    // 跳转到用户中心的课程列表
                    router.push("/user/course");
                  }, 1500);
                }else{
                  ElMessage.info("您的订单尚未支付！马上跳转到个人中心页面，请稍候~");
                  setTimeout(()=>{
                    // 跳转到用户中心的课程列表
                    router.push("/user/order");
                  }, 1500);
                }
              })
             // 1.5秒后关闭页面，跳转到用户中心的我的订单页面中
             setTimeout(()=>{
                // 跳转到用户的订单用心
                router.push("/user/order");
             }, 1500);
           }
        }, 1000);

    }).catch((error)=>{
      console.log('创建订单失败......');
      console.log(error);
    })
  },
  get_coupon_list(token) {
    // 获取本次下单的可用优惠券列表
    return http.get("/coupon/enable/", {
      headers: {
        Authorization: "Bearer " + token,
      }
    }).then(response=>{
      console.log('可用优惠券获取成功.....');
      console.log(response);
      this.coupon_list = response.data.coupon_list;
      // this.coupon_list = response.data;
      this.credit_to_money = response.data.credit_to_money;
      this.has_credit = response.data.has_credit;
      // 把用户拥有的积分与本次下单的最大兑换积分进行比较，判断用户可以使用的最大数量积分。
      if(this.has_credit < this.max_use_credit){
        this.max_use_credit = this.has_credit;
        console.log("this.max_use_credit", this.max_use_credit);
      }
    })
  },
  get_pay_link(order_id){
    // 获取支付宝支付链接地址
    return http.get("/pay/alipay/link/", {
      params: {
        order_id,
      }
    }).then(response=>{
      window.open(response.data,"_blank");
    })
  },
  get_alipay_return_result(){
    // 客户端转发支付宝的同步支付结果
    return http.get(`/pay/alipay/return_result/${location.search}`).then(response=>{
      this.course_list = response.data.course_list;
      this.pay_time = response.data.pay_time;
      this.real_price = response.data.real_price;
    })
  },
  check_order_result(){
    // 查询订单的支付状态
    console.log(`查询订单ID=${this.order_id}的支付结果！`);
    return http.get("/payments/alipay/query/", {
      params: {
        order_id: this.order_id,
      },
    })
  },
  get_order_status(){
    // 获取订单状态选项
    return http.get('/order/chioces/').then(response=>{
      this.order_status_chioces = response.data;
    })
  },
  get_order_list(token){
    // 获取当前登录用户的订单列表[分页显示]
     return http.get('/order/list', {
        params: {
          page: this.page,
          size: this.size,
          status: this.order_status,
        },
        headers: {
          Authorization: "Bearer " + token,
        }
     }).then(response=>{
       this.order_list = response.data.results;
       this.count = response.data.count;
     })
  },
  order_cancel(order_id, token){
    // 取消订单操作
    return http.put(`/orders/${order_id}/pay_cancel/`, {},{
        headers:{
            Authorization: "Bearer " + token,
        }
    })
  }
})

export default order;