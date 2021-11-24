"""
re模块的深入
"""
import re
"""
match(): 默认匹配开头, 满足匹配就返回, 如果要匹配结尾需要手动加上 $ 符号 , 应用 账号规范是否符合的检测
search(): 不匹配开头,而是从开头往后进行搜索,,,,只要匹配到了(一个)满足条件的数据,,就返回,,之后的就不再管了...
findall(): 不匹配开头,而是从开头往后进行搜索, 匹配到所有满足条件的数据
"""
str_ = '这个视频的点击量是:123456,下载量:123,转发量:666'

res1 = re.match(r'这个视频的点击量是:(\d+),下载量:(\d+),转发量:(\d+)', str_)
print(res1)
print(res1.group())
print(res1.group(1), res1.group(2), res1.group(3))


res2 = re.search(r'\d+', str_)
print(res2)
print(res2.group())


res3 = re.findall(r'\d+', str_)  # 0
print(res3)

"""
爬虫提取: findall 和 分组 进行数据的提取
"""
str_ = '<img class="c-img img_3wha2" src="https://dss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=3186738015,770569864&amp;fm=55&amp;app=54&amp;f=JPEG?w=1140&amp;h=640">xxxxx asdasdasdsadsa'

# .*? 非贪婪
res_ = re.findall(r'src="(.*?)">xxxx',str_)  # src="(想要提取的数据)">xxxx  想要提取的部分前面的数据是src=" , 后面的数据是">xxxx
print(res_)
print(res_[0])

"""
sub 替换   str.replace
"""

s = '视频的点击量:1'  # 先正则定位 > 再替换
res_ = re.sub(r'\d+', '2', s)
print(res_)


"""
split >> 切割  str.split()
"""
s = 'hello,world,hello>python,>'
res_ = re.split(r'[,|>]', s)  # ,> 这是一个整体  ,|>
print(res_)

"""
r的作用: 原生字符串
"""
s = r'D\\demo\\demo\\demo'  # r > 原生字符串
print(s)
