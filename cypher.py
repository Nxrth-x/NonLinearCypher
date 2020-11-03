import random

def Non_Linear_Ceasar_Cypher(word: str) -> str:
     arr = [random.randint(1, 5) for i in range(5)]
     ans = "".join(chr(element+96) for element in arr)
     for index, letter in enumerate(word):
          ans += chr(ord(letter) + arr[index%5])
     return ans

def Reverse_Non_Linear_Ceasar_Cypher(word: str) -> str:
     arr: list = [int(ord(word[i])-96) for i in range(5)]
     word: str = word[5:]
     
     ans: str = ""
     for index, letter in enumerate(word):
          ans += chr(ord(letter) - arr[index%5])
     return ans

palavra = input("\nMENSAGEM\nDigite: ")

cifrada: str = Non_Linear_Ceasar_Cypher(palavra)
print(f"\nCIFRADA:\n{cifrada}")

decifrada: str = Reverse_Non_Linear_Ceasar_Cypher(cifrada)
print(f"\nDECIFRADA:\n{decifrada}\n")