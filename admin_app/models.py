from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from admin_app.managers import MyUserManager


class Airport(models.Model):
    COUNTRY_CODES = (
        ('AF', 'Afghanistan'),
        ('AX', 'Aland Islands'),
        ('AL', 'Albania'),
        ('DZ', 'Algeria'),
        ('AS', 'American Samoa'),
        ('AD', 'Andorra'),
        ('AO', 'Angola'),
        ('AI', 'Anguilla'),
        ('AQ', 'Antarctica'),
        ('AG', 'AntiguaBarbuda'),
        ('AR', 'Argentina'),
        ('AM', 'Armenia'),
        ('AW', 'Aruba'),
        ('AU', 'Australia'),
        ('AT', 'Austria'),
        ('AZ', 'Azerbaijan'),
        ('BS', 'Bahamas'),
        ('BH', 'Bahrain'),
        ('BD', 'Bangladesh'),
        ('BB', 'Barbados'),
        ('BY', 'Belarus'),
        ('BE', 'Belgium'),
        ('BZ', 'Belize'),
        ('BJ', 'Benin'),
        ('BM', 'Bermuda'),
        ('BT', 'Bhutan'),
        ('BO', 'Bolivia'),
        ('BQ', 'Bonaire'),
        ('BA', 'BosniaHerzegovina'),
        ('BW', 'Botswana'),
        ('BV', 'BouvetIsland'),
        ('BR', 'Brazil'),
        ('IO', 'BritishIndianOceanTerritory'),
        ('BN', 'BruneiDarussalam'),
        ('BG', 'Bulgaria'),
        ('BF', 'BurkinaFaso'),
        ('BI', 'Burundi'),
        ('KH', 'Cambodia'),
        ('CM', 'Cameroon'),
        ('CA', 'Canada'),
        ('CV', 'CapeVerde'),
        ('KY', 'CaymanIslands'),
        ('CF', 'CentralAfricanRepublic'),
        ('TD', 'Chad'),
        ('CL', 'Chile'),
        ('CN', 'China'),
        ('CX', 'ChristmasIsland'),
        ('CC', 'CocosIslands'),
        ('CO', 'Colombia'),
        ('KM', 'Comoros'),
        ('CG', 'Congo'),
        ('CD', 'CongoDemocratic'),
        ('CK', 'CookIslands'),
        ('CR', 'CostaRica'),
        ('CI', 'CotedIvoire'),
        ('HR', 'Croatia'),
        ('CU', 'Cuba'),
        ('CW', 'Curaasao'),
        ('CY', 'Cyprus'),
        ('CZ', 'CzechRepublic'),
        ('DK', 'Denmark'),
        ('DJ', 'Djibouti'),
        ('DM', 'Dominica'),
        ('DO', 'DominicanRepublic'),
        ('EC', 'Ecuador'),
        ('EG', 'Egypt'),
        ('SV', 'ElSalvador'),
        ('GQ', 'EquatorialGuinea'),
        ('ER', 'Eritrea'),
        ('EE', 'Estonia'),
        ('ET', 'Ethiopia'),
        ('FK', 'FalklandIslands'),
        ('FO', 'FaroeIslands'),
        ('FJ', 'Fiji'),
        ('FI', 'Finland'),
        ('FR', 'France'),
        ('GF', 'FrenchGuiana'),
        ('PF', 'FrenchPolynesia'),
        ('TF', 'FrenchSouthernTerritories'),
        ('GA', 'Gabon'),
        ('GM', 'Gambia'),
        ('GE', 'Georgia'),
        ('DE', 'Germany'),
        ('GH', 'Ghana'),
        ('GI', 'Gibraltar'),
        ('GR', 'Greece'),
        ('GL', 'Greenland'),
        ('GD', 'Grenada'),
        ('GP', 'Guadeloupe'),
        ('GU', 'Guam'),
        ('GT', 'Guatemala'),
        ('GG', 'Guernsey'),
        ('GN', 'Guinea'),
        ('GW', 'GuineaBissau'),
        ('GY', 'Guyana'),
        ('HT', 'Haiti'),
        ('HM', 'HeardMcDonaldIslands'),
        ('VA', 'Vatican'),
        ('HN', 'Honduras'),
        ('HK', 'HongKong'),
        ('HU', 'Hungary'),
        ('IS', 'Iceland'),
        ('IN', 'India'),
        ('ID', 'Indonesia'),
        ('IR', 'Iran'),
        ('IQ', 'Iraq'),
        ('IE', 'Ireland'),
        ('IM', 'IsleofMan'),
        ('IL', 'Israel'),
        ('IT', 'Italy'),
        ('JM', 'Jamaica'),
        ('JP', 'Japan'),
        ('JE', 'Jersey'),
        ('JO', 'Jordan'),
        ('KZ', 'Kazakhstan'),
        ('KE', 'Kenya'),
        ('KI', 'Kiribati'),
        ('KP', 'KDPR'),
        ('KR', 'KR'),
        ('KW', 'Kuwait'),
        ('KG', 'Kyrgyzstan'),
        ('LA', 'Lao'),
        ('LV', 'Latvia'),
        ('LB', 'Lebanon'),
        ('LS', 'Lesotho'),
        ('LR', 'Liberia'),
        ('LY', 'Libya'),
        ('LI', 'Liechtenstein'),
        ('LT', 'Lithuania'),
        ('LU', 'Luxembourg'),
        ('MO', 'Macao'),
        ('MK', 'Macedonia'),
        ('MG', 'Madagascar'),
        ('MW', 'Malawi'),
        ('MY', 'Malaysia'),
        ('MV', 'Maldives'),
        ('ML', 'Mali'),
        ('MT', 'Malta'),
        ('MH', 'MarshallIslands'),
        ('MQ', 'Martinique'),
        ('MR', 'Mauritania'),
        ('MU', 'Mauritius'),
        ('YT', 'Mayotte'),
        ('MX', 'Mexico'),
        ('FM', 'Micronesia'),
        ('MD', 'Moldova'),
        ('MC', 'Monaco'),
        ('MN', 'Mongolia'),
        ('ME', 'Montenegro'),
        ('MS', 'Montserrat'),
        ('MA', 'Morocco'),
        ('MZ', 'Mozambique'),
        ('MM', 'Myanmar'),
        ('NA', 'Namibia'),
        ('NR', 'Nauru'),
        ('NP', 'Nepal'),
        ('NL', 'Netherlands'),
        ('NC', 'NewCaledonia'),
        ('NZ', 'NewZealand'),
        ('NI', 'Nicaragua'),
        ('NE', 'Niger'),
        ('NG', 'Nigeria'),
        ('NU', 'Niue'),
        ('NF', 'NorfolkIsland'),
        ('MP', 'NorthernMarianaIslands'),
        ('NO', 'Norway'),
        ('OM', 'Oman'),
        ('PK', 'Pakistan'),
        ('PW', 'Palau'),
        ('PS', 'Palestine'),
        ('PA', 'Panama'),
        ('PG', 'PapuaNewGuinea'),
        ('PY', 'Paraguay'),
        ('PE', 'Peru'),
        ('PH', 'Philippines'),
        ('PN', 'Pitcairn'),
        ('PL', 'Poland'),
        ('PT', 'Portugal'),
        ('PR', 'PuertoRico'),
        ('QA', 'Qatar'),
        ('RE', 'Raunion'),
        ('RO', 'Romania'),
        ('RU', 'RussianFederation'),
        ('RW', 'Rwanda'),
        ('BL', 'SaintBarthelemy'),
        ('SH', 'SaintHelena'),
        ('KN', 'SaintKittsNevis'),
        ('LC', 'SaintLucia'),
        ('MF', 'SaintMartin'),
        ('PM', 'SaintPierreMiquelon'),
        ('VC', 'SaintVincentGrenadines'),
        ('WS', 'Samoa'),
        ('SM', 'SanMarino'),
        ('ST', 'SaoTomePrincipe'),
        ('SA', 'SaudiArabia'),
        ('SN', 'Senegal'),
        ('RS', 'Serbia'),
        ('SC', 'Seychelles'),
        ('SL', 'SierraLeone'),
        ('SG', 'Singapore'),
        ('SX', 'SintMaarten'),
        ('SK', 'Slovakia'),
        ('SI', 'Slovenia'),
        ('SB', 'SolomonIslands'),
        ('SO', 'Somalia'),
        ('ZA', 'SouthAfrica'),
        ('GS', 'SouthGeorgiaSouthSandwichIslands'),
        ('SS', 'SouthSudan'),
        ('ES', 'Spain'),
        ('LK', 'SriLanka'),
        ('SD', 'Sudan'),
        ('SR', 'Suriname'),
        ('SJ', 'SvalbardJanMayen'),
        ('SZ', 'Swaziland'),
        ('SE', 'Sweden'),
        ('CH', 'Switzerland'),
        ('SY', 'SyrianArabRepublic'),
        ('TW', 'Taiwan'),
        ('TJ', 'Tajikistan'),
        ('TZ', 'Tanzania'),
        ('TH', 'Thailand'),
        ('TL', 'TimorLeste'),
        ('TG', 'Togo'),
        ('TK', 'Tokelau'),
        ('TO', 'Tonga'),
        ('TT', 'TrinidadTobago'),
        ('TN', 'Tunisia'),
        ('TR', 'Turkey'),
        ('TM', 'Turkmenistan'),
        ('TC', 'TurksCaicosIslands'),
        ('TV', 'Tuvalu'),
        ('UG', 'Uganda'),
        ('UA', 'Ukraine'),
        ('AE', 'UnitedArabEmirates'),
        ('GB', 'UnitedKingdom'),
        ('US', 'UnitedStates'),
        ('UM', 'UnitedStatesMinorOutlyingIslands'),
        ('UY', 'Uruguay'),
        ('UZ', 'Uzbekistan'),
        ('VU', 'Vanuatu'),
        ('VE', 'Venezuela'),
        ('VN', 'VietNam'),
        ('VG', 'VirginIslandsBritish'),
        ('VI', 'VirginIslandsUS'),
        ('WF', 'WallisFutuna'),
        ('EH', 'WesternSahara'),
        ('YE', 'Yemen'),
        ('ZM', 'Zambia'),
        ('ZW', 'Zimbabwe')
    )

    airportname = models.CharField(primary_key=True, max_length=100)
    cityname = models.CharField(max_length=100)
    countrycode = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'airport'


