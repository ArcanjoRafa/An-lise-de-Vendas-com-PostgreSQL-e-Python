import test_connection



try:
    connector = test_connection.connect()
    print("conexao bem sucedida")
    connector.close()
except Exception as e:
    print(f"Erro {e}")