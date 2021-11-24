"""
电脑:操作系统
    windows10 > 桌面操作系统  > 应用程序软件 > QQ 微信
                :占用资源比较大

    命令黑窗口 > cmd > 服务器操作系统
    : 占用资源比较小,不适合普通人去使用,,
"""

"""
Linux: 服务器操作系统 > 黑窗口
    centenOS, redhat
    ubuntu
        -- 服务器操作系统 > 黑窗口
        -- 桌面操作系统 > 
        
爬虫:windows,
web:linux 


mac:  贵  
  
"""

"""
1.解压软件: winrar

2.电脑虚拟化没有开启: win7 win10 mac BIOS

"""
"""
反斜杠 \
斜杠   /
"""

# 群文件: linux.rar > 解压 >
# ubuntu玩崩了怎么办, 删掉,,,重新解压一个新的即可

"""
快速打开命令行窗口: ctrl+alt+T
"""
"""
pwd: 显示此时此刻的位置(路径)  /home/sixstar
ls : 查看当前路径下的文件,文件夹
cd xxx: 进入桌面(相对路径)  绝对路径 cd /home/sixstar/Desktop
Tab: 自动补全:

ctrl  shift +  放大界面
ctrl  -        缩小界面

touch xxx  创建文件
rm    xxx  删除文件

clear 清空(界面往下翻一页)
快捷键: ctrl + L

mkdir xxx  创建文件夹
rm xxx -r  删除文件夹

cp xxx.txt xxx  复制一个文件到一个文件夹

cd ..  返回上一路径

tree xxx 查看这个里面都有啥,,,,

tree  当前的路径下文件结构

ctrl + C  终止

mv xxx.txt xxx  把xxx.txt文件移动到xxx里面
mv 123.txt 456.txt  重命名

history  查看历史命令

drwxr-xr-x 5 sixstar sixstar 4096 Feb  2 23:52 bushu
1.类型:d文件夹 -文件
rwx:创建这个文件的人: r 可读 w 可写 x 可执行
r-x:同组
r-x:其他人

ls
-a   显示隐藏文件(文件夹)
-l   规范的显示
-lh  大小规格
 
重定向  >   文件读写里面的w模式:没有就新建, 有了就覆盖
ls在终端执行之后的结果写进一个文件中
la > 1.txt
打开文件: 桌面操作系统才可以
gedit 1.txt

终端查看 
1.cat 1.txt      一次性显示出来所有的内容:默认是跳到了结尾
2.more 1.txt     从开头开始显示,f 空格是翻页看  回车一行行往下走
                 Q 直接退出  ctrl+C 直接退出

3.vim 1.txt  终端自带的编辑器:可以修改

追加重定向 >> 文件读写里面的a模式: 没有就新建, 有了就追加

cat 1.txt 3.txt 两个文件合并显示

grep "h" 4.txt 显示出所有带有 h 的数据 以行为单位, 不带这个 h 的数据那一行就不显示
搜索文件里面的数据
grep -i "h" 4.txt     -i 不需分大小写
grep -i -n "h" 4.txt  -n 显示行数
grep -i -n -v "h" 4.txt -v 代表取反 显示没有 h 的数据部分

find: 
路径下的文件:
find ./ -name "*.txt"
寻找 当前目录之下 以名称为条件 "*.txt" 

-size
find / -size 2M   2MB大小的文件 -size条件的大小  / 根目录
find / -size +2M 大于2MB
find / -size -2M  小于2MB


权限不够的情况:  以管理员的身份去运行这个命令
sudo xxxx

which xxx 查看这个东西的位置
"""



"""
vim编辑器的介绍:linux系统自带的编辑器
vim xxx  拥有就打开, 没有就新建 

命令模式:
只要按下ESC 就能够进入命令模式
只是为了进入另外两种模式

末行模式: 现在命令模式中 shift + :
保存退出

文本输入模式:(编辑模式)
内容编辑
命令模式进入编辑模式:
很多的键位:
都有不同的作用,,,

--插入-- 消失 退出了编辑模式
"""


























































