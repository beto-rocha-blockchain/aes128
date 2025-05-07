# 🔐 AES-128 em Python

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![MIT License](https://img.shields.io/badge/license-MIT-green)

> Implementação didática do algoritmo de criptografia simétrica AES-128 em Python.

---

## 📌 Visão Geral

Este projeto oferece uma implementação simples e educacional do algoritmo AES-128, permitindo a criptografia e descriptografia de mensagens utilizando uma chave de 128 bits. É ideal para estudantes e entusiastas que desejam compreender os fundamentos da criptografia simétrica.

---

## 🧩 Estrutura do Projeto

   ```bash
   aes128/
   ├── main.py # Interface principal para execução
   ├── aes_utils.py # Funções auxiliares para criptografia e descriptografia
   ├── requirements.txt # Dependências do projeto
   ├── LICENSE # Licença MIT
   └── README.md # Documentação do projeto
   ```

---

## 🚀 Como Utilizar

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/beto-rocha-blockchain/aes128.git
   cd aes128
   ```
2. **Instale as dependências:**

  ```bash
  pip install -r requirements.txt
  ```

3. **Execute o script principal:**

  ```bash
  python main.py
  ```
   >Siga as instruções no terminal para criptografar ou descriptografar mensagens.

## 🧠 Exemplo de Uso

   ```bash
   from aes_utils import encrypt, decrypt

   chave = 'minha_chave_128b'  # Deve ter 16 caracteres
   mensagem = 'Olá, mundo!'

   mensagem_criptografada = encrypt(mensagem, chave)
   print(f'Mensagem criptografada: {mensagem_criptografada}')

   mensagem_original = decrypt(mensagem_criptografada, chave)
   print(f'Mensagem original: {mensagem_original}')
   ```

## 📚 Recursos Adicionais

- Documentação do AES (NIST)
- Artigo sobre Criptografia Simétrica
- Implementação em C para comparação

## 📄 Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais detalhes.

## 🙋‍♂️ Contribuindo
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests para melhorias, correções ou sugestões.
