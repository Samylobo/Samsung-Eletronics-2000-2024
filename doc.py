# Este ambiente Python 3 vem com muitas bibliotecas analíticas úteis instaladas
# É definido pela imagem Docker kaggle/python: https://github.com/kaggle/docker-python
# Por exemplo, aqui estão vários pacotes úteis para carregar

'''importar numpy como np  álgebra linear
importar pandas como pd '''# processamento de dados, E/S de arquivo CSV (por exemplo, pd.read_csv)

# Os arquivos de dados de entrada estão disponíveis no diretório somente leitura "../input/"
# Por exemplo, executar isto (clicando em executar ou pressionando Shift+Enter) listará todos os arquivos no diretório de entrada
'''
importar sistema operacional
para dirname, _, nomes de arquivos em os.walk('/kaggle/input'):
    para nome de arquivo em nomes de arquivos:
        print(os.path.join(nome do diretório, nome do arquivo))
'''
# Você pode gravar até 20 GB no diretório atual (/kaggle/working/) que é preservado como saída quando você cria uma versão usando "Salvar e executar tudo"
# Você também pode gravar arquivos temporários em /kaggle/temp/, mas eles não serão salvos fora da sessão atual
'''
Data: A data do pregão.
Aberto: O preço de abertura das ações da Samsung Electronics no início do pregão.
Alto: O preço mais alto alcançado pela ação durante o pregão.
Baixo: O menor preço atingido pela ação durante o pregão.
Fechamento: O preço de fechamento das ações da Samsung Electronics no final do pregão.
Adj Close: O preço de fechamento ajustado, que leva em conta quaisquer ações corporativas ou outros ajustes que afetem o preço das ações.
Volume: Quantidade total de ações negociadas durante o pregão.
'''
'''Este conjunto de dados fornece preços diários de ações da Samsung Electronics, uma das principais empresas globais de tecnologia. Inclui métricas financeiras importantes para cada dia de negociação, permitindo uma análise aprofundada do desempenho das ações e da atividade do mercado durante esse período.

Usos potenciais:

Analisando tendências históricas nos preços das ações da Samsung Electronics.
(preços de fechamento das ações da samsung )
melhor preco de fechamento foi no ano de 2021 altingindo 9.0 em maio. 

Explorando correlações entre o volume de negociação e as flutuações de preços.
Coeficiente de correlação entre Volume e Preço de Fechamento: -0.2990272805025972


Investigar o impacto de fatores externos ou eventos de mercado no desempenho das ações.
Em 2021, vários eventos impactaram o mercado e, consequentemente, as ações da Samsung Electronics. Alguns dos principais eventos incluem:
o lançamento  Galaxy S21, tablets, smartwatches e outros dispositivos eletrônicos
no primeiro trimestre , os resultados trimestrais de açoes da samsung foram anunciados.
Em maio de 2021 na alta de fechamento em ações , houve uma mudança de liderança , onde a samsung anunciou que Kim Ki-nam assumiria o cargo de CEO da divisão de eletrônicos de consumo, enquanto Koh Dong-jin se tornaria o CEO da 
divisão de TI e comunicações móveis. 
Logo apos isso veio a Pandemia - COVID afetando a economia global em 2021, com impactos significativos nos mercados financeiros.


Nota: Este conjunto de dados pode ser utilizado por investidores, analistas e pesquisadores interessados ​​em compreender a dinâmica do comportamento do mercado de ações da Samsung Electronics durante o período especificado.
 texto pro github : O objetivo deste projeto é realizar uma ANÁLISE EXPLORATÓRIA e uma manipulação mais conhecida
 
 redmi : > Visualização da Tabela de notas e a tabela de alunos:

![PREVIEW](TabelaDeNotasAlunos.png)

> União Da Tabela Alunos e Notas:
 
 '''







