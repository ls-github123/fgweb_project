import {createRouter, createWebHistory} from 'vue-router'
import store from "../store";
import order from "../api/order";

// 路由列表
const routes = [
  {
    meta:{
      title: "浮光在线-站点首页",
      keepAlive: true
    },
    path: '/',         // uri访问地址
    name: "Home",
    component: ()=> import("../views/Home.vue")
  },
  {
    meta:{
      title: "项目课-浮光在线",
      keepAlive: true
    },
    path: '/project',
    name: "Course",            // 路由名称
    component: ()=> import("../views/Course.vue"),         // uri绑定的组件页面
  },
  {
    meta:{
      title: "课程详情-浮光在线",
      keepAlive: true
    },
    path: '/project/:id',
    name: "Info",            // 路由名称
    component: ()=> import("../views/Info.vue"),         // uri绑定的组件页面
  },
  {
    meta:{
      title: "浮光在线-用户登录",
      keepAlive: true
    },
    path:'/login',      // uri访问地址
    name: "Login",
    component: ()=> import("../views/Login.vue")
  },
  {
      meta:{
        title: "浮光在线-用户注册",
        keepAlive: true
      },
      path: '/register',
      name: "Register",            // 路由名称
      component: ()=> import("../views/Register.vue"),         // uri绑定的组件页面
  },
  {
    meta:{
        title: "浮光在线-购物车",
        keepAlive: true,
        authorization: true, // 当前页面需要验证登录状态
    },
    path: '/cart',
    name: "Cart",
    component: ()=> import("../views/Cart.vue"),
  },
  {
    meta: {
      title: "浮光在线-确认订单",
      keepAlive: true,
      authorization: true, // 当前页面需要验证登录状态
    },
    path: '/order',
    name: "Order",
    component: () => import("../views/Order.vue"),
  },
  {
    meta:{
      title: "支付成功",
      keepAlive: true,
      authorization: true, // 当前页面需要验证登录状态
    },
    path: '/alipay',
    name: "PaySuccess",
    component: ()=> import("../views/AliPaySuccess.vue"),
  },
  {
    meta:{
        title: "浮光在线-会员中心",
        keepAlive: true,
        authorization: true, // 当前页面需要验证登录状态
    },
    path: '/user',
    name: "User",
    component: ()=> import("../views/User.vue"),
    children: [ // 用户中心的子组件页面，children下面的子页面的url不能以/开头，否则报错
      {
        meta:{
          title: "浮光在线-会员中心-个人信息",
          keepAlive: true,
          authorization: true, // 当前页面需要验证登录状态
        },
        path: '',
        name: "UserInfo",
        component: ()=> import("../components/user/Info.vue"),
      },
      {
        meta:{
          title: "浮光在线-会员中心-我的订单",
          keepAlive: true,
          authorization: true, // 当前页面需要验证登录状态
        },
        path: 'order',
        name: "UserOrder",
        component: ()=> import("../components/user/Order.vue"),
      },
      {
        meta:{
          title: "浮光在线-会员中心-我的课程",
          keepAlive: true,
          authorization: true, // 当前页面需要验证登录状态
        },
        path: 'course',
        name: "UserCourse",
        component: ()=> import("../components/user/Course.vue"),
      },
      {
        meta:{
          title: "浮光在线-会员中心-我的优惠券",
          keepAlive: true,
          authorization: true, // 当前页面需要验证登录状态
        },
        path: 'coupon',
        name: "UserCoupon",
        component: ()=> import("../components/user/Coupon.vue"),
      },
      {
        meta:{
          title: "浮光在线-会员中心-我的钱包",
          keepAlive: true,
          authorization: true, // 当前页面需要验证登录状态
        },
        path: 'wallet',
        name: "UserWallet",
        component: ()=> import("../components/user/Wallet.vue"),
      },
      {
        meta:{
          title: "浮光在线-会员中心-消费记录",
          keepAlive: true,
          authorization: true, // 当前页面需要验证登录状态
        },
        path: 'bill',
        name: "UserBill",
        component: ()=> import("../components/user/Bill.vue"),
      },
    ]
  },
]

// 路由对象实例化
const router = createRouter({
  // history, 指定路由的模式
  history: createWebHistory(),
  // 路由列表
  routes,
});


// 导航守卫
router.beforeEach((to, from, next)=>{
  document.title = to.meta.title;
  order.loading = false;
  clearInterval(order.timer);
  // 登录状态验证
  if (to.meta.authorization && !store.getters.getUserInfo.user_id) {
    // 没有登录状态或者登录超时了，跳转到登录页面
    next({"name": "Login"});
  }else{
    next()
  }
})



// 暴露路由对象
export default router;