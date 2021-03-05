class HDBScraperConstants:
    project_code_map = {"Parkview": "N9%3BC17", "Beacon": "N9%3BC14A",}
    room = 4
    ethnic = "C"
    block = "233A"
    view_option = "A"
    project = "Parkview"
    project_code = project_code_map[project]

    constant_dict = {
        "base_url": f"https://services2.hdb.gov.sg/webapp/BP13AWFlatAvail/BP13EBSFlatSearch?Town=Toa+Payoh&Flat_Type=BTO&selectedTown=Toa+Payoh&Flat={room}-Room&ethnic={ethnic}&ViewOption={view_option}&projName={project_code}&Block=0&DesType=A&EthnicA=&EthnicM=&EthnicC=C&EthnicO=&numSPR=&dteBallot=202011&Neighbourhood=&Contract=&BonusFlats1=N&searchDetails=Y&brochure=true",
        "rooms": ["3", "4", "5"],
        "ethnics": ["A", "C", "M", "O"],
        "projects": ["Parkview", "Beacon"],
        "project_code_map": {"Parkview": "N9%3BC17", "Beacon": "N9%3BC14A",},
        "parkview_button_block_map": {"233A": 0, "233B": 1, "233C": 2},
        "bartley_button_block_map": {
            "222A": 0,
            "222B": 1,
            "223A": 2,
            "223C": 3,
            "224A": 4,
            "224B": 5,
            "224C": 6,
        },
    }

    @classmethod
    def base_url(cls):
        return cls.constant_dict["base_url"]

    @classmethod
    def rooms(cls):
        return cls.constant_dict["rooms"]

    @classmethod
    def ethnics(cls):
        return cls.constant_dict["ethnics"]

    @classmethod
    def projects(cls):
        return cls.constant_dict["projects"]

    @classmethod
    def project_code_map(cls):
        return cls.constant_dict["project_code_map"]

    @classmethod
    def parkview_button_block_map(cls):
        return cls.constant_dict["parkview_button_block_map"]

    @classmethod
    def bartley_button_block_map(cls):
        return cls.constant_dict["bartley_button_block_map"]