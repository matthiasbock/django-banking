# _synchronize.conf_ #

## Example ##
```
[DKB Demo Account]
url = https://hbci-pintan-by.s-hbci.de/PinTanServlet
certificate = dkb.cert
userid = 12345678901234567
customid = 1234567890
bankcode = 12030000
pin = abcde
```

## Deutsche Kreditbank ##

  * http://linuxwiki.de/OpenHBCI/GetesteteBanken/DKB
  * http://www.dkb.de/kundenservice/haeufige_fragen/internetbanking/

The DKB certificate is included in this repository. For security reasons you should ensure, that you downloaded a valid copy of the cert and also that the cert provided by the server, you interact with, matches.

The _user-id_ may be found in the DKB online banking below _Verwaltung & Sicherheit / Benutzerinfo / Legitimations-ID_:

![http://django-banking.googlecode.com/svn/trunk/doc/Legitimations-ID.jpg](http://django-banking.googlecode.com/svn/trunk/doc/Legitimations-ID.jpg)


The _custom-id_ is your bank account number.