from typing import *

# 此题做法O(n^2)依然不满足条件
# class Solution:
#     def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
#         # 确定本题使用方法
#         # 本题使用索引映射，将所有可能的结果计算出来
#         # 计算每个结果出现的值
#         # 本题可以使用拆分法
#         # 将题目的O(n^4)改为O(n^2)的情况
#         # 确定是否有特殊的边界条件
#         # 本题暂未有特殊的边界条件
#         # 索引集
#         index_tuple_1 = []
#         index_tuple_2 = []
#         # 完整索引集
#         index_tuple = []
#         # 结果集
#         result_dict = {}
#         # 可能情况
#         length = 0
#         # 前两个值构建
#         # 第一层
#         for i in range(len(nums1)):
#             # 第二层
#             for j in range(len(nums2)):
#                 index_tuple_1.append((i, j))
#         # 后两个值构建
#         # 第三层
#         for k in range(len(nums3)):
#             # 第四层
#             for l in range(len(nums4)):
#                 # 保存索引集
#                 index_tuple_2.append((k, l))
        
#         for index1 in index_tuple_1:
#             for index2 in index_tuple_2:
#                 # 将两者的索引值累加
#                 index = index1 + index2
#                 # 将其保存在索引值中
#                 index_tuple.append(index)
        
#         # 构建结果情况
#         for index in index_tuple:
#             # 索引进行map映射构建结果
#             result_dict[index] = nums1[index[0]] + nums2[index[1]] + nums3[index[2]] + nums4[index[3]]

#         # 输出满足结果的值
#         for value in result_dict.values():
#             if value == 0:
#                 length += 1
        
#         # 返回结果情况
#         return length

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # 构建一个map映射的字典
        nums_dict_1 = {}
        nums_dict_2 = {}
        nums_dict = {}
        
        # 对nums1和nums2两个值进行计算
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                # 构建一个key值 - 这里使用结果构建key值
                key = nums1[i] - nums2[j]
                # 如果这个key值存在
                if nums_dict_1.__contains__(key):
                    # 在这个key值中添加字典
                    nums_dict_1[key].append((i, j))
                # 如果这个key值不存在
                else:
                    # 构建这个key值的字典
                    nums_dict_1[key] = [(i, j)]
        
        # 对nums1和nums2两个值进行计算
        for i in range(len(nums3)):
            for j in range(len(nums4)):
                # 构建一个key值 - 这里使用结果构建key值
                key = nums3[i] - nums4[j]
                # 如果这个key值存在
                if nums_dict_2.__contains__(key):
                    # 在这个key值中添加字典
                    nums_dict_2[key].append((i, j))
                # 如果这个key值不存在
                else:
                    # 构建这个key值的字典
                    nums_dict_2[key] = [(i, j)]
        
        # 对两个字典进行计算
        for key_1 in nums_dict_1.keys():
            for key_2 in nums_dict_2.keys():
                pass
def main():
    s = Solution()
    # case 1
    nums1 = [1,2]
    nums2 = [-2,-1]
    nums3 = [-1,2]
    nums4 = [0,2]
    print(s.fourSumCount(nums1, nums2, nums3, nums4))
    # case 2
    nums1 = [0]
    nums2 = [0]
    nums3 = [0]
    nums4 = [0]
    print(s.fourSumCount(nums1, nums2, nums3, nums4))

if __name__ == '__main__':
    main()