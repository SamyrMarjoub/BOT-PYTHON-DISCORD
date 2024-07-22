from g4f.client import Client
import sys

def generate_text(prompt, max_tokens):
    client = Client()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um assistente útil para tudo, especialmente para criar cenarios de RPG e fantasia"},
            {"role": "user", "content": prompt},
        ],
        max_tokens=max_tokens,
      
    )
 
    content = response.choices[0].message.content
    
    return content

if __name__ == "__main__":
    prompt = sys.argv[1]
    max_tokens = int(sys.argv[2])
    min_tokens = int(sys.argv[3])
    result = generate_text(prompt, max_tokens)
    print(result)
