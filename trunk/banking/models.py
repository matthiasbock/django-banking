# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Bankkonten(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=180, db_column='Name') # Field name made lowercase.
    zusatz = models.CharField(max_length=180, db_column='Zusatz', blank=True) # Field name made lowercase.
    kontonummer = models.BigIntegerField(db_column='Kontonummer') # Field name made lowercase.
    iban = models.CharField(max_length=102, db_column='IBAN', blank=True) # Field name made lowercase.
    bankname = models.CharField(max_length=300, db_column='Bankname', blank=True) # Field name made lowercase.
    blz = models.IntegerField(db_column='BLZ') # Field name made lowercase.
    bic = models.CharField(max_length=99, db_column='BIC', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Bankkonten'

class Buchungen(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    kontoauszug = models.IntegerField(null=True, db_column='Kontoauszug', blank=True) # Field name made lowercase.
    bankkonto = models.IntegerField(db_column='Bankkonto') # Field name made lowercase.
    gegenseite = models.IntegerField(db_column='Gegenseite') # Field name made lowercase.
    datum = models.DateField(db_column='Datum') # Field name made lowercase.
    valuta = models.DateField(db_column='Valuta') # Field name made lowercase.
    betrag = models.DecimalField(decimal_places=2, max_digits=12, db_column='Betrag') # Field name made lowercase.
    zahlungsweise = models.IntegerField(null=True, db_column='Zahlungsweise', blank=True) # Field name made lowercase.
    primanota = models.IntegerField(db_column='Primanota') # Field name made lowercase.
    verwendungszweck = models.CharField(max_length=960, db_column='Verwendungszweck') # Field name made lowercase.
    geprueft = models.CharField(max_length=12, db_column='Geprueft', blank=True) # Field name made lowercase.
    gerechtfertigt = models.CharField(max_length=12, db_column='Gerechtfertigt', blank=True) # Field name made lowercase.
    kommentar = models.CharField(max_length=960, db_column='Kommentar', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Buchungen'

class Kontoauszuege(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    bankkonto = models.IntegerField(db_column='Bankkonto') # Field name made lowercase.
    jahr = models.IntegerField(db_column='Jahr') # Field name made lowercase.
    laufendenummer = models.IntegerField(db_column='LaufendeNummer') # Field name made lowercase.
    abrufdatum = models.DateField(db_column='Abrufdatum') # Field name made lowercase.
    url = models.CharField(max_length=300, db_column='URL') # Field name made lowercase.
    class Meta:
        db_table = u'Kontoauszuege'

class Quittungen(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    aussteller = models.IntegerField(db_column='Aussteller') # Field name made lowercase.
    datum = models.DateTimeField(db_column='Datum') # Field name made lowercase.
    konto = models.IntegerField(db_column='Konto') # Field name made lowercase.
    betrag = models.DecimalField(decimal_places=2, max_digits=11, db_column='Betrag') # Field name made lowercase.
    zahlungsweise = models.IntegerField(db_column='Zahlungsweise') # Field name made lowercase.
    kategorie = models.IntegerField(db_column='Kategorie') # Field name made lowercase.
    kommentar = models.CharField(max_length=960, db_column='Kommentar') # Field name made lowercase.
    buchung = models.IntegerField(null=True, db_column='Buchung', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Quittungen'

class Quittungsaussteller(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=90, db_column='Name') # Field name made lowercase.
    zusatz = models.CharField(max_length=90, db_column='Zusatz') # Field name made lowercase.
    buchungszusatz = models.CharField(max_length=90, db_column='Buchungszusatz') # Field name made lowercase.
    strasse = models.CharField(max_length=150, db_column='Strasse') # Field name made lowercase.
    hausnummer = models.IntegerField(db_column='Hausnummer') # Field name made lowercase.
    plz = models.IntegerField(db_column='PLZ') # Field name made lowercase.
    stadt = models.CharField(max_length=90, db_column='Stadt') # Field name made lowercase.
    class Meta:
        db_table = u'Quittungsaussteller'

class Quittungskategorien(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=180, db_column='Name') # Field name made lowercase.
    class Meta:
        db_table = u'Quittungskategorien'

class Zahlungsweisen(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    name = models.CharField(max_length=60, db_column='Name') # Field name made lowercase.
    class Meta:
        db_table = u'Zahlungsweisen'

