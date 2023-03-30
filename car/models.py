from django.db import models


class Cars(models.Model):
    CAR_TYPE = (
        ('Седан', 'Седан'),
        ("Хэтчбек", "Хэтчбек"),
        ("Универсал", "Универсал"),
        ("Пикап", "Пикап"),
        ("Купе", "Купе"),
        ("Кабриолет", "Кабриолет"),
    )
    title = models.CharField("Название марки машины", max_length=100)
    description = models.TextField("Описание машины")
    image = models.ImageField(upload_to='')
    car_type = models.CharField(max_length=100, choices=CAR_TYPE)
    created_data = models.DateTimeField(auto_now_add=True)
    cost = models.PositiveIntegerField()
    video = models.URLField()

    def __str__(self):
        return self.title


class CommentCar(models.Model):
    RATING = (
        ('*', '*'),
        ('**', '**'),
        ('***', '***'),
        ('****', '****'),
        ('*****', '*****')
    )
    car_choice_comment = models.ForeignKey(Cars, on_delete=models.CASCADE, related_name="comment_object")
    text = models.TextField()
    rate_stars = models.CharField(max_length=100, choices=RATING)
    created_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.rate_stars