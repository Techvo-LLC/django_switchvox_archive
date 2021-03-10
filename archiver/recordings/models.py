from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class recordings(models.Model):
    recording = models.URLField(_("recording"), max_length=500, unique=True)
    recording_tag = models.CharField(_("recording tag"), max_length=50)
    recorded_call_id = models.IntegerField(_("recorded call id"), unique=True, blank=False, null=False)
    recorder_cid = models.CharField(_("recorded cid"), max_length=50,blank=True,null=True)
    recorded_cid = models.CharField(_("recorded cid"), max_length=50,blank=True,null=True)
    recorder_account_id = models.IntegerField(_("recorder account id"),blank=True,null=True)
    recorded_account_id = models.IntegerField(_("recorded account id"),blank=True,null=True)
    from_account_id = models.IntegerField(_("Account ID (from)"),blank=True,null=True)
    from_caller_id = models.CharField(_("Caller ID (from)"), max_length=50)
    to_account_id = models.IntegerField(_("Account ID (to)"),blank=True,null=True)
    to_caller_id = models.CharField(_("Caller ID (to)"), max_length=50)
    duration = models.IntegerField(_("duration (in seconds)"))
    date_created_ts = models.DateTimeField(_("date created"), auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.recorded_call_id)

    class Meta:
        db_table = 'recordings'
        managed = True
        verbose_name = 'Recordings'
        verbose_name_plural = 'Recordings'