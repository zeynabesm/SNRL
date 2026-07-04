from schema.er_builder import ERBuilder

builder = ERBuilder("Data")

builder.load_tables()

builder.detect_entities()

builder.print_entities()