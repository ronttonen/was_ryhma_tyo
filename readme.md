# Jos toi virtualenv toimii ni aktivoituu:
## source was-projekti/bin/activate

# Jos teet uuden virtualenvin käytä python kolmosta
# Sen jälkeen asenna sinne tai koko koneelle, ihan sama requirementsit
## pip install -r requirements.txt
### Tosiaan jos python 2 käytössä ei tule toimimaan

# Jos tietokanta on kunnossa:
## python migrate.py runserver 8000
### komento pitää laittaa samassa kansiossa missä toi migrate.py tiedosto on

# Jos tietokanta on broken:
## poista db.sqlite3
## poista migrations kansion sisältö
## laita komento:
### python manage.py makemigrations was_ryhma_tyo
### python manage.py migrate

# Tietty jos joku haluu tehä git ignoren ni sinne vois laittaa ainaki db, pycache ja migrationit
