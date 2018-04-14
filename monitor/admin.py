from django.contrib import admin
from django.utils.html import format_html


from .models import StreamMonitor
from .models import Words

@admin.register(StreamMonitor)
class StreamMonitorAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        "stream_count",
        "stream_run",
        "stream_status",
        "authenticated",
        "redis_errors",
        "allowed_redis_errors",
        "redis_ip"
    )
    readonly_fields = (
        'stream_count',
        'redis_errors',
        'stream_status',
    )
    def account_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Start</a>&nbsp;'
            '<a class="button" href="{}">Stop</a>',
        )

    account_actions.short_description = 'Account Actions'
    account_actions.allow_tags = True

    
admin.site.register(StreamMonitor, StreamMonitorAdmin)