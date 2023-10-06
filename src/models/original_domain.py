from typing import List


from actors.analyser import Analyser
from actors.clone_finder import CloneFinder
from actors.investigator import Investigator
from models.typosquat import TypoSquat


class OriginalDomain:

    def __init__(self, name: str, dns_twist_link: str):
        self.name = name
        self.dns_twist_link = dns_twist_link
        self.clones: List[TypoSquat] = self.get_clones()

    def gather_info(self):
        self.get_clones()
        self.investigate_clones()
        self.analyze_clones()

    def get_clones(self) -> List[TypoSquat]:
        clones = []

        for domain, ip in CloneFinder.find_clones(self.dns_twist_link):
            typosquat = TypoSquat(domain, ip)
            clones.append(typosquat)

            # remove this break to process more that one clone
            break

        return clones


    def investigate_clones(self) -> None:
        for clone in self.clones:
            Investigator(clone).investigate()

        print()

    def analyze_clones(self) -> None:
        for clone in self.clones:
            Analyser(clone, self.name).categorize()
