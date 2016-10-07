from main.models import ModulesInfo
from datetime import datetime

def run():
    opleidingen = [ 'Wiskunde',
            'Natuurkunde',
            'Sterrenkunde',
            'Scheikunde',
            'Biologie',
            'Life Science and Technology',
            'Farmacie',
            'Informatica',
            'Kunstmatige Intelligentie',
            'Technische Bedrijfskunde',
    ]

    id_modules = [ 'opendag',
            'webklas',
            'dag_student'
            'case',
            'excursie',
            'borrel'
    ]

    #datetime = (year, month, day, hour, min, second)

    #wiskunde
    wiskunde_opendag = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    wiskunde_webklas = [datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    wiskunde_dag_student = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    wiskunde_case = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    wiskunde_excursie = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    wiskunde_borrel = [ datetime(2016, 11, 1, 16), datetime(2017, 2, 1, 16), datetime(2017, 4, 1, 16)]

    #Natuurkunde 
    natuurkunde_opendag = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    natuurkunde_webklas = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    natuurkunde_dag_student = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    natuurkunde_case = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    natuurkunde_excursie = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    natuurkunde_borrel =[ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]

    #scheikunde
    scheikunde_opendag = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    scheikunde_webklas = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    scheikunde_dag_student = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    scheikunde_case = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    scheikunde_excursie = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    scheikunde_borrel = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]

    #sterrenkunde
    sterrenkunde_opendag = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    sterrenkunde_webklas = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    sterrenkunde_dag_student = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    sterrenkunde_case = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    sterrenkunde_excursie = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    sterrenkunde_borrel = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]

    #biologie
    biologie_opendag = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    biologie_webklas = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    biologie_dag_student = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    biologie_case = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    biologie_excursie = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    biologie_borrel = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]

    #lst
    lst_opendag =[ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    lst_webklas = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    lst_dag_student = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    lst_case = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    lst_excursie = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    lst_borrel = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]

    #farmacie
    farmacie_opendag = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    farmacie_webklas =[ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    farmacie_dag_student = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    farmacie_case = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    farmacie_excursie =[ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    farmacie_borrel = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]

    #informatica
    informatica_opendag = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    informatica_webklas = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    informatica_dag_student =[ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    informatica_case = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    informatica_excursie =[ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    informatica_borrel = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]

    #ki
    ki_opendag = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    ki_webklas = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    ki_dag_student =[ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    ki_case = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    ki_excursie = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    ki_borrel = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]

    #tbk
    tbk_opendag = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    tbk_webklas = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    tbk_dag_student = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    tbk_case = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    tbk_excursie = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]
    tbk_borrel = [ datetime(2016, 11, 1), datetime(2017, 2, 1), datetime(2017, 4, 1)]

    for i in opleidingen:
        if i == 'Wiskunde':
            p = ModulesInfo(
                opleiding = 'Wiskunde',
                gebied='studie',
                naam='opendag op locatie',
                id_module = 'opendag',
                omschrijving='Een specifieke opleiding beter leren kennen',
                tijd=8,
                kosten=240,
                experience_vast=192,
                niveau=1,
                date1 = wiskunde_opendag[0],
                date2 = wiskunde_opendag[1],
                date3 = wiskunde_opendag[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Wiskunde',
                gebied='studie',
                naam = 'Webklas',
                id_module = 'webklas',
                omschrijving='Online cursus over bepaalde bachelor opleidingen',
                tijd=16,
                kosten=240,
                baten_vast=240,
                experience_vast=192,
                factor=50,
                module_type = 'Actief',
                niveau=2,
                date1 = wiskunde_webklas[0],
                date2 = wiskunde_webklas[1],
                date3 = wiskunde_webklas[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Wiskunde',
                gebied='studiesociaal',
                naam='Een dag student',
                id_module = 'dag_student',
                omschrijving='Een dagje student zijn',
                tijd=8,
                kosten=120,
                baten_vast=240,
                experience_vast=92,
                niveau=1,
                date1 = wiskunde_dag_student[0],
                date2 = wiskunde_dag_student[1],
                date3 = wiskunde_dag_student[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Wiskunde',
                gebied='toekomst',
                naam = 'Case voor een bedrijf',
                id_module = 'case',
                omschrijving='Een probleem oplossen voor een bedrijf',
                tijd=3,
                kosten=45,
                baten_vast=45,
                experience_vast= 72,
                factor=30,
                module_type = 'Actief',
                niveau=1,
                date1 = wiskunde_case[0],
                date2 = wiskunde_case[1],
                date3 = wiskunde_case[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Wiskunde',
                gebied='sociaaltoekomst',
                naam='Excursie met studievereniging',
                id_module = 'excursie',
                omschrijving='Bij een bedrijf op bezoek',
                tijd=4,
                kosten=120,
                experience_vast=94,
                factor=30,
                module_type = 'Actief',
                niveau=2,
                date1 = wiskunde_excursie[0],
                date2 = wiskunde_excursie[1],
                date3 = wiskunde_excursie[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Wiskunde',
                gebied='sociaal',
                naam='Borrel studievereniging',
                id_module = 'borrel',
                omschrijving='Vrijdag middag borrel met lezing/praatje',
                tijd=2,
                kosten=60,
                experience_vast=48,
                niveau=1,
                date1 = wiskunde_borrel[0],
                date2 = wiskunde_borrel[1],
                date3 = wiskunde_borrel[2],
                )
            p.save()
        if i == 'natuurkunde':
            p = ModulesInfo(
                opleiding = 'Natuurkunde',
                gebied='studie',
                naam='opendag op locatie',
                id_module = 'opendag',
                omschrijving='Een specifieke opleiding beter leren kennen',
                tijd=8,
                kosten=240,
                experience_vast=192,
                niveau=1,
                date1 = natuurkunde_opendag[0],
                date2 = natuurkunde_opendag[1],
                date3 = natuurkunde_opendag[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Natuurkunde',
                gebied='studie',
                naam = 'Webklas',
                id_module = 'webklas',
                omschrijving='Online cursus over bepaalde bachelor opleidingen',
                tijd=16,
                kosten=240,
                baten_vast=240,
                experience_vast=192,
                factor=50,
                module_type = 'Actief',
                niveau=2,
                date1 = natuurkunde_webklas[0],
                date2 = natuurkunde_webklas[1],
                date3 = natuurkunde_webklas[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Natuurkunde',
                gebied='studiesociaal',
                naam='Een dag student',
                id_module = 'dag_student',
                omschrijving='Een dagje student zijn',
                tijd=8,
                kosten=120,
                baten_vast=240,
                experience_vast=92,
                niveau=1,
                date1 = natuurkunde_dag_student[0],
                date2 = natuurkunde_dag_student[1],
                date3 = natuurkunde_dag_student[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Natuurkunde',
                gebied='toekomst',
                naam = 'Case voor een bedrijf',
                id_module = 'case',
                omschrijving='Een probleem oplossen voor een bedrijf',
                tijd=3,
                kosten=45,
                baten_vast=45,
                experience_vast= 72,
                factor=30,
                module_type = 'Actief',
                niveau=1,
                date1 = natuurkunde_case[0],
                date2 = natuurkunde_case[1],
                date3 = natuurkunde_case[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Natuurkunde',
                gebied='sociaaltoekomst',
                naam='Excursie met studievereniging',
                id_module = 'excursie',
                omschrijving='Bij een bedrijf op bezoek',
                tijd=4,
                kosten=120,
                experience_vast=94,
                factor=30,
                module_type = 'Actief',
                niveau=2,
                date1 = natuurkunde_excursie[0],
                date2 = natuurkunde_excursie[1],
                date3 = natuurkunde_excursie[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Natuurkunde',
                gebied='sociaal',
                naam='Borrel studievereniging',
                id_module = 'borrel',
                omschrijving='Vrijdag middag borrel met lezing/praatje',
                tijd=2,
                kosten=60,
                experience_vast=48,
                niveau=1,
                date1 = natuurkunde_borrel[0],
                date2 = natuurkunde_borrel[1],
                date3 = natuurkunde_borrel[2],
                )
            p.save()
        if i == 'scheikunde':
            p = ModulesInfo(
                opleiding = 'scheikunde',
                gebied='studie',
                naam='opendag op locatie',
                id_module = 'opendag',
                omschrijving='Een specifieke opleiding beter leren kennen',
                tijd=8,
                kosten=240,
                experience_vast=192,
                niveau=1,
                date1 = scheikunde_opendag[0],
                date2 = scheikunde_opendag[1],
                date3 = scheikunde_opendag[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'scheikunde',
                gebied='studie',
                naam = 'Webklas',
                id_module = 'webklas',
                omschrijving='Online cursus over bepaalde bachelor opleidingen',
                tijd=16,
                kosten=240,
                baten_vast=240,
                experience_vast=192,
                factor=50,
                module_type = 'Actief',
                niveau=2,
                date1 = scheikunde_webklas[0],
                date2 = scheikunde_webklas[1],
                date3 = scheikunde_webklas[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'scheikunde',
                gebied='studiesociaal',
                naam='Een dag student',
                id_module = 'dag_student',
                omschrijving='Een dagje student zijn',
                tijd=8,
                kosten=120,
                baten_vast=240,
                experience_vast=92,
                niveau=1,
                date1 = scheikunde_dag_student[0],
                date2 = scheikunde_dag_student[1],
                date3 = scheikunde_dag_student[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'scheikunde',
                gebied='toekomst',
                naam = 'Case voor een bedrijf',
                id_module = 'case',
                omschrijving='Een probleem oplossen voor een bedrijf',
                tijd=3,
                kosten=45,
                baten_vast=45,
                experience_vast= 72,
                factor=30,
                module_type = 'Actief',
                niveau=1,
                date1 = scheikunde_case[0],
                date2 = scheikunde_case[1],
                date3 = scheikunde_case[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'scheikunde',
                gebied='sociaaltoekomst',
                naam='Excursie met studievereniging',
                id_module = 'excursie',
                omschrijving='Bij een bedrijf op bezoek',
                tijd=4,
                kosten=120,
                experience_vast=94,
                factor=30,
                module_type = 'Actief',
                niveau=2,
                date1 = scheikunde_excursie[0],
                date2 = scheikunde_excursie[1],
                date3 = scheikunde_excursie[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'scheikunde',
                gebied='sociaal',
                naam='Borrel studievereniging',
                id_module = 'borrel',
                omschrijving='Vrijdag middag borrel met lezing/praatje',
                tijd=2,
                kosten=60,
                experience_vast=48,
                niveau=1,
                date1 = scheikunde_borrel[0],
                date2 = scheikunde_borrel[1],
                date3 = scheikunde_borrel[2],
                )
            p.save()
        if i == 'Sterrenkunde':
            p = ModulesInfo(
                opleiding = 'Sterrenkunde',
                gebied='studie',
                naam='opendag op locatie',
                id_module = 'opendag',
                omschrijving='Een specifieke opleiding beter leren kennen',
                tijd=8,
                kosten=240,
                experience_vast=192,
                niveau=1,
                date1 = sterrenkunde_opendag[0],
                date2 = sterrenkunde_opendag[1],
                date3 = sterrenkunde_opendag[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Sterrenkunde',
                gebied='studie',
                naam = 'Webklas',
                id_module = 'webklas',
                omschrijving='Online cursus over bepaalde bachelor opleidingen',
                tijd=16,
                kosten=240,
                baten_vast=240,
                experience_vast=192,
                factor=50,
                module_type = 'Actief',
                niveau=2,
                date1 = sterrenkunde_webklas[0],
                date2 = sterrenkunde_webklas[1],
                date3 = sterrenkunde_webklas[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Sterrenkunde',
                gebied='studiesociaal',
                naam='Een dag student',
                id_module = 'dag_student',
                omschrijving='Een dagje student zijn',
                tijd=8,
                kosten=120,
                baten_vast=240,
                experience_vast=92,
                niveau=1,
                date1 = sterrenkunde_dag_student[0],
                date2 = sterrenkunde_dag_student[1],
                date3 = sterrenkunde_dag_student[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Sterrenkunde',
                gebied='toekomst',
                naam = 'Case voor een bedrijf',
                id_module = 'case',
                omschrijving='Een probleem oplossen voor een bedrijf',
                tijd=3,
                kosten=45,
                baten_vast=45,
                experience_vast= 72,
                factor=30,
                module_type = 'Actief',
                niveau=1,
                date1 = sterrenkunde_case[0],
                date2 = sterrenkunde_case[1],
                date3 = sterrenkunde_case[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Sterrenkunde',
                gebied='sociaaltoekomst',
                naam='Excursie met studievereniging',
                id_module = 'excursie',
                omschrijving='Bij een bedrijf op bezoek',
                tijd=4,
                kosten=120,
                experience_vast=94,
                factor=30,
                module_type = 'Actief',
                niveau=2,
                date1 = sterrenkunde_excursie[0],
                date2 = sterrenkunde_excursie[1],
                date3 = sterrenkunde_excursie[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Sterrenkunde',
                gebied='sociaal',
                naam='Borrel studievereniging',
                id_module = 'borrel',
                omschrijving='Vrijdag middag borrel met lezing/praatje',
                tijd=2,
                kosten=60,
                experience_vast=48,
                niveau=1,
                date1 = sterrenkunde_borrel[0],
                date2 = sterrenkunde_borrel[1],
                date3 = sterrenkunde_borrel[2],
                )
            p.save()
        if i == 'Biologie':
            p = ModulesInfo(
                opleiding = 'Biologie',
                gebied='studie',
                naam='opendag op locatie',
                id_module = 'opendag',
                omschrijving='Een specifieke opleiding beter leren kennen',
                tijd=8,
                kosten=240,
                experience_vast=192,
                niveau=1,
                date1 = biologie_opendag[0],
                date2 = biologie_opendag[1],
                date3 = biologie_opendag[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Biologie',
                gebied='studie',
                naam = 'Webklas',
                id_module = 'webklas',
                omschrijving='Online cursus over bepaalde bachelor opleidingen',
                tijd=16,
                kosten=240,
                baten_vast=240,
                experience_vast=192,
                factor=50,
                module_type = 'Actief',
                niveau=2,
                date1 = biologie_webklas[0],
                date2 = biologie_webklas[1],
                date3 = biologie_webklas[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Biologie',
                gebied='studiesociaal',
                naam='Een dag student',
                id_module = 'dag_student',
                omschrijving='Een dagje student zijn',
                tijd=8,
                kosten=120,
                baten_vast=240,
                experience_vast=92,
                niveau=1,
                date1 = biologie_dag_student[0],
                date2 = biologie_dag_student[1],
                date3 = biologie_dag_student[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Biologie',
                gebied='toekomst',
                naam = 'Case voor een bedrijf',
                id_module = 'case',
                omschrijving='Een probleem oplossen voor een bedrijf',
                tijd=3,
                kosten=45,
                baten_vast=45,
                experience_vast= 72,
                factor=30,
                module_type = 'Actief',
                niveau=1,
                date1 = biologie_case[0],
                date2 = biologie_case[1],
                date3 = biologie_case[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Biologie',
                gebied='sociaaltoekomst',
                naam='Excursie met studievereniging',
                id_module = 'excursie',
                omschrijving='Bij een bedrijf op bezoek',
                tijd=4,
                kosten=120,
                experience_vast=94,
                factor=30,
                module_type = 'Actief',
                niveau=2,
                date1 = biologie_excursie[0],
                date2 = biologie_excursie[1],
                date3 = biologie_excursie[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Biologie',
                gebied='sociaal',
                naam='Borrel studievereniging',
                id_module = 'borrel',
                omschrijving='Vrijdag middag borrel met lezing/praatje',
                tijd=2,
                kosten=60,
                experience_vast=48,
                niveau=1,
                date1 = biologie_borrel[0],
                date2 = biologie_borrel[1],
                date3 = biologie_borrel[2],
                )
            p.save()
        if i == 'Life Science and Technology':
            p = ModulesInfo(
                opleiding = 'Life Science and Technology',
                gebied='studie',
                naam='opendag op locatie',
                id_module = 'opendag',
                omschrijving='Een specifieke opleiding beter leren kennen',
                tijd=8,
                kosten=240,
                experience_vast=192,
                niveau=1,
                date1 = lst_opendag[0],
                date2 = lst_opendag[1],
                date3 = lst_opendag[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Life Science and Technology',
                gebied='studie',
                naam = 'Webklas',
                id_module = 'webklas',
                omschrijving='Online cursus over bepaalde bachelor opleidingen',
                tijd=16,
                kosten=240,
                baten_vast=240,
                experience_vast=192,
                factor=50,
                module_type = 'Actief',
                niveau=2,
                date1 = lst_webklas[0],
                date2 = lst_webklas[1],
                date3 = lst_webklas[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Life Science and Technology',
                gebied='studiesociaal',
                naam='Een dag student',
                id_module = 'dag_student',
                omschrijving='Een dagje student zijn',
                tijd=8,
                kosten=120,
                baten_vast=240,
                experience_vast=92,
                niveau=1,
                date1 = lst_dag_student[0],
                date2 = lst_dag_student[1],
                date3 = lst_dag_student[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Life Science and Technology',
                gebied='toekomst',
                naam = 'Case voor een bedrijf',
                id_module = 'case',
                omschrijving='Een probleem oplossen voor een bedrijf',
                tijd=3,
                kosten=45,
                baten_vast=45,
                experience_vast= 72,
                factor=30,
                module_type = 'Actief',
                niveau=1,
                date1 = lst_case[0],
                date2 = lst_case[1],
                date3 = lst_case[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Life Science and Technology',
                gebied='sociaaltoekomst',
                naam='Excursie met studievereniging',
                id_module = 'excursie',
                omschrijving='Bij een bedrijf op bezoek',
                tijd=4,
                kosten=120,
                experience_vast=94,
                factor=30,
                module_type = 'Actief',
                niveau=2,
                date1 = lst_excursie[0],
                date2 = lst_excursie[1],
                date3 = lst_excursie[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Life Science and Technology',
                gebied='sociaal',
                naam='Borrel studievereniging',
                id_module = 'borrel',
                omschrijving='Vrijdag middag borrel met lezing/praatje',
                tijd=2,
                kosten=60,
                experience_vast=48,
                niveau=1,
                date1 = lst_borrel[0],
                date2 = lst_borrel[1],
                date3 = lst_borrel[2],
                )
            p.save()
        if i == 'Farmacie':
            p = ModulesInfo(
                opleiding = 'Farmacie',
                gebied='studie',
                naam='opendag op locatie',
                id_module = 'opendag',
                omschrijving='Een specifieke opleiding beter leren kennen',
                tijd=8,
                kosten=240,
                experience_vast=192,
                niveau=1,
                date1 = farmacie_opendag[0],
                date2 = farmacie_opendag[1],
                date3 = farmacie_opendag[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Farmacie',
                gebied='studie',
                naam = 'Webklas',
                id_module = 'webklas',
                omschrijving='Online cursus over bepaalde bachelor opleidingen',
                tijd=16,
                kosten=240,
                baten_vast=240,
                experience_vast=192,
                factor=50,
                module_type = 'Actief',
                niveau=2,
                date1 = farmacie_webklas[0],
                date2 = farmacie_webklas[1],
                date3 = farmacie_webklas[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Farmacie',
                gebied='studiesociaal',
                naam='Een dag student',
                id_module = 'dag_student',
                omschrijving='Een dagje student zijn',
                tijd=8,
                kosten=120,
                baten_vast=240,
                experience_vast=92,
                niveau=1,
                date1 = farmacie_dag_student[0],
                date2 = farmacie_dag_student[1],
                date3 = farmacie_dag_student[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Farmacie',
                gebied='toekomst',
                naam = 'Case voor een bedrijf',
                id_module = 'case',
                omschrijving='Een probleem oplossen voor een bedrijf',
                tijd=3,
                kosten=45,
                baten_vast=45,
                experience_vast= 72,
                factor=30,
                module_type = 'Actief',
                niveau=1,
                date1 = farmacie_case[0],
                date2 = farmacie_case[1],
                date3 = farmacie_case[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Farmacie',
                gebied='sociaaltoekomst',
                naam='Excursie met studievereniging',
                id_module = 'excursie',
                omschrijving='Bij een bedrijf op bezoek',
                tijd=4,
                kosten=120,
                experience_vast=94,
                factor=30,
                module_type = 'Actief',
                niveau=2,
                date1 = farmacie_excursie[0],
                date2 = farmacie_excursie[1],
                date3 = farmacie_excursie[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Farmacie',
                gebied='sociaal',
                naam='Borrel studievereniging',
                id_module = 'borrel',
                omschrijving='Vrijdag middag borrel met lezing/praatje',
                tijd=2,
                kosten=60,
                experience_vast=48,
                niveau=1,
                date1 = farmacie_borrel[0],
                date2 = farmacie_borrel[1],
                date3 = farmacie_borrel[2],
                )
            p.save()
        if i == 'Informatica':
            p = ModulesInfo(
                opleiding = 'Informatica',
                gebied='studie',
                naam='opendag op locatie',
                id_module = 'opendag',
                omschrijving='Een specifieke opleiding beter leren kennen',
                tijd=8,
                kosten=240,
                experience_vast=192,
                niveau=1,
                date1 = informatica_opendag[0],
                date2 = informatica_opendag[1],
                date3 = informatica_opendag[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Informatica',
                gebied='studie',
                naam = 'Webklas',
                id_module = 'webklas',
                omschrijving='Online cursus over bepaalde bachelor opleidingen',
                tijd=16,
                kosten=240,
                baten_vast=240,
                experience_vast=192,
                factor=50,
                module_type = 'Actief',
                niveau=2,
                date1 = informatica_webklas[0],
                date2 = informatica_webklas[1],
                date3 = informatica_webklas[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Informatica',
                gebied='studiesociaal',
                naam='Een dag student',
                id_module = 'dag_student',
                omschrijving='Een dagje student zijn',
                tijd=8,
                kosten=120,
                baten_vast=240,
                experience_vast=92,
                niveau=1,
                date1 = informatica_dag_student[0],
                date2 = informatica_dag_student[1],
                date3 = informatica_dag_student[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Informatica',
                gebied='toekomst',
                naam = 'Case voor een bedrijf',
                id_module = 'case',
                omschrijving='Een probleem oplossen voor een bedrijf',
                tijd=3,
                kosten=45,
                baten_vast=45,
                experience_vast= 72,
                factor=30,
                module_type = 'Actief',
                niveau=1,
                date1 = informatica_case[0],
                date2 = informatica_case[1],
                date3 = informatica_case[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Informatica',
                gebied='sociaaltoekomst',
                naam='Excursie met studievereniging',
                id_module = 'excursie',
                omschrijving='Bij een bedrijf op bezoek',
                tijd=4,
                kosten=120,
                experience_vast=94,
                factor=30,
                module_type = 'Actief',
                niveau=2,
                date1 = informatica_excursie[0],
                date2 = informatica_excursie[1],
                date3 = informatica_excursie[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Informatica',
                gebied='sociaal',
                naam='Borrel studievereniging',
                id_module = 'borrel',
                omschrijving='Vrijdag middag borrel met lezing/praatje',
                tijd=2,
                kosten=60,
                experience_vast=48,
                niveau=1,
                date1 = informatica_borrel[0],
                date2 = informatica_borrel[1],
                date3 = informatica_borrel[2],
                )
            p.save()
        if i == 'Kunstmatige Intelligentie':
            p = ModulesInfo(
                opleiding = 'Kunstmatige Intelligentie',
                gebied='studie',
                naam='opendag op locatie',
                id_module = 'opendag',
                omschrijving='Een specifieke opleiding beter leren kennen',
                tijd=8,
                kosten=240,
                experience_vast=192,
                niveau=1,
                date1 = ki_opendag[0],
                date2 = ki_opendag[1],
                date3 = ki_opendag[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Kunstmatige Intelligentie',
                gebied='studie',
                naam = 'Webklas',
                id_module = 'webklas',
                omschrijving='Online cursus over bepaalde bachelor opleidingen',
                tijd=16,
                kosten=240,
                baten_vast=240,
                experience_vast=192,
                factor=50,
                module_type = 'Actief',
                niveau=2,
                date1 = ki_webklas[0],
                date2 = ki_webklas[1],
                date3 = ki_webklas[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Kunstmatige Intelligentie',
                gebied='studiesociaal',
                naam='Een dag student',
                id_module = 'dag_student',
                omschrijving='Een dagje student zijn',
                tijd=8,
                kosten=120,
                baten_vast=240,
                experience_vast=92,
                niveau=1,
                date1 = ki_dag_student[0],
                date2 = ki_dag_student[1],
                date3 = ki_dag_student[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Kunstmatige Intelligentie',
                gebied='toekomst',
                naam = 'Case voor een bedrijf',
                id_module = 'case',
                omschrijving='Een probleem oplossen voor een bedrijf',
                tijd=3,
                kosten=45,
                baten_vast=45,
                experience_vast= 72,
                factor=30,
                module_type = 'Actief',
                niveau=1,
                date1 = ki_case[0],
                date2 = ki_case[1],
                date3 = ki_case[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Kunstmatige Intelligentie',
                gebied='sociaaltoekomst',
                naam='Excursie met studievereniging',
                id_module = 'excursie',
                omschrijving='Bij een bedrijf op bezoek',
                tijd=4,
                kosten=120,
                experience_vast=94,
                factor=30,
                module_type = 'Actief',
                niveau=2,
                date1 = ki_excursie[0],
                date2 = ki_excursie[1],
                date3 = ki_excursie[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Kunstmatige Intelligentie',
                gebied='sociaal',
                naam='Borrel studievereniging',
                id_module = 'borrel',
                omschrijving='Vrijdag middag borrel met lezing/praatje',
                tijd=2,
                kosten=60,
                experience_vast=48,
                niveau=1,
                date1 = ki_borrel[0],
                date2 = ki_borrel[1],
                date3 = ki_borrel[2],
                )
            p.save()
        if i == 'Technische Bedrijfskunde':
            p = ModulesInfo(
                opleiding = 'Technische Bedrijfskunde',
                gebied='studie',
                naam='opendag op locatie',
                id_module = 'opendag',
                omschrijving='Een specifieke opleiding beter leren kennen',
                tijd=8,
                kosten=240,
                experience_vast=192,
                niveau=1,
                date1 = tbk_opendag[0],
                date2 = tbk_opendag[1],
                date3 = tbk_opendag[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Technische Bedrijfskunde',
                gebied='studie',
                naam = 'Webklas',
                id_module = 'webklas',
                omschrijving='Online cursus over bepaalde bachelor opleidingen',
                tijd=16,
                kosten=240,
                baten_vast=240,
                experience_vast=192,
                factor=50,
                module_type = 'Actief',
                niveau=2,
                date1 = tbk_webklas[0],
                date2 = tbk_webklas[1],
                date3 = tbk_webklas[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Technische Bedrijfskunde',
                gebied='studiesociaal',
                naam='Een dag student',
                id_module = 'dag_student',
                omschrijving='Een dagje student zijn',
                tijd=8,
                kosten=120,
                baten_vast=240,
                experience_vast=92,
                niveau=1,
                date1 = tbk_dag_student[0],
                date2 = tbk_dag_student[1],
                date3 = tbk_dag_student[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Technische Bedrijfskunde',
                gebied='toekomst',
                naam = 'Case voor een bedrijf',
                id_module = 'case',
                omschrijving='Een probleem oplossen voor een bedrijf',
                tijd=3,
                kosten=45,
                baten_vast=45,
                experience_vast= 72,
                factor=30,
                module_type = 'Actief',
                niveau=1,
                date1 = tbk_case[0],
                date2 = tbk_case[1],
                date3 = tbk_case[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Technische Bedrijfskunde',
                gebied='sociaaltoekomst',
                naam='Excursie met studievereniging',
                id_module = 'excursie',
                omschrijving='Bij een bedrijf op bezoek',
                tijd=4,
                kosten=120,
                experience_vast=94,
                factor=30,
                module_type = 'Actief',
                niveau=2,
                date1 = tbk_excursie[0],
                date2 = tbk_excursie[1],
                date3 = tbk_excursie[2],
                )
            p.save()
            p = ModulesInfo(
                opleiding = 'Technische Bedrijfskunde',
                gebied='sociaal',
                naam='Borrel studievereniging',
                id_module = 'borrel',
                omschrijving='Vrijdag middag borrel met lezing/praatje',
                tijd=2,
                kosten=60,
                experience_vast=48,
                niveau=1,
                date1 = tbk_borrel[0],
                date2 = tbk_borrel[1],
                date3 = tbk_borrel[2],
                )
            p.save()