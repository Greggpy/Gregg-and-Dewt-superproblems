from app.fizzbuzz import fizzbuzz

def test_fizzbuzz():
    assert fizzbuzz(3) == ["1","2","Fizz"]

    assert fizzbuzz(5) == ["1","2","Fizz","4","Buzz"]

    assert fizzbuzz(15) == ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]