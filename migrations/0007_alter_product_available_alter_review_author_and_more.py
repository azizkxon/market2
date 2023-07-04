

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_category_options_alter_product_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=True, verbose_name='Доступность'),
        ),
        migrations.AlterField(
            model_name='review',
            name='author',
            field=models.CharField(max_length=50, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='review',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='review',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='shop.product', verbose_name='Продукт'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Рейтинг'),
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.TextField(blank=True, verbose_name='Текст'),
        ),
    ]
