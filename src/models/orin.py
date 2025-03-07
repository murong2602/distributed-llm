import json
import time
import requests
from models.server_manager import ServerManager

orin_ip = "10.96.184.122"  
local_port = 5000 
orin_port = 5000 
ssh_user = "orin" 
ssh_port = 30006

class Orin: 
    def __init__(self):
            self.server_manager = ServerManager(orin_ip, orin_port, local_port, ssh_user, ssh_port) 
            
    def process(self, query):
        """Routes a query to the Orin API."""
        if not self.server_manager.is_server_running():
            print("No running Orin server found, starting...")
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
#               {"role": "user", "content": "tell me about singapore in 20 words"}, {"role": "assistant", "content": "Singapore is a small island nation with a rich cultural heritage, vibrant city-state and cosmopolitan lifestyle."},{"role": "user", "content": "how small is it?"}
#                ]
#     orin = Orin()
    
#     # orin.server_manager.start_server()
#     # query = "tell me about singapore in 20 words"
#     # print(orin.process(query))
#     # response = orin.process(json.dumps(query))
#     # print(response)
#     orin.server_manager.stop_server()
    
    