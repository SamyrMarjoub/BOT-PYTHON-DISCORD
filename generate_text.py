from g4f.client import Client
import sys

def generate_random_event(prompt, max_tokens):
    client = Client()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f'Você é um narrador em terceira pessoa em um mundo de fantasia. \
             Gere eventos aleatórios com base nas informações dos \
             usuários (nome, status, armas, localização). Crie eventos onde eles podem ganhar ou perder algo. \
             Importante: você NÃO dará escolhas aos usuários, apenas narrará o que aconteceu e o resultado. Importante também: "Não GERE respostas INCOMPLETAS!. \
              Dados do usuario: {prompt}'},
        ],
        max_tokens=max_tokens,
    )

    content = response.choices[0].message.content
    
    return content

def get_random_event_results(prompt, max_tokens):
    client = Client()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f'Você é um narrador em terceira pessoa em um mundo de fantasia. \
             Você vai pegar o prompt do usuario e vai o analisar, caso o usuario tenha perdido algo\
             (HP, MP, OURO, ARMAS ou EQUIPAMENTOS, ITENS etc) ou caso o usuario ganhe algo (Ouro, itens, armas, skills, equipamentos etc) \
              vc vai separar e fazer uma lista. \
            Importante também: "Não GERE respostas INCOMPLETAS!". Prompt: {prompt}.'},
        ],
        max_tokens=max_tokens,
    )

    content = response.choices[0].message.content
    
    return content


if __name__ == "__main__":
    prompt = sys.argv[1]
    max_tokens = int(sys.argv[2])
    result = generate_random_event(prompt, max_tokens)
    print(result)
