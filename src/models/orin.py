import subprocess
import requests
import pexpect
import time

orin_ip = "10.96.184.122"  
local_port = 5000 
orin_port = 5000 
ssh_user = "orin" 
ssh_port = 30006

def start_orin_server():
    """Starts an SSH tunnel, activates virtualenv, and starts Flask on Orin."""

    ssh_cmd = f"ssh {ssh_user}@{orin_ip} -p {ssh_port}"
    tunnel_cmd = f"ssh -fN -L {local_port}:localhost:{orin_port} {ssh_user}@{orin_ip} -p {ssh_port}"

    print("Starting SSH connection to setup Flask server...")

    # Start SSH session with pexpect
    child = pexpect.spawn(ssh_cmd, encoding='utf-8', timeout=None)

    # Activate virtual environment
    child.sendline("source murong/venv/bin/activate")
    time.sleep(1) 

    # Start Flask server in the background
    child.sendline("nohup python3 murong/api.py > flask.log 2>&1 &")
    time.sleep(2) 

    # Close the SSH session properly
    child.sendline("exit")
    child.close()

    # Start SSH tunnel in background
    tunnel_process = subprocess.Popen(
        tunnel_cmd,
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    print("SSH tunnel established, and Flask server is running in the background.")

    return tunnel_process


def query_orin(prompt):
    """Sends a query to the Orin API server."""
    ssh_tunnel = start_orin_server() 
    time.sleep(3) # Wait for the tunnel to be established
    url = f"http://localhost:{local_port}/query"  # Use localhost since the tunnel forwards to Orin
    payload = {
        "model": "llama3", 
        "query": prompt
    }
    
    try:
        response = requests.post(url, json=payload)
        
        if not response.text:
            return {"error": "Empty response from Orin API"}
        return response.json()
    except requests.exceptions.ConnectionError:
        return {"error": "Could not connect to Orin API"}


if __name__ == "__main__":
    response = query_orin("Hello, Orin!")
    print(response)
    