from dataclasses import dataclass

from enums.threat_level import ThreatLevel


@dataclass
class TypoSquat:

    name: str = ''
    ip: str = ''
    threat_level: ThreatLevel = ThreatLevel.BENIGN
