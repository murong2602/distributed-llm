from token_counter import TokenCounter
from models.orin import Orin
from models.nano import Nano

class Router:
    def __init__(self):
        self.token_counter = TokenCounter()
        self.orin = Orin()
        self.nano = Nano()

    def route_query(self, conversation_history):
        """Decides whether to process the query on Orin or Nano."""
        context = conversation_history[-5:]
        context_size = self.token_counter.get_context_size(context)

        print("Context size = ", context_size, "tokens")

        if context_size > 100:
            print("Context size too large, routing to Orin...")
            return self.orin.process(context)
        else:
            return self.nano.process(context)
        