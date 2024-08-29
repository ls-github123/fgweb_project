<template>
  <div class="title">
    <span :class="{active:user.login_type==0}" @click="user.login_type=0">密码登录</span>
    <span :class="{active:user.login_type==1}" @click="user.login_type=1">短信登录</span>
  </div>
  <div class="inp" v-if="user.login_type==0">
    <input v-model="user.account" type="text" placeholder="用户名 / 手机号码 / 邮箱" class="user">
    <input v-model="user.password" type="password" class="pwd" placeholder="密码">
    <div class="rember">
      <label>
        <input type="checkbox" class="no" v-model="user.rememberMe"/>
        <span>记住我</span>
      </label>
      <p>忘记密码</p>
    </div>
    <button class="login_btn" @click="show_captcha">登录</button>
    <p class="go_login" >没有账号 <router-link to="/register">立即注册</router-link><a :href="ddurl">钉钉</a></p>
  </div>
  <div class="inp" v-show="user.login_type==1">
    <input v-model="user.account" type="text" placeholder="手机号码" class="user">
    <input v-model="user.code"  type="text" class="code" placeholder="短信验证码">
    <el-button id="get_code" type="primary" @click="sendsms">获取验证码</el-button>
    <div class="rember">
      <label>
        <input type="checkbox" class="no" v-model="user.rememberMe"/>
        <span>记住我</span>
      </label>
      <p>忘记密码</p>
    </div>
    <button class="login_btn" @click="loginmobile">登录</button>
    <p class="go_login" >没有账号 <router-link to="/register">立即注册</router-link></p>

  </div>
</template>

<script setup>
import user from "../api/user";
import {ElMessage} from "element-plus";
import {useStore} from "vuex";
import "../utils/TCaptcha";
import settings from "../settings";
import {onMounted,ref}  from "vue"

const store = useStore()

const ddurl = ref('')

onMounted(() => {
   
  user.getddurl().then(res=>{
    ddurl.value = res.data.url
  })
 
})
const emit = defineEmits(["successhandle",])

const loginmobile =()=>{
    user.login({"mobile":user.account,'code':user.code}).then(res=>{
     
      if(res.data.code ==200){
        localStorage.setItem('userid',res.data.userid)
        localStorage.setItem('token',res.data.token)
      }
    })
}

const sendsms = ()=>{
  //验证手机号是否正确
  let reg = /^1[3-9]\d{9}$/
  if(!reg.test(user.account)){
    alert('手机号不对')
    return false;
  }
  user.send_sms().then(res=>{

    if(res.data.code == 200){
      alert("发送成功")
    }else{
      alert(res.data.message)
    }
  })
}
const show_captcha = ()=>{
  // 显示验证码
  let captcha1 = new TencentCaptcha(settings.captcha_app_id, (res)=>{
      // 在用户操作验证码成功以后，客户端执行接收验证结果的回调函数
      /* res（验证成功） = {ret: 0, ticket: "String", randstr: "String"}
         res（客户端出现异常错误 仍返回可用票据） = {ret: 0, ticket: "String", randstr: "String", errorCode: Number, errorMessage: "String"}
         res（用户主动关闭验证码）= {ret: 2}
      */
      console.log(res);
      // 如果返回结果不是0，则不需要继续调用登录处理操作
      if(res.ret !== 0){
        return
      }
      // 调用登录处理
      loginhandle(res);
  });
  captcha1.show(); // 显示验证码
}

const loginhandle = (res)=>{
  // 基于密码的登录处理
    // 验证数据
  if(user.account.length<1 || user.password.length<1){
    // 错误提示
    console.log("错了哦，用户名或密码不能为空！");
    ElMessage.error("错了哦，用户名或密码不能为空！");
    return; // 阻止代码继续往下执行
  }

  // 登录请求处理
  user.login_by_password(res).then(response=>{
    // 先删除从前的登录状态
    localStorage.removeItem("refresh_token");
    localStorage.removeItem("access_token");
    sessionStorage.removeItem("refresh_token");
    sessionStorage.removeItem("access_token");

    if(user.rememberMe){
      // 记住登录
      localStorage.setItem("refresh_token", response.data.refresh);
      localStorage.setItem("access_token", response.data.access);
    }else{
      // 不记住登录
      sessionStorage.setItem("refresh_token", response.data.refresh);
      sessionStorage.setItem("access_token", response.data.access);
    }

    // 记录购物车商品总数
    store.commit("set_cart_total", response.data.cart_total);

    // 把用户登录的载荷信息，保存到vuex中
    let payload = response.data.access.split(".")[1]  // 载荷
    let payload_data = JSON.parse(atob(payload)) // 用户信息
    console.log(payload_data)
    store.commit("login", payload_data)
    store.commit("remember", user.rememberMe);
    console.log("登录成功");
    ElMessage.success("登录成功！");

    // 关闭登录弹窗，对外发送一个登录成功的信息
    user.reset();
    emit("successhandle");


  }).catch(error=>{
    console.log(error);
    ElMessage.error("登录失败！");
  })

}

</script>

<style scoped>
.title{
    font-size: 20px;
    color: #9b9b9b;
    letter-spacing: 0.32px;
    border-bottom: 1px solid #e6e6e6;
    display: flex;
    justify-content: space-around;
    padding: 0px 60px 0 60px;
    margin-bottom: 20px;
    cursor: pointer;
}
.title span.active{
	color: #4a4a4a;
    border-bottom: 2px solid #84cc39;
}

.inp{
	width: 350px;
	margin: 0 auto;
}
.inp .code{
    width: 220px;
    margin-right: 16px;
}
#get_code{
   margin-top: 6px;
}
.inp input{
    outline: 0;
    width: 100%;
    height: 45px;
    border-radius: 4px;
    border: 1px solid #d9d9d9;
    text-indent: 20px;
    font-size: 14px;
    background: #fff !important;
}
.inp input.user{
    margin-bottom: 16px;
}
.inp .rember{
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: relative;
    margin-top: 10px;
}
.inp .rember p:first-of-type{
    font-size: 12px;
    color: #4a4a4a;
    letter-spacing: .19px;
    margin-left: 22px;
    display: -ms-flexbox;
    display: flex;
    -ms-flex-align: center;
    align-items: center;
    /*position: relative;*/
}
.inp .rember p:nth-of-type(2){
    font-size: 14px;
    color: #9b9b9b;
    letter-spacing: .19px;
    cursor: pointer;
}

.inp .rember input{
    outline: 0;
    width: 30px;
    height: 45px;
    border-radius: 4px;
    border: 1px solid #d9d9d9;
    text-indent: 20px;
    font-size: 14px;
    background: #fff !important;
    vertical-align: middle;
    margin-right: 4px;
}

.inp .rember p span{
    display: inline-block;
    font-size: 12px;
    width: 100px;
}
.login_btn{
    cursor: pointer;
    width: 100%;
    height: 45px;
    background: #84cc39;
    border-radius: 5px;
    font-size: 16px;
    color: #fff;
    letter-spacing: .26px;
    margin-top: 30px;
    border: none;
    outline: none;
}
.inp .go_login{
    text-align: center;
    font-size: 14px;
    color: #9b9b9b;
    letter-spacing: .26px;
    padding-top: 20px;
}
.inp .go_login span{
    color: #84cc39;
    cursor: pointer;
}
</style>