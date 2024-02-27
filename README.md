# Jogo da Forca em Python

Este é um simples jogo da forca em Python. O jogo escolhe aleatoriamente uma palavra de um arquivo chamado `palavras.txt` e o jogador tenta adivinhar a palavra.

## Funções

### `lerPalavraArquivo`

- Gera um valor aleatório.
- Lê as palavras do arquivo `palavras.txt` e as armazena em uma lista.
- Retorna uma palavra aleatória da lista.

### `contarCaracteres`

- Aceita uma palavra como entrada.
- Retorna o número de caracteres na palavra.

### `pintar_palavra`

- Aceita uma palavra e uma cor como entrada.
- Imprime a palavra na cor especificada.

### `pintar_palavra_multicolorida`

- Aceita uma palavra e uma lista de cores como entrada.
- Imprime a palavra com cada caractere colorido de acordo com a lista de cores.

### `verificaPalpite`

- Aceita um palpite e a palavra secreta como entrada.
- Compara o palpite com a palavra, destacando corretamente os caracteres corretos e incorretos.
- Retorna 1 se o palpite for igual à palavra secreta, indicando uma vitória.

## Como Jogar

1. Clone ou baixe o repositório.
2. Certifique-se de ter o Python instalado em sua máquina.
3. Execute o script `main.py`.
4. Tente adivinhar a palavra secreta fornecendo palpites.
5. As letras corretas serão destacadas em verde, letras corretas no local errado em amarelo, e letras erradas em vermelho.

**Nota:** Certifique-se de ter um arquivo `palavras.txt` com palavras separadas por ponto e vírgula para que o jogo funcione corretamente.

**OBS:** Futuramente pretendo atualizar, isso é só um rascunho da maneira que o mesmo vai funcionar.

---

**Dica:** Personalize este README conforme necessário, incluindo informações adicionais, regras específicas do jogo ou qualquer outra coisa relevante ao contexto do seu código.
