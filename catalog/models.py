from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="Назва")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")


    class Meta:
        db_table = "category"
        verbose_name = "категорію"
        verbose_name_plural = "Категорії"

    def __str__(self) -> str:
        return self.name

class Goods(models.Model):
    category = models.ForeignKey(to=Categories, on_delete=models.PROTECT, verbose_name="Категорія")
    name = models.CharField(max_length=200, unique=True, verbose_name="Назва товару")
    description = models.TextField(blank=True, null=True, verbose_name="Опис")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Кільікість")
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name="Ціна без знижки")
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name="Знижка %")
    image = models.ImageField(upload_to="goods_images", blank=True, null=True, verbose_name="Фотографія")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL")


    class Meta:
        db_table = "product"
        verbose_name = "товар"
        verbose_name_plural = "товари"
        ordering = ("id",)

    def __str__(self) -> str:
        return f"{self.name} - {self.quantity}"

    
    def discount_price(self):
        return round(self.price - self.price*self.discount/100, 2)
