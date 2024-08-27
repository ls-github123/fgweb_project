<template>
  <div>
  <ul>
  {{meslist}}
  <li v-for="i in meslist">{{i.userid}}{{i.message}}</li>
  </ul>
  <div id='message'></div>
  <el-input v-model="sendms"></el-input>
  <el-button @click='submit'>提交</el-button>
  </div>
</template>

<script>
export default {
    data(){
        return{
            socket:null,
            sendms:'',
            chatname:'',
            meslist:[]

        }
    },
    methods: {
        submit(){
            // this.meslist.push({"key":this.chatname+"说:","value":sendms})
            this.socket.send(JSON.stringify({"userid":this.chatname+"说:",'message':this.sendms}))
        },
        initweb(){
          this.chatname = this.$route.query.id
        
            // 创建websocket对象，向后台发送请求
 this.socket = new WebSocket("ws://localhost:8000/room/"+this.chatname+"/");

// 当客户端和服务端刚创建好连接(self.accept)之后，自动触发.
this.socket.onopen = function (event){
  let tag = document.createElement("div");
  tag.innerText = "[连接成功]";
  document.getElementById("message").appendChild(tag);
}

// 回调函数，客户端接收服务端消息
this.socket.onmessage =  (event)=>{
  alert("33")
//   let tag = document.createElement("div");
//   tag.innerText = event.data;
//   document.getElementById("message").appendChild(tag);
     var mes = JSON.parse(event.data)
     this.meslist.push(mes)
}

// 当断开连接时，触发该函数
this.socket.onclose =function (event){
  let tag = document.createElement("div");
  tag.innerText = "[连接断开]";
  document.getElementById("message").appendChild(tag);
}

// function sendMessage(){
//   let tag = document.getElementById("txt");
//   socket.send(tag.value);
// }

// function closeMessage(){
//   socket.close();
// }

// function handleKeyPress(event){
//   if (event.keyCode === 13){
//     document.getElementById("send").click();
//     document.getElementById("txt").value = "";
//   }
// }

// document.onkeydown = handleKeyPress;

        }
    },

    mounted() {
        this.initweb()
    },

}
</script>

<style>

</style>