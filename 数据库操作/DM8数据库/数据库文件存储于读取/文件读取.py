import dmPython


def read_file(file_id, output_filename):
    try:
        # 连接到达梦数据库
        connection = dmPython.connect(user='SYSDBA', password='SYSDBA', server='localhost',
                        port=5236, autoCommit=True)
        cursor = connection.cursor()

        # 读取文件数据
        sql_query = "SELECT filedata FROM \"TEST0623\".\"files\" WHERE id = ?"
        cursor.execute(sql_query, (file_id,))
        record = cursor.fetchone()

        # 将文件写入本地
        with open(output_filename, 'wb') as file:
            file.write(record[0])
        print("读出文件成功")

    except dmPython.Error as e:
        print(f"Error: {e}")

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("DM 连接关闭")


# 使用示例
if __name__ == '__main__':
    file_name = input("自定义读出文件名和读出路径'/path/to/output/file/output_example.pdf'：")
    # D:/out_git.txt
    file_id = input("读出文件数据库id：")
    print("确认读出文件名和读出路径：", file_name, sep="")
    print("确认读出文件数据库id：", file_id, sep="")
    ensure = input("确认请输入[y]:")
    if ensure == "y":
        read_file(file_id, file_name)
