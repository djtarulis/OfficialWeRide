from django.conf import settings
from django.contrib import admin
from .models import Event, Sponsor, Photo
from django.core.mail import send_mail

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date', 'location', 'address', 'created_at', 'updated_at')
    search_fields = ('title', 'location', 'date', 'created_at')
    list_filter = ('date',)

@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'business_name', 'amount', 'message', 'created_at', 'updated_at')
    search_fields = ('name', 'email', 'phone', 'business_name', 'amount', 'message', 'created_at')
    list_filter = ('created_at',)

    def send_email_notification(self, request, queryset):
        for sponsor in queryset:
            send_mail(
                subject="New Donation Interest",
                message=f"Name: {sponsor.name}\nEmail: {sponsor.email}\nMessage: {sponsor.message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=settings.EMAIL_HOST_USER,  # Change this to your email
            )
        self.message_user(request, "Email notifications sent successfully!")

    send_email_notification.short_description = "Send Email Notification to Admin"

@admin.register(Photo)
class EventPhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at')