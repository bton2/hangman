import random

def jogar_forca():
    # Lista de palavras
    palavras = ["python", "programacao", "desenvolvedor", "inteligencia", "computador"]
    
    # Escolhe palavra aleatória
    palavra_secreta = random.choice(palavras)
    
    # Cria lista com underscores para representar as letras
    letras_descobertas = ["_" for _ in palavra_secreta]
    
    # Define tentativas
    tentativas = 6
    letras_erradas = []

    print("=== Jogo da Forca ===")
    print(" ".join(letras_descobertas))

    # Loop do jogo
    while tentativas > 0 and "_" in letras_descobertas:
        print(f"\nTentativas restantes: {tentativas}")
        print(f"Letras erradas: {', '.join(letras_erradas)}")
        
        chute = input("Digite uma letra: ").lower()
        
        # Valida entrada
        if len(chute) != 1 or not chute.isalpha():
            print("Digite apenas uma letra!")
            continue
        
        if chute in letras_descobertas or chute in letras_erradas:
            print("Você já tentou essa letra!")
            continue

        # Verifica se a letra está na palavra
        if chute in palavra_secreta:
            for i, letra in enumerate(palavra_secreta):
                if letra == chute:
                    letras_descobertas[i] = letra
            print("Boa! Letra correta.")
        else:
            tentativas -= 1
            letras_erradas.append(chute)
            print("Letra errada!")
        
        print(" ".join(letras_descobertas))

    # Fim do jogo
    if "_" not in letras_descobertas:
        print("\nParabéns! Você venceu!")
    else:
        print(f"\nVocê perdeu! A palavra era: {palavra_secreta}")

# Executa o jogo
jogar_forca()

