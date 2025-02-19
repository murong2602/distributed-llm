import pexpect
import time

orin_ip = "10.96.184.122"  
local_port = 5000 
orin_port = 5000 
ssh_user = "orin" 
ssh_port = 30006


import subprocess
import pexpect
import time

def start_ssh_tunnel():
    """Starts an SSH tunnel, activates virtualenv, and starts Flask on Orin."""

    ssh_cmd = f"ssh {ssh_user}@{orin_ip} -p {ssh_port}"
    tunnel_cmd = f"ssh -fN -L {local_port}:localhost:{orin_port} {ssh_user}@{orin_ip} -p {ssh_port}"

    print("Starting SSH connection to setup Flask server...")

    # Start SSH session with pexpect
    child = pexpect.spawn(ssh_cmd, encoding='utf-8', timeout=None)
    
    print("Successfully SSH-ed into Orin!")

    # Activate virtual environment
    child.sendline("source murong/venv/bin/activate")
    time.sleep(1)  # Allow activation to complete

    # Start Flask server in the background
    child.sendline("nohup python3 murong/api.py > flask.log 2>&1 &")
    time.sleep(2)  # Allow some time for Flask to start
    
    print("Flask server should now be running on Orin.")

    # Close the SSH session properly
    child.sendline("exit")
    # child.expect(pexpect.EOF)
    child.close()

    print("SSH session closed. Now starting the SSH tunnel.")

    # Start SSH tunnel in background
    tunnel_process = subprocess.Popen(
        tunnel_cmd,
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    print("SSH tunnel established, and Flask server is running in the background.")

    return tunnel_process

# Usage
child = start_ssh_tunnel()

# Now you can interact with the terminal session or monitor its output