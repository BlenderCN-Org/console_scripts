def execute(captured_locals):
    if "bpy" in captured_locals:
        # Reloaded multifiles
        import importlib

        global context_data
        global console_writer

        importlib.reload(context_data)
        importlib.reload(console_writer)

    else:
        print("imported")
        # Imported multifiles
        from .models import context_data
        from .utils import console_writer

