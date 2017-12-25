import bpy

# Pass the registration if the script doesn't have any blender classes
# ie: doesn't define operators/panels etc.

def register(name=""):
    #pass
    bpy.utils.register_module(name)
 
def unregister(name=""):
    #pass
    bpy.utils.unregister_module(name)

