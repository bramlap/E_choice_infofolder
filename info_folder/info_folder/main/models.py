from django.db import models
import time, datetime

# Create your models here.
class ModulesInfo(models.Model):
        AREAS = (
                ('studie', 'studie'),
                ('sociaal', 'sociaal'),
                ('toekomst', 'toekomst'),
                ('studiesociaal', 'studiesociaal'),
                ('studietoekomst', 'studietoekomst'),
                ('sociaaltoekomst', 'sociaaltoekomst')
        )

        TYPES_MODULES = (
                ('Beschikbaar', 'Beschikbaar'),
                ('Niet Beschikbaar', 'Niet Beschikbaar')
        )

        TYPES_MODULES = (
                ('Actief', 'Actief'),
                ('Pasief', 'Pasief')
        )

        opleiding = models.CharField(max_length=35, default='Opleiding')

        gebied = models.CharField(max_length=50, choices=AREAS, default='studie')
        naam = models.CharField(max_length=50, default="NAAM")
        id_module = models.CharField(max_length=15, default='' )
        omschrijving = models.TextField(default="OMSCHRIJVING")

        tijd =  models.IntegerField('Tijdsduur', default=0)
        kosten = models.IntegerField('Kosten', default=0)
        baten_vast = models.IntegerField('Vaste baten', default=0)
        baten_flex = models.IntegerField('Flexibele baten', default=0)
        experience_vast = models.IntegerField('Vaste exp', default=0)
        experience_flex = models.IntegerField('Flexibele exp', default=0)
        factor = models.PositiveIntegerField('Factor module', default=0)
        niveau = models.IntegerField('Niveau van course', default=1)
        status = models.CharField(max_length=30, default='Beschikbaar')
        module_type = models.CharField(max_length=15, default='Passief')
        
        exp_required = models.IntegerField('Experience benodigd', default=0)

        #dates
        date1 = models.DateTimeField(default=datetime.datetime(2016,7,1))
        date2 = models.DateTimeField(default=datetime.datetime(2016,2,1))
        date3 = models.DateTimeField(default=datetime.datetime(2016,4,1))

        def __str__(self):
                return str(self.opleiding)+'_'+self.naam