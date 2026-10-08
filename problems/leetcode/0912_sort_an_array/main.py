import sys


def quick_sort(nums: list[int]) -> None:
    """Sort nums in place with three-way quicksort."""

    def sort(left: int, right: int) -> None:
        while left < right:
            pivot = nums[(left + right) // 2]
            less = left
            current = left
            greater = right

            while current <= greater:
                if nums[current] < pivot:
                    nums[less], nums[current] = nums[current], nums[less]
                    less += 1
                    current += 1
                elif nums[current] > pivot:
                    nums[current], nums[greater] = nums[greater], nums[current]
                    greater -= 1
                else:
                    current += 1

            if less - left < right - greater:
                sort(left, less - 1)
                left = greater + 1
            else:
                sort(greater + 1, right)
                right = less - 1

    sort(0, len(nums) - 1)


def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    nums = data[1 : n + 1]
    quick_sort(nums)
    print(*nums)


if __name__ == "__main__":
    solve()
