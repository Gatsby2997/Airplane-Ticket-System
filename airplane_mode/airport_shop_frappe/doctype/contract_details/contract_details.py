# Copyright (c) 2024, Vikash Kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import getdate
from frappe import _
from datetime import timedelta



class ContractDetails(Document):
	def validate(self):
		if self.contract_start and self.contract_end:
			contract_start_date = getdate(self.contract_start)
			contract_end_date = getdate(self.contract_end)

			if contract_end_date < contract_start_date + timedelta(days=365):
				frappe.throw(
					_("Contract End Date must be at least one year after the Contract Start date."),
					title = _("Invalid Contract Dates")
				)
