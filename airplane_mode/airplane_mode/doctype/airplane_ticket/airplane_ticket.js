// Copyright (c) 2024, Vikash Kumar and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airplane Ticket", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on('Airplane Ticket', {
    refresh: function(frm) {
        // Add a custom button to the form view
        frm.add_custom_button(__('Assign Seat'), function() {
            // Create a new dialog with an input field
            let d = new frappe.ui.Dialog({
                title: __('Select seat'),
                fields: [
                    {
                        label: __('Seat Number'),
                        fieldname: 'seat_number',
                        fieldtype: 'Data',
                        reqd: 1
                    }
                ],
                primary_action_label: __('assign'),
                primary_action(values) {
                    // Set the seat number in the form field
                    frm.set_value('seat', values.seat_number);
                    d.hide();
                }
            });
            // Show the dialog
            d.show();
        }, __('Actions'));
    }
});

