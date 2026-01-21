import psycopg2
from test_connection import connect

def insert_clients():
    clientes = [
        ("Ana Silva", "ana@email.com", "12345678901", "São Paulo", "F", "SP"),
        ("João Souza", "joao@email.com", "23456789012", "Rio de Janeiro", "M", "RJ"),
        ("Maria Lima", "maria@email.com", "34567890123", "Belo Horizonte", "F", "MG"),
        ("Carlos Pereira", "carlos@email.com", "45678901234", "Curitiba", "M", "PR"),
        ("Fernanda Rocha", "fernanda@email.com", "56789012345", "Porto Alegre", "F", "RS"),
        ("Lucas Martins", "lucas@email.com", "67890123456", "Campinas", "M", "SP"),
        ("Patrícia Gomes", "patricia@email.com", "78901234567", "Salvador", "F", "BA"),
        ("Rafael Costa", "rafael@email.com", "89012345678", "Fortaleza", "M", "CE"),
        ("Juliana Alves", "juliana@email.com", "90123456789", "Recife", "F", "PE"),
        ("Bruno Santos", "bruno@email.com", "01234567890", "Manaus", "M", "AM")
    ]

    connector = connect()
    cursor = connector.cursor()

    cursor.executemany("""
        INSERT INTO CLIENTES(NOME, EMAIL, CPF, CIDADE, SEXO, UF)
        VALUES(%s, %s, %s, %s, %s, %s)
    """,clientes)

    connector.commit()
    cursor.close()
    connector.close()


def insert_products():
    produtos = [
        ("Notebook", 3500.00),
        ("Mouse", 80.00),
        ("Teclado", 150.00),
        ("Monitor", 900.00),
        ("Headset", 250.00),
        ("Impressora", 1200.00),
        ("Cadeira Gamer", 1100.00),
        ("HD Externo", 400.00),
        ("Pen Drive", 60.00),
        ("Webcam", 300.00)
    ]

    connector = connect()
    cursor = connector.cursor()

    cursor.executemany("""
        INSERT INTO PRODUTOS(NOME,PRECO)
         VALUES(%s, %s)
    """,produtos)

    connector.commit()
    cursor.close()
    connector.close()

def insert_sales():
    vendas = [
        (1, 1, 1, "2024-01-05"),
        (2, 2, 2, "2024-01-08"),
        (3, 3, 1, "2024-01-10"),
        (4, 4, 1, "2024-01-12"),
        (5, 5, 2, "2024-01-15"),
        (6, 1, 1, "2024-02-02"),
        (7, 7, 1, "2024-02-05"),
        (8, 8, 3, "2024-02-10"),
        (9, 9, 5, "2024-02-15"),
        (10, 10, 2, "2024-02-20"),
        (1, 3, 2, "2024-03-01"),
        (2, 6, 1, "2024-03-05"),
        (3, 4, 1, "2024-03-10"),
        (4, 5, 2, "2024-03-15"),
        (5, 2, 3, "2024-03-20")
    ]

    connector = connect()
    cursor= connector.cursor()

    cursor.executemany("""
        INSERT INTO VENDAS(ID_CLIENTE, ID_PRODUTO, QUANTIDADE, DATA)
        VALUES(%s, %s, %s, %s)
    """,vendas)

    connector.commit()
    cursor.close()
    connector.close()


if __name__ == "__main__":
    insert_clients()
    insert_products()
    insert_sales()
    print("Valores inseridos com sucesso!")