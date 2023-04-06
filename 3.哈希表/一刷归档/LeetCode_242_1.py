"""
242.有效的字母异位词
给定两个字符串 s 和 t ，
编写一个函数来判断 t 是否是 s 的字母异位词。
注意：若 s 和 t 中每个字符出现的次数都相同，
则称 s 和 t 互为字母异位词。

其本身为一个字符串，如果我们找到相等的
那么就删除位置上的字符 -> 删除字符操作较为麻烦

由于本身使用的是python，我们可以直接拆成
字典或哈希表，这里可以对两者进行循环
对两者循环 构建字典
利用一个的字典进行比对
如果出现另一个字典不存在这个字母
或者所拥有的数值不匹配，那么就返回False
否则整体匹配就返回True
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 构建两个字典
        dict_s = {}
        dict_t = {}

        # 进行循环遍历，将字母存入
        for char in s:
            # 判断字典是否有此key
            if char not in dict_s:
                dict_s[char] = 0
            else:
                dict_s[char] += 1
        
        # 进行循环遍历，将字母存入
        for char in t:
            # 判断字典是否有此key
            if char not in dict_t:
                dict_t[char] = 0
            else:
                dict_t[char] += 1
        
        # 长度 这里是后补的漏洞
        if len(dict_s) != len(dict_t):
            return False
        
        # 字典遍历
        for key in dict_s.keys():
            # 判断key是否在另一个函数中
            if key in dict_t:
                # 对比两个值
                if dict_t[key] != dict_s[key]:
                    return False
            # 否则直接False
            else:
                return False
        
        # 返回True
        return True

