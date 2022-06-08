from django.db import models
from user_management.models import  *
# Create your models here.
class RequestType(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    class Meta:
        db_table = 'travel_request_type'

class RequestTypeClass(models.Model):
    name = models.CharField(max_length=50)
    type = models.IntegerField()
    request_type = models.ForeignKey(RequestType,on_delete=models.CASCADE,related_name='class_request_type')
    class Meta:
        db_table = 'travel_request_type_class'

class UserRequestTypeHeader(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='userrequesttypeheader_user')
    name = models.CharField(max_length=50)
    class Meta:
        db_table = 'travel_user_request_type_header'

class UserRequestType(models.Model):
    user_request_type_header = models.ForeignKey(UserRequestTypeHeader,on_delete=models.CASCADE,related_name='userrequesttype_header')
    request_type = models.ForeignKey(RequestType,on_delete=models.CASCADE,related_name='userrequesttype_request_type')
    request_type_class = models.ForeignKey(RequestTypeClass,on_delete=models.CASCADE,related_name='userrequesttype_request_type_class')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='userrequesttype_user')
    from_location = models.TextField()
    to_location = models.TextField()
    from_date = models.DateTimeField()
    to_date = models.DateTimeField(null=True)
    is_return = models.BooleanField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField()
    budjet_code = models.IntegerField()

    class Meta:
        db_table = 'travel_user_request_type'

class TravelTrackingStatus(models.Model):
    user_request_type_header = models.ForeignKey(UserRequestTypeHeader, on_delete=models.CASCADE,related_name='traveltrackingstatus_header')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='traveltrackingstatus_user')
    emp_id = models.IntegerField()
    campus = models.CharField(max_length=100,null=True)
    description = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    designation = models.CharField(max_length=100,null=True)
    institution = models.CharField(max_length=100,null=True)
    department = models.CharField(max_length=100,null=True)

    class Meta:
        db_table = 'travel_tracking_status'

class TravelTrackingStatusMapping(models.Model):
    user_request_type_header = models.ForeignKey(UserRequestTypeHeader, on_delete=models.CASCADE,
                                                 related_name='traveltrackingstatusmapping_header')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='traveltrackingstatusmapping_user')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='traveltrackingstatusmapping_to_user')
    travel_tracking_status = models.ForeignKey(TravelTrackingStatus, on_delete=models.CASCADE, related_name='traveltrackingstatusmapping_travel_tracking_status')
    travel_tracking_respond_status = models.ForeignKey(TravelTrackingStatus, on_delete=models.CASCADE, related_name='traveltrackingstatusmapping_travel_tracking_respond_status')
    is_respond = models.BooleanField(default=False)
    last_seen_time = models.DateTimeField(null=True)
    is_seen = models.BooleanField(default=False)
    seen_time = models.DateTimeField(null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'travel_tracking_status_mapping'