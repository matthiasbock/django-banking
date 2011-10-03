# -*- coding: iso-8859-15 -*-

from accountInfoList import accountInfoList

class DKB_response:
	def __init__(self, filename):
		self.accountInfoList = accountInfoList( open(filename).read() )

