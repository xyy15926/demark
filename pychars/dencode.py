# %% [markdown]
#
# ## Base64
#
# - BaseXX编码：将若干bytes编为一组，拆分为 N * Mbits，将 Mbits
#   映射为<XX>个字符
#   - 对末尾不满足N * Mbits部分
#     - 填充0至M的倍数，然后映射
#     - 对不满足N字符倍数部分，填充字符`=`（标准）至N的倍数
#   - 每3bytes（24bits）拆分为4组6bits，映射至64个ASCII字符
#   `[A-Za-z0-9+/]`
#   - 使用的64个字符的Base64编码和ASCII编码值不同
#   - 末尾不满足24bits则用0填充至6的倍数再映射
#   - 最后填充`=`（标准）至整个编码结果字符数为4的倍数（解码时同样需填充）
#
# - 同理根据分组、拆分的不同还有
#   - Base16：1bytes -> 2*4bits，`[0-9A-F]`
#   - Base32：5bytes -> 8*5bits
#     - Alphabet方案：`[A-Z2-7]`
#     - Extend Hex方案：`[0-9A-V]`
#   - Base64：3bytes -> 4*6bits
#     - Alphabet方案：`[A-Za-z0-9+/]`
#     - URL and Filename Safe方案：`[A-Za-z0-9-_]`
#   - Base85
#   - ASCII85
#
# 
# |编码方案|解码|编码|特征|
# |-----|-----|-----|-----|
# |b64|`b64encode`|`b64decode`|可替换padding|
# |b64|`standard_b64encode`|`standard_64decode`|标准|
# |b64|`urlsafe_b64encode`|`urlsafe_b64decode`|URL、文件安全|
# |b32|`b32encode`|`b32decode`||
# |b32|`b16encode`|`b16decode`||
# |a85|`a85encode`|`a85decode`||
# |b85|`b85encode`|`b85decode`||
# |b64|`decodebytes`|`encodebytes`||
# |b64|`decode`|`encode`|文件输入输出|

import base64

# fill bits will `0`, fill encoded bytes with `=`
encoded = base64.b64encode("a".encode("ASCII"))
print(encoded)
decoded = base64.b64decode(encoded).decode("ASCII")
print(decoded)

# %%
