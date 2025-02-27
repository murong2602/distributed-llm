import subprocess

class Nano:
    def __init__(self):
        self.model_name = "ollama/tinyllama" 
            
    def process(self, query):
        formatted_query = "\n".join(
            [f"{msg['role']}: {msg['content']}" for msg in query]
        )
        
        result = subprocess.run(
            ["ollama", "run", "tinyllama", formatted_query],
            input= "",
            capture_output=True,
            text=True
        )
        return result.stdout
