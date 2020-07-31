import urllib.request
import tabula 
# import pandas as pd

urllib.request.urlretrieve('http://www.ans.gov.br/images/stories/Plano_de_saude_e_Operadoras/tiss/Padrao_tiss/tiss3/Padrao_TISS_Componente_Organizacional_202006.pdf', "Padrao_TISS_Componente_Organizacional_202006.pdf")
pdf_file = open('Padrao_TISS_Componente_Organizacional_202006.pdf', 'rb')

path = '/Users/mrock/Desktop/python/Padrao_TISS_Componente_Organizacional_202006.pdf'
df = tabula.read_pdf(path, pages = '81,82,83,84,85,86,87,88', lattice  = False)
print(df)
