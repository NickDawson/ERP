# Generated by Django 2.2.6 on 2020-04-14 07:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('control', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('expense_type', models.CharField(choices=[('normal', 'normal'), ('asset', 'asset'), ('staff', 'staff')], default='normal', max_length=200)),
                ('expense_date', models.DateField(default=django.utils.timezone.now)),
                ('expense_for', models.CharField(blank=True, max_length=200, null=True)),
                ('asset', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='for_asset', to='control.Asset')),
                ('authorized_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to='control.UserProfile')),
                ('expense_branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='expense_branch', to='control.Branch')),
                ('staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='for_staff', to='control.UserProfile')),
            ],
            options={
                'verbose_name': 'Expense',
                'verbose_name_plural': 'Expenses',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=200)),
                ('unit', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ROR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=200)),
                ('b_price', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('s_price', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
            ],
            options={
                'verbose_name': 'ROR',
                'verbose_name_plural': 'RORs',
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('sale_type', models.BooleanField(default=False)),
                ('sale_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('total_amount', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('amount_paid', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('waiting_approval', models.BooleanField(default=False)),
                ('approved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='approved_by', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='authorization', to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='customer', to=settings.AUTH_USER_MODEL)),
                ('sale_branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='sale_branch', to='control.Branch')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='staff', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Sale',
                'verbose_name_plural': 'Sales',
            },
        ),
        migrations.CreateModel(
            name='SaleItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('quantity', models.IntegerField()),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='purchased_item', to='home.Product')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale_info', to='home.Sale')),
            ],
            options={
                'verbose_name': 'SaleItem',
                'verbose_name_plural': 'SaleItems',
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('purchase_type', models.BooleanField(default=False)),
                ('purchase_date', models.DateField(default=django.utils.timezone.now)),
                ('receipt', models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/')),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('selling_price', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('buying_price', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('quantity', models.IntegerField(default=1)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='authorized_by', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='purchased_product', to='home.Product')),
                ('purchase_branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='purchase_branch', to='control.Branch')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='supplier', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Purchase',
                'verbose_name_plural': 'Purchases',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('payment_type', models.CharField(choices=[('customer payment', 'customer payment'), ('staff collection', 'staff collection'), ('loan collection', 'loan collection'), ('supplier payment', 'supplier payment'), ('other payment', 'other payment'), ('loan provision', 'loan provision'), ('staff loan', 'staff loan')], default='customer payment', max_length=200)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('deduction_amount', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('payment_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('authorized_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='payment_authorized_by', to=settings.AUTH_USER_MODEL)),
                ('collected_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='payment_collector', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='payment_created_by', to=settings.AUTH_USER_MODEL)),
                ('payment_branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='payment_branch', to='control.Branch')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='payment_to', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
            },
        ),
        migrations.CreateModel(
            name='ExpenseDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('detail', models.CharField(blank=True, max_length=200, null=True)),
                ('expense_amount', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('expense', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Expense')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BadDebt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('description', models.TextField(max_length=300)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='debtor', to='control.UserProfile')),
                ('staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='charged_to', to='control.UserProfile')),
            ],
            options={
                'verbose_name': 'BadDebt',
                'verbose_name_plural': 'BadDebts',
            },
        ),
    ]
