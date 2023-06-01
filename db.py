import mysql.connector
from objects import Ad

db = mysql.connector.connect(
    host="localhost", user="vinted", password="password", database="vinted-scraper"
)

cursor = db.cursor()


def save(ad: Ad) -> None:
    cursor.execute("INSERT INTO ad (id) VALUES (%s)", [ad.id])
    db.commit()


def exists(ad: Ad) -> bool:
    cursor.execute("SELECT * FROM ad WHERE id = %s", [ad.id])
    return len(cursor.fetchall()) > 0
