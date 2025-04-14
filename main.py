import sys
from database import setup_database, insert_malicious_ip, select_all_malicious_ips, delete_all_ip
from view.autentification import authenticate_user 

if __name__ == "__main__":
    authentication = authenticate_user()
    if not authentication:
        sys.exit() # Finalize the process

    connection, cursor = setup_database()
    try:
        # Exemplos dos comandos no banco de dados:
        # insert_malicious_ip(connection, cursor, "192.168.0.1", "::1")
        # select_all_malicious_ips(cursor)
        # delete_all_ip(connection, cursor)

        print()

        

    finally:
        connection.close()
