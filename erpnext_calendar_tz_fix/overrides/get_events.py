import frappe
from datetime import datetime, date
from typing import Union


def parse_date_string(date_str):
    """Parse date string handling timezone offsets"""
    if isinstance(date_str, (date, datetime)):
        return date_str if isinstance(date_str, date) else date_str.date()
    
    if not isinstance(date_str, str):
        return date_str
    
    # Handle datetime strings with time component
    if ' ' in date_str:
        date_str = date_str.split()[0]
    
    # Parse ISO format date
    try:
        return datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        return date_str


@frappe.whitelist()
def get_events(
    start: Union[str, date],
    end: Union[str, date],
    user: str = None,
    for_reminder: bool = False,
    filters=None
):
    """
    Override of frappe.desk.doctype.event.event.get_events
    Converts string dates to date objects before calling original logic
    """
    # Import the original function's logic
    from frappe.desk.doctype.event.event import get_events as original_get_events
    
    # Convert dates
    start = parse_date_string(start)
    end = parse_date_string(end)
    
    # Call original function
    return original_get_events(
        start=start,
        end=end,
        user=user,
        for_reminder=for_reminder,
        filters=filters
    )
