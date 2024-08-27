import axios from "axios"
import settings from "../settings";
import router from "../router"

const http = axios.create({
    // timeout: 2500,                          // 请求超时，有大文件上传需要关闭这个配置
    baseURL: settings.host, // 设置api服务端的默认地址[如果基于服务端实现的跨域，这里可以填写api服务端的地址，如果基于nodejs客户端测试服务器实现的跨域，则这里不能填写api服务端地址]
    withCredentials: false, // 是否允许客户端ajax请求时携带cookie
})

// 请求拦截器
http.interceptors.request.use((config) => {
    console.log("http请求之前");
    //获取token
    let token = localStorage.getItem('token')
    if (token) {
        config.headers.Authorization = localStorage.getItem('token')
    }

    return config;
}, (error) => {
    console.log("http请求错误");
    return Promise.reject(error);
});


// 响应拦截器
http.interceptors.response.use((response) => {
    return response;
}, (error) => {
    if (error.code === "ERR_NETWORK") {
        ElMessage.error("网络异常，无法请求服务端信息！");
    }
    if (error.response.status === 401) {
        ElMessage.error("未登录或登录超时！限制本次请求操作！请求登录后继续！");
        return router.push("/login");
    }

    return Promise.reject(error);
});

export default http;