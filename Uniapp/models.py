from django.db import models


class Yonalish(models.Model):
    nom = models.CharField(max_length=50)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Yonalish"
        verbose_name_plural = "Yonalishlar"


class Fan(models.Model):
    nom = models.CharField(max_length=250)
    yonalish = models.ForeignKey(Yonalish, on_delete=models.CASCADE)
    asosiy = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.yonalish}:{self.nom}"

    class Meta:
        verbose_name = "Fan"
        verbose_name_plural = "Fanlar"


class Ustoz(models.Model):
    JINS = (
        ('Erkak', 'Erkak'),
        ('Ayol', 'Ayol'),
    )

    DARAJA = (
        ('Bakalavr', 'Bakalavr'),
        ('Magsitr', 'Magsitr'),
        ('Aspirant', 'Aspirant'),
        ('Dokotrant', 'Dokotrant'),
    )

    ism = models.CharField(max_length=50)
    jins = models.CharField(max_length=10, choices=JINS)
    yosh = models.PositiveIntegerField(blank=True)
    daraja = models.CharField(max_length=50, choices=DARAJA)
    fan = models.ForeignKey(Fan, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.ism}"

    class Meta:
        verbose_name = "Ustoz"
        verbose_name_plural = "Ustozlar"
