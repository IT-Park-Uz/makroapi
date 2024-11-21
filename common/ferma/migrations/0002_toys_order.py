from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('ferma', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='Toys',
            name='order',
            field=models.IntegerField(default=1),
        ),
    ]
