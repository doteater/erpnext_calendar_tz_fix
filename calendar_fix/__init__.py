# Apply the monkey patch as soon as the module is imported
# This ensures it's active before any requests are processed

def _apply_patch():
    """Apply patch on module import"""
    try:
        from calendar_fix.patches.calendar_timezone_fix import apply_monkey_patch
        apply_monkey_patch()
    except Exception as e:
        # Log but don't break if patching fails
        import frappe
        if frappe.logger:
            frappe.logger().error(f"Failed to apply calendar patch on import: {str(e)}")

_apply_patch()
