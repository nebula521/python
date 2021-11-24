"""
正则表达式
"""
"""
匹配单个字符
"""
import re
# \d   匹配任意一个数字 0-9
# [ ]  匹配[]中列举的单个字符，1234567 >>> 1-7， abcdefg > a-g，ABCDEFG > A-G     [a-zA-Z0-9_]
# .    匹配任意1个字符(除了\n之外)    .*?
# (了解)\w  匹配单词字符, 即a-z,A-Z,0-9,_中文也能匹配成功
# (了解)\s  匹配空白, 即 空格 和 tab 键
"""
匹配多个字符
"""
# * 前一个字符0次或者无限次（可有可无）
# +	      1次或者无限次（>=1）
# ?	      1次或者0次
# {m}	      m次
# {m,n}	  [m,n]次

str_ = """hello,中国
hello,湖南
hello,长沙
"""
# .匹配任务字符 *无数次 >>>  re.S 这个参数 可以匹配到换行符
res_ = re.match(r'.*', str_, re.S)

print(res_)
print(res_.group())

"""
演示匹配开头和结尾
"""
# ^	匹配字符串开头
# $	匹配字符串结尾
# re.match: 默认匹配开头
name_ = input('请输入一个变量名:')  # 1.必须是由字母,数字,下划线组成  2.不能以数字开头
res1 = re.match(r'[a-zA-Z_][a-zA-Z_0-9]*$', name_)
print(res1.group())

"""匹配分组"""
#  \.  .代表就是表面上一个点,  不再具有特殊作用
# ()    分组
email_ = input('请输入一个QQ邮箱地址:')
res2 = re.match(r'[a-zA-Z0-9_]{4,13}@((q{2}|Q{2})|163)\.com$', email_)
print(res2.group(), '\n', res2.group(1))