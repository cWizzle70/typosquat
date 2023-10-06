
from enums.threat_level import ThreatLevel
from models.typosquat import TypoSquat


class Analyser:

    def __init__(self, culprit: TypoSquat):
        self.culprit = culprit

    def categorize(self):
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
