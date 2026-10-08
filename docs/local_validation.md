# 本地验证记录

验证日期：2026-10-08。使用 `tools.run_tests.run_problem` 对全部题目执行当前完整测试，每组超时限制为 2 秒。

共有 60 道题、483 组测试；通过 323 组，运行错误 25 组，输出不匹配 135 组，超时 0 组。

本记录是本地执行快照，不是官方 AC 或完整静态审查结论。未实现的空文件和骨架按练习记录保留，不视为仓库结构缺失。修改代码或用例后请重新运行对应题目并更新本记录。

## 已知情况

- Hot 100 第 06 题保留未完成尝试，存在语法错误；第 08 题存在字符串与整数相减的运行错误。
- 历史 LeetCode 第 06 题在单行 Z 字形场景运行错误；第 16 题解析输入时运行错误。
- Hot 100 第 24～35 题为骨架，历史第 17～20 题为空文件，均明确标记未实现。
- 第 47 题改用半开区间右侧中点的确定构造规则，06/07 的期望输出同步修正；解答未变更。
- 新增历史题目测试可能暴露更多未覆盖的边界问题，以下表格以实际运行结果为准。

## 各题状态

| 题目目录 | 状态 | 通过 / 总数 | 其他结果 |
| --- | --- | --- | --- |
| [problems/hot100/01_0001_two_sum](../problems/hot100/01_0001_two_sum/) | 本地用例通过 | 8 / 8 | — |
| [problems/hot100/02_0049_group_anagrams](../problems/hot100/02_0049_group_anagrams/) | 本地用例通过 | 8 / 8 | — |
| [problems/hot100/03_0128_longest_consecutive_sequence](../problems/hot100/03_0128_longest_consecutive_sequence/) | 本地用例通过 | 8 / 8 | — |
| [problems/hot100/04_0015_3sum](../problems/hot100/04_0015_3sum/) | 本地用例通过 | 8 / 8 | — |
| [problems/hot100/05_0042_trapping_rain_water](../problems/hot100/05_0042_trapping_rain_water/) | 本地用例通过 | 8 / 8 | — |
| [problems/hot100/06_0011_container_with_most_water](../problems/hot100/06_0011_container_with_most_water/) | 练习中：运行错误 | 0 / 8 | RUNTIME_ERROR: 8 |
| [problems/hot100/07_0283_move_zeroes](../problems/hot100/07_0283_move_zeroes/) | 本地用例通过 | 8 / 8 | — |
| [problems/hot100/08_0438_find_all_anagrams_in_a_string](../problems/hot100/08_0438_find_all_anagrams_in_a_string/) | 练习中：运行错误 | 0 / 8 | RUNTIME_ERROR: 8 |
| [problems/hot100/09_0003_longest_substring_without_repeating_characters](../problems/hot100/09_0003_longest_substring_without_repeating_characters/) | 本地用例通过 | 8 / 8 | — |
| [problems/hot100/10_0560_subarray_sum_equals_k](../problems/hot100/10_0560_subarray_sum_equals_k/) | 本地用例通过 | 8 / 8 | — |
| [problems/hot100/22_0025_reverse_nodes_in_k_group](../problems/hot100/22_0025_reverse_nodes_in_k_group/) | 本地用例通过 | 8 / 8 | — |
| [problems/hot100/23_0146_lru_cache](../problems/hot100/23_0146_lru_cache/) | 本地用例通过 | 8 / 8 | — |
| [problems/hot100/24_0024_swap_nodes_in_pairs](../problems/hot100/24_0024_swap_nodes_in_pairs/) | 未实现 | 0 / 8 | WRONG_ANSWER: 8 |
| [problems/hot100/25_0002_add_two_numbers](../problems/hot100/25_0002_add_two_numbers/) | 未实现 | 0 / 8 | WRONG_ANSWER: 8 |
| [problems/hot100/26_0019_remove_nth_node_from_end_of_list](../problems/hot100/26_0019_remove_nth_node_from_end_of_list/) | 未实现 | 0 / 8 | WRONG_ANSWER: 8 |
| [problems/hot100/27_0206_reverse_linked_list](../problems/hot100/27_0206_reverse_linked_list/) | 未实现 | 0 / 8 | WRONG_ANSWER: 8 |
| [problems/hot100/28_0023_merge_k_sorted_lists](../problems/hot100/28_0023_merge_k_sorted_lists/) | 未实现 | 0 / 8 | WRONG_ANSWER: 8 |
| [problems/hot100/29_0021_merge_two_sorted_lists](../problems/hot100/29_0021_merge_two_sorted_lists/) | 未实现 | 0 / 8 | WRONG_ANSWER: 8 |
| [problems/hot100/30_0234_palindrome_linked_list](../problems/hot100/30_0234_palindrome_linked_list/) | 未实现 | 0 / 8 | WRONG_ANSWER: 8 |
| [problems/hot100/31_0148_sort_list](../problems/hot100/31_0148_sort_list/) | 未实现 | 0 / 8 | WRONG_ANSWER: 8 |
| [problems/hot100/32_0141_linked_list_cycle](../problems/hot100/32_0141_linked_list_cycle/) | 未实现 | 0 / 8 | WRONG_ANSWER: 8 |
| [problems/hot100/33_0142_linked_list_cycle_ii](../problems/hot100/33_0142_linked_list_cycle_ii/) | 未实现 | 0 / 8 | WRONG_ANSWER: 8 |
| [problems/hot100/34_0160_intersection_of_two_linked_lists](../problems/hot100/34_0160_intersection_of_two_linked_lists/) | 未实现 | 0 / 8 | WRONG_ANSWER: 8 |
| [problems/hot100/35_0138_copy_list_with_random_pointer](../problems/hot100/35_0138_copy_list_with_random_pointer/) | 未实现 | 0 / 8 | WRONG_ANSWER: 8 |
| [problems/hot100/36_0230_kth_smallest_element_in_a_bst](../problems/hot100/36_0230_kth_smallest_element_in_a_bst/) | 本地用例通过 | 8 / 8 | — |
| [problems/hot100/37_0124_binary_tree_maximum_path_sum](../problems/hot100/37_0124_binary_tree_maximum_path_sum/) | 本地用例通过 | 8 / 8 | — |
| [problems/hot100/38_0114_flatten_binary_tree_to_linked_list](../problems/hot100/38_0114_flatten_binary_tree_to_linked_list/) | 本地用例通过 | 8 / 8 | — |
| [problems/hot100/39_0094_binary_tree_inorder_traversal](../problems/hot100/39_0094_binary_tree_inorder_traversal/) | 本地用例通过 | 8 / 8 | — |
| [problems/hot100/40_0199_binary_tree_right_side_view](../problems/hot100/40_0199_binary_tree_right_side_view/) | 本地用例通过 | 8 / 8 | — |
| [problems/hot100/41_0102_binary_tree_level_order_traversal](../problems/hot100/41_0102_binary_tree_level_order_traversal/) | 本地用例通过 | 8 / 8 | — |
| [problems/hot100/42_0104_maximum_depth_of_binary_tree](../problems/hot100/42_0104_maximum_depth_of_binary_tree/) | 本地用例通过 | 8 / 8 | — |
| [problems/hot100/43_0236_lowest_common_ancestor_of_a_binary_tree](../problems/hot100/43_0236_lowest_common_ancestor_of_a_binary_tree/) | 本地用例通过 | 8 / 8 | — |
| [problems/hot100/44_0543_diameter_of_binary_tree](../problems/hot100/44_0543_diameter_of_binary_tree/) | 本地用例通过 | 8 / 8 | — |
| [problems/hot100/45_0105_construct_binary_tree_from_preorder_and_inorder_traversal](../problems/hot100/45_0105_construct_binary_tree_from_preorder_and_inorder_traversal/) | 本地用例通过 | 8 / 8 | — |
| [problems/hot100/46_0101_symmetric_tree](../problems/hot100/46_0101_symmetric_tree/) | 本地用例通过 | 8 / 8 | — |
| [problems/hot100/47_0108_convert_sorted_array_to_binary_search_tree](../problems/hot100/47_0108_convert_sorted_array_to_binary_search_tree/) | 本地用例通过 | 8 / 8 | — |
| [problems/hot100/48_0226_invert_binary_tree](../problems/hot100/48_0226_invert_binary_tree/) | 本地用例通过 | 8 / 8 | — |
| [problems/hot100/49_0437_path_sum_iii](../problems/hot100/49_0437_path_sum_iii/) | 本地用例通过 | 8 / 8 | — |
| [problems/hot100/50_0098_validate_binary_search_tree](../problems/hot100/50_0098_validate_binary_search_tree/) | 本地用例通过 | 11 / 11 | — |
| [problems/leetcode/0001_two_sum](../problems/leetcode/0001_two_sum/) | 本地用例通过 | 8 / 8 | — |
| [problems/leetcode/0002_add_two_numbers](../problems/leetcode/0002_add_two_numbers/) | 练习中：输出不匹配 | 0 / 8 | WRONG_ANSWER: 8 |
| [problems/leetcode/0003_longest_substring_without_repeating_characters](../problems/leetcode/0003_longest_substring_without_repeating_characters/) | 本地用例通过 | 8 / 8 | — |
| [problems/leetcode/0004_median_of_two_sorted_arrays](../problems/leetcode/0004_median_of_two_sorted_arrays/) | 本地用例通过 | 8 / 8 | — |
| [problems/leetcode/0005_longest_palindromic_substring](../problems/leetcode/0005_longest_palindromic_substring/) | 本地用例通过 | 8 / 8 | — |
| [problems/leetcode/0006_zigzag_conversion](../problems/leetcode/0006_zigzag_conversion/) | 练习中：运行错误 | 7 / 8 | RUNTIME_ERROR: 1 |
| [problems/leetcode/0007_reverse_integer](../problems/leetcode/0007_reverse_integer/) | 本地用例通过 | 8 / 8 | — |
| [problems/leetcode/0008_string_to_integer_atoi](../problems/leetcode/0008_string_to_integer_atoi/) | 本地用例通过 | 8 / 8 | — |
| [problems/leetcode/0009_palindrome_number](../problems/leetcode/0009_palindrome_number/) | 本地用例通过 | 8 / 8 | — |
| [problems/leetcode/0010_regular_expression_matching](../problems/leetcode/0010_regular_expression_matching/) | 本地用例通过 | 8 / 8 | — |
| [problems/leetcode/0011_container_with_most_water](../problems/leetcode/0011_container_with_most_water/) | 本地用例通过 | 8 / 8 | — |
| [problems/leetcode/0012_integer_to_roman](../problems/leetcode/0012_integer_to_roman/) | 本地用例通过 | 8 / 8 | — |
| [problems/leetcode/0013_roman_to_integer](../problems/leetcode/0013_roman_to_integer/) | 本地用例通过 | 8 / 8 | — |
| [problems/leetcode/0014_longest_common_prefix](../problems/leetcode/0014_longest_common_prefix/) | 本地用例通过 | 8 / 8 | — |
| [problems/leetcode/0015_3sum](../problems/leetcode/0015_3sum/) | 本地用例通过 | 8 / 8 | — |
| [problems/leetcode/0016_3sum_closest](../problems/leetcode/0016_3sum_closest/) | 练习中：运行错误 | 0 / 8 | RUNTIME_ERROR: 8 |
| [problems/leetcode/0017_letter_combinations_of_a_phone_number](../problems/leetcode/0017_letter_combinations_of_a_phone_number/) | 未实现 | 0 / 8 | WRONG_ANSWER: 8 |
| [problems/leetcode/0018_4sum](../problems/leetcode/0018_4sum/) | 未实现 | 0 / 8 | WRONG_ANSWER: 8 |
| [problems/leetcode/0019_remove_nth_node_from_end_of_list](../problems/leetcode/0019_remove_nth_node_from_end_of_list/) | 未实现 | 1 / 8 | WRONG_ANSWER: 7 |
| [problems/leetcode/0020_valid_parentheses](../problems/leetcode/0020_valid_parentheses/) | 未实现 | 0 / 8 | WRONG_ANSWER: 8 |
| [problems/leetcode/0912_sort_an_array](../problems/leetcode/0912_sort_an_array/) | 本地用例通过 | 8 / 8 | — |
