from django import forms
from django.contrib import admin, messages
from modeltranslation.admin import TranslationAdmin, TabbedTranslationAdmin, TranslationStackedInline
from django.contrib.auth.models import User, Group
from .models.counters_model import Counter
from .models.contacts_model import Contacts, SocialMedia
from .models.banners_model import Banner
from .models.blocks_and_departments_model import Block, Department
from .models.general_structure_model import GeneralStructure
from .models.scientific_activity_models import (ScientificActivity,
                                                ScientificActivityContent, Document)
from .models.about_us_models import (AboutNCOMID,
                                     AboutUs,
                                     Charter,
                                     Directorate,
                                     History)
from .models.resources_model import (Report,
                                     Journal,
                                     Link,
                                     Resource)
from .services import TranslatorMediaMixin


class ScientificActivityContentInline(TranslationStackedInline, TranslatorMediaMixin):
    model = ScientificActivityContent
    extra = 1


class HistoryInline(TranslationStackedInline, TranslatorMediaMixin):
    model = History
    extra = 1
    max_num = 1


class AboutUsInline(TranslationStackedInline, TranslatorMediaMixin):
    model = AboutUs
    extra = 1
    max_num = 1


class CharterInline(TranslationStackedInline, TranslatorMediaMixin):
    model = Charter
    extra = 1


class DirectorateInline(TranslationStackedInline, TranslatorMediaMixin):
    model = Directorate
    extra = 1
    max_num = 1


class AboutNCOMIDForm(forms.ModelForm):
    Информация = forms.CharField(max_length=255,
                                 required=False,
                                 disabled=True,
                                 initial='Информация страницы Все об НЦОМиД')

    class Meta:
        model = AboutNCOMID
        fields = '__all__'


@admin.register(AboutNCOMID)
class AboutNCOMIDAdmin(admin.ModelAdmin):
    form = AboutNCOMIDForm
    inlines = [HistoryInline, AboutUsInline, CharterInline, DirectorateInline]
    exclude = ('',)

    def has_add_permission(self, request):
        if AboutNCOMID.objects.all().count() == 1:
            return False
        return True


class RecourseForm(forms.ModelForm):
    Информация = forms.CharField(max_length=255,
                                 required=False,
                                 disabled=True,
                                 initial='Информация страницы Ресурсы')

    class Meta:
        model = Resource
        fields = '__all__'


class JournalInline(TranslationStackedInline, TranslatorMediaMixin):
    model = Journal
    extra = 1
    max_num = 20


class ReportInline(TranslationStackedInline, TranslatorMediaMixin):
    model = Report
    extra = 1
    max_num = 20


class LinkInline(TranslationStackedInline, TranslatorMediaMixin):
    model = Link
    extra = 1
    max_num = 20


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    form = RecourseForm
    inlines = [JournalInline, ReportInline, LinkInline]
    exclude = ('',)

    def has_add_permission(self, request):
        if Resource.objects.all().count() == 1:
            return False
        return True


class ScientificActivityAdmin(TranslatorMediaMixin, TabbedTranslationAdmin):
    def has_add_permission(self, request):
        if ScientificActivity.objects.all().count() == 4:
            return False
        return True

    inlines = [ScientificActivityContentInline]


class DocumentAdmin(TranslatorMediaMixin, TranslationAdmin):
    pass


class CounterAdmin(TranslatorMediaMixin, TranslationAdmin):
    def has_add_permission(self, request):
        if Counter.objects.all().count() == 4:
            return False
        return True

    def save_model(self, request, obj, form, change):
        if Counter.objects.count() >= 4 and not change:
            self.message_user(request, 'Вы не можете добавлять более 1 счетчика, вы можете только изменять существующий счетчик.', level=messages.ERROR)
            return
        super().save_model(request, obj, form, change)


class ContactsAdmin(TranslatorMediaMixin, TranslationAdmin):
    def has_add_permission(self, request):
        if Contacts.objects.all().count() == 5:
            return False
        return True

    def save_model(self, request, obj, form, change):
        if Contacts.objects.count() >= 5 and not change:
            self.message_user(request, 'Вы не можете добавлять более 5 контакт, вы можете только изменять существующий контакт.', level=messages.ERROR)
            return
        super().save_model(request, obj, form, change)


class SocialMediaAdmin(TranslatorMediaMixin, TranslationAdmin):
    def has_add_permission(self, request):
        if SocialMedia.objects.all().count() == 3:
            return False
        return True

    def save_model(self, request, obj, form, change):
        if SocialMedia.objects.count() >= 3 and not change:
            self.message_user(request, 'Вы не можете добавлять более 3 социальных сетей, вы можете только изменять существующий социальные сети.', level=messages.ERROR)
            return
        super().save_model(request, obj, form, change)


class BannerAdmin(TranslatorMediaMixin, TranslationAdmin):
    def has_add_permission(self, request):
        if Banner.objects.all().count() == 1:
            return False
        return True

    def save_model(self, request, obj, form, change):
        if Banner.objects.count() >= 1 and not change:
            self.message_user(request, 'Вы не можете добавлять более 1 баннер, вы можете только изменять существующие баннеры.', level=messages.ERROR)
            return
        super().save_model(request, obj, form, change)


class BlockAdmin(TranslatorMediaMixin, TranslationAdmin):
    def has_add_permission(self, request):
        if Block.objects.all().count() == 4:
            return False
        return True
    def save_model(self, request, obj, form, change):
        if change:
            Department.objects.filter(block=obj).delete()

        if Block.objects.count() >= 4 and not change:
            self.message_user(request, "Вы не можете добавлять более 4 блоков, вы можете только изменить существующие блоки.", level=messages.ERROR)
        else:
            super().save_model(request, obj, form, change)


class DepartmentAdmin(TranslatorMediaMixin, TranslationAdmin):
    pass


class GeneralStructureAdmin(TranslatorMediaMixin, TranslationAdmin):
    def has_add_permission(self, request):
        if GeneralStructure.objects.all().count() == 4:
            return False
        return True

    def save_model(self, request, obj, form, change):
        if GeneralStructure.objects.count() >= 4 and not change:
            self.message_user(request, "Вы не можете добавлять более 4 блоков, вы можете только изменить существующие блоки.", level=messages.ERROR)
        else:
            super().save_model(request, obj, form, change)


admin.site.register(Block, BlockAdmin)
admin.site.register(GeneralStructure, GeneralStructureAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Counter, CounterAdmin)
admin.site.register(ScientificActivity, ScientificActivityAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)
