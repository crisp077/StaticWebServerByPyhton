"""
    @File      : 01_静态Web服务器_返回固定页面数据.py
    @Software  : PyCharm
    @Author    : Crisp077
    @CreateTime: 2022/9/4 15:37
"""

import socket

if __name__ == '__main__':
    # 1. 编写一个 TCP 服务端程序
    # 创建 socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口复用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 绑定地址
    tcp_server_socket.bind(("", 8888))
    # 设置监听
    tcp_server_socket.listen()
    while True:
        # 2. 获取浏览器发送的 HTTP 请求报文数据
        client_socket, client_addr = tcp_server_socket.accept()
        # 获取浏览器的请求信息
        client_request_data = client_socket.recv(1024).decode()
        # 打印请求报文
        print(client_request_data)
        # 3. 读取固定页面数据，把页面数据组装成 HTTP 响应报文数据发送给浏览器
        with open("./static/index.html", "rb") as f:
            file_data = f.read()

        # 应答行
        response_line = "HTTP/1.1 200 OK\r\n"
        # 应答头
        response_header = "Server:PythonWeb\r\n"
        # 应答体
        response_body = file_data
        # 组装数据
        response_data = (response_line + response_header + "\r\n").encode() + response_body
        # 发送数据
        client_socket.send(response_data)
        # 4. HTTP 响应波阿文数据发送完成以后，关闭服务于客户端的套接字
        client_socket.close()