class MyUser(AbstractBaseUser):
    CUSTOMER_CONTENT_MAKER = 'contentmaker'
    CUSTOMER_USER = 'user'
    CUSTOMER_ADMIN = 'admin'
    CUSTOMER_FLIGHT_WORKER = 'flightworker'

    CUSTOMER_TYPES = (
        (CUSTOMER_CONTENT_MAKER, 'Content maker'),
        (CUSTOMER_USER, 'User'),
        (CUSTOMER_ADMIN, 'Admin'),
        (CUSTOMER_FLIGHT_WORKER, 'Flight worker'),
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        null=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    customerid = models.AutoField(primary_key=True)
    login = models.CharField(max_length=100, unique=True)
    passportid = models.ForeignKey('Passportdata', models.CASCADE, db_column='passportid', blank=True, null=True)
    customertype = models.CharField(max_length=100)
    password = models.CharField(db_column='customerpassword', max_length=100)
    objects = MyUserManager()

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.login

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_admin_type(self):
        return self.customertype in self.CUSTOMER_ADMIN

    @property
    def is_content_maker_type(self):
        return self.customertype in self.CUSTOMER_CONTENT_MAKER

    @property
    def is_flight_worker_type(self):
        return self.customertype in self.CUSTOMER_FLIGHT_WORKER

    @property
    def is_staff(self):
        return self.customertype in (self.CUSTOMER_CONTENT_MAKER,
                                     self.CUSTOMER_FLIGHT_WORKER,
                                     self.CUSTOMER_ADMIN)

    class Meta:
        db_table = 'customer'


class Flight(models.Model):
    flightid = models.AutoField(primary_key=True)
    arrivaltime = models.DateTimeField()
    departuretime = models.DateTimeField()
    seatsuiteid = models.ForeignKey('Seatsuite', models.CASCADE, db_column='seatsuiteid')
    trackid = models.ForeignKey('Track', models.CASCADE, db_column='trackid')
    economycost = models.FloatField()
    firstclasscost = models.FloatField()
    luxcost = models.FloatField()

    class Meta:
        managed = False
        db_table = 'flight'


class Infoblock(models.Model):
    infoblockid = models.AutoField(primary_key=True)
    header = models.TextField()
    main = models.TextField()

    class Meta:
        managed = False
        db_table = 'infoblock'


class News(models.Model):
    newsid = models.AutoField(primary_key=True)
    infoblockid = models.ForeignKey(Infoblock, models.CASCADE, db_column='infoblockid', blank=True, null=True)
    customerid = models.ForeignKey(MyUser, models.CASCADE, db_column='customerid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news'


class Offer(models.Model):
    offerid = models.AutoField(primary_key=True)
    infoblockid = models.ForeignKey(Infoblock, models.CASCADE, db_column='infoblockid', blank=True, null=True)
    promocodeid = models.ForeignKey('Promocode', models.CASCADE, db_column='promocodeid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offer'


class Passportdata(models.Model):
    passportid = models.AutoField(primary_key=True)
    sex = models.BooleanField()
    givenname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    dateofbirth = models.DateField()
    dateofissue = models.DateField()
    dateofexpery = models.DateField()
    idnumber = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    authority = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'passportdata'


class Promocode(models.Model):
    promocodeid = models.AutoField(primary_key=True)
    promocodevalue = models.CharField(max_length=30)
    discount = models.IntegerField()
    trackid = models.ForeignKey('Track', models.CASCADE, db_column='trackid')
    usecount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'promocode'


class Seatsuite(models.Model):
    seatsuiteid = models.AutoField(primary_key=True)
    economytotal = models.IntegerField()
    firstclasstotal = models.IntegerField()
    luxtotal = models.IntegerField()
    economyreserved = models.IntegerField(default=0)
    firstclassreserved = models.IntegerField(default=0)
    luxreserved = models.IntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'seatsuite'


class Ticket(models.Model):
    ticketid = models.AutoField(primary_key=True)
    seatclass = models.CharField(max_length=100)
    ticketcost = models.FloatField()
    customerid = models.ForeignKey(MyUser, models.CASCADE, db_column='customerid', blank=True, null=True)
    flightid = models.ForeignKey(Flight, models.CASCADE, db_column='flightid')

    class Meta:
        managed = False
        db_table = 'ticket'


class Track(models.Model):
    trackid = models.AutoField(primary_key=True)
    startairport = models.ForeignKey(Airport, models.CASCADE, db_column='startairport', related_name='start_tracks')
    endairport = models.ForeignKey(Airport, models.CASCADE, db_column='endairport', related_name='end_tracks')
    isinwheel = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'track'
