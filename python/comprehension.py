# comprehension 예제 따라하기
# 참고: https://mingrammer.com/introduce-comprehension-of-python/#list-comprehension-lc

# 1. List Comprehension

# 1) 짝수 출력 (~20)
evens = [x*2 for x in range(11)]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# 2) 각 리스트의 원소들의 조합 출력
people = ['elle', 'john', 'jose', 'george']
jobs = ['programmer', 'teacher', 'singer', 'bus driver', 'doctor']

people_and_jobs = [(j, p) for j in jobs for p in people]
# [('programmer', 'elle'), ('programmer', 'john'), ('programmer', 'jose'), ('programmer', 'george'), ('teacher', 'elle'), ('teacher', 'john'), ('teacher', 'jose'), ('teacher', 'george'), ('singer', 'elle'), ('singer', 'john'), ('singer', 'jose'), ('singer', 'george'), ('bus driver', 'elle'), ('bus driver', 'john'), ('bus driver', 'jose'), ('bus driver', 'george'), ('doctor', 'elle'), ('doctor', 'john'), ('doctor', 'jose'), ('doctor', 'george')]

# 3) 단어에서 모음만 제거
word = 'mathematics'
without_vowels = ''.join([c for c in word if c not in ['a', 'e', 'i', 'o', 'u']])
# 'mthmtcs'

# 4) 2차원 행렬 1차원화
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
flatten = [e for r in matrix for e in r]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# 2. Set Comprehension

no_primes = [j for i in range(2, 9) for j in range(i * 2, 50, i)]
# [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 10, 15, 20, 25, 30, 35, 40, 45, 12, 18, 24, 30, 36, 42, 48, 14, 21, 28, 35, 42, 49, 16, 24, 32, 40, 48]

# list와 동일한 방법이지만 SC를 사용하면 중복값을 제외할 수 있음
no_primes = {j for i in range(2, 9) for j in range(i * 2, 50, i)}
# {4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49}

# 3. Dict Comprehension

# list든 tuple이든 하나의 dict으로 합침, 하나는 key, 나머지는 value로 사용함
# list 예제
subjects = ['PE', 'history', 'math']
grades = [100, 39, 49]

subjects_grades = {key: value for key, value in zip(subjects, grades)}
# {'PE': 100, 'history': 39, 'math': 49}

# tuple list 예제
grades_tuple = [('PE', 100), ('history', 39), ('math', 49)]
grades_dict = {t[0]: t[1] for t in grades_tuple}
# {'PE': 100, 'history': 39, 'math': 49}

# 4. Generator Expression
gen = (x**2 for x in range(10))
print(gen)
print(next(gen))
# gen은 한 번에 모든 원소를 반환하는 것이 아니라 한 번에 하나의 원소만 반환함

