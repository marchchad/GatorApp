from django import forms
from django.contrib import admin
from jobs.models import Job, Material, Client, Contract, About, Image, Tag

from datetime import datetime

# These classes define what model parameters will appear and which are editable

class ImageInline(admin.StackedInline):
	model = Image
	extra = 0

	# override the save method to save the pub_date as the current time
	def save_model(self, request, obj, form, change):
		obj.pub_date = datetime.now()
		obj.save()

class TagInline(admin.StackedInline):
	# TODO: figure out how to display the tag value instead of the tag object
	model = Tag.entity.through
	fields = ['value']

class TagAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['value']})
	]
	list_display = ['value']
	list_filter = ['value']
	search_fields = ['value']

class ClientAdmin(admin.ModelAdmin):
	fieldsets = [ # Any fields you want to edit should be included in the fieldset
		("Client", {'fields': ['fname','lname','address', 'current','job']})
	]
	list_display = ['fname', 'lname', 'address', 'current']
	list_filter = ['fname','lname','address']
	search_fields = ['fname','lname','address']

class JobAdmin(admin.ModelAdmin):
	fieldsets = [ # Any fields you want to edit should be included in the fieldset
		('Job', {'fields': ['name','desc','location_addr','tags']}),
		('Dates', {'fields': ['start_date', 'end_date','pub_date']}),
		('Costs', {'fields': ['estimated_cost','current_cost','final_cost']})
	]
	list_display = ['name','desc','location_addr','start_date','end_date','image_name_base', 'image_count']
	list_filter = ['start_date','end_date']
	search_fields = ['name','desc','location_addr','start_date','end_date']
	inlines = [ImageInline]

class AboutAdmin(admin.ModelAdmin):
	fieldsets = [
		('About Us', {'fields': ['content']})
	]
	list_display = ['content', 'pub_date']

	def save_model(self, request, obj, form, change):
		obj.pub_date = datetime.now()
		obj.save()

admin.site.register(Job, JobAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Material)
admin.site.register(Contract)