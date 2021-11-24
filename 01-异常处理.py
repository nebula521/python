"""
异常处理
"""
"""
用户输入用户名, 密码后对信息进行校验
1. 用户名长度在3-8个字符
2. 用户名中只能出现英文字母和数字
3. 密码长度必须是6位
4. 密码必须由纯数字组成
"""

name = input("请输入用户名：")
password = input("请输入密码：")


class NameIsError(Exception):
    pass


class PwdIsError(Exception):
    pass


def check(name, password):
    if len(name) < 3 or len(name) > 8:
        raise NameIsError("用户名长度在3-8个字符")
    if not name.isalnum():
        raise NameIsError("用户名中只能出现英文字母和数字")
    if len(password) != 6:
        raise PwdIsError("密码长度必须是6位")
    if not password.isnumeric():
        raise PwdIsError("密码必须由纯数字组成")
    print("登录成功")


try:
    check(name, password)
except NameIsError as e:
    print(e)
except PwdIsError as e:
    print(e)



