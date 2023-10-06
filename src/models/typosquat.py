from dataclasses import dataclass, field
from typing import Dict, List

from enums.threat_level import ThreatLevel


@dataclass
class TypoSquat:
    ip: str = ""
    asn: str = ""
    city: str = ""
    name: str = ""
    country: str = ""
    creation_date: str = ""
    ip_is_flagged: bool = False
    levenshtein_distance: int = 0
    threat_level: ThreatLevel = ThreatLevel.BENIGN
    nameservers: List[str] = field(default_factory=list)
    registrar: Dict[str, str] = field(default_factory=dict)
