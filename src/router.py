from enum import Enum
from token_counter import TokenCounter
from models.orin import Orin
from models.nano import Nano


class Router:
    def __init__(self, threshold=100):
        self.token_counter = TokenCounter()
        self.orin = Orin()
        self.nano = Nano()
        self.threshold = threshold
    
    def set_threshold(self, threshold):
        """Sets the context threshold for routing."""
        self.threshold = threshold

    def route_query(self, conversation_history):
        """Decides whether to process the query on Orin or Nano."""
        context = conversation_history
        context_size = self.token_counter.get_context_size(context)

        print("Context size = ", context_size, "tokens")

        if context_size > self.threshold:
            print("Processing query on Orin")
            response = self.orin.process(context)
            response_tokens = self.token_counter.count_tokens({"role": "assistant", "content": response["response"]})
            return response, response_tokens, "orin"
        else:
            print("Processing query on Nano")
            response = self.nano.process(context)
            response_tokens = self.token_counter.count_tokens({"role": "assistant", "content": response["response"]})
            return response, response_tokens, "nano"
        