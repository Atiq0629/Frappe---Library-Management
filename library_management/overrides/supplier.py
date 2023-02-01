from __future__ import unicode_literals
import frappe
from erpnext.buying.doctype.supplier.supplier import Supplier


class SupplierController(Supplier):
    def after_insert(self):
        self.save_contact()

    def save_contact(self):
        for row in self.get("contact_and_address"):
            doc = frappe.new_doc('Contact')
            doc.first_name = str(row.first_name)
            doc.append("email_ids",
                       {
                            "email_id": row.email_id,
                            "is_primary": 1
                       }),
            doc.append("phone_nos",
                       {
                            "phone": row.phone,
                            "is_primary_phone": 1
                       }),
            doc.append("links",
                       {
                            "link_doctype": "Supplier",
                            "link_name": self.name,
                       }),
            doc.save()
            
    # def save_address(self):
    #     for row in self.get("contact_and_address"):
    #         doc = frappe.new_doc('Address')
    #         doc.address_line1 = str(row.address)
    #         doc.city = str(row.city)
    #         doc.append("links",
    #                    {
    #                         "link_doctype": "Supplier",
    #                         "link_name": self.name,
    #                    }),
    #         doc.save()

        
    # def validate_contact(self):
    #     for row in self.get("contact_and_address"):
    #         valid_contact = frappe.db.exists(
    #             'Contact',
    #             {
    #                 'first_name': row.first_name
    #             },
    #         )
    #         if valid_contact:
    #             frappe.throw('The contact already exists.')
    