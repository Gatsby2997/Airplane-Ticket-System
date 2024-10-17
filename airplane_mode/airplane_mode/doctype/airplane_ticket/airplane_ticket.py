# Copyright (c) 2024, Vikash Kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import random
import string

class AirplaneTicket(Document):
	def validate(self):
		add_on_types = set()
		unique_add_ons = []

        # Loop through the add-ons in the child table
		for add_on in self.add_ons:
            # If the add-on type is not in the set, add it
			if add_on.add_on_type not in add_on_types:
				add_on_types.add(add_on.add_on_type)
				unique_add_ons.append(add_on)
			else:
				frappe.msgprint(("Duplicate add-on '{0}' removed.").format(add_on.add_on_type))

        # Update the add_ons table with only unique entries
		self.add_ons = unique_add_ons
	
	def before_submit(self):
		if self.status != "Boarded":
			frappe.throw(f'Dear {self.passenger}! you are not boarded yet',frappe.ValidationError)

	
	# This is code for price calculation
	def validate(self):
		t=0
		for i in self.add_ons:
			t += i.amount
		
		self.total_price = self.flight_price + t


	#Code for random Seat Number
	def before_save(self):
		random_number = random.randint(1,60)
		rand_letter = random.choice(string.ascii_uppercase[:5])
		self.seat = f"{random_number}{rand_letter}"


