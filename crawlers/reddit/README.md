# Resolução Desafio 2

## Execução

Para executar o crawler de subreddits, você poderá usar o Docker ou Python.

### Docker

Caso queira rodar o programa pelo Docker, execute o comando seguinte na pasta do algoritmo (/crawlers/reddit/):

```docker build -t reddit_crawl .```

Em seguida execute a imagem do algoritmo com o comando:

```docker run reddit_crawl scrapy runspider reddit.py -L ERROR -a subreddits="askreddit;cats"```

### Python

Para rodar o algoritmo sem o Docker, primeiro é necessário importar a biblioteca [Scrapy](https://scrapy.org/):

```pip install scrapy```

Após instalada, digite o comando no seu terminal:

```scrapy runspider reddit.py -L ERROR -a subreddits="askreddit;cats"```

#

Independente de como você rodar o programa, você deverá substituir o valor do parâmetro `subreddits=` com os subreddits de sua escolha.

Separando o comando em partes, a primeira parte diz `docker run reddit_crawl`, que roda a imagem com o nome `reddit_crawl` que você atribuiu no comando anterior. Em seguida, `scrapy runspider` é um comando da biblioteca [Scrapy](https://scrapy.org/) para executar uma spider (crawler) de nome `reddit.py`, que é o nome do arquivo que contém a lógica principal de scraping para navegar pelas páginas. `-L ERROR` atribui o valor `ERROR` para o nível de logging que o comando imprimirá no terminal. `-a` indica que o próximo valor será um parâmetro reconhecido pelo programa. Nesse caso, `subreddits`.

## Desenvolvimento

Para realizar o scraping, foi utilizada a biblioteca [Scrapy](https://scrapy.org/), devido à sua simples e direta configuração para projetos pequenos.

O Reddit disponibiliza publicamente uma relação em JSON atualizada para cada um dos seus subreddits contendo inúmeras informações de todas as threads daquele subreddit. Isso facilita a complexidade do scraping no nosso caso visto que os dados necessários estão disponíveis de forma mais limpa, acessível e menos propensa a erros caso o site sofra alguma alteração visual.

Com isso, é preciso somente receber a lista dos subreddits e mandar um crawler para suas respectivas páginas em JSON.

Ao receber a informações de cada um, o algoritmo filtra as threads que possuem pontuação acima ou igual a 5000 e a imprime juntamente com seu título, nome do subreddit e link para visualização da thread no terminal.
