from re import *
import jinja2  as j2




def extract(): # extrai a informação do relatório em XML

	with open("livros.xml") as f:
		report=f.read()
	
	info=[]

	labels = findall(r'<.*>',report)

	for label in labels:
		chave=search(r'</(.*)>',label)
		v=search(r'>(.*)<',label)
		if v:
			info.append((chave[1],v[1]))

	return info

def refile(filename): # devolve texto

	with open(filename) as f:
		report=f.read()

	return report


def extract_dict(l,report): # devolve dicionário

	info = {}
	for elem in l:
		v=findall(rf"<({elem} .*)>((?:.|\n)*?)</{elem}>",report)
		for vl in v:
			info[vl[0]]=vl[1]

	return info

def extract_dict_sem_vals(l,report): # devolve dicionário

	info = {}
	for elem in l:
		v=findall(rf"<({elem})>((?:.|\n)*?)</{elem}>",report)
		for vl in v:
			info[vl[0]]=vl[1]

	return info

def extrai_listaH(xml,tag):

	info = []

	for miolo in findall(rf'<{tag}>((?:.|\n)*?)</{tag}>',xml):
		info.append(miolo)

	return info


def preenche2(info,i):

	t = j2.Template( """
<html>
<head>
  <title> Livros </title>
  <meta charset="UTF-8"/>
</head>
<body>
    {% for el in livros %}
     <h2> Título da Obra: </h2>
     <p> {{el['title']}}  </p>
	 <hr/>
	 <h2> Autor: </h2>
	 <p> {{el['author']}} </p>
	 <hr/>
	 <h2> Género da Obra Literária: </h2>
	 <p> {{el['genre']}} </p>
	 <hr/>
	 <h2> Data de Publicação: </h2>
	 <p> {{el['published']}}</p>
	 <hr/>
	 <h2> Frase Caracteristica Do Livro </h2>
	 <p> {{el['quote']}} </p>
    {% endfor %}

</body>
</html>
""")

	print(t.render(info))
	d=open("HTML%s.html"%(str(i)), "w")
	d.write(t.render(info))



def extrai_relatorio1():
	info = extract()
	f = refile('livros.xml') 
	livros=extract_dict( ['livro'],f )
	dic={}
	#dic['livros']=[]
	i=0
	for livro,linfo in livros.items():
		
		d = extract_dict_sem_vals(['title','author','genre','published', 'quote'] ,linfo) 
		dic['livros']=[d]
		#print(dic)
		preenche2(dic,i)
		i+=1
	
extrai_relatorio1()

