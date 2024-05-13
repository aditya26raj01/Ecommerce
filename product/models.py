from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=255)
    # A slug is a string that can only include characters, numbers, dashes, and underscores.
    # It is the part of a URL that identifies a particular page on a website, in a human-friendly form.
    slug=models.SlugField()
    class Meta:
        ordering=("name",)
    def __str__(self) -> str:
        return f"{self.name}"

class Product(models.Model):
    name=models.CharField(max_length=255)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="products")
    slug=models.SlugField()
    descriptions=models.TextField(blank=True,null=True)
    price=models.PositiveIntegerField()
    created_at=models.TimeField(auto_now_add=True)
    class Meta:
        ordering=("-created_at",)
    def __str__(self) -> str:
        return f"{self.name}"



