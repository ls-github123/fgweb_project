import {createStore, mapMutations} from "vuex"
import createPersistedState from "vuex-persistedstate"
// 实例化一个vuex存储库
export default createStore({
    // 调用永久存储vuex数据的插件，localstorage里会多一个名叫vuex的Key，里面就是vuex的数据
    plugins: [createPersistedState()],
    state () {  // 数据存储位置，相当于一个超全局的组件中的data
        return {
          user: {}, // 用户信息
          remember_me: true,  // 是否记住登录状态
          cart_total: 0, // 购物车中的商品总数
        }
    },
    mutations: { // 操作数据的方法，相当于一个超全局的组件中methods
        login (state, user) {  // state 就是上面的state   state.user 就是上面的数据
          state.user = user
        },
        remember(state, remember){
          state.remember_me = remember;
        },
        logout(state){ // 退出登录
            state.user = {}
            state.remember_me = false;
            localStorage.removeItem("access_token");
            localStorage.removeItem("refresh_token");
            sessionStorage.removeItem("access_token");
            sessionStorage.removeItem("refresh_token");
        },
        set_cart_total(state, cart_total){ // 设置商品数量
            state.cart_total = cart_total;
        }
    },
    getters: {  // 计算属性的方法，相当于一个超全局的组件中computed
        getUserInfo(state){
            // 从jwt的载荷中提取用户信息
            let now = parseInt( (new Date() - 0) / 1000 );
            if(state.user.exp === undefined) {
                // 没登录
                state.user = {}
                localStorage.removeItem("access_token");
                localStorage.removeItem("refresh_token");
                sessionStorage.removeItem("access_token");
                sessionStorage.removeItem("refresh_token");
            }

            if(parseInt(state.user.exp) < now) {
                // 过期处理
                state.user = {}
                localStorage.removeItem("access_token");
                localStorage.removeItem("refresh_token");
                sessionStorage.removeItem("access_token");
                sessionStorage.removeItem("refresh_token");
            }
            return state.user;
        }
    },
})