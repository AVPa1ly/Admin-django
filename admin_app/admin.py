from django.contrib import admin
from django.contrib.auth.models import Group

from admin_app.admin_customer import UserAdmin
from admin_app.admin_filghts import AirportAdmin, TrackAdmin, SeatsuiteAdmin, FlightAdmin
from admin_app.admin_news import InfoblockAdmin, PromocodeAdmin, OfferAdmin
from admin_app.models import MyUser, Infoblock, Airport, Track, Seatsuite, Flight, Promocode, Offer

admin.site.register(MyUser, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Infoblock, InfoblockAdmin)
admin.site.register(Airport, AirportAdmin)
admin.site.register(Track, TrackAdmin)
admin.site.register(Seatsuite, SeatsuiteAdmin)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Promocode, PromocodeAdmin)
admin.site.register(Offer, OfferAdmin)

admin.site.site_header = 'Flexair Admin'
