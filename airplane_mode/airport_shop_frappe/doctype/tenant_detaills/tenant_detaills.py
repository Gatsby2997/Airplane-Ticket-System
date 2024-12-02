# Copyright (c) 2024, Vikash Kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import getdate
from datetime import timedelta
from datetime import datetime
from frappe import _

from frappe.model.document import Document


class TenantDetaills(Document):
	def validate(self):
		if self.govt_id == "Pan card":
			if (self.id_number).isalnum() and len(self.id_number) == 10:
				frappe.msgprint( _("Tenant's Details submitted"), title = _("Valid Pan id Details"))
			else:
				frappe.throw( _("Please check details of pan card"), title = _("Invalid Pan id Details"))
		elif self.govt_id == "Aadhaar card":
			if (self.id_number).isdigit() == True and len(self.id_number) == 12:
				frappe.msgprint( _("Tenant's Details submitted"), title = _("Valid Aadhaar id Details"))
			else:
				frappe.throw( _("Please check details of aadhaar card"), title = _("Invalid Aadhaar id Details"))

		# cur_date = datetime.today().date()
		# dob_date = datetime.strptime(self.dob, "%Y-%m-%d").date()
		# age = cur_date - dob_date.year
		# if (cur_date.month, cur_date.day) < (dob_date.month, dob_date.day):
		# 	age -= 1

		# if age < 18:
		# 	frappe.throw( _("Age must be 18 or older"), title = _("Inavlid Age"))	
		


