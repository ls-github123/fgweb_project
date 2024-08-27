<template>
  <div>
  <div>
  <ul>
  
  <li v-for="i  in allmes"> {{i.name}} 
  <p v-if="i.flag == true">正常</p>
  <p v-else>异常</p></li>
  </ul>
  </div>
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
            allmes:[],

        }
    },
  

    methods: {
        submit(){
            this.socket.send("23423423")
        },
        //获取所有信息
        getmes(){
          this.allmes=[{"id":1,'name':'A大鹏','flag':true},{"id":2,'name':'B大鹏','flag':true}]
        },
        initweb(){

          this.chatname = 2
        //   alert(this.chatname)
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
  var data = JSON.parse(event.data)
  this.allmes.forEach(element => {
    if(element['id'] == data['id']){
      element['flag'] = false
    }
  });
  // let tag = document.createElement("div");
  // tag.innerText = event.data;
  // if(event.data.flag == false){
  //       allmes.forEach(element => {
  //           if(element.id == event.data.id){
  //               element.value = false
  //           }
  //       });
  // }

  // document.getElementById("message").appendChild(tag);
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
        this.getmes()
    },

}
</script>

<style>

</style>