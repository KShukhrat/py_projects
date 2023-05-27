# pip install psycopg2
#https://www.psycopg.org/docs/usage.html
import psycopg2

# Ulanish
connect = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="username",
    password="password"
)

# Cursor yaratish
cur = connect.cursor()


# GetAll barchasini olib berish uchun
def get_all():
    cur.execute("SELECT * FROM database")  # query bazaga murojat qilish uchun
    return cur.fetchall()


# Table yaratish
def create_table():
    try:
        cur.execute("""create table test(
        id uuid default uuid_generate_v4(),
        name varchar,
        date timestamp default now()
        );""")
        print("Table yaratildi")
    except psycopg2.errors.DuplicateTable as e:
        print('Table yaratilmadi: ', e)

def get_by_username(username):
    cur.execute("select * from test where name=%s", (username,))
    return cur.fetchall()#topilgan ma'lumotlarni chiqazib beradi.
    # Bunda: fetchall()->barchasini olib berishda ishlatida
    #        fetchmany(limit_num)->topilgan ma'lumotlarni sonniga limit quyib chiqazib beradi
    #        frtchone()->boshidagi bittasini chiqazib beradi

def add(name: str, date=None):
    if date is not None:
        cur.execute("INSERT INTO test(name, date) values (%s, %s)", [name, date])#qovuslar () yoki bu [] ko'rinishda bo'lishi mumkin
    else:
        cur.execute("INSERT INTO test(name) values (%s)", (name,))


connect.commit()#berilgan querylarni amalga oshirilishini ta'minlaydi
cur.close()#cursorni yopadi
connect.close()#baza bilan boglanishni uzadi
