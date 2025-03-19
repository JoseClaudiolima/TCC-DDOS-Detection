import sqlite3
from utils import is_valid_ipv4, is_valid_ipv6

def insert_malicious_ip(connection, cursor, ipv4, ipv6):
    if not is_valid_ipv4(ipv4):
        print(f"Erro: '{ipv4}' não é um IPv4 válido!")
        return
    if not is_valid_ipv6(ipv6):
        print(f"Erro: '{ipv6}' não é um IPv6 válido!")
        return
    
    cursor.execute("""
        INSERT INTO malicious_ip (ipv4, ipv6)
        VALUES (?, ?)
    """, (ipv4, ipv6))
    connection.commit()
    
def select_all_malicious_ips( cursor):
    cursor.execute("SELECT * FROM malicious_ip")
    resultados = cursor.fetchall()
    if resultados:
        for linha in resultados:
            print(linha)
    else:
        print("Nenhum IP malicioso adicionado por enquanto.")

def delete_all_ip(connection, cursor):
    cursor.execute("DELETE FROM malicious_ip")
    connection.commit()

def setup_database():
    connection = sqlite3.connect("ddos_detection.db")
    cursor = connection.cursor()
    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS malicious_ip (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ipv4 TEXT,
            ipv6 TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        cursor.execute("""
        CREATE TRIGGER IF NOT EXISTS update_timestamp
        AFTER UPDATE ON malicious_ip
        BEGIN
            UPDATE malicious_ip
            SET updated_at = CURRENT_TIMESTAMP
            WHERE id = NEW.id;
        END;
        """)
    except sqlite3.Error as erro:
        print(f"Erro ao configurar o banco de dados: {erro}")
    return connection, cursor
