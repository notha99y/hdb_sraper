# Scrape HDB Website to get unit prices and sqm
To get the unit prices sqm, I would have to mouseover each unit number. This script uses the web automation tool, Selenium, to mouseover each unit number and capture the each unit price and sqm, giving me a `.csv`.

Currently, the script only works for **Toa Payoh Bidadari Parkview**, but I believe if the structure of HDB web page is similar, it can be generalized to other projects as well.

## How to run
1. [Download](https://chromedriver.chromium.org/downloads) selenium's chrome driver. 
1. Create conda environment
```bash
conda env create -f env.yml
```
1. ~~edit config in `config.toml`~~. The new code has deprecated `config.toml` Change the arguments in the `.scrape` method of `HDBScraper`
1. change path to chrome driver in `utils.py`
1. Run script
```bash
conda activate hdb_scraper
python scrape.py
```

## Some Gotchas
1. The script will sometimes fail when selenium controlled broswer is not big enough or have not loaded the tables.
 