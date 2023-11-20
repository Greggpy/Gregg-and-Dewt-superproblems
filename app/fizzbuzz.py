def fizzbuzz(n):
    answer = []
    for i in range(n+1):
        if i == 0:
            pass
        elif (i % 3 == 0) and (i % 5 == 0):
            answer.append('FizzBuzz')
        elif i % 3 == 0:
            answer.append('Fizz')
        elif i % 5 == 0:
            answer.append('Buzz')
        else:
            answer.append(f'{i}')
    return answer