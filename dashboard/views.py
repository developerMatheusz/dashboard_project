import os
import oracledb
from django.shortcuts import render
from django.http import JsonResponse
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    conn = oracledb.connect(
        user=os.getenv("ORACLE_USER"),
        password=os.getenv("ORACLE_PASSWORD"),
        dsn=os.getenv("ORACLE_DSN")
    )
    return conn


def dashboard_page(request):
    return render(request, "dashboard.html")


def pedidos_data(request):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        select num_pedido, dt_emis, vlr_liq_ipi
        from tpedidos_venda
        where tipo = 'PDV'
        fetch first 10 rows only
    """

    cursor.execute(query)

    data = []
    for num_pedido, dt_emis, vlr in cursor.fetchall():
        data.append({
            "num_pedido": num_pedido,
            "dt_emis": dt_emis.strftime("%Y-%m-%d") if dt_emis else None,
            "vlr_liq_ipi": float(vlr) if vlr else 0
        })

    cursor.close()
    conn.close()

    return JsonResponse(data, safe=False)
