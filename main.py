from model.database import setup_database, insert_malicious_ip, select_all_malicious_ips, delete_all_ip
from view.interface import create_an_authentication_interface, initialize_the_network_manager_interface

if __name__ == "__main__":
    create_an_authentication_interface()

    connection, cursor = setup_database()

    initialize_the_network_manager_interface()

    try:
        # Exemplos dos comandos no banco de dados:
        # insert_malicious_ip(connection, cursor, "192.168.0.1", "::1")
        # select_all_malicious_ips(cursor)
        # delete_all_ip(connection, cursor)

        print()

    finally:
        connection.close()
        