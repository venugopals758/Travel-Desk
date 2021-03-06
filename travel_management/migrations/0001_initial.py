# Generated by Django 4.0.5 on 2022-06-08 16:20

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
            name='RequestType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'travel_request_type',
            },
        ),
        migrations.CreateModel(
            name='RequestTypeClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.IntegerField()),
                ('request_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_request_type', to='travel_management.requesttype')),
            ],
            options={
                'db_table': 'travel_request_type_class',
            },
        ),
        migrations.CreateModel(
            name='TravelTrackingStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField()),
                ('campus', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('designation', models.CharField(max_length=100, null=True)),
                ('institution', models.CharField(max_length=100, null=True)),
                ('department', models.CharField(max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='traveltrackingstatus_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'travel_tracking_status',
            },
        ),
        migrations.CreateModel(
            name='UserRequestTypeHeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userrequesttypeheader_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'travel_user_request_type_header',
            },
        ),
        migrations.CreateModel(
            name='UserRequestType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_location', models.TextField()),
                ('to_location', models.TextField()),
                ('from_date', models.DateTimeField()),
                ('to_date', models.DateTimeField(null=True)),
                ('is_return', models.BooleanField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField()),
                ('budjet_code', models.IntegerField()),
                ('request_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userrequesttype_request_type', to='travel_management.requesttype')),
                ('request_type_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userrequesttype_request_type_class', to='travel_management.requesttypeclass')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userrequesttype_user', to=settings.AUTH_USER_MODEL)),
                ('user_request_type_header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userrequesttype_header', to='travel_management.userrequesttypeheader')),
            ],
            options={
                'db_table': 'travel_user_request_type',
            },
        ),
        migrations.CreateModel(
            name='TravelTrackingStatusMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_respond', models.BooleanField(default=False)),
                ('last_seen_time', models.DateTimeField(null=True)),
                ('is_seen', models.BooleanField(default=False)),
                ('seen_time', models.DateTimeField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='traveltrackingstatusmapping_to_user', to=settings.AUTH_USER_MODEL)),
                ('travel_tracking_respond_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='traveltrackingstatusmapping_travel_tracking_respond_status', to='travel_management.traveltrackingstatus')),
                ('travel_tracking_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='traveltrackingstatusmapping_travel_tracking_status', to='travel_management.traveltrackingstatus')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='traveltrackingstatusmapping_user', to=settings.AUTH_USER_MODEL)),
                ('user_request_type_header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='traveltrackingstatusmapping_header', to='travel_management.userrequesttypeheader')),
            ],
            options={
                'db_table': 'travel_tracking_status_mapping',
            },
        ),
        migrations.AddField(
            model_name='traveltrackingstatus',
            name='user_request_type_header',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='traveltrackingstatus_header', to='travel_management.userrequesttypeheader'),
        ),
    ]
