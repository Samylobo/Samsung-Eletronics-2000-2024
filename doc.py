Desafio retirado do site :
https://www.kaggle.com/datasets/michellevp/samsung-electronics-stock-price-2000-2024


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









