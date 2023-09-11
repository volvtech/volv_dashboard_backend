# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Articletimestamp(models.Model):
    id = models.IntegerField(primary_key=True)
    article_id = models.IntegerField(blank=True, null=True)
    time_ago = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ArticleTimeStamp'


class ArticleAuthorHistories(models.Model):
    id = models.BigAutoField(primary_key=True)
    article_id = models.IntegerField()
    user_id = models.IntegerField()
    article_heading = models.TextField()
    article_summary = models.TextField()
    created_at = models.TextField()
    updated_at = models.TextField()
    article_status = models.CharField(max_length=45)
    notification_text = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article_author_histories'


class ArticleAuthorSummaries(models.Model):
    id = models.BigAutoField(primary_key=True)
    article_id = models.IntegerField()
    author_id = models.IntegerField()
    article_status = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article_author_summaries'


class ArticleBias(models.Model):
    id = models.BigAutoField(primary_key=True)
    article_id = models.IntegerField()
    left_bias = models.CharField(max_length=255, blank=True, null=True)
    right_bias = models.CharField(max_length=255, blank=True, null=True)
    center_bias = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article_bias'


class ArticleBiasedSentences(models.Model):
    id = models.BigAutoField(primary_key=True)
    article_id = models.IntegerField(blank=True, null=True)
    biased_sentence = models.TextField(blank=True, null=True)
    biased_type = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article_biased_sentences'


class ArticleBreakingNews(models.Model):
    id = models.BigAutoField(primary_key=True)
    article_id = models.IntegerField()
    breaking_news_period = models.IntegerField()
    article_visited = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article_breaking_news'


class ArticleCategories(models.Model):
    id = models.BigAutoField(primary_key=True)
    category_title = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article_categories'


class ArticleDeleteProofs(models.Model):
    id = models.BigAutoField(primary_key=True)
    article_id = models.IntegerField()
    uid = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    article_heading = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article_delete_proofs'


class ArticleHashtags(models.Model):
    id = models.BigAutoField(primary_key=True)
    category_ids = models.CharField(max_length=255, blank=True, null=True)
    sub_category = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    left_color = models.CharField(max_length=45, blank=True, null=True)
    right_color = models.CharField(max_length=45, blank=True, null=True)
    is_available = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article_hashtags'


class ArticlePolls(models.Model):
    id = models.BigAutoField(primary_key=True)
    article_id = models.IntegerField()
    poll_question = models.TextField()
    option1 = models.TextField()
    option2 = models.TextField()
    poll_image = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    left_color = models.CharField(max_length=255, blank=True, null=True)
    right_color = models.CharField(max_length=255, blank=True, null=True)
    poll_published = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article_polls'


class ArticlePublishTimes(models.Model):
    id = models.BigAutoField(primary_key=True)
    article_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    article_publish_time = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article_publish_times'


class ArticleSentenceBias(models.Model):
    id = models.BigAutoField(primary_key=True)
    article_heading = models.TextField(blank=True, null=True)
    article_sentence = models.TextField(blank=True, null=True)
    bias_type = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article_sentence_bias'


