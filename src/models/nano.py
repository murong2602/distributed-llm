import requests
from models.server_manager import ServerManager

# home: 192.168.1.83
# school: 172.20.238.177
nano_ip = "192.168.1.84"  
local_port = 5001 
nano_port = 5001
ssh_user = "nano" 
ssh_port = 22

class Nano: 
    def __init__(self):
            self.server_manager = ServerManager(nano_ip, nano_port, local_port, ssh_user, ssh_port) 
            
    def process(self, query):
        """Routes a query to the nano API."""
        if not self.server_manager.is_server_running():
            print("No running Nano server found, starting...")
            self.server_manager.start_server()


        url = f"http://localhost:{self.server_manager.local_port}/query"
        payload = {"query": query}

        try:
            response = requests.post(url, json=payload)
            return response.json() if response.text else {"error": "Empty response"}
        except Exception as e:
            return {"error": f"Request failed: {str(e)}"}
    
    

# if __name__ == "__main__":
#     query = [
#               {"role": "user", "content": "what is 1+1"},
#     ]
#     nano = nano()
    
#     print(nano.process(query))
#     nano.server_manager.stop_server()
    
    