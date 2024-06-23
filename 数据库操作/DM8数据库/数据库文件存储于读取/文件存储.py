import dmPython


def insert_file(filename):
    try:
        # 连接到达梦数据库
        connection = dmPython.connect(user='SYSDBA', password='SYSDBA', server='localhost',
                                      port=5236, autoCommit=True)
        cursor = connection.cursor()

        # 读取文件
        """
        with open(filename, 'rb') as file::
            open(filename, 'rb'): 使用 open 函数打开文件。这里的 filename 是文件的路径。
            filename: 要打开的文件的路径或文件名。
            'rb': 模式参数，表示以二进制读取模式打开文件（r 表示读取，b 表示二进制）。
            as file: 使用 with 语句，这是一种上下文管理器，用于确保文件在读取后自动关闭，即使在读取过程中发生了异常。
        binary_data = file.read():
            file.read(): 读取整个文件的内容并将其作为一个二进制数据块返回。
            binary_data: 将读取到的二进制数据存储在变量 binary_data 中。
        """
        with open(filename, 'rb') as file:
            binary_data = file.read()

        # 插入文件到数据库
        sql_query = "INSERT INTO \"TEST0623\".\"files\" (filename, filedata) VALUES (?, ?)"
        cursor.execute(sql_query, (filename, binary_data))
        print("文件写入成功")

    except dmPython.Error as e:
        print(f"Error: {e}")

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("DM 连接关闭")


# 使用示例
if __name__ == '__main__':
    my_file = input("输入文件的绝对路径/path/to/your/file/example.pdf:")
    # D:/git.txt
    print("确认路径：", my_file,sep="")
    ensure = input("确认请输入[y]:")
    if ensure == "y":
        insert_file(my_file)
