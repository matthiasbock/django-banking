# -*- coding: iso-8859-15 -*-
#!/usr/bin/python

from subprocess import Popen, PIPE
from shlex import split

import aqhbci_tool4
from parser import HBCI_response

class AqBanking:
	def __init__(self, url, cert, customerid, accountnumber, bankcode, pin)
		self.url = url
		self.cert = cert
		self.userid = userid
		self.accountnumber = accountnumber
		self.bankcode = bankcode
		self.pin = pin

		installed = aqhbci_tool4.listmedia
		if (not userid in installed.keys()) or (not accountnumber in installed[userid]):
			m_id = aqhbci_tool.addmedium('pintan')
			aqhbci_tool.adduser(m_id, url, cert, bankcode, customerid, accountnumber)

	def listaccs(self):
		return []

	def request_transactions(self):
		command = '/usr/bin/aqbanking-cli -P /dev/stdin -n request --transactions --account='+self.accountnumber+' --bank='+self.bankcode+'
		print command
		return HBCI_response( Popen(split(command), stdout=PIPE).communicate()[0] )

