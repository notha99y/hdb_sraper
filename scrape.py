import pandas as pd
import toml
from bs4 import BeautifulSoup

from utils import get_browser

if __name__ == "__main__":
    config = toml.load("config.toml")
    fields = config["fields"]
    url = f"https://services2.hdb.gov.sg/webapp/BP13AWFlatAvail/BP13EBSFlatSearch?Town=Toa+Payoh&Flat_Type=BTO&selectedTown=Toa+Payoh&Flat={fields.get('room')}-Room&ethnic={fields.get('ethnic')}&ViewOption=A&projName=N9%3BC17&Block=0&DesType=A&EthnicA=&EthnicM=&EthnicC=C&EthnicO=&numSPR=&dteBallot=202011&Neighbourhood=&Contract=&BonusFlats1=N&searchDetails=Y&brochure=true"

    browser = get_browser()
    browser.get(url)
    block_buttons = browser.find_elements_by_class_name("e-more-info")

    parkview_button_block_dict = {"A": 0, "B": 1, "C": 2}

    interested_block = fields.get("block")

    block_buttons[parkview_button_block_dict[interested_block]].click()
    soup = BeautifulSoup(browser.page_source, "html.parser")

    tables = soup.find_all("table")

    unit_table = tables[1]
    unit_anchors = unit_table.find_all("a")

    unit_numbers = []
    for anchor in unit_anchors:
        unit_numbers.append(anchor.font.text)

    prices = []
    sqms = []

    for unit_number in unit_numbers:
        browser.find_element_by_id(f"{unit_number}").click()
        soup = BeautifulSoup(browser.page_source, "html.parser")
        price, sqm = soup.find("span", {"id": f"{unit_number}k"}).text.split(
            "____________________"
        )
        raw_string = sqm.encode("unicode_escape").decode()
        sqm = raw_string.split("\\x")[0]
        prices.append(price)
        sqms.append(sqm)

    res_df = pd.DataFrame()
    res_df["unit_number"] = unit_numbers
    res_df["price"] = prices
    res_df["sqm"] = sqms

    res_df.to_csv(
        f"{fields.get('project')}_unitprices_{fields.get('room')}room_block{fields.get('block')}.csv",
        index=False,
    )
