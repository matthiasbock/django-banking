# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Wikidjangolog(models.Model):
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    datum = models.DateTimeField(db_column='Datum') # Field name made lowercase.
    vorgang = models.CharField(max_length=3072, db_column='Vorgang') # Field name made lowercase.
    ergebnis = models.CharField(max_length=3072, db_column='Ergebnis') # Field name made lowercase.
    class Meta:
        db_table = u'WikiDjangoLog'

class Archive(models.Model):
    ar_namespace = models.IntegerField()
    ar_title = models.CharField(max_length=765)
    ar_text = models.TextField()
    ar_comment = models.TextField()
    ar_user = models.IntegerField()
    ar_user_text = models.CharField(max_length=765)
    ar_timestamp = models.CharField(max_length=42)
    ar_minor_edit = models.IntegerField()
    ar_flags = models.TextField()
    ar_rev_id = models.IntegerField(null=True, blank=True)
    ar_text_id = models.IntegerField(null=True, blank=True)
    ar_deleted = models.IntegerField()
    ar_len = models.IntegerField(null=True, blank=True)
    ar_page_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'archive'

class Categorylinks(models.Model):
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    cl_from = models.IntegerField()
    cl_to = models.CharField(max_length=765)
    cl_sortkey = models.CharField(max_length=258)
    cl_timestamp = models.DateTimeField()
    class Meta:
        db_table = u'categorylinks'

class Externallinks(models.Model):
    el_from = models.IntegerField()
    el_to = models.TextField()
    el_index = models.TextField()
    class Meta:
        db_table = u'externallinks'

class Filearchive(models.Model):
    fa_id = models.IntegerField(primary_key=True)
    fa_name = models.CharField(max_length=765)
    fa_archive_name = models.CharField(max_length=765, blank=True)
    fa_storage_group = models.CharField(max_length=48, blank=True)
    fa_storage_key = models.CharField(max_length=192, blank=True)
    fa_deleted_user = models.IntegerField(null=True, blank=True)
    fa_deleted_timestamp = models.CharField(max_length=42, blank=True)
    fa_deleted_reason = models.TextField(blank=True)
    fa_size = models.IntegerField(null=True, blank=True)
    fa_width = models.IntegerField(null=True, blank=True)
    fa_height = models.IntegerField(null=True, blank=True)
    fa_metadata = models.TextField(blank=True)
    fa_bits = models.IntegerField(null=True, blank=True)
    fa_media_type = models.CharField(max_length=30, blank=True)
    fa_major_mime = models.CharField(max_length=33, blank=True)
    fa_minor_mime = models.CharField(max_length=96, blank=True)
    fa_description = models.TextField(blank=True)
    fa_user = models.IntegerField(null=True, blank=True)
    fa_user_text = models.CharField(max_length=765, blank=True)
    fa_timestamp = models.CharField(max_length=42, blank=True)
    fa_deleted = models.IntegerField()
    class Meta:
        db_table = u'filearchive'

class Hitcounter(models.Model):
    hc_id = models.IntegerField()
    class Meta:
        db_table = u'hitcounter'

class Image(models.Model):
    id = models.BigIntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    img_name = models.CharField(unique=True, max_length=765)
    img_size = models.IntegerField()
    img_width = models.IntegerField()
    img_height = models.IntegerField()
    img_metadata = models.TextField()
    img_bits = models.IntegerField()
    img_media_type = models.CharField(max_length=30, blank=True)
    img_major_mime = models.CharField(max_length=33)
    img_minor_mime = models.CharField(max_length=96)
    img_description = models.TextField()
    img_user = models.IntegerField()
    img_user_text = models.CharField(max_length=765)
    img_timestamp = models.CharField(max_length=42)
    img_sha1 = models.CharField(max_length=32)
    class Meta:
        db_table = u'image'

class Imagelinks(models.Model):
    il_from = models.IntegerField()
    il_to = models.CharField(max_length=765)
    class Meta:
        db_table = u'imagelinks'

