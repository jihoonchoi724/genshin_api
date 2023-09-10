from django.db import models


class Character(models.Model):
    ELEMENTS = [
        ("ANEMO", "Anemo"),
        ("GEO", "Geo"),
        ("ELECTRO", "Electro"),
        ("DENDRO", "Dendro"),
        ("HYDRO", "Hydro"),
        ("PYRO", "Pyro"),
        ("CRYO", "Cryo"),
        ("FUTURE1", "Future Element"),
    ]

    WEAPONS = [
        ("SWORD", "Sword"),
        ("POLEARM", "Polearm"),
        ("CLAYMORE", "Claymore"),
        ("CATALYST", "Catalyst"),
        ("BOW", "Bow"),
        ("FUTURE1", "Future Weapon 1"),
        ("FUTURE2", "Future Weapon 2"),
    ]

    NATIONS = [
        ("MONDSTADT", "Mondstadt"),
        ("LIYUE", "Liyue"),
        ("INAZUMA", "Inazuma"),
        ("SUMERU", "Sumeru"),
        ("FONTAINE", "Fontaine"),
        ("NATLAN", "Natlan"),
        ("SNEZHNAYA", "Snezhnaya"),
        ("KHAENRIAH", "Khaenri'ah"),
        ("UNKNOWN", "Unknown"),
    ]

    character_id = models.CharField(max_length=64, primary_key=True)
    name = models.CharField(max_length=64)
    vision = models.CharField(max_length=64, choices=ELEMENTS)
    weapon = models.CharField(max_length=64, choices=WEAPONS)
    nation = models.CharField(max_length=64, choices=NATIONS)
    rarity = models.PositiveSmallIntegerField()
    birthday = models.CharField(max_length=10)
    release_version = models.CharField(max_length=5)
    title = models.CharField(max_length=64)
    affiliation = models.CharField(max_length=64)
    constellation_name = models.CharField(max_length=64)

    class Meta:
        ordering = ["name"],
        constraints = [
            models.UniqueConstraint(
                fields=["character_id", "name"], name="unique_character")
        ]


class Talent(models.Model):
    character = models.ForeignKey(
        Character, related_name="talents", on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField()
    talent_type = models.CharField(max_length=64)
    talent_name = models.CharField(max_length=64)
    talent_desc = models.TextField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["order", "talent_type", "talent_name", "talent_desc"], name="unique_talent")
        ]


class Constellation(models.Model):
    character = models.ForeignKey(
        Character, related_name="constellations", on_delete=models.CASCADE)
    con_number = models.PositiveSmallIntegerField()
    con_name = models.CharField(max_length=64)
    con_desc = models.TextField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["con_number", "con_name", "con_desc"], name="unique_constellation")
        ]
