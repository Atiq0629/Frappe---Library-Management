# Copyright (c) 2023, Atiq Rahman and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Person(Document):
    
    def validate(self):
        self.get_name()
        
    def get_full_name(self):
        """Returns the full name of the person"""
        return f"{self.first_name} {self.last_name}"
    
    def get_name(self):
        doc = frappe.get_doc("Person", "Alex")
        frappe.msgprint(doc.get_full_name())
 
    
    
 
 
