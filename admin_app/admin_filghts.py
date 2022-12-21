from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError

from admin_app.models import Airport, Track, Seatsuite, Flight


class AirportCreationForm(forms.ModelForm):
    countrycode = forms.ChoiceField(choices=Airport.COUNTRY_CODES)

    class Meta:
        model = Airport
        fields = ('airportname', 'cityname', 'countrycode')


class AirportChangeForm(forms.ModelForm):
    countrycode = forms.ChoiceField(choices=Airport.COUNTRY_CODES)

    class Meta:
        model = Airport
        fields = ('cityname', 'countrycode')


class AirportAdmin(admin.ModelAdmin):
    form = AirportChangeForm
    add_form = AirportCreationForm

    list_display = ('airportname', 'countrycode')
    list_filter = ('airportname', 'cityname')
    fieldsets = (
        (None, {'fields': ('airportname', 'cityname', 'countrycode')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('cityname', 'countrycode'),
        }),
    )
    search_fields = ('airportname', 'cityname',)
    ordering = ('airportname', 'cityname',)
    filter_horizontal = ()

    def has_module_permission(self, request):
        return not request.user.is_anonymous and request.user.is_flight_worker_type


class TrackCreationForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ('startairport', 'endairport', 'isinwheel')


class TrackChangeForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ('startairport', 'endairport', 'isinwheel')


class TrackAdmin(admin.ModelAdmin):
    form = TrackChangeForm
    add_form = TrackCreationForm

    list_display = ('startairport', 'endairport', 'isinwheel')
    list_filter = ('startairport', 'endairport', 'isinwheel')
    fieldsets = (
        (None, {'fields': ('startairport', 'endairport', 'isinwheel')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('startairport', 'endairport', 'isinwheel'),
        }),
    )
    search_fields = ('startairport', 'endairport', 'isinwheel')
    ordering = ('startairport', 'endairport', 'isinwheel')
    filter_horizontal = ()

    def has_module_permission(self, request):
        return not request.user.is_anonymous and request.user.is_flight_worker_type


class SeatsuiteCreationForm(forms.ModelForm):
    class Meta:
        model = Seatsuite
        fields = ('economytotal', 'firstclasstotal', 'luxtotal')


class SeatsuiteChangeForm(forms.ModelForm):
    class Meta:
        model = Seatsuite
        fields = ('economytotal', 'firstclasstotal', 'luxtotal')

    def clean_economytotal(self):
        economytotal = self.cleaned_data.get("economytotal")
        economyreserved = self.cleaned_data.get("economyreserved")
        if economytotal < economyreserved:
            raise ValidationError("Economy total must exceed economy reserved value")
        return economytotal

    def clean_firstclasstotal(self):
        firstclasstotal = self.cleaned_data.get("firstclasstotal")
        firstclassreserved = self.cleaned_data.get("firstclassreserved")
        if firstclasstotal < firstclassreserved:
            raise ValidationError("1-st class total must exceed 1-st class reserved value")
        return firstclasstotal

    def clean_luxtotal(self):
        luxtotal = self.cleaned_data.get("luxtotal")
        luxreserved = self.cleaned_data.get("luxreserved")
        if luxtotal < luxreserved:
            raise ValidationError("Lux total must exceed lux reserved value")
        return luxtotal


class SeatsuiteAdmin(admin.ModelAdmin):
    form = TrackChangeForm
    add_form = TrackCreationForm

    list_display = (
        'economytotal', 'firstclasstotal', 'luxtotal', 'economyreserved', 'firstclassreserved', 'luxreserved')
    list_filter = (
        'economytotal', 'firstclasstotal', 'luxtotal', 'economyreserved', 'firstclassreserved', 'luxreserved')
    fieldsets = (
        (None, {'fields': ('economytotal', 'firstclasstotal', 'luxtotal')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('economytotal', 'firstclasstotal', 'luxtotal'),
        }),
    )
    search_fields = ('economytotal', 'firstclasstotal', 'luxtotal')
    ordering = ('economytotal', 'firstclasstotal', 'luxtotal')
    filter_horizontal = ()

    def has_module_permission(self, request):
        return not request.user.is_anonymous and request.user.is_flight_worker_type


class FlightCreationForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ('departuretime', 'arrivaltime', 'seatsuiteid', 'trackid', 'economycost', 'firstclasscost', 'luxcost')

    def clean(self):
        arrivaltime = self.cleaned_data.get("arrivaltime")
        departuretime = self.cleaned_data.get("departuretime")
        if arrivaltime <= departuretime:
            raise ValidationError("Incorrect time.")
        return self.cleaned_data


class FlightChangeForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ('departuretime', 'arrivaltime', 'trackid', 'economycost', 'firstclasscost', 'luxcost')


class FlightAdmin(admin.ModelAdmin):
    form = FlightCreationForm
    add_form = FlightCreationForm

    list_display = (
        'departuretime', 'arrivaltime', 'seatsuiteid', 'trackid', 'economycost', 'firstclasscost', 'luxcost')
    list_filter = ('departuretime', 'arrivaltime', 'seatsuiteid', 'trackid', 'economycost', 'firstclasscost', 'luxcost')
    fieldsets = (
        (None, {'fields': (
            'departuretime', 'arrivaltime', 'trackid', 'seatsuiteid', 'economycost', 'firstclasscost', 'luxcost')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'departuretime', 'arrivaltime', 'seatsuiteid', 'trackid', 'economycost', 'firstclasscost', 'luxcost'),
        }),
    )
    search_fields = (
        'departuretime', 'arrivaltime', 'seatsuiteid', 'trackid', 'economycost', 'firstclasscost', 'luxcost')
    ordering = ('departuretime', 'arrivaltime', 'seatsuiteid', 'trackid', 'economycost', 'firstclasscost', 'luxcost')
    filter_horizontal = ()

    def has_module_permission(self, request):
        return not request.user.is_anonymous and request.user.is_flight_worker_type