class ArticleStatuses(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article_statuses'


class Articles(models.Model):
    id = models.BigAutoField(primary_key=True)
    article_heading = models.CharField(max_length=200)
    article_summary = models.CharField(max_length=500)
    article_author = models.CharField(max_length=255)
    main_source = models.TextField()
    additional_sources = models.TextField(blank=True, null=True)
    article_image = models.TextField(blank=True, null=True)
    article_category = models.CharField(max_length=255)
    article_keywords = models.TextField(blank=True, null=True)
    targetting_states = models.TextField(blank=True, null=True)
    left_color = models.CharField(max_length=255, blank=True, null=True)
    right_color = models.CharField(max_length=255, blank=True, null=True)
    publish_article = models.CharField(max_length=255)
    article_status = models.CharField(max_length=255)
    article_priority = models.CharField(max_length=255, blank=True, null=True)
    button_class = models.CharField(max_length=255, blank=True, null=True)
    priority_button_class = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    priority_class = models.CharField(max_length=255, blank=True, null=True)
    time_ago = models.CharField(max_length=255, blank=True, null=True)
    notification_text = models.TextField(blank=True, null=True)
    notification_sent_status = models.CharField(max_length=45, blank=True, null=True)
    trending_news = models.CharField(max_length=45, blank=True, null=True)
    breaking_news = models.CharField(max_length=45, blank=True, null=True)
    article_bias = models.CharField(max_length=45, blank=True, null=True)
    additional_source_bias = models.CharField(max_length=45, blank=True, null=True)
    is_embed_link = models.CharField(max_length=10, blank=True, null=True)
    read_more_text = models.CharField(max_length=45, blank=True, null=True)
    read_more_text_color = models.CharField(max_length=45, blank=True, null=True)
    article_subcategories = models.CharField(max_length=45, blank=True, null=True)
    likes_count = models.BigIntegerField()
    comments_count = models.BigIntegerField()
    article_publisher = models.BigIntegerField()
    article_video_url = models.TextField(blank=True, null=True)
    pop_score = models.FloatField(blank=True, null=True)
    article_video_validity_checked = models.CharField(max_length=45, blank=True, null=True)
    auto_likes_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'articles'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Authors(models.Model):
    id = models.BigAutoField(primary_key=True)
    author_name = models.CharField(max_length=255)
    author_email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'authors'


class Categories(models.Model):
    id = models.BigAutoField(primary_key=True)
    category_title = models.CharField(max_length=255)
    category_image_path = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_available = models.CharField(max_length=10, blank=True, null=True)
    left_color = models.CharField(max_length=45, blank=True, null=True)
    right_color = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'


class Digs(models.Model):
    id = models.BigAutoField(primary_key=True)
    dig_title = models.CharField(max_length=255)
    dig_body = models.TextField()
    dig_image_path = models.CharField(max_length=255)
    dig_author = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'digs'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Feedback(models.Model):
    id = models.BigAutoField(primary_key=True)
    documentid = models.CharField(db_column='documentId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    article_id = models.IntegerField(blank=True, null=True)
    feedback_title = models.TextField()
    feedback_type = models.CharField(max_length=255, blank=True, null=True)
    feedback_body = models.TextField(blank=True, null=True)
    options_count = models.CharField(max_length=45, blank=True, null=True)
    option1 = models.TextField(blank=True, null=True)
    option2 = models.TextField(blank=True, null=True)
    option3 = models.TextField(blank=True, null=True)
    slider_min = models.CharField(max_length=255, blank=True, null=True)
    slider_max = models.CharField(max_length=255, blank=True, null=True)
    slider_stops = models.IntegerField(blank=True, null=True)
    feedback_image = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    left_color = models.CharField(max_length=255, blank=True, null=True)
    right_color = models.CharField(max_length=255, blank=True, null=True)
    feedback_published = models.CharField(max_length=45, blank=True, null=True)
    has_slides = models.CharField(max_length=45, blank=True, null=True)
    slides_count = models.IntegerField(blank=True, null=True)
    slides = models.CharField(max_length=255, blank=True, null=True)
    option4 = models.CharField(max_length=45, blank=True, null=True)
    option5 = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feedback'


class FeedbackResults(models.Model):
    uid = models.IntegerField(blank=True, null=True)
    feedback_id = models.CharField(max_length=45, blank=True, null=True)
    feedbackid = models.BigIntegerField(db_column='feedbackId', blank=True, null=True)  # Field name made lowercase.
    documentid = models.CharField(db_column='documentId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    disabled = models.CharField(max_length=10, blank=True, null=True)
    slide_id = models.CharField(max_length=45, blank=True, null=True)
    user_id = models.CharField(max_length=45, blank=True, null=True)
    feedback_type = models.CharField(max_length=45, blank=True, null=True)
    feedback_answer = models.CharField(max_length=1000, blank=True, null=True)
    option_selected = models.TextField(blank=True, null=True)
    slider_value = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feedback_results'


class FeedbackSlides(models.Model):
    id = models.BigAutoField(primary_key=True)
    feedback_title = models.TextField()
    feedback_type = models.CharField(max_length=255, blank=True, null=True)
    feedback_body = models.TextField(blank=True, null=True)
    options_count = models.CharField(max_length=45, blank=True, null=True)
    option1 = models.TextField(blank=True, null=True)
    option2 = models.TextField(blank=True, null=True)
    option3 = models.TextField(blank=True, null=True)
    slider_min = models.CharField(max_length=255, blank=True, null=True)
    slider_max = models.CharField(max_length=255, blank=True, null=True)
    slider_stops = models.IntegerField(blank=True, null=True)
    feeback_image = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    left_color = models.CharField(max_length=255, blank=True, null=True)
    right_color = models.CharField(max_length=255, blank=True, null=True)
    option4 = models.CharField(max_length=45, blank=True, null=True)
    option5 = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feedback_slides'


class GoogleTrendsArticles(models.Model):
    article_title = models.CharField(max_length=200, blank=True, null=True)
    article_url = models.CharField(max_length=200, blank=True, null=True)
    article_source = models.CharField(max_length=200, blank=True, null=True)
    article_category = models.CharField(max_length=200, blank=True, null=True)
    article_pubilsh_time = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'google_trends_articles'


class GoogleTrendsArticlesBusiness(models.Model):
    article_title = models.CharField(max_length=200, blank=True, null=True)
    article_url = models.CharField(max_length=200, blank=True, null=True)
    article_source = models.CharField(max_length=200, blank=True, null=True)
    article_category = models.CharField(max_length=200, blank=True, null=True)
    article_pubilsh_time = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'google_trends_articles_business'


class GoogleTrendsArticlesEntertainment(models.Model):
    article_title = models.CharField(max_length=200, blank=True, null=True)
    article_url = models.CharField(max_length=200, blank=True, null=True)
    article_source = models.CharField(max_length=200, blank=True, null=True)
    article_category = models.CharField(max_length=200, blank=True, null=True)
    article_pubilsh_time = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'google_trends_articles_entertainment'


class GoogleTrendsArticlesHealth(models.Model):
    article_title = models.CharField(max_length=200, blank=True, null=True)
    article_url = models.CharField(max_length=200, blank=True, null=True)
    article_source = models.CharField(max_length=200, blank=True, null=True)
    article_category = models.CharField(max_length=200, blank=True, null=True)
    article_pubilsh_time = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'google_trends_articles_health'


class GoogleTrendsArticlesSciNTech(models.Model):
    article_title = models.CharField(max_length=200, blank=True, null=True)
    article_url = models.CharField(max_length=200, blank=True, null=True)
    article_source = models.CharField(max_length=200, blank=True, null=True)
    article_category = models.CharField(max_length=200, blank=True, null=True)
    article_pubilsh_time = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'google_trends_articles_sci_n_tech'


class GoogleTrendsArticlesSports(models.Model):
    article_title = models.CharField(max_length=200, blank=True, null=True)
    article_url = models.CharField(max_length=200, blank=True, null=True)
    article_source = models.CharField(max_length=200, blank=True, null=True)
    article_category = models.CharField(max_length=200, blank=True, null=True)
    article_pubilsh_time = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'google_trends_articles_sports'


class GoogleTrendsArticlesTopStories(models.Model):
    article_title = models.CharField(max_length=200, blank=True, null=True)
    article_url = models.CharField(max_length=200, blank=True, null=True)
    article_source = models.CharField(max_length=200, blank=True, null=True)
    article_category = models.CharField(max_length=200, blank=True, null=True)
    article_pubilsh_time = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'google_trends_articles_top_stories'


class Migrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class NotificationAuthorSummaries(models.Model):
    id = models.BigAutoField(primary_key=True)
    article_id = models.IntegerField()
    author_id = models.IntegerField()
    notification_text = models.CharField(max_length=255)
    notffication_status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    notification_sent_count = models.IntegerField(blank=True, null=True)
    notification_failure_count = models.CharField(max_length=45, blank=True, null=True)
    invalid_count = models.CharField(max_length=45, blank=True, null=True)
    not_registered_count = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notification_author_summaries'


class NotificationOpens(models.Model):
    id = models.BigAutoField(primary_key=True)
    app_user_id = models.IntegerField()
    article_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notification_opens'


class NotificationStatusEachUsers(models.Model):
    id = models.BigAutoField(primary_key=True)
    article_heading = models.TextField()
    app_username = models.CharField(max_length=255)
    sent_status = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    article_image = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notification_status_each_users'


class NotificationTemp(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notification_temp'


class PasswordResets(models.Model):
    email = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_resets'


class PollResults(models.Model):
    poll_id = models.CharField(max_length=45, blank=True, null=True)
    user_id = models.CharField(max_length=45, blank=True, null=True)
    option_selected = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'poll_results'


class Publishers(models.Model):
    id = models.BigAutoField(primary_key=True)
    publisher_title = models.CharField(max_length=255, blank=True, null=True)
    publisher_image_path = models.CharField(max_length=255, blank=True, null=True)
    publisher_content = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_available = models.CharField(max_length=10, blank=True, null=True)
    left_color = models.CharField(max_length=45, blank=True, null=True)
    right_color = models.CharField(max_length=45, blank=True, null=True)
    order_id = models.IntegerField(blank=True, null=True)
    article_publish_time = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'publishers'


class RepublishableArticles(models.Model):
    id = models.BigAutoField(primary_key=True)
    article_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'republishable_articles'


class RssPoliticsNews(models.Model):
    id = models.BigAutoField(primary_key=True)
    article_title = models.TextField()
    article_description = models.TextField()
    published_date = models.TextField()
    main_source = models.TextField()
    image_url = models.TextField()
    source_name = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rss_politics_news'


class RssUsNews(models.Model):
    id = models.BigAutoField(primary_key=True)
    article_title = models.TextField()
    article_description = models.TextField()
    published_date = models.TextField()
    main_source = models.TextField()
    image_url = models.TextField()
    source_name = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rss_us_news'


class RssWorldNews(models.Model):
    id = models.BigAutoField(primary_key=True)
    article_title = models.TextField()
    article_description = models.TextField()
    published_date = models.TextField()
    main_source = models.TextField()
    image_url = models.TextField()
    source_name = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rss_world_news'


class SaveBreakingNewsTokens(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    fcm_token = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'save_breaking_news_tokens'


class SponsoredArticles(models.Model):
    article = models.ForeignKey(Articles, models.DO_NOTHING)
    weight = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sponsored_articles'


class States(models.Model):
    id = models.BigAutoField(primary_key=True)
    state_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'states'


class SubscriptionPaymentTypes(models.Model):
    type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscription_payment_types'


class SubscriptionPlans(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    description = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscription_plans'


class SubscriptionPricing(models.Model):
    plan = models.ForeignKey(SubscriptionPlans, models.DO_NOTHING, blank=True, null=True)
    type = models.ForeignKey(SubscriptionPaymentTypes, models.DO_NOTHING, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscription_pricing'


class SubscriptionPromoCodes(models.Model):
    pricing = models.ForeignKey(SubscriptionPricing, models.DO_NOTHING, blank=True, null=True)
    promo_code = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscription_promo_codes'


class Subscriptions(models.Model):
    uid = models.PositiveBigIntegerField(unique=True, blank=True, null=True)
    pricing = models.ForeignKey(SubscriptionPricing, models.DO_NOTHING, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    payment_status = models.IntegerField(blank=True, null=True)
    is_trial = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscriptions'


class TrendingArticles(models.Model):
    id = models.BigAutoField(primary_key=True)
    article_heading = models.CharField(max_length=255)
    main_source = models.CharField(max_length=255)
    article_image = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trending_articles'


class TrendingCategories(models.Model):
    id = models.BigAutoField(primary_key=True)
    trending_title = models.CharField(max_length=255)
    trending_category_image = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trending_categories'


class TrendingSaveArticles(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    main_source = models.TextField(blank=True, null=True)
    url_to_image = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    publishedat = models.CharField(db_column='publishedAt', max_length=255, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trending_save_articles'


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=255)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    role = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class VolvAppUsers(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    date_of_registration = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    fcm_token = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'volv_app_users'


class WeekendArticles(models.Model):
    id = models.BigAutoField(primary_key=True)
    article_id = models.IntegerField()
    publish_datetime = models.DateTimeField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weekend_articles'
