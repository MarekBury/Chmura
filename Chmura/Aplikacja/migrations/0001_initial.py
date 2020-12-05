# Generated by Django 3.1.4 on 2020-12-05 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produkt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=80, null=True)),
                ('cena', models.FloatField(null=True)),
                ('kategoria', models.CharField(choices=[('Domowe', 'Domowe'), ('Zewnętrzne', 'Zewnętrzne')], max_length=80, null=True)),
                ('opis', models.CharField(blank=True, max_length=80, null=True)),
                ('data_utworzenia', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, null=True)),
                ('password', models.CharField(max_length=80, null=True)),
                ('email', models.CharField(max_length=80, null=True)),
                ('telefon', models.CharField(max_length=80, null=True)),
                ('data_utworzenia', models.DateTimeField(auto_now_add=True, null=True)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Zamowienie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_utworzenia', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Oczekiwanie', 'Oczekiwanie'), ('W doręczeniu', 'W doręczeniu'), ('Dostarczono', 'Dostarczono')], max_length=80, null=True)),
                ('klient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Aplikacja.users')),
                ('produkt', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Aplikacja.produkt')),
            ],
        ),
        migrations.AddField(
            model_name='produkt',
            name='tags',
            field=models.ManyToManyField(to='Aplikacja.Tags'),
        ),
    ]