class Interwiki(models.Model):
    iw_prefix = models.CharField(unique=True, max_length=96)
    iw_url = models.CharField(max_length=381)
    iw_local = models.IntegerField()
    iw_trans = models.IntegerField()
    class Meta:
        db_table = u'interwiki'

class Ipblocks(models.Model):
    ipb_id = models.IntegerField(primary_key=True)
    ipb_address = models.TextField(unique=True)
    ipb_user = models.IntegerField()
    ipb_by = models.IntegerField()
    ipb_reason = models.TextField()
    ipb_timestamp = models.CharField(max_length=14)
    ipb_auto = models.IntegerField(unique=True)
    ipb_anon_only = models.IntegerField()
    ipb_create_account = models.IntegerField()
    ipb_expiry = models.CharField(max_length=14)
    ipb_range_start = models.TextField()
    ipb_range_end = models.TextField()
    ipb_enable_autoblock = models.IntegerField()
    ipb_deleted = models.IntegerField()
    ipb_block_email = models.IntegerField()
    class Meta:
        db_table = u'ipblocks'

class IpblocksOld(models.Model):
    ipb_id = models.IntegerField(primary_key=True)
    ipb_address = models.CharField(max_length=120)
    ipb_user = models.IntegerField()
    ipb_by = models.IntegerField()
    ipb_reason = models.TextField()
    ipb_timestamp = models.CharField(max_length=42)
    ipb_auto = models.IntegerField()
    ipb_expiry = models.CharField(max_length=42)
    ipb_range_start = models.CharField(max_length=96)
    ipb_range_end = models.CharField(max_length=96)
    class Meta:
        db_table = u'ipblocks_old'

class Job(models.Model):
    job_id = models.IntegerField(primary_key=True)
    job_cmd = models.CharField(max_length=765)
    job_namespace = models.IntegerField()
    job_title = models.CharField(max_length=765)
    job_params = models.TextField()
    class Meta:
        db_table = u'job'

class Langlinks(models.Model):
    ll_from = models.IntegerField(unique=True)
    ll_lang = models.CharField(max_length=30)
    ll_title = models.CharField(max_length=765)
    class Meta:
        db_table = u'langlinks'

class Logging(models.Model):
    log_type = models.CharField(max_length=30)
    log_action = models.CharField(max_length=30)
    log_timestamp = models.CharField(max_length=42)
    log_user = models.IntegerField()
    log_namespace = models.IntegerField()
    log_title = models.CharField(max_length=765)
    log_comment = models.CharField(max_length=765)
    log_params = models.TextField()
    log_id = models.IntegerField(primary_key=True)
    log_deleted = models.IntegerField()
    class Meta:
        db_table = u'logging'

class Math(models.Model):
    math_inputhash = models.CharField(unique=True, max_length=48)
    math_outputhash = models.CharField(max_length=48)
    math_html_conservativeness = models.IntegerField()
    math_html = models.TextField(blank=True)
    math_mathml = models.TextField(blank=True)
    class Meta:
        db_table = u'math'

class Objectcache(models.Model):
    keyname = models.CharField(unique=True, max_length=765)
    value = models.TextField(blank=True)
    exptime = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'objectcache'

class Oldimage(models.Model):
    oi_name = models.CharField(max_length=765)
    oi_archive_name = models.CharField(max_length=765)
    oi_size = models.IntegerField()
    oi_width = models.IntegerField()
    oi_height = models.IntegerField()
    oi_bits = models.IntegerField()
    oi_description = models.TextField()
    oi_user = models.IntegerField()
    oi_user_text = models.CharField(max_length=765)
    oi_timestamp = models.CharField(max_length=42)
    oi_metadata = models.TextField()
    oi_media_type = models.CharField(max_length=30, blank=True)
    oi_major_mime = models.CharField(max_length=33)
    oi_minor_mime = models.CharField(max_length=32)
    oi_deleted = models.IntegerField()
    oi_sha1 = models.CharField(max_length=32)
    class Meta:
        db_table = u'oldimage'

