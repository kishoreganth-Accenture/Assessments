import pymysql

class Avg_time:
    def __init__(self):
        db = pymysql.Connect(host='localhost', user="root", passwd="root", db="hw",port="8080")
        self.db = db
        self.cursor = db.cursor()

    def time(self):
        try:
            year = int(input("Enter the year(2018/2019):"))
            sql = "select id, month(swipe_date) as month, avg_time from (select id, swipe_date, round(avg(time_out-time_in) " \
                  "over(partition by month(swipe_date) order by month(swipe_date)),4)avg_time from swipe " \
                  "where year(swipe_date) = '{}')t group by month(swipe_date)".format(year)
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            for i in res:
                print(i)

        except Exception as e:
            print(e)
        finally:
            self.db.close()

if __name__=="__main__":
    obj=Avg_time()
    obj.time()