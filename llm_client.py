import cohere

# Initialize Cohere client
co = cohere.Client("API KEY")

def get_completion(prompt):
    response = co.generate(
        model='command-xlarge',  # Or 'command-medium' for smaller model
        prompt=prompt,
        max_tokens=100
    )
    return response.generations[0].text.strip()

# Test the model
prompt = "What is Alzheimer's disease?"
print(get_completion(prompt))

