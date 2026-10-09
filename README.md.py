```python
import time

def match():
    print("Match Calculator")
    
    n1 = input("Your name: ")
    n2 = input("Crush name: ")
    
    print("Calculating...")
    time.sleep(1)
    
    # podi logic ekak
    score = (len(n1) * len(n2) * 7) % 100
    
    print(f"\nResult: {n1} & {n2}")
    print(f"Score: {score}%")
    
    if score > 80:
        print("Sira maru match eka! ❤️")
    elif score > 50:
        print("Podi try ekak dila balapan 😉")
    else:
        print("Aiyooo sapa wenna epa machan 😂")

if __name__ == "__main__":
    match()
