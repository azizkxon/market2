

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_review'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'Категории', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('title',), 'verbose_name': 'Товары', 'verbose_name_plural': 'Товары'},
        ),
    ]
