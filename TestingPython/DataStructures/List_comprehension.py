
# Simple way to declare lists:
pow2 = [2 ** x for x in range(10)]

# Output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
print(pow2)

pow2 = [2 ** x for x in range(10) if x > 5]
print(pow2)


odd_numbers = [x for x in range(20) if x % 2 == 1]
print(odd_numbers)

cross_combination = [first + second for first in ['Alpha','Beta', 'Gamma'] for second in ['one','two', 'three']]
print(cross_combination)