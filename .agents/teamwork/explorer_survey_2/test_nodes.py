import bpy

# Inspect all node types available in bpy.types that inherit from Node
comp_nodes = [cls.__name__ for cls in bpy.types.Node.__subclasses__() if 'comp' in cls.__name__.lower()]
print("Comp node subclasses count:", len(comp_nodes))
print("Sample comp nodes:", comp_nodes[:30])

# Also check how scene compositing is structured
for t in dir(bpy.types):
    if 'compositor' in t.lower() or 'glare' in t.lower():
        print("Type match:", t)
