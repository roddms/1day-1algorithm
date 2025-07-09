N = int(input())

target = 1000 - N


# 큰 값의 동전을 먼저 처리해야함
use500 = target // 500
target %= 500

use100 = target // 100
target %= 100

use50 = target // 50
target %= 50

use10 = target // 10
target %= 10

use5 = target // 5
target %= 5

use1 = target // 1
target %= 1

print(use500 + use100+ use50+ use10 + use5 + use1)