from database import setup_database, insert_malicious_ip, select_all_malicious_ips, delete_all_ip

if __name__ == "__main__":
    connection, cursor = setup_database()

    # Interação com banco de dados:
    try:
        # insert_malicious_ip(connection, cursor, "192.168.0.1", "::1")
        # select_all_malicious_ips(cursor)
        # delete_all_ip(connection, cursor)
        print()
    finally:
        connection.close()
