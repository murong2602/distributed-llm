import json
from litellm import token_counter

class TokenCounter:
    def count_tokens(self, msg):
        """Counts tokens for a single message."""
        msg_payload = [{"role": msg["role"], "content": json.dumps(msg)}]
        return token_counter(model="ollama/llama2", messages=msg_payload)

    def get_context_size(self, context):
        """Gets token count for the last 5 messages."""
        return sum(self.count_tokens(msg) for msg in context)



# if __name__ == "__main__":
#     counter = TokenCounter()
#     conversation_history = [{"role": "user", "content": "tell me about singapore in 20 words"},
#     {"role": "assistant", "content": "Singapore is a small island nation with a rich cultural heritage, vibrant city-state and cosmopolitan lifestyle."},
#     {"role": "user", "content": "how small is it?"}]
#     print(counter.get_context_size(conversation_history))