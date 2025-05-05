# missing-number-review

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