from django.contrib import admin
from .models import MainUserInfo, MainUserExp, MainUserSkill

class MainUserInfoAdmin(admin.ModelAdmin):
    list_display = [
        'user_id',
        'user_login',
        'user_name',
        'user_image',
        'user_sur_name',
        'user_birthday',
        'user_email',
        'user_phone',
        'user_site',
        'reg_date',
        'user_subscribe',
        ]
    # list_filter = ['available', 'created', 'updated']
    list_editable = ['user_phone', 'user_subscribe', 'user_image']
    # fields = ['user_id','user_id',
    #     'user_login',
    #     'user_name',
    #     'user_image',
    #     'user_sur_name',
    #     'user_birthday',
    #     'user_email',
    #     'user_phone',
    #     'user_site',
    #     'reg_date',
    #     'user_subscribe',]
    # prepopulated_fields = {'slug': ('user_name',)}
admin.site.register(MainUserInfo, MainUserInfoAdmin)

class MainUserExpAdmin(admin.ModelAdmin):
    list_display = [
        'work_id',
        'work_company',
        'work_position',
        'work_description',
        'work_start',
        'work_end',
        ]
    # list_filter = ['available', 'created', 'updated']
    list_editable = ['work_company', 'work_position',
                     'work_position', 'work_description',
                     'work_start', 'work_end']
    # prepopulated_fields = {'slug': ('work_company',)}
admin.site.register(MainUserExp, MainUserExpAdmin)

class MainUserSkillAdmin(admin.ModelAdmin):
    list_display = [
        'skill_id',
        'skill_name',
        'skill_count',
        'skill_status',
        'skill_description',
        ]
    # list_filter = ['available', 'created', 'updated']
    list_editable = ['skill_name', 'skill_count',
                     'skill_status', 'skill_description',
                     ]
    # prepopulated_fields = {'slug': ('work_company',)}
admin.site.register(MainUserSkill, MainUserSkillAdmin)
