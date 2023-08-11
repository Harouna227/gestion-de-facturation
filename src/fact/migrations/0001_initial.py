# Generated by Django 4.2.3 on 2023-07-13 11:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=123)),
                ('email', models.CharField(max_length=225)),
                ('telephone', models.CharField(max_length=123)),
                ('sexe', models.CharField(choices=[('M', 'Masculin'), ('F', 'Feminin')], max_length=1)),
                ('age', models.CharField(max_length=12)),
                ('adresse', models.CharField(max_length=225)),
                ('ville', models.CharField(max_length=23)),
                ('code_postal', models.CharField(max_length=7)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('enregistrer_par', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Customer',
            },
        ),
        migrations.CreateModel(
            name='Facture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_facture', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('dernier_update', models.DateTimeField(blank=True, null=True)),
                ('paie', models.BooleanField(default=False)),
                ('type_facture', models.CharField(choices=[('R', 'Reçu'), ('P', 'Facture Proforma'), ('F', 'Facture')], max_length=1)),
                ('commentaires', models.CharField(blank=True, max_length=1000, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fact.customer')),
                ('enregistrer_par', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Facture',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_article', models.CharField(max_length=50)),
                ('quantite', models.IntegerField(default=0)),
                ('prix_unit', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('prix_total', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('facture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fact.facture')),
            ],
            options={
                'verbose_name': 'Articles',
            },
        ),
    ]