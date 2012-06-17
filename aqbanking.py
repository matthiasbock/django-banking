# -*- coding: iso-8859-15 -*-
#!/usr/bin/python

from subprocess import Popen, PIPE
from shlex import split
from parser import HBCI_response

class AqBanking:
	
command = "aqbanking-cli -P input -n request --account=... --transactions"
print command

print HBCI_response( Popen(split(command), stdout=PIPE).communicate()[0] )

