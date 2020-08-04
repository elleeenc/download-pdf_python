import urllib.request
import tabula 

urllib.request.urlretrieve('http://www.ans.gov.br/images/stories/Plano_de_saude_e_Operadoras/tiss/Padrao_tiss/tiss3/Padrao_TISS_Componente_Organizacional_202006.pdf', "Padrao_TISS_Componente_Organizacional_202006.pdf")
pdf_file = open('Padrao_TISS_Componente_Organizacional_202006.pdf','rb')

path ='/Users/mrock/Desktop/python/Padrao_TISS_Componente_Organizacional_202006.pdf'
df = (tabula.io.read_pdf(path,pages = '81-88', encoding = 'utf-8'))
print(df)

tabula.convert_into(path,output_path= 'tabela.csv', output_format = 'csv', pages = '81-88')

