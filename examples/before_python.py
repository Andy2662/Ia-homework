import smtplib
import sqlite3

def process(u, p, e, t):
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username='" + u + "'")
    r = c.fetchone()
    if r != None:
        print("user exists")
        return False
    c.execute("INSERT INTO users VALUES ('" + u + "','" + p + "','" + e + "')")
    conn.commit()
    conn.close()
    if t == 1:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login('myapp@gmail.com', 'password123')
        msg = 'Hi ' + u + ' welcome!'
        s.sendmail('myapp@gmail.com', e, msg)
        s.quit()
        print("sent")
    elif t == 2:
        print("no email")
    x = u + ':' + p
    print(x)
    return True

def getUsers():
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    d = c.fetchall()
    conn.close()
    l = []
    for i in d:
        l.append({'user': i[0], 'pass': i[1], 'mail': i[2]})
    return l

def delUser(u):
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE username='" + u + "'")
    conn.commit()
    conn.close()
