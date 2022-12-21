from django import forms
from django.contrib import admin
from django.db import transaction
from django.core.exceptions import ValidationError

from admin_app.models import Infoblock, News, Offer, Promocode


class InfoblockCreationForm(forms.ModelForm):
    class Meta:
        model = Infoblock
        fields = ('header', 'main')


class InfoblockChangeForm(forms.ModelForm):
    class Meta:
        model = Infoblock
        fields = ('header', 'main')


class InfoblockAdmin(admin.ModelAdmin):
    form = InfoblockChangeForm
    add_form = InfoblockCreationForm

    list_display = ('header',)
    list_filter = ('header',)
    fieldsets = (
        (None, {'fields': ('header', 'main')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('header', 'main'),
        }),
    )
    search_fields = ('header',)
    ordering = ('header',)
    filter_horizontal = ()

    def has_module_permission(self, request):
        return not request.user.is_anonymous and request.user.is_content_maker_type

    def get_queryset(self, request):
        return super().get_queryset(request).filter(
            infoblockid__in=News.objects.filter(customerid=request.user.customerid).values('infoblockid')
        )

    def save_model(self, request, obj, form, change):
        with transaction.atomic():
            super().save_model(request, obj, form, change)
            News.objects.create(customerid=request.user, infoblockid=obj)


class PromocodeCreationForm(forms.ModelForm):
    class Meta:
        model = Promocode
        fields = ('promocodevalue', 'discount', 'trackid', 'usecount')

    def clean_usecount(self):
        usecount = self.cleaned_data.get("usecount")
        if usecount < 0:
            raise ValidationError("Amount of usages must be a positive integer")
        return usecount

    def clean_discount(self):
        discount = self.cleaned_data.get("discount")
        if discount < 0 or discount > 100:
            raise ValidationError("Discount takes any value in range [0, 100]")
        return discount


class PromocodeChangeForm(forms.ModelForm):
    class Meta:
        model = Promocode
        fields = ('promocodevalue', 'discount', 'trackid', 'usecount')


class PromocodeAdmin(admin.ModelAdmin):
    form = PromocodeCreationForm
    add_form = PromocodeCreationForm

    list_display = ('promocodevalue', 'discount', 'trackid', 'usecount')
    list_filter = ('promocodevalue', 'discount', 'trackid', 'usecount')
    fieldsets = (
        (None, {'fields': ('promocodevalue', 'discount', 'trackid', 'usecount')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('promocodevalue', 'discount', 'trackid', 'usecount'),
        }),
    )
    search_fields = ('promocodevalue', 'discount', 'trackid', 'usecount')
    ordering = ('promocodevalue', 'discount', 'trackid', 'usecount')
    filter_horizontal = ()

    def has_module_permission(self, request):
        return not request.user.is_anonymous and request.user.is_content_maker_type


class OfferCreationForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ('promocodeid', 'infoblockid')


class OfferChangeForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ('promocodeid', 'infoblockid')


class OfferAdmin(admin.ModelAdmin):
    form = OfferChangeForm
    add_form = PromocodeCreationForm

    list_display = ('promocodeid', 'infoblockid')
    list_filter = ('promocodeid', 'infoblockid')
    fieldsets = (
        (None, {'fields': ('promocodeid', 'infoblockid')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('promocodeid', 'infoblockid'),
        }),
    )
    search_fields = ('promocodeid', 'infoblockid')
    ordering = ('promocodeid', 'infoblockid')
    filter_horizontal = ()

    def has_module_permission(self, request):
        return not request.user.is_anonymous and request.user.is_content_maker_type