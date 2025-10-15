app_name = "calendar_fix"
app_title = "Calendar Fix"
app_publisher = "Your Name"
app_description = "Fixes calendar timezone bug"
app_email = "your@email.com"
app_license = "mit"
required_apps = ["frappe"]

# Override the whitelisted method
override_whitelisted_methods = {
    "frappe.desk.doctype.event.event.get_events": "calendar_fix.overrides.get_events.get_events"
}
