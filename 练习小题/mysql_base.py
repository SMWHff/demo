import pymysql


class MySQL(object):
    """
    MySQL数据库
    """
    def __init__(self, database='TESTDB', user='root', pwd='root'):
        # 打开数据库连接
        self.db = pymysql.connect(host='localhost', user=user, password=pwd, database=database)
        # 使用 cursor() 方法创建一个游标对象 cursor
        self.cursor = self.db.cursor()

    def __del__(self):
        # 关闭数据库连接
        self.db.close()

    def execute(self, query):
        """
        查询SQL语句，返回单行
        :param query:
        :return:
        """
        # 使用 execute() 方法执行 SQL 查询
        self.cursor.execute(query)
        # 使用 fetchone() 方法获取单条数据
        data = self.cursor.fetchone()
        return data

    def executes(self, query):
        """
        查询SQL语句，返回所有
        :param query:
        :return:
        """
        # 使用 execute() 方法执行 SQL 查询
        self.cursor.execute(query)
        # 使用 fetchone() 方法获取单条数据
        data = self.cursor.fetchall()
        return data