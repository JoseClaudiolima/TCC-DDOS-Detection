from model.database import setup_database, insert_malicious_ip, select_all_malicious_ips, delete_all_ip
from view.interface import create_an_authentication_interface, initialize_the_network_manager_interface
from controller.controller import read_data_with_sample_of_conections

if __name__ == "__main__":
    try:
        create_an_authentication_interface()

        connection, cursor = setup_database()

        data = read_data_with_sample_of_conections()

        initialize_the_network_manager_interface(data)

        # In real situation, we'll need to do a thread here, because will happen at the same time: 
        # 1. Interface Iniciation
        # 2. Network Management (and its own threads)
        
        # Commands examples to use in database:
        # insert_malicious_ip(connection, cursor, "192.168.0.1", "::1")
        # select_all_malicious_ips(cursor)
        # delete_all_ip(connection, cursor)

    finally:
        connection.close()
