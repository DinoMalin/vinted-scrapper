import mysql.connector
import scrapper

db = mysql.connector.connect(
    host='localhost',
    user='vinted',
    password='password',
    database='vinted-scraper'
)

cursor = db.cursor()


def save(ad: scrapper.Ad) -> None:
    cursor.execute('INSERT INTO ad (id) VALUES (%s)', [ad.id])
    db.commit()


def exists(ad: scrapper.Ad) -> bool:
    cursor.execute('SELECT * FROM ad WHERE id = %s', [ad.id])
    return len(cursor.fetchall()) > 0
