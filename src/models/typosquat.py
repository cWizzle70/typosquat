from dataclasses import dataclass, field
from types import CoroutineType
from typing import Dict, List

from enums.threat_level import ThreatLevel


@dataclass
class TypoSquat:

    name: str = ''
    ip: str = ''
    threat_level: ThreatLevel = ThreatLevel.BENIGN
    creation_date: str = ''
    nameservers: List[str] = field(default_factory=list)
    registrar: Dict[str, str] = field(default_factory=dict)
    country: str = ''
    city: str = ''
    asn: str = ''
    ip_is_flagged: bool = False
    levenshtein_distance: int = 0
