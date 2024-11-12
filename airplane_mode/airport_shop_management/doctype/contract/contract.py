# Copyright (c) 2024, Vikash Kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import getdate
from frappe import _
from datetime import timedelta


class Contract(Document):
	def validate(self):
		if self.contract_start and self.contract_end:
			contract_start_date = getdate(self.contract_start)
			contract_end_date = getdate(self.contract_end)

			if contract_end_date < contract_start_date + timedelta(days=365):
				frappe.throw(
					_("Contract End Date must be at least one year after the Contract Start date."),
					title = _("Invalid Contract Dates")
				)
				
		#Validate Shop Status
		if self.shop:
			shop_doc = frappe.get_doc("Shop", self.shop)
			if shop_doc.status == "Leased":
				frappe.throw(
					_("Shop {0} is already leased and cannot be contracted.").format(shop_doc.shop_name),
					title = _("Shop Leased")
				)


		def after_start(self):
			if self.shop:
				shop_doc = frappe.get_doc("Shop", self.shop)
				shop_doc.status = "Leased"
				shop_doc.tenant_details = self.tenant
				shop_doc.contract_expiry = self.contract_end

				shop_doc.save(ignore_permissions = True)

				frappe.msgprint(_("Shop {0} has been marked as Leased.").format(shop.shop_name),alert = True)
