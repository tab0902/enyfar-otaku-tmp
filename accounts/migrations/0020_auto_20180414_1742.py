# Generated by Django 2.0.4 on 2018-04-14 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meta', '0003_auto_20180327_1448'),
        ('accounts', '0019_auto_20180412_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='arrival_country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrival_country_set', to='meta.Country', verbose_name='到着国・地域ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transfer',
            name='arrival_district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrival_district_set', to='meta.District', verbose_name='到着行政区画ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transfer',
            name='departure_country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departure_country_set', to='meta.Country', verbose_name='出発国・地域ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transfer',
            name='departure_district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departure_district_set', to='meta.District', verbose_name='出発行政区画ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transfer',
            name='flight_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='フライトナンバー'),
        ),
    ]
