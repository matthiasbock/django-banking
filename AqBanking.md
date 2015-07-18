# AqBanking #

Online Banking tool, written by Martin Preuß.

  * http://www.aquamaniac.de/sites/aqbanking/index.php
  * http://linuxwiki.de/AqBanking
  * http://linuxwiki.de/AqBanking?action=AttachFile&do=view&target=aqbanking-tool-README.txt
  * http://linuxwiki.de/OpenHBCI/GetesteteBanken/DKB

# Example usage #

```
 $ aqhbci-tool4 mkpinlist -o PINFILE
 $ aqbanking-cli -P PINFILE -n request --account=123456789 --transactions
```

# aqhbci-tool4 HOWTO #

  * http://linuxwiki.de/AqBanking/aqhbci-tool

# aqbanking-tool-README.txt #

... from the source tarball

```
This folder contains a tool for basic operations on AqBanking.

Usage:
aqbanking-tool [GLOBAL-OPTIONS] COMMAND [COMMAND-SPECIFIC-OPTIONS]

Every command may have local command line options which must follow the
command. These local arguments are described with the individual commands
below.


Return Values
=============
 0: ok
 1: parameter error (missing/bad/invalid arguments)
 2: setup error (AB_Banking_Init)
 3: error executing the command
 4: error *after* executing the command
 5: deinit error (AB_Banking_Fini)
99: job has been executed but is still pending (mostly used with transfer
    requests which are delayed by the bank)



Global Options
==============

This tool has global options and command-specific options.

Globals options are those before the COMMAND, command-specific options
follow the COMMAND.

[-C           ARG]     AqBanking configuration file
[-P           ARG]     PINFILE to be used for automatic PIN lookup
                       For HBCI pins you can use the tool "aqhbci-tool" to 
                       create an empty pin file:
                       "aqhbci-tool mkpinlist -o PINFILE"
                       After that just edit the newly created file with your
                       favorite editor and insert the pins you want to use
                       automatically.
[-n              ]     Work in non-interactive mode
[--charset   =ARG]     Select the character set for console output (defaults
                       to "ISO-8859-15")
[--logtype   =ARG]     type of logging (console, file)
[--loglevel  =ARG]     log level (info, notice, warning, error)
[--logfile   =ARG]     log file (if log type is "file")


The following is a list of commands which are implemented so far.


"listaccs"
==========

This command prints a TAB separated list of currently available accounts
to stdout.


Options
-------
--bank       =ARG      Bank code ("Bankleitzahl")
--account    =ARG      Account number
--bankname   =ARG      Bank name
--accountname=ARG      Account name
Wildcards ("*") and jokers ("?") are allowed. Every missing option of those
above automatically matches any account.


Examples
--------
aqbanking-tool listaccs
aqbanking-tool listaccs --bank=28250110
aqbanking-tool listaccs --bankname="*Sparkasse*"
aqbanking-tool listaccs --account=123456



"request"
=========

This command enqueues a request for specified accounts. To actually perform
the request (i.e. send it to the bank) you will have to use the command
"exec" after "request".


Options
-------
[--bank       =ARG]      Bank code ("Bankleitzahl")
[--account    =ARG]      Account number
[--bankname   =ARG]      Bank name
[--accountname=ARG]      Account name
Wildcards ("*") and jokers ("?") are allowed. Every missing option of those
above automatically matches any account.

At least one of the following options must be specified:
[--transactions   ]      Add a request for transactions
[--balance        ]      Add a request for account balance
[--sto            ]      Add a request for standing orders

For transaction requests these options are supported in addition:
[--fromdate   =ARG]      Specify the first date for which transactions are to
                         requested
[--todate     =ARG]      Specify the last date for which transactions are to
                         requested


Examples
--------
aqbanking-tool request --balance
aqbanking-tool request --transactions
aqbanking-tool request --transactions --fromdate=20050501
aqbanking-tool request --transactions --fromdate=20050501 --todate=20050513
aqbanking-tool request --transactions --balance
aqbanking-tool request --transactions --balance --sto



"exec"
======

This command executes previously enqueued requests.
The results are either printed to stdout or written to a file.


Options
-------
[--ctxfile    =ARG]      Specify the file to which the results are to be
                         stored. This file is needed for some other commands
                         so it is best to specify it. Defaults to stdout.


Examples
--------
aqbanking-tool exec --ctxfile=result.ctx



"listtrans"
===========

This command inspects the result file from the command "exec" and dumps 
transaction statements from this file to stdout or a file.


Options
-------
[--bank        =ARG]     Bank code ("Bankleitzahl")
[--account     =ARG]     Account number
[--bankname    =ARG]     Bank name
[--accountname =ARG]     Account name
Wildcards ("*") and jokers ("?") are allowed. Every missing option of those
above automatically matches any account.

[--ctxfile     =ARG]     The result file to be used (defaults to stdin)
[--outfile     =ARG]     Name of the output file to which the transactions
                         are to be stored. Defaults to stdout.
[--exporter    =ARG]     Name of the export plugin to be used for storage.
                         This defaults to "csv".
[--profile     =ARG]     Name of the profile of the exporter plugin to be
                         used. Defaults to "default" (for every exporter
                         plugin a "default" profile is provided by AqBanking).

Normally the system-wide profiles (and local AqBanking profiles of the user)
are used when searching for a profile. However, with the following option
you can use your own profiles database.
[--profile-file=ARG]     Optional profile database file (a GWEN_DB)


Examples
--------
aqbanking-tool listtrans --ctxfile=result.ctx --outfile=result.csv
aqbanking-tool listtrans --bankname="*Sparkasse*" --ctxfile=result.ctx
                         --outfile=result.csv
aqbanking-tool listtrans --ctxfile=result.ctx --outfile=result.csv
                         --profile=MyOwnProfile



"listbal"
===========

This command inspects the result file from the command "exec" and dumps 
account balances from this file to stdout or a file (format: CSV).


Options
-------
[--bank        =ARG]     Bank code ("Bankleitzahl")
[--account     =ARG]     Account number
[--bankname    =ARG]     Bank name
[--accountname =ARG]     Account name
Wildcards ("*") and jokers ("?") are allowed. Every missing option of those
above automatically matches any account.

[--ctxfile     =ARG]     The result file to be used (defaults to stdin)
[--outfile     =ARG]     Name of the output file to which the transactions
                         are to be stored. Defaults to stdout.


Output Format
-------------
The statements are written in TAB-delimited CSV lines. Each line contains
the following data:

Column! Data                                     ! Example Data
------!------------------------------------------!---------------------
 1    ! "Account" (fixed)                        ! Account
 2    ! Bank code (Bankleitzahl)                 ! 20050550
 3    ! Account number                           ! 1234567890
 4    ! Bank name (if known, empty otherwise)    ! Hamburger Sparkasse
 5    ! Account name (empty if unknown)          ! Giro
      !                                          !
 6-9  ! Booked balance                           !
 6    ! Date of balance (DD.MM.YYYY or empty)    ! 19.05.2005
 7    ! Time of balance (hh:mm or empty)         ! 16:53
 8    ! Balance (10 digits, precision 2)         ! 12345,04
 9    ! Currency (ISO code, empty if unknown)    ! EUR
      !                                          !
10-13 ! Noted balance                            !
10    ! Date of balance (DD.MM.YYYY or empty)    ! 19.05.2005
11    ! Time of balance (hh:mm or empty)         ! 16:53
12    ! Balance (10 digits, precision 2)         ! 12345,04
13    ! Currency (ISO code, empty if unknown)    ! EUR



Examples
--------
aqbanking-tool listbal --ctxfile=result.ctx --outfile=result.csv
aqbanking-tool listbal --bankname="*Sparkasse*" --ctxfile=result.ctx
                       --outfile=result.csv



"transfer"
===========

This command enqueues a transfer request. To actually perform the request
the command "exec" must be used afterwards.


Options
-------
The following options can be used to specify the local account. It must be
specified unambiguously.
[--bank        =ARG]     Bank code ("Bankleitzahl")
[--account     =ARG]     Account number
[--bankname    =ARG]     Bank name
[--accountname =ARG]     Account name
Wildcards ("*") and jokers ("?") are allowed. Every missing option of those
above automatically matches any account.

--rbank        =ARG      Remote bank id
--raccount     =ARG      Remote account id
--value        =ARG      Amount to transfer including currency (1234,56:EUR)
--textkey      =ARG      Text key (defaults to 51 for standard transfers)
--rname        =ARG      Remote name (payee name), can be specified multiple
                         times
--purpose      =ARG      Purpose of the transfer, can be specified multiple
                         times
--force-check            If given then the check for the combination of
                         remote bank code and account number is required to
                         succeed in order to allow the transfer.
                         If omitted the transfer will only be rejected if
                         AqBanking is sure that the combination is invalid.
-x                       Immediately execute the queue after enqueing the
                         transfer


There are special return values when using this command:
0:   everything is ok
1-x: error (see above)
99:  transfer has been executed and accepted by the bank, but the bank did not
     yet decide on whether the transfer is to be performed (job is pending)


Examples
--------
aqbanking-tool transfer --bank=2345678 --account=12345
                        --rbank=12345678 --raccount=67890
                        --rname=Test-User
                        --value="123,45:EUR"
                        --textkey=51
                        --purpose="Small test"
                        --force-check


"debitnote"
===========

This command enqueues a debit note request. To actually perform the request
the command "exec" must be used afterwards.


Options
-------
The following options can be used to specify the local account. It must be
specified unambiguously.
[--bank        =ARG]     Bank code ("Bankleitzahl")
[--account     =ARG]     Account number
[--bankname    =ARG]     Bank name
[--accountname =ARG]     Account name
Wildcards ("*") and jokers ("?") are allowed. Every missing option of those
above automatically matches any account.

--rbank        =ARG      Remote bank id
--raccount     =ARG      Remote account id
--value        =ARG      Amount to draw including currency (1234,56:EUR)
--textkey      =ARG      Text key (defaults to 51 for standard debitnotes)
--rname        =ARG      Remote name (payee name), can be specified multiple
                         times
--purpose      =ARG      Purpose of the debit note, can be specified multiple
                         times
--force-check            If given then the check for the combination of
                         remote bank code and account number is required to
                         succeed in order to allow the debitnote.
                         If omitted the debit note will only be rejected if
                         AqBanking is sure that the combination is invalid.
-x                       Immediately execute the queue after enqueing the
                         transfer


There are special return values when using this command:
0:   everything is ok
1-x: error (see above)
99:  transfer has been executed and accepted by the bank, but the bank did not
     yet decide on whether the transfer is to be performed (job is pending)


Examples
--------
aqbanking-tool debitnote --bank=2345678 --account=12345
                         --rbank=12345678 --raccount=67890
                         --rname=Test-User
                         --value="123,45:EUR"
                         --textkey=5
                         --purpose="Small test"
                         --force-check


"import"
========

This command imports a given file (or from stdin) using a given importer and
writes the imported data to a new context-file which can be used for the
commands "listtrans" etc.


Options
-------
[--ctxfile     =ARG]     The result file to be used (defaults to stdout)
[--infile      =ARG]     Name of the input file from which the transactions
                         are to be read. Defaults to stdin.
[--importer    =ARG]     Name of the import plugin to be used for storage.
                         This defaults to "csv".
[--profile     =ARG]     Name of the profile of the importer plugin to be
                         used. Defaults to "default" (for every importer
                         plugin a "default" profile is provided by AqBanking).

Normally the system-wide profiles (and local AqBanking profiles of the user)
are used when searching for a profile. However, with the following option
you can use your own profiles database.
[--profile-file=ARG]     Optional profile database file (a GWEN_DB)


Examples
--------
aqbanking-tool import --ctxfile=out.ctx --infile=testfile 
                      --importer=swift --profile=SWIFT-MT940
aqbanking-tool import --ctxfile=out.ctx --infile=testfile 
                      --importer=csv --profile=MyProfile
                      --profile-file=myProfileFile
```