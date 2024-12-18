# Copyright (c) 2024, Vikash Kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.document import Document


class AirplaneFlight(WebsiteGenerator):
    # def set_status_to_completed(doc, method):
    # # Set the Status field to 'Completed' after the document is submitted
    # 	doc.status = "Completed"
    def on_submit(self):
        # Set status to 'Completed' after submission
        self.status = "Completed"


