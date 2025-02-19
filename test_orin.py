import requests

orin_ip = "10.0.1.8"  # Replace with your Orin's actual IP
url = f"http://{orin_ip}:5000/query"
query = "Explain quantum computing in simple terms"

payload = {
    "model": "llama3",
    "prompt": query
}

response = requests.post(url, json=payload)
print(response.json())  # Print response from Orin
