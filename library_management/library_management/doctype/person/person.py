# Copyright (c) 2023, Frappe and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Person(Document):
	# def validate(self):
	# 	if self.age < 18:
	# 		frappe.throw("Person's age must be at least 18")
		
	# 	def after_insert(self):
	# 		frappe.sendmail(recipients=[self.email], message="Thank you for registering")

	def validate(self):
		# self.create_document()
		# self.load_document()
		# self.last_doc()
		self.create_new_doc()



	# Create a document 
	def create_document(self):	
		doc = frappe.get_doc({
			'doctype': 'Library Member',
			'first_name': 'John',
			'email_id':  'johnwick@gmail.com'
		})
		doc.insert()
	
	# Load a document
	def load_document(self):
		doc = frappe.get_doc('Library Member', 'MEM00001')
		frappe.msgprint(doc.owner)
		
	# frappe.get_last_doc
	#Returns the last Document object created under the mentioned doctype.
	# get the last Task created
	def last_doc(self):
		doc = frappe.get_last_doc('Articles', order_by="creation asc")
		frappe.msgprint(doc.name)

	# frappe.new_doc
	# Alternative way to create a new Document.
	def create_new_doc(self):
		doc = frappe.new_doc('Articles')
		doc.article_name = 'Harry Potter Series'
		doc.author = 'J.K. Rowling'
		doc.status = 'Available'
		doc.insert()


