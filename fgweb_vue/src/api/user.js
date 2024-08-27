import { reactive } from "vue";
import http from "../http";

const user = reactive({
    login_type: 0, // 登录类型，0表示密码登录，1表示验证码登录
    account: "", // 用户名，邮箱，手机号
    password: "", // 密码
    re_password: "", // 确认密码
    code: "", // 验证码
    rememberMe: false, // 是否记住登录状态
    is_send: false, // 是否处于发送短信冷却状态中
    sms_interval: 60, // 发送短信的冷却时间
    interval: null, // 定时器的唯一标记符
    sms_btn_text: "点击获取验证码",

    login_by_password(res) {
        // 基于密码的登录处理
        return http.post("/users/jwt/access/", {
            ticket: res.ticket,
            randstr: res.randstr,
            username: this.account,
            password: this.password,
        })
    },
    check_mobile() {
        // 验证手机号是否已注册（唯一性校验）
        return http.get(`/users/mobile/${this.account}/`)
    },
    register(res) {
        // 注册处理
        return http.post("/users/register/", {
            ticket: res.ticket,
            randstr: res.randstr,
            mobile: this.account,
            password: this.password,
            re_password: this.re_password,
            sms_code: this.code,
        })
    },
    login(data) {
        return http.post('login/', data)
    },
    getddurl() {
        return http.get('getddurl/')
    },
    reset() {
        // 重置信息
        // 关闭登录弹窗，对外发送一个登录成功的信息
        this.account = ""
        this.password = ""
        this.re_password = ""
        this.code = ""
        this.rememberMe = false
    },
    send_sms() {
        // 发送短信验证码
        return http.get(`users/sendsms/${this.account}/`)
    },
});

export default user;