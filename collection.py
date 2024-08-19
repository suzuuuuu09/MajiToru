from icrawler.builtin import BingImageCrawler

keuwords = ["風景", "動物", "植物", "人間", "夜景", "世界の風景"]
for keyword in keuwords:
    crawler = BingImageCrawler(storage={"root_dir": "img/" + keyword})
    crawler.crawl(keyword=keyword, max_num=20)