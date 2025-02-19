import subprocess

def query_nano(prompt):
    result = subprocess.run(["ollama", "run", "tinyllama"], input=prompt.encode(), capture_output=True)
    return result.stdout.decode().strip()