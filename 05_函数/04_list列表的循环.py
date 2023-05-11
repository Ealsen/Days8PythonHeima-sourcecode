"""
演示对list列表的循环，使用while和for循环2种方式
"""


def list_while_func():
    """
    使用while循环遍历列表的演示函数
    :return: None
    """
    my_list = ["传智教育", "黑马程序员", "Python"]
    # 循环控制变量通过下标索引来控制，默认0
    # 每一次循环将下标索引变量+1
    # 循环条件：下标索引变量 < 列表的元素数量

    # 定义一个变量用来标记列表的下标
    index = 0           # 初始值为0
    while index < len(my_list):
        # 通过index变量取出对应下标的元素
        element = my_list[index]
        print(f"列表的元素：{element}")

        # 至关重要 将循环变量（index）每一次循环都+1
        index += 1


def list_for_func():
    """
    使用for循环遍历列表的演示函数
    :return: None
    """
    my_list = [1, 2, 3, 4, 5]
    # for  临时变量  in  数据容器:
    for element in my_list:
        print(f"列表的元素有：{element}")


# list_while_func()
list_for_func()
