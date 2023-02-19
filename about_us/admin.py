from django.contrib import admin
from .models import AboutUsTopInfo, FirstBenefitsBlock, SecondBenefitsBlock, PhotosAndNumbers, TeamMember

# Register your models here.

admin.site.register(AboutUsTopInfo)
admin.site.register(PhotosAndNumbers)


@admin.register(FirstBenefitsBlock)
class FirstBenefitsBlockAdmin(admin.ModelAdmin):

    list_display = ['house_point_header', 'agents_point_header', 'safety_point_header', 'image', ]


@admin.register(SecondBenefitsBlock)
class SecondBenefitsBlockAdmin(admin.ModelAdmin):
    list_display = ['house_point_header', 'agents_point_header', 'safety_point_header', 'image', ]


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'short_about']
