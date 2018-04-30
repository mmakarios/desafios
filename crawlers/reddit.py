import json
import scrapy


class Reddit(scrapy.Spider):
    name = "reddit"
    reddit_url_preffix = "https://www.reddit.com"

    def start_requests(self):
        try:
            subreddits = getattr(self, 'subreddits')
        except AttributeError:
            raise AttributeError(
                "Indique os subreddits separando-os com ponto e virgula (;). Exemplo:\n scrapy runspider reddit.py -a subreddits=askreddit;cats;brasil")
        else:
            if not subreddits:
                raise AttributeError(
                    "Indique os subreddits separando-os com ponto e virgula (;). Exemplo:\n scrapy runspider reddit.py -a subreddits=\"askreddit;cats;brasil\"")
            for subreddit in subreddits.split(";"):
                url = f'{self.reddit_url_preffix}/r/{subreddit}.json'
                yield scrapy.Request(url)

    def parse(self, response):
        jsonresponse = json.loads(response.body_as_unicode())
        threads = jsonresponse["data"]["children"]

        for thread in threads:
            data = thread["data"]
            if data["score"] >= 1500:
                print("Pontuação:", data["score"])
                print("Subreddit:", data["subreddit"])
                print("Título:", data["title"])
                print("Link:", self.reddit_url_preffix + data["permalink"])
                print()
