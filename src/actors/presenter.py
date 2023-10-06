
from models.original_domain import OriginalDomain


class Presenter:

    def __init__(self, domain: OriginalDomain):
        self.domain = domain

    def display(self) -> None:
        pass

    def convert_to_df(self):
        pass
