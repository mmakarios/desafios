# Resolução Desafio 1

## Execução

Para execução do script, primeiramente coloque o texto que deseja formatar no arquivo "input.txt", que será lido pelo programa.

### Docker

Para execução do script utilizando o Docker, rode na linha de comando:

```docker build -t my-text-formatter .```

E em seguida:

```docker run -rm my-text-formatter```

### Python

Caso queira rodar o programa sem o Docker, simplesmente execute `python text_formatter.py` na linha de comando. Você não precisa estar no mesmo diretório do script para executá-lo.

#

Para passar um tamanho de linha máximo diferente do padrão (40 caracteres), adicione `--limit` ou `-l` seguido do número desejado no seu comando de execução no terminal. Por exemplo, para limitar o tamanho das linhas formatadas para 25 caracteres:

```docker run -rm my-text-formatter -l 25```

ou

```python text_formatter.py -l 25```

A execução do algoritmo formatará o seu texto e exibirá o resultado no terminal do seu sistema operacional.

## Desenvolvimento

Para o desenvolvimento do desafio das strings, antes de mais nada, o algoritmo procura um arquivo texto com nome de "input.txt" no mesmo diretório do script "text_formatter.py". A utilização da biblioteca `os.path` do Python permite que o programa encontre o caminho da origem da sua execução até o caminho do arquivo texto, permitindo a execução do script fora da pasta do mesmo (útil para ferramentas de debug).

A string resultante do arquivo texto então é passada para a função de formatação `text_formatter`.

Na função, as palavras do texto são percorridas verificando seu tamanho em caracteres, e são inseridas em linhas respeitando o limite máximo estipulado ao chamar a função, e caso a palavra tenha uma quebra de linha (`\n`).

Com essa divisão por linhas, é trivial aplicar a função de justificação na linha já existente, chamando a função `justify_text`. Nela, são contados os espaços entre as palavras na linha, e quantos espaços faltam para a justificação da mesma. Os espaços restantes então são distribuidos igualmente entre as palavras.

Por fim, as linhas são atribuídas à string `output` que é impressa no terminal ao final da execução (todas as palavras do texto foram percorridas).
