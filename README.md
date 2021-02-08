# KhanBank Scrape
KhanBank Exchange Rate Scraping tool

Utilized scrapy to scrape [Khan Bank Daily Rate](https://www.khanbank.com/mn/home/ratesForSites/ "Khanbank's exchange rate page")
 

Output would be
- date: Date of Exchange Rate
- from_currency: Static string 'MNT'
- to_currency: Currency code
- buy: Exchange Rate

To run the command:
```
scrapy crawl DailyRate -o output.json
```