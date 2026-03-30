import os
import oracledb
from django.shortcuts import render
from django.http import JsonResponse
from dotenv import load_dotenv
from django.http import HttpResponse
from docx import Document
from bs4 import BeautifulSoup
from openai import OpenAI
import io

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_connection():
    conn = oracledb.connect(
        user=os.getenv("ORACLE_USER"),
        password=os.getenv("ORACLE_PASSWORD"),
        dsn=os.getenv("ORACLE_DSN")
    )
    return conn


def revisar_texto(request):
    html = request.POST.get("html")

    soup = BeautifulSoup(html, "html.parser")

    for img in soup.find_all("img"):
        img.decompose()

    texto = soup.get_text(separator="\n")

    prompt = f"""
    Você é um consultor de negócios. Melhore o texto abaixo para uma proposta profissional:

    {texto}
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return JsonResponse({
        "texto": response.choices[0].message.content
    })


def dashboard_page(request):
    return render(request, "dashboard.html")


def relatorios_page(request):
    return render(request, "relatorios.html")


def gerar_word(request):
    html = request.POST.get("html")

    soup = BeautifulSoup(html, "html.parser")

    doc = Document()
    doc.add_heading("Proposta", 0)

    for linha in soup.get_text().split("\n"):
        if linha.strip():
            doc.add_paragraph(linha)

    buffer = io.BytesIO()
    doc.save(buffer)
    buffer.seek(0)

    response = HttpResponse(
        buffer,
        content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    )
    response['Content-Disposition'] = 'attachment; filename=proposta.docx'

    return response


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
