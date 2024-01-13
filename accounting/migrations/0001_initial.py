# Generated by Django 2.1.7 on 2019-03-23 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loans', '0003_loanissue_loanpayment'),
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('payed_to', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='ExpenseType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='IncomeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='income',
            name='income_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.IncomeType'),
        ),
        migrations.AddField(
            model_name='income',
            name='loan_num',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loans.LoanIssue'),
        ),
        migrations.AddField(
            model_name='income',
            name='received_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Member'),
        ),
        migrations.AddField(
            model_name='expense',
            name='expense_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.ExpenseType'),
        ),
    ]