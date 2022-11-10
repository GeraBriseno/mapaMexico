from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils.translation import gettext as _
#from pyrsistent import v

class Poblacion(models.Model):

    estado = models.CharField(_("estado"), max_length=50)
    a2020 = models.IntegerField(_("2020"))
    a2010 = models.IntegerField(_("2010"))
    a2000 = models.IntegerField(_("2000"))
    a1990 = models.IntegerField(_("1990"))
    a1980 = models.IntegerField(_("1980"))
    a1970 = models.IntegerField(_("1970"))
    a1960 = models.IntegerField(_("1960"))
    a1950 = models.IntegerField(_("1950"))
    a1940 = models.IntegerField(_("1940"))
    a1930 = models.IntegerField(_("1930"))
    a1920 = models.IntegerField(_("1920"))
    a1910 = models.IntegerField(_("1910"))

    def __str__(self):
        return f"{self.estado}"

class PIB(models.Model):

    estado = models.CharField(_("estado"), max_length=50)
    a2003 = models.FloatField(_("2003"))
    a2004 = models.FloatField(_("2004"))
    a2005 = models.FloatField(_("2005"))
    a2006 = models.FloatField(_("2006"))
    a2007 = models.FloatField(_("2007"))
    a2008 = models.FloatField(_("2008"))
    a2009 = models.FloatField(_("2009"))
    a2010 = models.FloatField(_("2010"))
    a2011 = models.FloatField(_("2011"))
    a2012 = models.FloatField(_("2012"))
    a2013 = models.FloatField(_("2013"))
    a2014 = models.FloatField(_("2014"))
    a2015 = models.FloatField(_("2015"))
    a2016 = models.FloatField(_("2016"))
    a2017 = models.FloatField(_("2017"))
    a2018 = models.FloatField(_("2018"))
    a2019 = models.FloatField(_("2019"))
    a2020 = models.FloatField(_("2020"))

    def __str__(self):
        return f"{self.estado}"

class Densidad(models.Model):
    estado = models.CharField(_("estado"), max_length=50)
    a1990 = models.FloatField(_("1990"))
    a1995 = models.FloatField(_("1995"))
    a2000 = models.FloatField(_("2000"))
    a2005 = models.FloatField(_("2005"))
    a2010 = models.FloatField(_("2010"))
    a2015 = models.FloatField(_("2015"))
    a2020 = models.FloatField(_("2020"))

    def __str__(self):
        return f"{self.estado}"
