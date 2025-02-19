from token_counter import count_tokens
from models.nano import query_nano
from models.orin import query_orin

TOKEN_THRESHOLD = 100  # Example threshold

def route_query(user_input):
    token_count = count_tokens(user_input)
    if token_count <= TOKEN_THRESHOLD:
        return query_nano(user_input)
    else:
        return query_orin(user_input)