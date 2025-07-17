import socket
import threading

DECODE = 'utf-8'
class Loadbalancer():
    
    servers = [('172.16.82.36',3000),('172.16.82.36',3001)]
    
    def __init__(self,ip,port):
        self.current_server = 0
        self.port = port
        self.ip = ip
     
    def get_next_available_server(self):
        attempts = 0
        total_servers = len(self.servers)

        while attempts < total_servers:
            server = self.servers[self.current_server]
            self.current_server = (self.current_server + 1) % total_servers

            try:
                test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                test_socket.settimeout(1)  
                test_socket.connect(server)
                test_socket.close()
                return server 
            except:
                attempts += 1
                continue

        return None 

        
    def forward(self,source,destrination):
        try :
            while True:
                data = source.revc(4096)

                if not data:
                    break
                destrination.sendall(data)

        finally :
            source.close
            destrination.close()        
        
    def start(self):
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as cs:
            cs.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
            cs.bind((self.ip,self.port))
            cs.listen(5)
            print(f"load balancer is now listning on {self.ip}:{self.port}")
    
            while True:
                client_sock,addr = cs.accept()
                print(f"accepted connection from {addr}")

                server = self.get_next_available_server()

                if not server:
                    print("No server is available at this perticular time")
                    client_sock.close()
                    continue
                
                backend_ip, backend_port = server

                
                with socket.socket(socket.AF_INET,socket.SO_REUSEADDR) as backend_socket:
                    try :
                        backend_socket.connect((backend_ip,backend_port))
                        print(f"Connected to backend server at {backend_ip}:{backend_port}")
                        
                        threading.Thread(target=self.forward ,args=(cs,backend_socket))
                        threading.Thread(target=self.forward ,args=(backend_socket,cs))
                        
                        
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