class Page(models.Model):
    page_id = models.IntegerField(primary_key=True)
    page_namespace = models.IntegerField(unique=True)
    page_title = models.CharField(unique=True, max_length=765)
    page_restrictions = models.TextField()
    page_counter = models.BigIntegerField()
    page_is_redirect = models.IntegerField()
    page_is_new = models.IntegerField()
    page_random = models.FloatField()
    page_touched = models.CharField(max_length=42)
    page_latest = models.IntegerField()
    page_len = models.IntegerField()
    class Meta:
        db_table = u'page'

class PageRestrictions(models.Model):
    pr_page = models.IntegerField(primary_key=True)
    pr_type = models.CharField(max_length=60)
    pr_level = models.CharField(max_length=60)
    pr_cascade = models.IntegerField()
    pr_user = models.IntegerField(null=True, blank=True)
    pr_expiry = models.CharField(max_length=14, blank=True)
    pr_id = models.IntegerField(unique=True)
    class Meta:
        db_table = u'page_restrictions'

class Pagelinks(models.Model):
    pl_from = models.IntegerField()
    pl_namespace = models.IntegerField()
    pl_title = models.CharField(max_length=765)
    class Meta:
        db_table = u'pagelinks'

class ProtectedTitles(models.Model):
    pt_namespace = models.IntegerField(primary_key=True)
    pt_title = models.CharField(max_length=765, primary_key=True)
    pt_user = models.IntegerField()
    pt_reason = models.TextField(blank=True)
    pt_timestamp = models.CharField(max_length=14)
    pt_expiry = models.CharField(max_length=14)
    pt_create_perm = models.CharField(max_length=60)
    class Meta:
        db_table = u'protected_titles'

class Querycache(models.Model):
    qc_type = models.CharField(max_length=96)
    qc_value = models.IntegerField()
    qc_namespace = models.IntegerField()
    qc_title = models.CharField(max_length=765)
    class Meta:
        db_table = u'querycache'

class QuerycacheInfo(models.Model):
    qci_type = models.CharField(unique=True, max_length=96)
    qci_timestamp = models.CharField(max_length=42)
    class Meta:
        db_table = u'querycache_info'

class Querycachetwo(models.Model):
    qcc_type = models.CharField(max_length=32)
    qcc_value = models.IntegerField()
    qcc_namespace = models.IntegerField()
    qcc_title = models.CharField(max_length=765)
    qcc_namespacetwo = models.IntegerField()
    qcc_titletwo = models.CharField(max_length=765)
    class Meta:
        db_table = u'querycachetwo'

class Recentchanges(models.Model):
    rc_id = models.IntegerField(primary_key=True)
    rc_timestamp = models.CharField(max_length=42)
    rc_cur_time = models.CharField(max_length=42)
    rc_user = models.IntegerField()
    rc_user_text = models.CharField(max_length=765)
    rc_namespace = models.IntegerField()
    rc_title = models.CharField(max_length=765)
    rc_comment = models.CharField(max_length=765)
    rc_minor = models.IntegerField()
    rc_bot = models.IntegerField()
    rc_new = models.IntegerField()
    rc_cur_id = models.IntegerField()
    rc_this_oldid = models.IntegerField()
    rc_last_oldid = models.IntegerField()
    rc_type = models.IntegerField()
    rc_moved_to_ns = models.IntegerField()
    rc_moved_to_title = models.CharField(max_length=765)
    rc_patrolled = models.IntegerField()
    rc_ip = models.CharField(max_length=45)
    rc_old_len = models.IntegerField(null=True, blank=True)
    rc_new_len = models.IntegerField(null=True, blank=True)
    rc_deleted = models.IntegerField()
    rc_logid = models.IntegerField()
    rc_log_type = models.CharField(max_length=255, blank=True)
    rc_log_action = models.CharField(max_length=255, blank=True)
    rc_params = models.TextField(blank=True)
    class Meta:
        db_table = u'recentchanges'

