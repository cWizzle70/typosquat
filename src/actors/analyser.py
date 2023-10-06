
from enums.threat_level import ThreatLevel
from models.typosquat import TypoSquat
import Levenshtein

class Analyser:

    def __init__(self, culprit: TypoSquat, original_domain: str):
        self.culprit: TypoSquat = culprit
        self.original_domain: str = original_domain

    def categorize(self) -> None:

        self.culprit.levenshtein_distance = Levenshtein.distance(self.original_domain, self.culprit.name)

        print()

        if self.is_malicious():
            self.culprit.threat_level = ThreatLevel.MALICIOUS

        elif self.is_suspicious():
            self.culprit.threat_level = ThreatLevel.SUSPICIOUS

        else:
            return

    def is_malicious(self):
        pass

    def is_suspicious(self):
        pass
