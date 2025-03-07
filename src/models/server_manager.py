import shlex
import time
import pexpect
import requests
import subprocess


class ServerManager:
    def __init__(self, device_ip, device_port, local_port, ssh_user, ssh_port):
        self.ssh_user = ssh_user
        self.device_ip = device_ip
        self.local_port = local_port
        self.device_port = device_port
        self.ssh_port = ssh_port
        self.ssh_tunnel = None

    def start_server(self):
        """Starts an SSH tunnel, activates virtualenv, and starts Flask on device."""
        ssh_cmd = f"ssh {self.ssh_user}@{self.device_ip} -p {self.ssh_port}"
        tunnel_cmd = f"ssh -fN -L {self.local_port}:localhost:{self.device_port} {self.ssh_user}@{self.device_ip} -p {self.ssh_port}"

        try:
            # Start SSH session with pexpect
            child = pexpect.spawn(ssh_cmd, encoding='utf-8', timeout=30)
            
            # Wait for shell prompt
            child.expect(r'\$')  # Wait for default shell prompt
            
            # Change directory
            child.sendline("cd murong")
            child.expect(r'\$')  # Wait for command completion
            
            # Activate virtual environment
            child.sendline("source venv/bin/activate")
            child.expect(r'\(venv\)')  # Wait for virtualenv prompt
            
            # Start Flask server with proper nohup
            child.sendline("nohup python3 -u api.py > flask.log 2>&1 &")
            child.expect(r'\$')  # Ensure command is accepted
            
            # Add verification
            child.sendline("pgrep -f 'python3 api.py'")
            child.expect(r'\d+')  # Look for process ID
            pid = child.match.group(0)
            print(f"Found running server with PID: {pid}")
            
            # Clean exit
            child.sendline("exit")
            child.expect(pexpect.EOF)
            
        except pexpect.EOF:
            print("EOF Error: Connection closed prematurely")
        except pexpect.TIMEOUT:
            print("Timeout Error: Command took too long")
            
        # Start SSH tunnel
        try:
            tunnel_process = subprocess.Popen(
                shlex.split(tunnel_cmd),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            time.sleep(2)  # Let tunnel establish
            print(f"Tunnel PID: {tunnel_process.pid}")
            return tunnel_process
        
        except Exception as e:
            print(f"Tunnel error: {str(e)}")

    def stop_server(self):
        """Stops the Flask server and tunnel reliably."""
        try:
            # First check if server process exists
            check_cmd = (
                f"ssh {self.ssh_user}@{self.device_ip} -p {self.ssh_port} "
                "'pgrep -f \"python3 -u api.py\"'"
            )
            result = subprocess.run(
                check_cmd,
                shell=True,
                capture_output=True,
                text=True
            )

            # If process exists (pgrep found something)
            if result.returncode == 0:
                print(f"Found running server with PIDs: {result.stdout.strip()}")
                # Now kill it gently
                kill_cmd = (
                    f"ssh {self.ssh_user}@{self.device_ip} -p {self.ssh_port} "
                    "'pkill -f \"python3 -u api.py\"'"
                )
                kill_result = subprocess.run(
                    kill_cmd,
                    shell=True,
                    capture_output=True,
                    text=True
                )
                
                if kill_result.returncode != 0:
                    print(f"Warning: Kill command exited with {kill_result.returncode}")
                    print(f"Stderr: {kill_result.stderr.strip()}")
            else:
                print("No running server process found")

            # Kill tunnel process using specific port pattern
            tunnel_kill = subprocess.run(
                f"pkill -f '{self.local_port}:localhost:{self.device_port}'",
                shell=True
            )
            
            if tunnel_kill.returncode == 0:
                print("SSH tunnel stopped successfully")
            else:
                print("No tunnel process found or error stopping")

        except Exception as e:
            print(f"Error during cleanup: {str(e)}")

    
    def is_server_running(self):
        """Checks if the Flask server is already running."""
        try:
            response = requests.get(f"http://localhost:{self.local_port}/")
            print(response.text)
            return response.status_code == 200
        except requests.ConnectionError:
            return False