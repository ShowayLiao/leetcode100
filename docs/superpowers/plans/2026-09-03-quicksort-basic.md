# 快速排序基础题 实现计划

> 面向仓库中的 Python ACM 练习题：新增一道要求手写快速排序的基础题，并保留可复现的本地测试。

**目标：** 在 `problems/leetcode/0912_sort_an_array/` 编入 LeetCode 912 的 ACM 化版本，明确要求使用快速排序思想完成升序排序。

**方案：** 采用单组输入：第一行给出 `n`，第二行给出 `n` 个整数；输出一行升序数组。题目文档明确禁止调用 `sort()` / `sorted()`，解答使用原地分区加递归。测试覆盖普通乱序、重复值、负数、已排序、逆序和单元素数组。

**技术栈：** Python 标准库、`sys.stdin.buffer.read()`、原地快速排序。

### 任务 1：建立题目契约和本地测试

**文件：**

- 创建：`problems/leetcode/0912_sort_an_array/problem.md`
- 创建：`problems/leetcode/0912_sort_an_array/notes.md`
- 创建：`problems/leetcode/0912_sort_an_array/tests/01.in` 至 `06.out`

- [x] 写清楚来源、ACM 输入输出协议、约束、禁止事项和示例。
- [x] 写入普通乱序、重复值、负数、已排序、逆序、单元素六组输入输出。
- [x] 运行题目测试，先验证缺少实现时失败，再验证完整实现通过。

### 任务 2：实现手写快速排序

**文件：**

- 创建：`problems/leetcode/0912_sort_an_array/main.py`

- [x] 解析输入并处理空输入情况。
- [x] 实现原地三路分区，并递归较小区间、循环处理较大区间。
- [x] 通过 `if __name__ == "__main__"` 调用 `solve()`。
- [x] 不调用 Python 内置排序函数。
- [x] 运行六组本地测试，全部通过。

### 任务 3：验证和复核

- [x] 使用 `python tools/run_tests.py problems/leetcode/0912_sort_an_array` 运行完整题目测试。
- [x] 使用 Python 编译检查确认新文件无语法错误。
- [x] 复核 `problem.md`、`main.py`、`notes.md` 和测试文件是否齐全，检查复杂度和边界说明。
