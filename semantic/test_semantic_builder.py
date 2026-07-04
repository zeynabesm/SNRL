from schema.er_builder import ERBuilder
from semantic.semantic_builder import SemanticBuilder


builder = ERBuilder()

builder.load_tables()

builder.detect_entities()

builder.detect_relationships()


semantic = SemanticBuilder(builder.graph)

semantic.build()

semantic.print_objects()