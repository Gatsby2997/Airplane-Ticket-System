# Copyright (c) 2024, Vikash Kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.website.website_generator import WebsiteGenerator



class ShopDetails(Document):
	def before_save(self):
		self.shop_code = frappe.generate_hash(self.name, 8)

		y = frappe.get_doc("Monthly Rent")
		self.monthly_rent = y.amount

class ShopDetails(WebsiteGenerator):
	pass