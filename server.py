import socket
import threading

# 保存在线客户端
client_list = []

def handle_client(conn, addr):
    print(f"新客户端接入：{addr}")
    client_list.append(conn)
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            msg = data.decode("utf-8")
            print(f"收到 {addr}：{msg}")
            # 广播给所有在线客户端
            for c in client_list:
                try:
                    c.sendall(f"{addr}: {msg}".encode("utf-8"))
                except:
                    pass
        except Exception as e:
            print(f"连接异常 {addr}: {e}")
            break
    conn.close()
    client_list.remove(conn)
    print(f"客户端下线：{addr}")

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("127.0.0.1", 8888))
    server_socket.listen(5)
    print("TCP聊天服务端启动，监听 127.0.0.1:8888")
    while True:
        conn, addr = server_socket.accept()
        t = threading.Thread(target=handle_client, args=(conn, addr))
        t.daemon = True
        t.start()

if __name__ == "__main__":
    main()
