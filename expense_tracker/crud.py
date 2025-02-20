from datetime import datetime
from database import cursor, connection



def insert_expense(amount, description, date=None):

    date = date if date else datetime.now().date()

    cursor.execute(f"insert into expense (amount, description, date) values ({amount}, '{description}', '{date}')")
    connection.commit()



def list_expenses():
    res = cursor.execute("select id, date, description, amount  from expense")

    return res.fetchall()


def delete_expense(id):
    cursor.execute(f"delete from expense where id={id}")
    connection.commit()


def get_summary(month=None):
    if month:
        month =  f"0{month}" if month < 10 else f"{month}"
        res = cursor.execute(f"select sum(amount) from expense where date like '%-{month}-%'")
    else:
        res = cursor.execute("select sum(amount) from expense")

    return res.fetchone()[0]

def get_count():
    res = cursor.execute("select count(*) from expense")

    return res.fetchone()[0]

