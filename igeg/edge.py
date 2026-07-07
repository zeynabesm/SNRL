from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, Any
import uuid


class EdgeType(Enum):

    SEMANTIC = "semantic"

    MAPPING = "mapping"

    RELATIONAL = "relational"

    FEATURE = "feature"

    INFERENCE = "inference"


@dataclass
class IGEGEdge:

    source: str

    target: str

    edge_type: EdgeType

    weight: float = 1.0

    metadata: Dict[str, Any] = field(default_factory=dict)

    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    def to_dict(self):

        return {

            "id": self.id,

            "source": self.source,

            "target": self.target,

            "type": self.edge_type.value,

            "weight": self.weight,

            "metadata": self.metadata

        }