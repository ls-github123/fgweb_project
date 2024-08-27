import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import AutoImport from 'unplugin-auto-import/vite'
import Components from 'unplugin-vue-components/vite'
import { ElementPlusResolver } from 'unplugin-vue-components/resolvers'


// https://vitejs.dev/config/
export default defineConfig({
    plugins: [
        vue(),
        AutoImport({
            resolvers: [ElementPlusResolver()],
        }),
        Components({
            resolvers: [ElementPlusResolver()],
        }),
    ],
    server: {
        port: '3000', // 客户端的运行端口，此处也可以绑定vue运行的端口，当然也可以写在pycharm下
        host: '127.0.0.1', // 客户端的运行地址，此处也可以绑定vue运行的域名，当然也可以写在pycharm下
        // 跨域代理
        // proxy: {
        //     '/api': {
        //         // 凡是遇到 /api 路径的请求，都映射到 target 属性  /api/home/test/  ---> http://api.fuguang.cn:8000/home/test/
        //         target: 'http://api.fuguang.cn:8000/',
        //         changeOrigin: true,
        //         ws: true,    // 是否支持websocket跨域
        //         rewrite: path => path.replace(/^\/api/, '')
        //     }
        // }
    }
})