class Redirect(models.Model):
    rd_from = models.IntegerField()
    rd_namespace = models.IntegerField()
    rd_title = models.CharField(max_length=765)
    class Meta:
        db_table = u'redirect'

class Revision(models.Model):
    rev_id = models.IntegerField(unique=True)
    rev_page = models.IntegerField()
    rev_text_id = models.IntegerField()
    rev_comment = models.TextField()
    rev_user = models.IntegerField()
    rev_user_text = models.CharField(max_length=765)
    rev_timestamp = models.CharField(max_length=42)
    rev_minor_edit = models.IntegerField()
    rev_deleted = models.IntegerField()
    rev_len = models.IntegerField(null=True, blank=True)
    rev_parent_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'revision'

class Searchindex(models.Model):
    si_page = models.IntegerField(unique=True)
    si_title = models.CharField(max_length=765)
    si_text = models.TextField()
    class Meta:
        db_table = u'searchindex'

class SiteStats(models.Model):
    ss_row_id = models.IntegerField(unique=True)
    ss_total_views = models.BigIntegerField(null=True, blank=True)
    ss_total_edits = models.BigIntegerField(null=True, blank=True)
    ss_good_articles = models.BigIntegerField(null=True, blank=True)
    ss_total_pages = models.BigIntegerField(null=True, blank=True)
    ss_users = models.BigIntegerField(null=True, blank=True)
    ss_admins = models.IntegerField(null=True, blank=True)
    ss_images = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'site_stats'

class Templatelinks(models.Model):
    tl_from = models.IntegerField()
    tl_namespace = models.IntegerField()
    tl_title = models.CharField(max_length=765)
    class Meta:
        db_table = u'templatelinks'

class Text(models.Model):
    old_id = models.IntegerField(primary_key=True)
    old_text = models.TextField()
    old_flags = models.TextField()
    class Meta:
        db_table = u'text'

class Trackbacks(models.Model):
    tb_id = models.IntegerField(primary_key=True)
    tb_page = models.IntegerField(null=True, blank=True)
    tb_title = models.CharField(max_length=765)
    tb_url = models.CharField(max_length=765)
    tb_ex = models.TextField(blank=True)
    tb_name = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'trackbacks'

class Transcache(models.Model):
    tc_url = models.CharField(unique=True, max_length=765)
    tc_contents = models.TextField(blank=True)
    tc_time = models.IntegerField()
    class Meta:
        db_table = u'transcache'

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(unique=True, max_length=765)
    user_real_name = models.CharField(max_length=765)
    user_password = models.TextField()
    user_newpassword = models.TextField()
    user_email = models.TextField()
    user_options = models.TextField()
    user_touched = models.CharField(max_length=42)
    user_token = models.CharField(max_length=96)
    user_email_authenticated = models.CharField(max_length=42, blank=True)
    user_email_token = models.CharField(max_length=96, blank=True)
    user_email_token_expires = models.CharField(max_length=42, blank=True)
    user_registration = models.CharField(max_length=42, blank=True)
    user_newpass_time = models.CharField(max_length=14, blank=True)
    user_editcount = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'user'

class UserGroups(models.Model):
    ug_user = models.IntegerField(primary_key=True)
    ug_group = models.CharField(max_length=48)
    class Meta:
        db_table = u'user_groups'

class UserNewtalk(models.Model):
    user_id = models.IntegerField()
    user_ip = models.CharField(max_length=120)
    class Meta:
        db_table = u'user_newtalk'

class Watchlist(models.Model):
    wl_user = models.IntegerField(unique=True)
    wl_namespace = models.IntegerField()
    wl_title = models.CharField(max_length=765)
    wl_notificationtimestamp = models.CharField(max_length=42, blank=True)
    class Meta:
        db_table = u'watchlist'

