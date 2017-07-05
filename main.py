#!/usr/bin/python3
# -*- coding: utf-8 -*-
import datetime
import re
from nltk import ngrams
from nltk.tokenize import wordpunct_tokenize

days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "weekend"]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
words = {"today": 0, "tomorrow": 1, "yesterday": -1, "day before yesterday": -2, "day after tomorrow": 2}
prefix = {"this": 0, "coming": 0, "last": 1, "previous": 1, "next": 2}
words_s = ["today", "tomorrow", "yesterday", "day before yesterday", "day after tomorrow"]
prefix_s = ["this", "coming", "last", "previous", "next"]


class CustomDate:
	""" Custom Date class which converts a valid user input
		to DD-MM-YYYY format date.
	"""

	def __init__(self, user_input):
		self.user_input = user_input.lower().replace("weekend", "saturday")
		self.output_date = datetime.datetime.today()
		self.date = -1
		self.month = -1
		self.year = datetime.datetime.now().year
		self.errors = ""
		if not any(char.isdigit() for char in self.user_input):
			self.getDate()
		else:
			self.convert()
		self.output_date = self.output_date.strftime('%d-%m-%Y')
		# print(self.user_input, self.output_date, self.errors)

	def convert(self):
		""" Converts a given date to DD-MM-YYYY format
		"""
		date_list = re.split(r'[-. ,/|\'\\]+', self.user_input)
		date_list = [x for x in date_list if x]
		didx, midx = 0, 1
		if not date_list[0][0].isnumeric():
			didx, midx = 1, 0
		self.date = int(re.sub('[^0-9]', '', date_list[didx]))
		if len(date_list) > 1:
			if date_list[midx].isnumeric():
				self.month = int(date_list[midx])
			else:
				for it in range(len(months)):
					if months[it].lower().startswith(date_list[midx].lstrip("0").lower()):
						self.month = it + 1
						break
			try:
				self.year = int(date_list[2])
			except Exception:
				self.year = datetime.datetime.now().year
		else:
			self.month = datetime.datetime.now().month
		self.output_date = datetime.date(self.year, self.month, self.date)

	# Method for getting date from keyword here


	# Method for getting date of next and previous weekday here



if __name__ == '__main__':
	user_input = input("Enter Input: ")
	user_input.replace(',', " ")
	user_input = user_input.split()
	user_input = [word for word in user_input if word != "of"]
	# Write Code for Processing user input

