num1= (int(i) for i in input().split())
num2 = (int(k) for k in input().split())

def cosine_similarity(num1, num2):
    dp = sum(a * b for a, b in zip(num1, num2))  
    norm_num1 = sum(a**2 for a in num1) ** 0.5  
    norm_num2 = sum(b**2 for b in num2) ** 0.5  
    return dp / (norm_num1 * norm_num2)