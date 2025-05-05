# missing-number-review

arrayを見てそれぞれあっているかを総当たりさせる
arrayの中に存在していたら続けさせて、存在していなかったらその時のiの値を返す
時間計算量:O(n**2)
for文を2重に回しているため

```
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(0, len(nums) + 1):
            if i in nums:
                continue
            else:
                return i
```

chatgptに相談すると以下のような提案がなされた
時間計算量:O(n)
sum関数でn個の要素にアクセスするため

```
def missingNumber(nums):
    """
    0 から n までの範囲のうち、配列 nums に存在しない数を返す関数。
    nums は 0〜n のうち n 個の異なる整数を含む。
    """
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum
```
