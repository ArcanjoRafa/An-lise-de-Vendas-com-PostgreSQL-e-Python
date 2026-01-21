import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
from test_connection import connect

graficos = []


def plot(column1, column2, title, xlabel, ylabel):
        fig = plt.figure()
        plt.bar(column1,column2 )
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.xticks(rotation=45)
        plt.tight_layout()
        return fig


def query_cliente():
    query_cliente = """
        SELECT 
        c.nome AS cliente,
        SUM(v.quantidade * p.preco) AS faturamento
    FROM vendas v
    JOIN clientes c ON v.id_cliente = c.idcliente
    JOIN produtos p ON v.id_produto = p.idproduto
    GROUP BY c.nome
    ORDER BY faturamento DESC;
    """

    connector = connect()
    df_cliente = pd.read_sql(query_cliente, connector)
    connector.close()

    graf1=plot(column1=df_cliente["cliente"], column2=df_cliente["faturamento"],
         title="Faturamento por Cliente", xlabel="Cliente", ylabel="Faturamento")

    if graf1 not in graficos:
        graficos.append(graf1)



def query_mes():
    query_mes = """
        SELECT
        DATE_TRUNC('month', v.data) AS mes,
        SUM(v.quantidade * p.preco) AS faturamento
    FROM vendas v
    JOIN produtos p ON v.id_produto = p.idproduto
    GROUP BY mes
    ORDER BY mes;
    """

    connector = connect()
    df_mes = pd.read_sql(query_mes, connector)
    connector.close()

    graf2 = plot(column1=df_mes["mes"], column2=df_mes["faturamento"],
                 title="Faturamento Mensal", xlabel="Mês", ylabel="Faturamento")

    if graf2 not in graficos:
        graficos.append(graf2)



def query_produto():
    query_produto = """
    SELECT
        p.nome AS produto,
        SUM(v.quantidade) AS total_vendidos
    FROM vendas v
    JOIN produtos p ON v.id_produto = p.idproduto
    GROUP BY p.nome
    ORDER BY total_vendidos DESC;
    """

    connector = connect()
    df_produto = pd.read_sql(query_produto, connector)
    connector.close()

    graf3 = plot(column1=df_produto["produto"], column2=df_produto["total_vendidos"],
                 title="Produtos mais Vendidos", xlabel="Produto", ylabel="Quantidade Vendida")

    if graf3 not in graficos:
        graficos.append(graf3)



query_cliente()
query_mes()
query_produto()


print("""
Escolha o gráfico:
1) Faturamento por Cliente
2) Faturamento Mensal
3) Produtos Mais Vendidos
""")

op = int(input("Escolha uma opçao [1, 2, 3]: "))

grafico = graficos[op-1]
plt.show()

