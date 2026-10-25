tcp-socket-chat
Python Socket 实现TCP简易聊天室，包含服务端、客户端，支持消息广播，练习TCP网络编程、多线程。

功能清单
- 服务端监听端口，接收多个客户端连接
- 客户端发送消息，服务端广播给所有在线用户
- 多线程处理多个客户端并发通信

技术栈
Python3，socket、threading 内置库，无第三方依赖

运行方式
1. 先启动服务端
```bash
python server.py
2.新开终端，启动客户端（可以开多个终端模拟多人）
python client.py
项目结构
├── server.py     # TCP服务端
├── client.py     # TCP客户端
├── README.md
