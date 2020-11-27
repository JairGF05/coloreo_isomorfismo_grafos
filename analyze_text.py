import nltk
import string
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
from nltk import SnowballStemmer
from nltk.corpus import stopwords#palabras cerradas
import networkx as nx
from nltk.util import bigrams
from graphviz import Digraph
from graphviz import Source


def tokenizar_texto(texto):# de manera normal solo separa en tokens sin ningun tipo de filtro excepto las minus
  #convertir a minusculas
  texto = texto.lower()
  #tokenizar texto
  texto_tokenizado = nltk.word_tokenize(texto)
  return texto_tokenizado

def limpiar_texto(texto):
  '''En esta función el texto se va a tokenizar pero a partir de una expresión regular '''
  spanishstemmer=SnowballStemmer('spanish')

  pattern = r'''(?x)                 #set flag to allow verbose regexps
              (?:[A-Z]\.)+          #abbreviations, e.g. U.S.A.
              | \w+(?:-\w+)*        #words with optional internal hyphens(guiones internos)
              | \$?\d+(?:\.\d+)?%?  #currency(dinero) and percentages, e.g. $12.40, 82%
              
  ''' 
  #Definiendo stop words(palabras de interrupción)
  stop_words = set(stopwords.words('spanish'))
  #convertir a minusculas
  texto = texto.lower()  

  #aplicando tokenización por medio de la expresión regular
  texto_tokenizado = nltk.regexp_tokenize(texto,pattern)

  #quitando palabras de intrerrupción (cerradas)
  words = [w for w in texto_tokenizado if not w in stop_words]

  #convirtiendo palabras en raices
  stems = [spanishstemmer.stem(token) for token in words]
  return stems

def crear_bigramas(texto):
  #tokenizando texto
  #texto_tokenizado = limpiar_texto(texto)
  #creando bigramas
  bigramas = list(bigrams(texto))
  #filtrando de  bigramas del texto sin tomar en cuenta caracteres especiales
  threshold = 1 # Con esto se eliminan signos de puntuación y caracteres especiales/
  bigramas_filtrados = [bigram for bigram in bigramas if len(bigram[0])>=threshold and len(bigram[1])>=threshold]
  return bigramas_filtrados

#función para crear tags
def crear_tags(texto):
  #texto = tokenizar_texto(texto)
  #texto_limpio = limpiar_texto(texto)
  text_tag = nltk.pos_tag(texto) #genera lista tipo [('i','NN'),...]

  #guardando los tags del texto en una nueva lista
  tag_new =[]
  for a,b in text_tag:
    tag_new.append(b)
  
  #Crear bigramas de los tags
  bigramas_tags = list(bigrams(tag_new))


  #ordenando los tags en una lista nueva
  partag = []
  for a,b in bigramas_tags:
    partag.append(a + "-" + b)

  return partag

#funcion para crear el grafo con el texto de interes
def analyze_texto(texto):
  #creando bigramas
  texto_limpio = limpiar_texto(texto)
  print("Se limpió el texto")

  bigramas_texto=[]
  bigramas_texto = crear_bigramas(texto_limpio)
  print("Se crearon los bigramas")

  #obteniendo tags
  partag=[]
  partag = crear_tags(texto_limpio)
  print("Se crearon tags")

  #creando grafo con graphviz
  #g = Digraph('G', filename='grafo.gv', format="png" )
  G = nx.Graph()

  #estableciendo atributos del grafo
  #hace el grafo mas pequeño
  #g.attr(size = '5')

  #hace que el grafo vaya de izquierda a derecha
  #g.attr(rankdir="LR")
  
  #modificando el tamaño de los nodos
  #g.attr('node', width = '.2', height ='.2')

  for a,b in bigramas_texto:
    subtag = partag.pop(0)
    G.add_edge(str(a), str(b),label=subtag)
  # g.view()
  return G

#importando
'''
archivo = open('el_quijote.txt', encoding="utf8")
texto = archivo.read()
print("Se leyó el archivo")
analyze_texto(texto)
print("Se grafico")
archivo.close()
'''
#texto = texto.lower()
#print(texto)

'''
Aqui empieza parte de isomorfismo
'''

def get_nodes(grafo):
  length= len(grafo.nodes)
  return length

def get_edges(grafo):
  length= len(grafo.edges)
  return length

def get_degree(grafo):
  degree = nx.degree(grafo)
  return degree

def coloring(G, node, color, colors_of_nodes):
  for neighbor in G.neighbors(node):
    color_of_neighbor = colors_of_nodes.get(neighbor, None)
    if color_of_neighbor == color:
      return False
  return True

def get_color_for_node(G, node, colors_of_nodes, colors):
  for color in colors:
    if coloring(G, node, color, colors_of_nodes): 
      return color

#funcion que colorea grafos
def coloreo_grafos(G, partag, bigramas_texto):
  #definiendo lista de colores
  colors = ['Red', 'Blue', 'Green', 'Yellow',  'Black', 'Pink', 'Orange', 'White', 'Gray', 'Purple', 'Brown', 'Navy']
  #lista = [(1,5),(1,3),(1,2),(1,4),(4,5),(1,5),(5,6),(1,6)]
  #definiendo diccionario para obtener color de los nodos
  colors_of_nodes={}
  #guardando los colores de cada nodo/ aqui deberia poder pintar cada nodo con su respectivo color
  
  for node in G.nodes():
      colors_of_nodes[node] = get_color_for_node(G, node, colors_of_nodes, colors)

  #pintando primer grafo con graphviz
  #creando nodos y pintandolos
  g = Digraph('G', filename='grafo.gv')
  g.attr(rankdir="LR")

  for nodo,color in colors_of_nodes.items():
    g.node(str(nodo),style ='filled', fillcolor=color) 

  #ahora hacer esto en un ciclo para evitar las delclaraciones
  for a,b in bigramas_texto:
    subtag = partag.pop(0)
    g.edge(str(a), str(b),label=subtag)   

  g.view()