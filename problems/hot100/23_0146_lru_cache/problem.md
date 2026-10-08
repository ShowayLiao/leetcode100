# LeetCode Hot 100 23 - LRU 缓存

> 状态：本地用例通过。验证日期：2026-10-08；仅代表当前本地用例。

- Source: [LeetCode 146. LRU 缓存](https://leetcode.cn/problems/lru-cache/)
- Difficulty: 中等
- Tags: 哈希表、双向链表、设计
- Local mode: ACM-style standard input and output

## Local input contract

第一行输入容量 capacity 和操作数 q；随后 q 行，每行是 put key value 或 get key。

## Local output contract

每次 get 输出一行：存在时输出当前值，不存在时输出 -1。put 不输出。访问或更新已有键会使它成为最近使用项；容量满时删除最久未使用项。

## Constraints

- 1 <= capacity <= 3000；1 <= q <= 100000；key 和 value 为整数。

## Example

Input:
```text
2 9
put 1 1
put 2 2
get 1
put 3 3
get 2
put 4 4
get 1
get 3
get 4
```

Output:
```text
1
-1
-1
3
4
```

The local format is a concise practice contract; consult the source link for the original statement.
