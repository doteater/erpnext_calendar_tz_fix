__version__ = "0.0.1"

def _apply_patch():
    """Apply the monkey patch when explicitly called, not at import time"""
    try:
        from calendar_fix.patches.calendar_timezone_fix import apply_monkey_patch
        apply_monkey_patch()
    except ImportError:
        import frappe
        # rest of the patch logic

# Don't call _apply_patch() here at module level
# It should be called by frappe's hooks or explicitly when needed
