book_list = ['坏蛋是怎样炼成的', '上门女婿', 'D调的华丽', 'java', '数据结构与算法']
for num in range(0, 50):
    jud = input('借书or还书:')

    # 借书
    if jud == '借书':
        print(book_list)
        str_lend = input('请输入要借的书名:')
        if str_lend in book_list:
            print('图书馆有1本'+str_lend)
            str_judge = input('是否要借出:是/否')
            if str_judge == '是':
            # 图书清单中删除已借出的图书
                book_list.remove(str_lend)
                print(str_lend, '已成功借出')
                print(book_list)

            else:
                print('本次借书已结束')
        else:
            print(str_lend, '已被借出')
            print(book_list)
# 还书
    else:
        str_return = input('请输入要还的书名:')
        book_list.append(str_return)
        print(str_return, '已成功还入')
        print(book_list)
