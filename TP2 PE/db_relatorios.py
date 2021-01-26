import shelve


def find_all():
    with shelve.open('relatorios.db') as s:
        return list(s.keys())


def find_one(relatorio):
    with shelve.open('relatorios.db') as s:
        return { 'titulo': relatorio, 'conteudo': s[relatorio] }

def remove(titulo):
	with shelve.open('relatorios.db', writeback=True) as s:
		del s[titulo]
		return list(s.keys())

def insert(relatorio_data):
    with shelve.open('relatorios.db', writeback=True) as s:
        print(relatorio_data)
        s[relatorio_data['titulo']] = relatorio_data['conteudo']
        return list(s.keys())



def alterar(relatorio):
    with shelve.open('relatorios.db', writeback=True) as s:
        print(relatorio_data)
        s[relatorio_data['titulo']] = relatorio_data['conteudo']
        return list(s.keys())
        

