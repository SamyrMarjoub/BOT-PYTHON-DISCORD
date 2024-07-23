import firebase_admin
from firebase_admin import credentials, firestore

# Caminho para o arquivo JSON da chave privada
cred = credentials.Certificate('firebasejson.json')

# Inicialize o aplicativo Firebase
firebase_admin.initialize_app(cred)

# Obtenha uma referência ao Firestore
db = firestore.client()

usuario_data = {
    'nome': 'João',
    'classe': 'Guerreiro',
    'level': 10,
    'itens': ['Espada', 'Escudo'],
    'armas': ['Espada Longa'],
    'skills': ['Ataque Poderoso', 'Defesa'],
    'equipamentos': {
        'capacete': 'Capacete de Ferro',
        'armadura': 'Armadura de Couro'
    }
}

# Adicionar o documento à coleção 'usuarios'
doc_ref = db.collection('usuarios').document('usuario1')
doc_ref.set(usuario_data)

print('Documento adicionado com sucesso!')