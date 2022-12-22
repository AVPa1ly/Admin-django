from django.contrib import admin
from django.contrib.auth.models import Group

from admin_app.admin_customer import UserAdmin
from admin_app.admin_filghts import AirportAdmin, TrackAdmin, SeatsuiteAdmin, FlightAdmin
from admin_app.admin_news import InfoblockAdmin, PromocodeAdmin, OfferAdmin, NewsAdmin
from admin_app.models import MyUser, Infoblock, Airport, Track, Seatsuite, Flight, Promocode, Offer, News

admin.site.register(MyUser, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Infoblock, InfoblockAdmin)
admin.site.register(Airport, AirportAdmin)
admin.site.register(Track, TrackAdmin)
admin.site.register(Seatsuite, SeatsuiteAdmin)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Promocode, PromocodeAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(News, NewsAdmin)

admin.site.site_header = 'Flexair Admin'
admin.site.index_title = 'Flexair administration'
admin.site.site_title = 'Flexair web administration'
