def additive_alphabet_ciper(a, k): # k -> key value
    c = ord(a) - 96
    b = 26 if (c + k) == 26 else (c + k) % 26 # 모듈로 연산을 통해 e(k를 더한 값이 26이어서 모듈로 연산에 의해 0인 경우) 예외
    print(chr(b + 64))

# for i in range(97, 123):
#   additive_alphabet_ciper(chr(i), 21)

def multiple_alphabet_ciper(a, k):
    c = ord(a) - 96
    b = 26 if (c * k) % 26 == 0 else (c * k) % 26 # 모듈로 연산의 값이 26일때 예외
    print(chr(b + 64))

# Bad KEY : 모듈로 연산의 제수의 약수는 키로 쓰이기 부적절함.

# for i in range(97, 123):
#   multiple_alphabet_ciper(chr(i), 3)

def euclidean_algorithm(a, b):
    print(a, b)
    r = a % b
    if r == 0: # 나머지가 0이라면
        print(b) # 나눈 수가 최대공약수
    else:
        euclidean_algorithm(b, r)

# euclidean_algorithm(26, 3)