import socket
import threading

def recv_msg(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                print("服务器断开连接")
                break
            print("\n" + data.decode("utf-8"))
        except:
            break

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 8888))
    # 开启子线程持续接收消息
    t = threading.Thread(target=recv_msg, args=(s,))
    t.daemon = True
    t.start()
    print("连接成功，可以发消息了！")
    while True:
        msg = input()
        s.sendall(msg.encode("utf-8"))

if __name__ == "__main__":
    main()
