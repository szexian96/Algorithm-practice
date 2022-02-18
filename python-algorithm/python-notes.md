1. +multiple input 1 line code+ (###!!!IMPORTANT###)
~~~
s = input()
my_nums = list(map(int,s.split()))
~~~
2. float to 2 decimal place

round(a_float, 2)

先try做完所有C的练习先

3. regex check
```
re.search('[a-zA-Z]', the_string)
```
4. replace vowel
```
vowels = 'aeiouAEIOU'
test_str = input()
for vowel in vowels:
    
    test_str = test_str.replace(vowel, "")

print(test_str)
```
5. lambda
~~~
x = lambda a: a + 10
print(x(5))

#output: 15
~~~

6. ** asterik
- [LINK HERE](https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/#Asterisks_for_unpacking_into_function_call)

7. empty lists create

```
lst = [[] for _ in xrange(a)]
```