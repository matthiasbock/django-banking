# -*- coding: iso-8859-15 -*-

# http://www.bundesbank.de/zahlungsverkehr/zahlungsverkehr_bankleitzahlen_listeblz.php?mode=blz&start=0&op=or&count=1000

import httplib

def UpgradeBankenliste( request ):
	# http://www.bundesbank.de/zahlungsverkehr/zahlungsverkehr_bankleitzahlen_suche.php?mode=search&blz=10050000&op=or&count=10

	...
	
	key = '">'+str(BLZ)+'</a></td><td>'
	p = page.find(key)
	q = page.find("<td>", p)+4
	r = page.find("</td>", q)
	return page[q:r]
