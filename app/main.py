import os
import openai
import argparse

MAX_LENGTH = 25

# Load API key from an environment variable or secret management service
def load_and_check_api_key():
    if os.getenv("OPENAI_API_KEY") not in [None, ""]:
        openai.api_key = os.getenv("OPENAI_API_KEY")
        return True
    return False

def validate_input(user_input):
    if len(user_input) > MAX_LENGTH:
        print(f"Max Length Allowed: {MAX_LENGTH}")
        exit()
    if (user_input == ""):
        print("Please enter a value")
        exit()

def show_snippet(response):
    if (response["choices"][0]["finish_reason"] != "stop"):
        snippet = response["choices"][0]["text"] + "..."
        print(f"\nSnippet: {snippet}")
    else:
        snippet = response["choices"][0]["text"]
        print(f"\nSnippet: {snippet}")

def generate_snippet(user_input):
    validate_input(user_input)
    is_key = load_and_check_api_key()
    if is_key == False:
        print("API Key not found")
        exit()

    print(f"Value: {user_input}")
    print("Generating snippet...")

    subject = user_input

    prompt = f"Generate branding snippet for {subject}"

    response = openai.Completion.create(model="text-davinci-002", prompt=prompt, temperature=0, max_tokens=100)

    show_snippet(response)

def get_input():
    parse = argparse.ArgumentParser()
    parse.add_argument("--input", "-i", type=str, required=True)
    args = parse.parse_args()
    user_input = args.input
    return user_input

def main():
    user_input = get_input()
    generate_snippet(user_input)

if __name__ == "__main__":
    main()