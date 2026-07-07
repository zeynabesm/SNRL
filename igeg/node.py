from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, Any
import uuid


class NodeType(Enum):
    INTENT = "intent"
    CONCEPT = "concept"
    TABLE = "table"
    ATTRIBUTE = "attribute"
    OPERATOR = "operator"
    FEATURE = "feature"
    TARGET = "target"


@dataclass
class IGEGNode:

    node_type: NodeType
    name: str

    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self):

        return {

            "id": self.id,
            "type": self.node_type.value,
            "name": self.name,
            "metadata": self.metadata

        }