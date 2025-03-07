import requests
from models.server_manager import ServerManager

nano_ip = "192.168.1.87"  
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
            print("server is not running")
            self.server_manager.start_server()


        url = f"http://localhost:{self.server_manager.local_port}/query"
        payload = {"query": query}
        print(payload)

        try:
            response = requests.post(url, json=payload)
            print(f"Response status: {response.status_code}, Response text: {response.text}")
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
    
    