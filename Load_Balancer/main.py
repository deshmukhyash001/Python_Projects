import socket

DECODE = 'utf-8'
class Loadbalancer():
    servers = [('172.16.82.36',3000),('172.16.82.36',3001)]
    
    def __init__(self,ip,port):
        self.port = port
        self.ip = ip
        
    def start(self):
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as cs:
            cs.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
            cs.bind((self.ip,self.port))
            cs.listen(5)
            print(f"load balancer is now listning on {self.ip}:{self.port}")
    
            while True:
                client_sock,addr = cs.accept()
                print(f"accepted connection from {addr}")

                backend_ip,backend_port = self.servers[0]
                
                with socket.socket(socket.AF_INET,socket.SO_REUSEADDR) as backend_socket:
                    try :
                        backend_socket.connect((backend_ip,backend_port))
                        print(f"Connected to backend server at {backend_ip}:{backend_port}")
                        
                        backend_socket.sendall(b"Hello from load balancer ")
                        responce = backend_socket.recv(1024)
                        print(f"received from backend : {responce.decode(DECODE)}")
                        
                    except Exception as e:
                        print(f"failed connect backend {e}")
                
                cs.close()
                
    def cs(self):
        pass
    
def main():
    Loadbalancer('127.0.0.1',2000,).start()
    print("load balancer is started")

if __name__ == '__main__':
    main()
