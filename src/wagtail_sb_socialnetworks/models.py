from django.db import models
from django.utils.translation import gettext_lazy as _
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.core.models import Orderable
from wagtail.images import get_image_model_string
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet

IMAGE_MODEL = get_image_model_string()


@register_snippet
class SocialNetwork(models.Model):
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=63,
    )
    icon = models.ForeignKey(
        IMAGE_MODEL,
        verbose_name=_("Icon"),
        on_delete=models.CASCADE,
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("name"),
                ImageChooserPanel("icon"),
            ],
            heading=_("Social network"),
        )
    ]

    class Meta:
        app_label = "wagtail_sb_socialnetworks"
        verbose_name = _("Social network")
        verbose_name_plural = _("Social networks")

    def __str__(self):
        return self.name


@register_snippet
class SocialNetworkProfile(models.Model):
    social_network = models.ForeignKey(
        "wagtail_sb_socialnetworks.SocialNetwork",
        verbose_name=_("Social network"),
        on_delete=models.CASCADE,
    )
    profile_url = models.URLField(
        verbose_name=_("Profile URL"),
        max_length=200,
    )

    panels = [
        MultiFieldPanel(
            [
                SnippetChooserPanel("social_network"),
                FieldPanel("profile_url"),
            ],
            heading=_("Social network profile"),
        )
    ]

    class Meta:
        app_label = "wagtail_sb_socialnetworks"
        verbose_name = _("Social network profile")
        verbose_name_plural = _("Social network profiles")

    def __str__(self):
        return f"{self.social_network}: {self.profile_url}"


@register_setting
class SocialNetworkSettings(ClusterableModel, BaseSetting):
    panels = [
        InlinePanel("site_socialnetworks", label=_("Social network profiles")),
    ]

    class Meta:
        app_label = "wagtail_sb_socialnetworks"


class SiteSocialNetworkProfile(Orderable):
    sitesettings = ParentalKey(
        "wagtail_sb_socialnetworks.SocialNetworkSettings",
        verbose_name=_("Site settings"),
        on_delete=models.CASCADE,
        related_name="site_socialnetworks",
        related_query_name="site_socialnetwork",
    )
    profile = models.ForeignKey(
        "wagtail_sb_socialnetworks.SocialNetworkProfile",
        verbose_name=_("Social network profile"),
        on_delete=models.CASCADE,
        related_name="+",
    )

    panels = [
        FieldPanel("sitesettings"),
        SnippetChooserPanel("profile"),
    ]

    class Meta:
        unique_together = ("sitesettings", "profile")
