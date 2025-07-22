
import os
from dotenv import load_dotenv
import pandas as pd
import psycopg2 as pg
from sqlalchemy import create_engine
import panel as pn

pn.extension('tabulator', notifications=True)

load_dotenv()
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

con = pg.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASS)
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}')

usuario_id = pn.widgets.IntInput(name="ID do Usuário", value=1)
data = pn.widgets.DatePicker(name="Data")
hora_dormir = pn.widgets.TimePicker(name="Hora de Dormir")
hora_acordar = pn.widgets.TimePicker(name="Hora de Acordar")
nota_qualidade = pn.widgets.IntSlider(name="nota_qualidade (0-10)", start=0, end=10, value=5)

cpf_busca = pn.widgets.TextInput(name="Buscar por ID Usuário (opcional)", placeholder="Deixe em branco para todos")
btnConsultar = pn.widgets.Button(name="Consultar", button_type="primary")
btnInserir = pn.widgets.Button(name="Inserir", button_type="success")
btnAtualizar = pn.widgets.Button(name="Atualizar", button_type="warning")
btnExcluir = pn.widgets.Button(name="Excluir", button_type="danger")
id_registro = pn.widgets.IntInput(name="ID do Registro para Atualizar ou Excluir", value=0)

def queryAll():
    filtro = cpf_busca.value.strip()
    if filtro:
        df = pd.read_sql(f"SELECT * FROM sono WHERE usuario_id = {filtro}", engine)
    else:
        df = pd.read_sql("SELECT * FROM sono", engine)
    return pn.widgets.Tabulator(df)

def on_inserir(event=None):
    try:
        cur = con.cursor()
        cur.execute("""
            INSERT INTO sono (usuario_id, data, hora_dormir, hora_acordar, nota_qualidade)
            VALUES (%s, %s, %s, %s, %s)
        """, (usuario_id.value, data.value, hora_dormir.value, hora_acordar.value, nota_qualidade.value))
        con.commit()
        return queryAll()
    except Exception as e:
        cur.execute("ROLLBACK")
        return pn.pane.Alert(f"Erro ao inserir: {e}")

def on_atualizar(event=None):
    try:
        cur = con.cursor()
        cur.execute("""
            UPDATE sono SET
                usuario_id=%s,
                data=%s,
                hora_dormir=%s,
                hora_acordar=%s,
               nota_qualidade=%s
            WHERE id=%s
        """, (usuario_id.value, data.value, hora_dormir.value, hora_acordar.value, nota_qualidade.value, id_registro.value))
        con.commit()
        return queryAll()
    except Exception as e:
        cur.execute("ROLLBACK")
        return pn.pane.Alert(f"Erro ao atualizar: {e}")

def on_excluir(event=None):
    try:
        cur = con.cursor()
        cur.execute("DELETE FROM sono WHERE id=%s", (id_registro.value,))
        con.commit()
        return queryAll()
    except Exception as e:
        cur.execute("ROLLBACK")
        return pn.pane.Alert(f"Erro ao excluir: {e}")

crud_table = pn.bind(
    lambda c, i, a, e: on_inserir() if i else on_atualizar() if a else on_excluir() if e else queryAll(),
    btnConsultar, btnInserir, btnAtualizar, btnExcluir
)

pn.Row(
    pn.Column(
        pn.pane.Markdown("## Controle de Sono"),
        usuario_id, data, hora_dormir, hora_acordar, nota_qualidade,
        id_registro,
        pn.Row(btnConsultar, btnInserir, btnAtualizar, btnExcluir),
        cpf_busca
    ),
    pn.Column(crud_table)
).servable()

