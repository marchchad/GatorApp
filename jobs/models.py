import datetime

from django.db import models
from django.utils import timezone
# Find out if order of model declaration really matters because it seems like it does

#TODOs: Listed in order of priority\
    #TODO: Create Estimate class to associate with clients and jobs
    #TODO: Create Contractor class to associate other contractors to jobs and contracts
    #TODO: Create Tools class to associate with jobs

class Tag(models.Model):
    value = models.CharField(max_length=50)
    entity = models.ManyToManyField('self')

class Permit(models.Model):
    permit_type = models.CharField('Permit', max_length=100)
    number = models.IntegerField('Permit #')
    agency = models.CharField('Permitted By', max_length=200)
    issue_date = models.DateField('Date Issued')
    valid_on = models.DateField('Valid On')
    expires_on = models.DateField('Expires On')

    def __str__(self):
        return permit_type

    def days_until_expired(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.expires_on <= now
    days_until_expired.admin_order_field = 'expires_on'
    days_until_expired.boolean = True
    days_until_expired.short_description = 'Is Expired?'

class Inspection(models.Model):
    name = models.CharField('Inspection', max_length=100)
    desc = models.CharField('Description', max_length=300)
    inspector = models.CharField('Inspector', max_length=50)
    inspection_date = models.DateField('Inspection Date')
    initial_inspection = models.BooleanField(default=True)
    was_rescheduled = models.BooleanField(default=False)

    def __str__(self):
        return name

class Job(models.Model):
    desc = models.CharField('Description', max_length=200)
    name = models.CharField('Name', max_length=100)
    start_date = models.DateTimeField('Job Start Date') #Change to Date field when migrating to different db
    end_date = models.DateTimeField('Job End Date') #Change to Date field when migrating to different db
    pub_date = models.DateTimeField('Date Published') #Change to Date field when migrating to different db
    estimated_cost = models.FloatField('Estimate')
    current_cost = models.FloatField('Current Cost')
    final_cost = models.FloatField('Final Cost')
    location_addr = models.CharField('Address', max_length=200)
    share_location = models.BooleanField(default=False)
    share_job = models.BooleanField(default=False)
    # Temp solution for using stock images
    image_name_base = models.CharField(max_length=50)
    image_count = models.IntegerField()
    tags = models.ManyToManyField(Tag)

    # activate these when moving databases or clear db then rerun migrations
    #permits = models.ForeignKey(Permit)
    #inspection = models.ForeignKey(Inspection)

    def __str__(self):
        return self.name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Client(models.Model):
    """
    A client can have multiple jobs, but a job cannot have multiple clients.
    """
    job = models.ForeignKey(Job)
    fname = models.CharField('First name', max_length=50)
    lname = models.CharField('Last name', max_length=50)
    address = models.CharField('Address', max_length=200)
    current = models.BooleanField(default=False)

    def __str__(self):
        return self.fname + ' ' + self.lname

class Contract(models.Model):
    job = models.ForeignKey(Job)
    start_date = models.DateTimeField('Contract Start Date') #Change to Date field when migrating to different db
    end_date = models.DateTimeField('Contract End Date') #Change to Date field when migrating to different db
    agreement_date = models.DateTimeField('Date Signed')
    active = models.BooleanField(default=False)

class Material(models.Model):
    job = models.ForeignKey(Job)
    mat_type = models.CharField('Material', max_length=100)
    count = models.FloatField('Count')
    weight = models.FloatField('Weight')
    weight_unit = models.CharField('Unit',max_length=3)
    cost_per_unit = models.FloatField('Cost per unit')
    cost_per_weight = models.FloatField('Cost per weight')

    def __str__(self):
        return mat_type

class About(models.Model):
    content = models.TextField('Content')
    pub_date = models.DateTimeField('Added On')

class Image(models.Model):
    job = models.ForeignKey(Job)
    imgFile = models.FileField(upload_to='job/')
    title = models.CharField('Title', max_length=100)
    desc = models.CharField('Description', max_length=300)
    public = models.BooleanField('Is Visible to Public?', default=True)
    pub_date = models.DateTimeField('Date Added')

# TODO: Finish user mgmt
# Add this import: from django import forms
# class LoginForm(forms.ModelForm):
#   username = forms.CharField(max_length='50')
#   password = forms.CharField(widget=forms.PasswordInput)