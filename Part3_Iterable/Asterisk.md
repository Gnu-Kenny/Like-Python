# Asterisk(\*)

> - 곱셈 및 거듭제곱 연산
> - 리스트형 컨테이너 타입 데이터 반복 확장
> - 가변인자
> - Unpacking

## 1. 곱셈 및 거듭제곱 연산

    2 * 3 = 6

<br>

## 2. 리스트형 컨테이너 타입의 데이터를 반복 확장하고자 할 때

```python
zeros_list = [0] * 100
# 길이 100의 제로값 리스트 초기화
```

```python
vector_list = [[1, 2, 3]]
for i, vector in enumerate(vector_list * 3):
    print("{0} scalar product of vector: {1}".format(
    (i+1), [(i + 1)*e for e in vector]))
# 1 scalar product of vector: [1, 2, 3]
# 2 scalar product of vector: [2, 4, 6]
# 3 scalar product of vector: [3, 6, 9]
```

<br>

## 3. 가변인자 (Variadic Arguments) 매개변수의 갯수를 동적으로 받을 수 있음

- ### p**ositional arguments** : 위치에 따라 정해지는 인자

- ### **keyword arguments** : 이름을 가진 인자

<br>

## positional arguments(\*)

```python
def save_ranking(*args):
    print(args)

save_ranking('ming', 'alice', 'tom', 'wilson', 'roy')
```

## keyword arguments(\*\*)

```python
def save_ranking(**kwargs):
    print(kwargs)

save_ranking(first='ming', second='alice',
fourth='wilson', third='tom', fifth='roy')
```

<br>

## 4. 컨테이너 타입의 데이터를 Unpacking 할 때

> 우리가 list나 tuple 또는 dict 형태의 데이터를 가지고 있고
> 어떤 함수가 가변인자를 받는 경우에 그 요소를 출력

```python
primes = [2, 3, 5, 7, 11, 13]

def product(_numbers):
    p = reduce(lambda x, y: x _ y, numbers) # 집계 함수
    return p

product(*primes)
# 30030

product(primes)
# [2, 3, 5, 7, 11, 13]
```
