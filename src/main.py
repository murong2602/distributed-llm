from src.router import route_query

def main():
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = route_query(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()