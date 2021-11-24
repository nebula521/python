# 操作字节文件
file1 = open('迪丽热巴.jpg', 'rb')
data_ = file1.read()
file1.close()

with open('瑶瑶老师.jpg', 'wb') as file2:
    file2.write(data_)