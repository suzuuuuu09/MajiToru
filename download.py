from icrawler.builtin import GoogleImageCrawler
from icrawler.downloader import Downloader

keywords = {
        "風景":"landscape",
        "動物":"animal",
        "植物":"plant",
        "食べ物":"food",
        "夜景":"night_view",
        "建築物":"building"
    }

for keyword in keywords:
    crawler = GoogleImageCrawler(storage={"root_dir": "img/" + keywords[keyword]})
    crawler.crawl(keyword=keyword, max_num=100)