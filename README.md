This addon is a sample of API exposure to other addons.  
## Usage example

The [header_buttons addon](https://github.com/Walid-Shouman/header_buttons) is an example usage of this (console_scripts) addon.  

I'm not sure though, whether it's a better practice, to include the scripts everytime in the new module or modularize functionalities into addons.  
If the addon is to be split we have one of 2 options through which we create an API to be used by the other modules:

### First Usage Example
By using methods and classes that are available directly in the addon.  
This method is more python oriented, ie, we don't rely on Blender as a way of exposing the API; even though we always need to import the console_scripts addon before using it in Blender.  

```python
try:
    from console_scripts.utils import console_writer
    console_script_is_installed=True
except ImportError:
    console_script_is_installed=False

def custom_print(str):
    if console_script_is_installed==True:
        console_writer.console_write(str)
    else:
        print(str)

def myOperator(bpy.types.Operator):
    bl_idname = "wm.demo"
    bl_label = "Demo"

    custom_print("my message")
```

**Pros**:  
- API exposure could be anything, classes, methods etc.
- No Operator wrapping headache.

**Cons**:  
- Prior knowledge about the addon internal structure is necessary, notice the ```console_scripts.utils import console_writer``` and ```console_writer.console_write(str)```.
- Not how Blender addon system is designed which results in: 
1. Loading the script doesn't take effect directly (after adding the addon we need to restart Blender).
2. Unloading the script doesn't take effect directly (after removing the addon we need to restart Blender).
3. Registering/unregistering the addon doesn't make any difference.

**Recommendation**:  
Heavy structural functionalities, where multiple classes and complex functionalities exist/could exist.  

### Second Usage (Blender way)
Creating an API that comply with Blender's exposable items.  

```python
def myOperator(bpy.types.Operator):
    bl_idname = "wm.demo"
    bl_label = "Demo"

    bpy.ops.console.console_write_operator(myString="my message")
```

**Pros**:  
- No Prior knowledge about the addon is necessary, only the operator name and arguments.
- Integrates well with Blender addon system, through registration/unregistration.

**Cons**:  
- Any method that should be used must have an operator wrapper, arguments should comply with Blender attributes.
- Limited API exposure: Only Blender operators could be exposed, and argument types are the supported Blender attributes.

**Recommendation**:  
Basic functionalities that could be defined a limited number of operators, with Blender complying attributes.

