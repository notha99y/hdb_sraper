from datetime import datetime

import pandas as pd
from bs4 import BeautifulSoup

from constants import HDBScraperConstants as HSC
from utils import get_browser


class HDBScraper:
    def __init__(self,):
        self.button_block_dict = {
            "Parkview": {"A": 0, "B": 1, "C": 2},
            "Beacon": {
                "222A": 0,
                "222B": 1,
                "223A": 2,
                "223B": 3,
                "223C": 4,
                "224A": 5,
                "224B": 6,
                "224C": 7,
            },
        }
        self.project_code_dict = {
            "Parkview": "N9%3BC17",
            "Beacon": "N9%3BC14A",
        }

    def print_summary(self):
        if self.project:
            print("Scraping Summary")
            print("-" * 30)
            print(f"Project: {self.project}")
            print(f"{self.room}-Room")
            print(f"Ethnic: {self.ethnic}")
            print(f"Scrape all: {self.scrape_all}")
            print(f"With price: {self.with_price}")
        else:
            print("Summary is not available")

    def scrape(
        self,
        room=4,
        block="A",
        ethnic="C",
        project="Parkview",
        scrape_all=True,
        with_price=True,
    ):
        self.room = room
        self.block = block
        self.ethnic = ethnic
        self.project = project
        self.scrape_all = scrape_all
        if not self.scrape_all:
            self.with_price = False
        else:
            self.with_price = with_price

        project_code = self.project_code_dict[self.project]
        if scrape_all:
            view_option = "A"
        else:
            view_option = 2

        self.print_summary()
        self.url = f"https://services2.hdb.gov.sg/webapp/BP13AWFlatAvail/BP13EBSFlatSearch?Town=Toa+Payoh&Flat_Type=BTO&selectedTown=Toa+Payoh&Flat={room}-Room&ethnic={ethnic}&ViewOption={view_option}&projName={project_code}&Block=0&DesType=A&EthnicA=&EthnicM=&EthnicC=C&EthnicO=&numSPR=&dteBallot=202011&Neighbourhood=&Contract=&BonusFlats1=N&searchDetails=Y&brochure=true"
        print("-" * 88)
        print(self.url)
        print("-" * 88)
        browser = get_browser()

        browser.get(self.url)
        block_buttons = browser.find_elements_by_class_name("e-more-info")
        project_block_button_dict = self.button_block_dict[self.project]

        block_buttons[project_block_button_dict[self.block]].click()
        soup = BeautifulSoup(browser.page_source, "html.parser")

        tables = soup.find_all("table")

        unit_table = tables[1]
        if self.scrape_all:
            unit_anchors = unit_table.find_all("a")

            unit_numbers = []
            for anchor in unit_anchors:
                unit_numbers.append(anchor.font.text)
            res_df = pd.DataFrame()
            res_df["unit_number"] = unit_numbers

        else:
            unit_numbers = []
            unit_table_datas = unit_table.find_all("td")
            for td in unit_table_datas:
                unit_numbers.append(td.text.strip())
            print(unit_numbers)
            res_df = pd.DataFrame()
            res_df["unit_number"] = unit_numbers

        if self.with_price and self.scrape_all:
            prices = []
            sqms = []

            for unit_number in unit_numbers:
                browser.find_element_by_id(f"{unit_number}").click()
                soup = BeautifulSoup(browser.page_source, "html.parser")
                price, sqm = soup.find(
                    "span", {"id": f"{unit_number}k"}
                ).text.split("____________________")
                raw_string = sqm.encode("unicode_escape").decode()
                sqm = raw_string.split("\\x")[0]
                prices.append(price)
                sqms.append(sqm)

            res_df["price"] = prices
            res_df["sqm"] = sqms

        self.res_df = res_df

    def save_results(self):
        if self.scrape_all:
            self.res_df.to_csv(
                f"{self.project}_unitprices_{self.room}room_block{self.block}.csv",
                index=False,
            )

        else:
            today = datetime.now().date()
            self.res_df.to_csv(
                f"Taken_{today}_block{self.block}.csv", index=False
            )


if __name__ == "__main__":
    scraper = HDBScraper()

    # interested_blocks = [
    #     "A", "B", "C"
    # ]
    interested_blocks = [
        # "222A",
        # "222B",
        # "223A",
        # "223B",
        "223C",
        "224A",
        "224B",
        "224C",
    ]

    for block in interested_blocks:
        scraper.scrape(scrape_all=True, block=block, project="Beacon")
        scraper.save_results()
