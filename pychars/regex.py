# %%
import string
import re

# %% [markdown]
# 
# ## 模式、编译、标志
#
# ### 编译
#
# - `re.compile`：将正则表达式编译为正则表达式对象`Pattern`
#   - 需多次使用正则表达式可以编译以便复用
#   - 编译后的模式、模块级函数会被缓存，所以少数的正则表达式
#     无需考虑编译问题
# - `re.purge`：清除正则表达式缓存
#
# ### Flags
#
# |标记|用途|内联标记|
# |-----|-----|
# |`re.A`/`re.ASCII`|`\w\W\b\B\d\D\s\S`只匹配ASCII|`?a`|
# |`re.DEBUG`|显示编译debug信息||
# |`re.I`/`re.IGNORECASE`|忽略大小写匹配|`?i`|
# |`re.L`/`re.LOCALE`|由语言区域决定`\w\W\b\B`和大小写匹配|`?L`|
# |`re.M`/`re.MULTILINE`|`^`匹配行首、`$`匹配行尾|`?m`|
# |`re.S`/`re.DOTALL`|`.`匹配换行符|`?s`|
# |`re.X`/`re.VERBOSE`|允许正则表达式分段、添加注释、忽略空格|`?x`|

# verbose mod
float_ptn_v = re.compile(r"""
\d +    # the integral part
\.      # the decimal point
\d *    # some fractional digits
""", re.X)
float_ptn = re.compile(r"\d+\.\d*")

# %% [markdown]
#
# ### 匹配函数
#
# |函数|搜索范围|返回结果|匹配数量|
# |-----|-----|-----|-----| 
# |`re.search`|字符串内|匹配对象/`None`|首个|
# |`re.match`|字符串起始|匹配对象/`None`|1个|
# |`re.fullmatch`|完整字符串|匹配对象/`None`|1个|
# |`re.split`|字符串内|切分结果、模式中`()`匹配部分列表|`maxsplit`|
# |`re.findall`|字符串内|模式中包含组则元素为元组，包含空匹配|全部|
# |`re.finditer`|同上|同上|同上|
# |`re.sub`|字符串内|替换最左边非重叠模式结果（空匹配在不连续相邻情况下被替换）|`count`|
# |`re.subn`|同上|`(同上, 替换次数)`|同上|
# |`re.escape`|字符串内|转义特殊字符|1个|
#
# > - 返回列表者，列表内元素按字符串中顺序
# > - 编译后正则表达式对象`Pattern`具有以上方法

# `re.match`, refer to indexed subgroup or named subgroup
mt_matched = re.match(r"(\d+).(\1)", "12.123")
mt_unmatched = re.match(r"(\d+).(\1)", "12.13")
print(mt_matched, mt_unmatched)
mt_matched = re.match(r"(?P<int>\d+).(?P=int)", "12.123")
mt_unmatched = re.match(r"(?P<int>\d+).(?P=int)", "12.13")
print(mt_matched, mt_unmatched)

# `re.split`
splited = re.split(r"\w+,", "Words, words, words.")
print(splited)
splited = re.split(r"(\w+),", "Words, words, words.")
print(splited)

# `re.sub`
subed = re.sub("x*", "-", "abxd")
print(subed)
# `re.sub` with reference, only indexed subgroup works
sub_ref = re.sub(r"(.*)\.(.*)", r"\2.\1", "xyz.123")
print(sub_ref)
# `re.sub` with function
sub_func = re.sub(r"(.*)\.(.*)", lambda x: x.group() + "asdf", "xyz.123")
print(sub_func)
# `re.sub` with re-escape
sub_reescape = re.sub(r"\\", r"\\\\", r"\d")
print(sub_reescape)


# `re.escape`
print(re.escape("https://python.org"))

# %% [markdown]
#
# ## 正则对象`Pattern`
#
# - `Pattern`具有以上匹配方法，另外还有属性
#   - `Pattern.groups`：模式中组数量
#   - `Pattern.groupindex`：映射由`(?P<id>)`定义的符号组合、数字组合字典
#   - `Pattern.pattern`：原始模式字符串

print(float_ptn_v.pattern)

# %% [markdown]
#
# ## 匹配对象`Match`
#
# - `Match`总是可以通过bool判断是否匹配 

# %% [markdown]
#
# ### Group
 
# `Match.group([group1, ...])`
mt = re.match(r"(?P<first>\w+) (?P<last>\w+)", "Isaac Newton, physicist")
# The entire matched
print(mt.group(0))
# The parenthesized subgroups
print(mt.group(0, 1))
# The parenthesized subgroups named with `?P<id>`
print(mt.group("last"))
# Return last match if parenthesized ptn matched more than 1 times
mt = re.match(r"(..)+", "a1b2c3")
print(mt.group(1))


# `Match.groups(default=None)`
# Tuple with all parenthesized subgroups
mt = re.match(r"(\d+)\.?(\d+)?", "23.12")
print(mt.groups())
# Return default value if parentheiszed ptn is not matched
mt = re.match(r"(\d+)\.?(\d+)?", "23")
print(mt.groups("OK"))

# `Match.groupdict(default=None)`
mt = re.match(r"(?P<first>\w+) (?P<last>\w+)", "Isaac Newton, physicist")
print(mt.groupdict("OK"))
# Only named parenthesized subgroups
mt = re.match(r"(\d+)\.?(\d+)?", "23.12")
print(mt.groupdict("OK"))


# %% [markdown]
# 
# ### Position

# `Match.start(group=0)`, `Match.end(group=0)`
mt = re.match(r"(?P<first>\w+) (?P<last>\w+)", "Isaac Newton, physicist")
print(mt.string[mt.start(): mt.end()])

# `Match.span(group=0)`
print(mt.span(1))

# `Match.pos`, `Match.endpos`
# The start position of the first matched
print(mt.pos, mt.endpos)

# `Match.lastindex`, `Match.lastgroup`
# The last group-name, group-index of the matched
print(mt.lastgroup, mt.lastindex)

# `Match.re`, `Match.string`
print(mt.re, mt.string)

