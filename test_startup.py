import sys
import os
sys.path.append(os.path.join(os.getcwd(), 'backend'))

try:
    from main import app
    print("SUCCESS: App imported and initialized successfully.")
except Exception as e:
    import traceback
    print("FAILED: App failed to initialize.")
    traceback.print_exc()
    sys.exit(1)
