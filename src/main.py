from router import Router

class Chatbot:
    def __init__(self):
        self.router = Router()
        self.conversation_history = []

    def add_message(self, role, content):
        """Stores conversation history."""
        self.conversation_history.append({"role": role, "content": content})

    def chat(self):
        """Main chat loop."""
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit"]:
                self.router.orin.server_manager.stop_server()
                self.router.nano.server_manager.stop_server()
                break

            self.add_message("user", user_input)
            response = self.router.route_query(self.conversation_history)
            self.add_message("assistant", response)

            print(f"Assistant: {response.get('response', 'No response available')}")

if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.chat()