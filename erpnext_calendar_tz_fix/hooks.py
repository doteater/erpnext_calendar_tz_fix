app_name = "erpnext_calendar_tz_fix"
app_title = "ERPNext Calendar tz fix"
app_publisher = "doeater"
app_description = "Fixes calendar timezone bug"
app_email = "doteater@github"
app_license = "mit"
required_apps = ["frappe"]

# Override the whitelisted method
override_whitelisted_methods = {
    "frappe.desk.doctype.event.event.get_events": "calendar_fix.overrides.get_events.get_events"
}
