# Scrape HDB Website to get unit prices and sqm
To get the unit prices sqm, I would have to mouseover each unit number. This script uses the web automation tool, Selenium, to mouseover each unit number and capture the each unit price and sqm, giving me a `.csv`.

Currently, the script only works for Toa Payoh Bidadari Parkview, but I believe is the structure of HDB web page is similar, it can be generalized to other projects as well.

## How to run
1. Create conda environment
```bash
conda env create -f env.yml
```
1. edit config in `config.toml`
1. Run script
```bash
conda activate hdb_scraper
python scrape.py
```