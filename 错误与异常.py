
class MyException(Exception):
    def __init__(self, msg):
        print(f"这是一个异常值：{msg}")


def TRY():
    try:
        a=1/1
        b=[1,2,3]
        #print(b[3])
        raise ValueError("抛出异常")
    except Exception as e:
        print("异常：", e)
    else:
        print("没有异常我会运行！")
    finally:
        print("有没有异常我都会运行！")

TRY()