from modeltranslation.translator import translator, TranslationOptions, register
from .models.scientific_activity_models import (ScientificActivityContent,
                                                ScientificActivity, Document)
from .models.about_us_models import (AboutUs,
                                     History,
                                     Charter,
                                     Directorate)
from .models.banners_model import Banner
from .models.blocks_and_departments_model import Block, Department
from .models.general_structure_model import GeneralStructure
from .models.counters_model import Counter
from .models.contacts_model import Contacts, SocialMedia
from .models.resources_model import Journal, Report, Link


class JournalTranslationOptions(TranslationOptions):
    fields = ['title']

class LinkTranslationOptions(TranslationOptions):
    fields = ['title']

class ReportTranslationOptions(TranslationOptions):
    fields = ['title']

class DocumentTranslationOptions(TranslationOptions):
    fields = ['title']

class CounterTranslationOptions(TranslationOptions):
    fields = 'title'.split()

class ContactsTranslationOptions(TranslationOptions):
    fields = ['title', 'text']
    
class SocialMediaTranslationOptions(TranslationOptions):
    fields = ['title']

class CharterTranslationOptions(TranslationOptions):
    fields = ['title']

class AboutUsTranslationOptions(TranslationOptions):
    fields = ['description']

class HistoryTranslationOptions(TranslationOptions):
    fields = ['description']

class ScientificActivityTranslationOptions(TranslationOptions):
    fields = 'title'.split()

class ScientificActivityContentTranslationOptions(TranslationOptions):
    fields = ['title_content', 'text_content']

class BannerTranslationOptions(TranslationOptions):
    fields = ['title', 'text']

@register(Block)
class BlockTranslationOptions(TranslationOptions):
    fields = ('title',) 

class DepartmentTranslationOptions(TranslationOptions):
    fields = ('name','description') 

class GeneralStructureTranslationOptions(TranslationOptions):
    fields = ('title','description')

class DirectorateTranslationOptions(TranslationOptions):
    fields = ('name', 'description',  )


translator.register(GeneralStructure, GeneralStructureTranslationOptions)
translator.register(Department, DepartmentTranslationOptions) 
translator.register(Banner, BannerTranslationOptions)
# translator.register(Block, BlockTranslationOptions)
translator.register(ScientificActivity, ScientificActivityTranslationOptions)
translator.register(ScientificActivityContent, ScientificActivityContentTranslationOptions)
translator.register(Document, DocumentTranslationOptions)
translator.register(AboutUs, AboutUsTranslationOptions)
translator.register(History, HistoryTranslationOptions)
translator.register(Counter, CounterTranslationOptions)
translator.register(Contacts, ContactsTranslationOptions)
translator.register(SocialMedia, SocialMediaTranslationOptions)
translator.register(Directorate, DirectorateTranslationOptions)
translator.register(Link, LinkTranslationOptions)
translator.register(Report, ReportTranslationOptions)
translator.register(Journal, JournalTranslationOptions)
translator.register(Charter, CharterTranslationOptions)

