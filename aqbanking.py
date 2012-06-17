# -*- coding: iso-8859-15 -*-

from subprocess import Popen, PIPE
from shlex import split

from DKB_parser import DKB_response

command = "aqbanking-cli -P input -n request --account=... --transactions"
print command
print DKB_response( Popen(split(command), stdout=PIPE).communicate()[0] )

