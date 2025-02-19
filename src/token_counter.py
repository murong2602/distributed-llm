from litellm import token_counter

def count_tokens(msg):
    msg_payload = [{"role": "user", "content": msg}]
    return token_counter(model="ollama/llama2", messages=msg_payload)

# count tokens with context of past 5 messages 
def get_context_size(conversation_history):
    return sum(count_tokens(msg) for msg in conversation_history[-5:])  # Last 5 messages

# if get_context_size(conversation_history) > 2048:  
#     send_to_orin(full_context)
# else:
#     process_on_nano(full_context)