# Generated by Django 3.2 on 2022-05-23 09:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('insuranceProducts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='dumpData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'DRAFT'), ('active', 'ACTIVE'), ('deactivate', 'DEACTIVATE')], default='draft', max_length=10)),
                ('data', models.JSONField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InsuranceCreditProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('credit_product_code', models.CharField(help_text='Credit Product Code', max_length=100, unique=True, verbose_name='Credit Product Code')),
                ('credit_product_name', models.CharField(help_text='Credit Product Name', max_length=200, verbose_name='Credit Product  Name')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
            ],
            options={
                'verbose_name_plural': 'Insurance Credit Products Master',
                'db_table': 'insurance_credit_products',
            },
        ),
        migrations.AddField(
            model_name='insurancediscussion',
            name='approxNetIncome',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Approximate Net Income'),
        ),
        migrations.AddField(
            model_name='insurancediscussion',
            name='coGender',
            field=models.CharField(blank=True, choices=[('m', 'Male'), ('f', 'Female'), ('o', 'Other')], max_length=2, null=True, verbose_name='Co Borrower - Gender'),
        ),
        migrations.AddField(
            model_name='insurancediscussion',
            name='currentApplicationPmt',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Current Application Payment'),
        ),
        migrations.AddField(
            model_name='insurancediscussion',
            name='currentSection',
            field=models.CharField(blank=True, choices=[('customerInfoMin', 'customerInfoMin'), ('lovedOnes', 'lovedOnes'), ('creditInfo', 'creditInfo'), ('incomeExpenseSvgs', 'incomeExpenseSvgs'), ('detailedIncome', 'detailedIncome'), ('detailedExpense', 'detailedExpense'), ('detailedSavings', 'detailedSavings'), ('otherInsCoverage', 'otherInsCoverage'), ('personalPresentment', 'personalPresentment')], max_length=40, null=True, verbose_name='Discussion Section'),
        ),
        migrations.AddField(
            model_name='insurancediscussion',
            name='primaryGender',
            field=models.CharField(blank=True, choices=[('m', 'Male'), ('f', 'Female'), ('o', 'Other')], max_length=2, null=True, verbose_name='Gender'),
        ),
        migrations.AddField(
            model_name='insurancediscussion',
            name='savingsEmergencyFund',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Saving & Emergency Fund'),
        ),
        migrations.AddField(
            model_name='insurancediscussion',
            name='sssavingsEmergencyFund',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Saving & Emergency Fund'),
        ),
        migrations.AddField(
            model_name='insurancediscussion',
            name='totalExistingDebt',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Total Existing Debt'),
        ),
        migrations.AddField(
            model_name='insurancediscussion',
            name='totalMonthlyPmt',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Total Monthly Payment'),
        ),
        migrations.AddField(
            model_name='insurancediscussion',
            name='totalSecuredAmt',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Total Secured Amount'),
        ),
        migrations.AddField(
            model_name='insurancediscussion',
            name='totalUnsecuredAmt',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Total Unsecured Amount'),
        ),
        migrations.AlterField(
            model_name='insurancediscussion',
            name='agentOverallPerceptionOfCustomerResp',
            field=models.CharField(blank=True, choices=[('positive', 'positive'), ('neutral', 'neutral'), ('negative', 'negative')], max_length=20, null=True, verbose_name='Agent Perception of customer response'),
        ),
        migrations.AlterField(
            model_name='insurancediscussion',
            name='canada_provence',
            field=models.CharField(blank=True, choices=[('nl', 'Newfoundland and Labrador'), ('pw', 'Prince Edward Island'), ('ns', 'Nova Scotia'), ('nb', 'New Brunswick'), ('qc', 'Quebec'), ('on', 'Ontario'), ('mb', 'Manitoba'), ('sk', 'Saskatchewan'), ('ab', 'Alberta'), ('bc', 'British Columbia'), ('yt', 'Yukon'), ('nt', 'Northwest Territories'), ('nu', 'Nunavut')], max_length=2, null=True, verbose_name='Province'),
        ),
        migrations.AlterField(
            model_name='insurancediscussion',
            name='coFirstName',
            field=models.CharField(blank=True, max_length=50, verbose_name='Co Borrower - First Name'),
        ),
        migrations.AlterField(
            model_name='insurancediscussion',
            name='coLastName',
            field=models.CharField(blank=True, max_length=50, verbose_name='Co Borrower - Last Name'),
        ),
        migrations.AlterField(
            model_name='insurancediscussion',
            name='coMiddleName',
            field=models.CharField(blank=True, max_length=50, verbose_name='Co Borrower - Middle Name'),
        ),
        migrations.AlterField(
            model_name='insurancediscussion',
            name='discussionOutcomes',
            field=models.CharField(blank=True, choices=[('declined', 'declined'), ('acceptedOffer', 'acceptedOffer'), ('requiresFollowup', 'requiresFollowup')], max_length=20, null=True, verbose_name='Outcome of discussion'),
        ),
        migrations.AlterField(
            model_name='insurancediscussion',
            name='hasChildrenFinResponsibility',
            field=models.CharField(blank=True, choices=[('y', 'Yes'), ('n', 'No')], max_length=2, null=True, verbose_name='Children Financial Responsibility'),
        ),
        migrations.AlterField(
            model_name='insurancediscussion',
            name='hasOthersFinResponsibility',
            field=models.CharField(blank=True, choices=[('y', 'Yes'), ('n', 'No')], max_length=2, null=True, verbose_name='Other Financial Responsibility'),
        ),
        migrations.AlterField(
            model_name='insurancediscussion',
            name='hasParentsFinResponsibility',
            field=models.CharField(blank=True, choices=[('y', 'Yes'), ('n', 'No')], max_length=2, null=True, verbose_name='Other Relatives Financial Responsibility'),
        ),
        migrations.AlterField(
            model_name='insurancediscussion',
            name='hasPartnerFinResponsibility',
            field=models.CharField(blank=True, choices=[('y', 'Yes'), ('n', 'No')], max_length=2, null=True, verbose_name='Partner Financial Responsibility'),
        ),
        migrations.AlterField(
            model_name='insurancediscussion',
            name='primaryAge',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Age'),
        ),
        migrations.CreateModel(
            name='InsuranceEligibility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('minAge', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Min Age')),
                ('maxAge', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Max Age')),
                ('residency', models.CharField(blank=True, choices=[('y', 'Yes'), ('n', 'No')], max_length=2, null=True, verbose_name='Canadian Residency')),
                ('military', models.CharField(blank=True, choices=[('y', 'Yes'), ('n', 'No')], max_length=2, null=True, verbose_name='Canadian Military')),
                ('effective_start_date', models.DateField(default=django.utils.timezone.now, verbose_name='Effective Start Date')),
                ('effective_end_date', models.DateField(default='2099-12-31', verbose_name='Effective End Date')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('insProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insuranceProducts.insuranceproduct')),
            ],
            options={
                'verbose_name_plural': 'Insurance Eligibility Master',
                'db_table': 'insurance_eligibility_master',
            },
        ),
        migrations.AddField(
            model_name='insuranceproduct',
            name='creditProduct_code',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='creditProduct_code', to='insuranceProducts.insurancecreditproduct'),
        ),
    ]