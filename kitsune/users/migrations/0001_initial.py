# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import kitsune.search.models
import kitsune.sumo.models
import timezones.fields
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Deactivation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EmailChange',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activation_key', models.CharField(max_length=40, verbose_name='activation key')),
                ('email', models.EmailField(max_length=75, null=True, db_index=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Display name', blank=True)),
                ('public_email', models.BooleanField(default=False, verbose_name='Make my email public')),
                ('avatar', models.ImageField(max_length=250, upload_to=b'uploads/avatars/', null=True, verbose_name='Avatar', blank=True)),
                ('bio', models.TextField(null=True, verbose_name='Biography', blank=True)),
                ('website', models.URLField(max_length=255, null=True, verbose_name='Website', blank=True)),
                ('twitter', models.CharField(blank=True, max_length=15, null=True, verbose_name='Twitter Username', validators=[django.core.validators.RegexValidator(b'^[\\w]+$', message=b'Please enter correct Twitter Handle', code=b'Invalid name')])),
                ('facebook', models.URLField(max_length=255, null=True, verbose_name='Facebook URL', blank=True)),
                ('mozillians', models.CharField(max_length=255, null=True, verbose_name='Mozillians Username', blank=True)),
                ('irc_handle', models.CharField(max_length=255, null=True, verbose_name='IRC nickname', blank=True)),
                ('timezone', timezones.fields.TimeZoneField(default=b'US/Pacific', choices=[(b'Africa/Abidjan', b'(GMT+0000) Africa/Abidjan'), (b'Africa/Accra', b'(GMT+0000) Africa/Accra'), (b'Africa/Addis_Ababa', b'(GMT+0300) Africa/Addis_Ababa'), (b'Africa/Algiers', b'(GMT+0100) Africa/Algiers'), (b'Africa/Asmara', b'(GMT+0300) Africa/Asmara'), (b'Africa/Bamako', b'(GMT+0000) Africa/Bamako'), (b'Africa/Bangui', b'(GMT+0100) Africa/Bangui'), (b'Africa/Banjul', b'(GMT+0000) Africa/Banjul'), (b'Africa/Bissau', b'(GMT+0000) Africa/Bissau'), (b'Africa/Blantyre', b'(GMT+0200) Africa/Blantyre'), (b'Africa/Brazzaville', b'(GMT+0100) Africa/Brazzaville'), (b'Africa/Bujumbura', b'(GMT+0200) Africa/Bujumbura'), (b'Africa/Cairo', b'(GMT+0200) Africa/Cairo'), (b'Africa/Casablanca', b'(GMT+0000) Africa/Casablanca'), (b'Africa/Ceuta', b'(GMT+0200) Africa/Ceuta'), (b'Africa/Conakry', b'(GMT+0000) Africa/Conakry'), (b'Africa/Dakar', b'(GMT+0000) Africa/Dakar'), (b'Africa/Dar_es_Salaam', b'(GMT+0300) Africa/Dar_es_Salaam'), (b'Africa/Djibouti', b'(GMT+0300) Africa/Djibouti'), (b'Africa/Douala', b'(GMT+0100) Africa/Douala'), (b'Africa/El_Aaiun', b'(GMT+0000) Africa/El_Aaiun'), (b'Africa/Freetown', b'(GMT+0000) Africa/Freetown'), (b'Africa/Gaborone', b'(GMT+0200) Africa/Gaborone'), (b'Africa/Harare', b'(GMT+0200) Africa/Harare'), (b'Africa/Johannesburg', b'(GMT+0200) Africa/Johannesburg'), (b'Africa/Juba', b'(GMT+0300) Africa/Juba'), (b'Africa/Kampala', b'(GMT+0300) Africa/Kampala'), (b'Africa/Khartoum', b'(GMT+0300) Africa/Khartoum'), (b'Africa/Kigali', b'(GMT+0200) Africa/Kigali'), (b'Africa/Kinshasa', b'(GMT+0100) Africa/Kinshasa'), (b'Africa/Lagos', b'(GMT+0100) Africa/Lagos'), (b'Africa/Libreville', b'(GMT+0100) Africa/Libreville'), (b'Africa/Lome', b'(GMT+0000) Africa/Lome'), (b'Africa/Luanda', b'(GMT+0100) Africa/Luanda'), (b'Africa/Lubumbashi', b'(GMT+0200) Africa/Lubumbashi'), (b'Africa/Lusaka', b'(GMT+0200) Africa/Lusaka'), (b'Africa/Malabo', b'(GMT+0100) Africa/Malabo'), (b'Africa/Maputo', b'(GMT+0200) Africa/Maputo'), (b'Africa/Maseru', b'(GMT+0200) Africa/Maseru'), (b'Africa/Mbabane', b'(GMT+0200) Africa/Mbabane'), (b'Africa/Mogadishu', b'(GMT+0300) Africa/Mogadishu'), (b'Africa/Monrovia', b'(GMT+0000) Africa/Monrovia'), (b'Africa/Nairobi', b'(GMT+0300) Africa/Nairobi'), (b'Africa/Ndjamena', b'(GMT+0100) Africa/Ndjamena'), (b'Africa/Niamey', b'(GMT+0100) Africa/Niamey'), (b'Africa/Nouakchott', b'(GMT+0000) Africa/Nouakchott'), (b'Africa/Ouagadougou', b'(GMT+0000) Africa/Ouagadougou'), (b'Africa/Porto-Novo', b'(GMT+0100) Africa/Porto-Novo'), (b'Africa/Sao_Tome', b'(GMT+0000) Africa/Sao_Tome'), (b'Africa/Tripoli', b'(GMT+0200) Africa/Tripoli'), (b'Africa/Tunis', b'(GMT+0100) Africa/Tunis'), (b'Africa/Windhoek', b'(GMT+0200) Africa/Windhoek'), (b'America/Adak', b'(GMT-0900) America/Adak'), (b'America/Anchorage', b'(GMT-0800) America/Anchorage'), (b'America/Anguilla', b'(GMT-0400) America/Anguilla'), (b'America/Antigua', b'(GMT-0400) America/Antigua'), (b'America/Araguaina', b'(GMT-0300) America/Araguaina'), (b'America/Argentina/Buenos_Aires', b'(GMT-0300) America/Argentina/Buenos_Aires'), (b'America/Argentina/Catamarca', b'(GMT-0300) America/Argentina/Catamarca'), (b'America/Argentina/Cordoba', b'(GMT-0300) America/Argentina/Cordoba'), (b'America/Argentina/Jujuy', b'(GMT-0300) America/Argentina/Jujuy'), (b'America/Argentina/La_Rioja', b'(GMT-0300) America/Argentina/La_Rioja'), (b'America/Argentina/Mendoza', b'(GMT-0300) America/Argentina/Mendoza'), (b'America/Argentina/Rio_Gallegos', b'(GMT-0300) America/Argentina/Rio_Gallegos'), (b'America/Argentina/Salta', b'(GMT-0300) America/Argentina/Salta'), (b'America/Argentina/San_Juan', b'(GMT-0300) America/Argentina/San_Juan'), (b'America/Argentina/San_Luis', b'(GMT-0300) America/Argentina/San_Luis'), (b'America/Argentina/Tucuman', b'(GMT-0300) America/Argentina/Tucuman'), (b'America/Argentina/Ushuaia', b'(GMT-0300) America/Argentina/Ushuaia'), (b'America/Aruba', b'(GMT-0400) America/Aruba'), (b'America/Asuncion', b'(GMT-0300) America/Asuncion'), (b'America/Atikokan', b'(GMT-0500) America/Atikokan'), (b'America/Bahia', b'(GMT-0300) America/Bahia'), (b'America/Bahia_Banderas', b'(GMT-0600) America/Bahia_Banderas'), (b'America/Barbados', b'(GMT-0400) America/Barbados'), (b'America/Belem', b'(GMT-0300) America/Belem'), (b'America/Belize', b'(GMT-0600) America/Belize'), (b'America/Blanc-Sablon', b'(GMT-0400) America/Blanc-Sablon'), (b'America/Boa_Vista', b'(GMT-0400) America/Boa_Vista'), (b'America/Bogota', b'(GMT-0500) America/Bogota'), (b'America/Boise', b'(GMT-0600) America/Boise'), (b'America/Cambridge_Bay', b'(GMT-0600) America/Cambridge_Bay'), (b'America/Campo_Grande', b'(GMT-0400) America/Campo_Grande'), (b'America/Cancun', b'(GMT-0600) America/Cancun'), (b'America/Caracas', b'(GMT-0430) America/Caracas'), (b'America/Cayenne', b'(GMT-0300) America/Cayenne'), (b'America/Cayman', b'(GMT-0500) America/Cayman'), (b'America/Chicago', b'(GMT-0500) America/Chicago'), (b'America/Chihuahua', b'(GMT-0700) America/Chihuahua'), (b'America/Costa_Rica', b'(GMT-0600) America/Costa_Rica'), (b'America/Creston', b'(GMT-0700) America/Creston'), (b'America/Cuiaba', b'(GMT-0400) America/Cuiaba'), (b'America/Curacao', b'(GMT-0400) America/Curacao'), (b'America/Danmarkshavn', b'(GMT+0000) America/Danmarkshavn'), (b'America/Dawson', b'(GMT-0700) America/Dawson'), (b'America/Dawson_Creek', b'(GMT-0700) America/Dawson_Creek'), (b'America/Denver', b'(GMT-0600) America/Denver'), (b'America/Detroit', b'(GMT-0400) America/Detroit'), (b'America/Dominica', b'(GMT-0400) America/Dominica'), (b'America/Edmonton', b'(GMT-0600) America/Edmonton'), (b'America/Eirunepe', b'(GMT-0400) America/Eirunepe'), (b'America/El_Salvador', b'(GMT-0600) America/El_Salvador'), (b'America/Fortaleza', b'(GMT-0300) America/Fortaleza'), (b'America/Glace_Bay', b'(GMT-0300) America/Glace_Bay'), (b'America/Godthab', b'(GMT-0200) America/Godthab'), (b'America/Goose_Bay', b'(GMT-0300) America/Goose_Bay'), (b'America/Grand_Turk', b'(GMT-0400) America/Grand_Turk'), (b'America/Grenada', b'(GMT-0400) America/Grenada'), (b'America/Guadeloupe', b'(GMT-0400) America/Guadeloupe'), (b'America/Guatemala', b'(GMT-0600) America/Guatemala'), (b'America/Guayaquil', b'(GMT-0500) America/Guayaquil'), (b'America/Guyana', b'(GMT-0400) America/Guyana'), (b'America/Halifax', b'(GMT-0300) America/Halifax'), (b'America/Havana', b'(GMT-0400) America/Havana'), (b'America/Hermosillo', b'(GMT-0700) America/Hermosillo'), (b'America/Indiana/Indianapolis', b'(GMT-0400) America/Indiana/Indianapolis'), (b'America/Indiana/Knox', b'(GMT-0500) America/Indiana/Knox'), (b'America/Indiana/Marengo', b'(GMT-0400) America/Indiana/Marengo'), (b'America/Indiana/Petersburg', b'(GMT-0400) America/Indiana/Petersburg'), (b'America/Indiana/Tell_City', b'(GMT-0500) America/Indiana/Tell_City'), (b'America/Indiana/Vevay', b'(GMT-0400) America/Indiana/Vevay'), (b'America/Indiana/Vincennes', b'(GMT-0400) America/Indiana/Vincennes'), (b'America/Indiana/Winamac', b'(GMT-0400) America/Indiana/Winamac'), (b'America/Inuvik', b'(GMT-0600) America/Inuvik'), (b'America/Iqaluit', b'(GMT-0400) America/Iqaluit'), (b'America/Jamaica', b'(GMT-0500) America/Jamaica'), (b'America/Juneau', b'(GMT-0800) America/Juneau'), (b'America/Kentucky/Louisville', b'(GMT-0400) America/Kentucky/Louisville'), (b'America/Kentucky/Monticello', b'(GMT-0400) America/Kentucky/Monticello'), (b'America/Kralendijk', b'(GMT-0400) America/Kralendijk'), (b'America/La_Paz', b'(GMT-0400) America/La_Paz'), (b'America/Lima', b'(GMT-0500) America/Lima'), (b'America/Los_Angeles', b'(GMT-0700) America/Los_Angeles'), (b'America/Lower_Princes', b'(GMT-0400) America/Lower_Princes'), (b'America/Maceio', b'(GMT-0300) America/Maceio'), (b'America/Managua', b'(GMT-0600) America/Managua'), (b'America/Manaus', b'(GMT-0400) America/Manaus'), (b'America/Marigot', b'(GMT-0400) America/Marigot'), (b'America/Martinique', b'(GMT-0400) America/Martinique'), (b'America/Matamoros', b'(GMT-0500) America/Matamoros'), (b'America/Mazatlan', b'(GMT-0700) America/Mazatlan'), (b'America/Menominee', b'(GMT-0500) America/Menominee'), (b'America/Merida', b'(GMT-0600) America/Merida'), (b'America/Metlakatla', b'(GMT-0800) America/Metlakatla'), (b'America/Mexico_City', b'(GMT-0600) America/Mexico_City'), (b'America/Miquelon', b'(GMT-0200) America/Miquelon'), (b'America/Moncton', b'(GMT-0300) America/Moncton'), (b'America/Monterrey', b'(GMT-0600) America/Monterrey'), (b'America/Montevideo', b'(GMT-0300) America/Montevideo'), (b'America/Montreal', b'(GMT-0400) America/Montreal'), (b'America/Montserrat', b'(GMT-0400) America/Montserrat'), (b'America/Nassau', b'(GMT-0400) America/Nassau'), (b'America/New_York', b'(GMT-0400) America/New_York'), (b'America/Nipigon', b'(GMT-0400) America/Nipigon'), (b'America/Nome', b'(GMT-0800) America/Nome'), (b'America/Noronha', b'(GMT-0200) America/Noronha'), (b'America/North_Dakota/Beulah', b'(GMT-0500) America/North_Dakota/Beulah'), (b'America/North_Dakota/Center', b'(GMT-0500) America/North_Dakota/Center'), (b'America/North_Dakota/New_Salem', b'(GMT-0500) America/North_Dakota/New_Salem'), (b'America/Ojinaga', b'(GMT-0600) America/Ojinaga'), (b'America/Panama', b'(GMT-0500) America/Panama'), (b'America/Pangnirtung', b'(GMT-0400) America/Pangnirtung'), (b'America/Paramaribo', b'(GMT-0300) America/Paramaribo'), (b'America/Phoenix', b'(GMT-0700) America/Phoenix'), (b'America/Port-au-Prince', b'(GMT-0400) America/Port-au-Prince'), (b'America/Port_of_Spain', b'(GMT-0400) America/Port_of_Spain'), (b'America/Porto_Velho', b'(GMT-0400) America/Porto_Velho'), (b'America/Puerto_Rico', b'(GMT-0400) America/Puerto_Rico'), (b'America/Rainy_River', b'(GMT-0500) America/Rainy_River'), (b'America/Rankin_Inlet', b'(GMT-0500) America/Rankin_Inlet'), (b'America/Recife', b'(GMT-0300) America/Recife'), (b'America/Regina', b'(GMT-0600) America/Regina'), (b'America/Resolute', b'(GMT-0500) America/Resolute'), (b'America/Rio_Branco', b'(GMT-0400) America/Rio_Branco'), (b'America/Santa_Isabel', b'(GMT-0800) America/Santa_Isabel'), (b'America/Santarem', b'(GMT-0300) America/Santarem'), (b'America/Santiago', b'(GMT-0300) America/Santiago'), (b'America/Santo_Domingo', b'(GMT-0400) America/Santo_Domingo'), (b'America/Sao_Paulo', b'(GMT-0300) America/Sao_Paulo'), (b'America/Scoresbysund', b'(GMT+0000) America/Scoresbysund'), (b'America/Shiprock', b'(GMT-0600) America/Shiprock'), (b'America/Sitka', b'(GMT-0800) America/Sitka'), (b'America/St_Barthelemy', b'(GMT-0400) America/St_Barthelemy'), (b'America/St_Johns', b'(GMT-0230) America/St_Johns'), (b'America/St_Kitts', b'(GMT-0400) America/St_Kitts'), (b'America/St_Lucia', b'(GMT-0400) America/St_Lucia'), (b'America/St_Thomas', b'(GMT-0400) America/St_Thomas'), (b'America/St_Vincent', b'(GMT-0400) America/St_Vincent'), (b'America/Swift_Current', b'(GMT-0600) America/Swift_Current'), (b'America/Tegucigalpa', b'(GMT-0600) America/Tegucigalpa'), (b'America/Thule', b'(GMT-0300) America/Thule'), (b'America/Thunder_Bay', b'(GMT-0400) America/Thunder_Bay'), (b'America/Tijuana', b'(GMT-0700) America/Tijuana'), (b'America/Toronto', b'(GMT-0400) America/Toronto'), (b'America/Tortola', b'(GMT-0400) America/Tortola'), (b'America/Vancouver', b'(GMT-0700) America/Vancouver'), (b'America/Whitehorse', b'(GMT-0700) America/Whitehorse'), (b'America/Winnipeg', b'(GMT-0500) America/Winnipeg'), (b'America/Yakutat', b'(GMT-0800) America/Yakutat'), (b'America/Yellowknife', b'(GMT-0600) America/Yellowknife'), (b'Antarctica/Casey', b'(GMT+0800) Antarctica/Casey'), (b'Antarctica/Davis', b'(GMT+0700) Antarctica/Davis'), (b'Antarctica/DumontDUrville', b'(GMT+1000) Antarctica/DumontDUrville'), (b'Antarctica/Macquarie', b'(GMT+1100) Antarctica/Macquarie'), (b'Antarctica/Mawson', b'(GMT+0500) Antarctica/Mawson'), (b'Antarctica/McMurdo', b'(GMT+1300) Antarctica/McMurdo'), (b'Antarctica/Palmer', b'(GMT-0300) Antarctica/Palmer'), (b'Antarctica/Rothera', b'(GMT-0300) Antarctica/Rothera'), (b'Antarctica/South_Pole', b'(GMT+1300) Antarctica/South_Pole'), (b'Antarctica/Syowa', b'(GMT+0300) Antarctica/Syowa'), (b'Antarctica/Vostok', b'(GMT+0600) Antarctica/Vostok'), (b'Arctic/Longyearbyen', b'(GMT+0200) Arctic/Longyearbyen'), (b'Asia/Aden', b'(GMT+0300) Asia/Aden'), (b'Asia/Almaty', b'(GMT+0600) Asia/Almaty'), (b'Asia/Amman', b'(GMT+0300) Asia/Amman'), (b'Asia/Anadyr', b'(GMT+1200) Asia/Anadyr'), (b'Asia/Aqtau', b'(GMT+0500) Asia/Aqtau'), (b'Asia/Aqtobe', b'(GMT+0500) Asia/Aqtobe'), (b'Asia/Ashgabat', b'(GMT+0500) Asia/Ashgabat'), (b'Asia/Baghdad', b'(GMT+0300) Asia/Baghdad'), (b'Asia/Bahrain', b'(GMT+0300) Asia/Bahrain'), (b'Asia/Baku', b'(GMT+0500) Asia/Baku'), (b'Asia/Bangkok', b'(GMT+0700) Asia/Bangkok'), (b'Asia/Beirut', b'(GMT+0300) Asia/Beirut'), (b'Asia/Bishkek', b'(GMT+0600) Asia/Bishkek'), (b'Asia/Brunei', b'(GMT+0800) Asia/Brunei'), (b'Asia/Choibalsan', b'(GMT+0800) Asia/Choibalsan'), (b'Asia/Chongqing', b'(GMT+0800) Asia/Chongqing'), (b'Asia/Colombo', b'(GMT+0530) Asia/Colombo'), (b'Asia/Damascus', b'(GMT+0300) Asia/Damascus'), (b'Asia/Dhaka', b'(GMT+0600) Asia/Dhaka'), (b'Asia/Dili', b'(GMT+0900) Asia/Dili'), (b'Asia/Dubai', b'(GMT+0400) Asia/Dubai'), (b'Asia/Dushanbe', b'(GMT+0500) Asia/Dushanbe'), (b'Asia/Gaza', b'(GMT+0200) Asia/Gaza'), (b'Asia/Harbin', b'(GMT+0800) Asia/Harbin'), (b'Asia/Hebron', b'(GMT+0200) Asia/Hebron'), (b'Asia/Ho_Chi_Minh', b'(GMT+0700) Asia/Ho_Chi_Minh'), (b'Asia/Hong_Kong', b'(GMT+0800) Asia/Hong_Kong'), (b'Asia/Hovd', b'(GMT+0700) Asia/Hovd'), (b'Asia/Irkutsk', b'(GMT+0900) Asia/Irkutsk'), (b'Asia/Jakarta', b'(GMT+0700) Asia/Jakarta'), (b'Asia/Jayapura', b'(GMT+0900) Asia/Jayapura'), (b'Asia/Jerusalem', b'(GMT+0300) Asia/Jerusalem'), (b'Asia/Kabul', b'(GMT+0430) Asia/Kabul'), (b'Asia/Kamchatka', b'(GMT+1200) Asia/Kamchatka'), (b'Asia/Karachi', b'(GMT+0500) Asia/Karachi'), (b'Asia/Kashgar', b'(GMT+0800) Asia/Kashgar'), (b'Asia/Kathmandu', b'(GMT+0545) Asia/Kathmandu'), (b'Asia/Khandyga', b'(GMT+1000) Asia/Khandyga'), (b'Asia/Kolkata', b'(GMT+0530) Asia/Kolkata'), (b'Asia/Krasnoyarsk', b'(GMT+0800) Asia/Krasnoyarsk'), (b'Asia/Kuala_Lumpur', b'(GMT+0800) Asia/Kuala_Lumpur'), (b'Asia/Kuching', b'(GMT+0800) Asia/Kuching'), (b'Asia/Kuwait', b'(GMT+0300) Asia/Kuwait'), (b'Asia/Macau', b'(GMT+0800) Asia/Macau'), (b'Asia/Magadan', b'(GMT+1200) Asia/Magadan'), (b'Asia/Makassar', b'(GMT+0800) Asia/Makassar'), (b'Asia/Manila', b'(GMT+0800) Asia/Manila'), (b'Asia/Muscat', b'(GMT+0400) Asia/Muscat'), (b'Asia/Nicosia', b'(GMT+0300) Asia/Nicosia'), (b'Asia/Novokuznetsk', b'(GMT+0700) Asia/Novokuznetsk'), (b'Asia/Novosibirsk', b'(GMT+0700) Asia/Novosibirsk'), (b'Asia/Omsk', b'(GMT+0700) Asia/Omsk'), (b'Asia/Oral', b'(GMT+0500) Asia/Oral'), (b'Asia/Phnom_Penh', b'(GMT+0700) Asia/Phnom_Penh'), (b'Asia/Pontianak', b'(GMT+0700) Asia/Pontianak'), (b'Asia/Pyongyang', b'(GMT+0900) Asia/Pyongyang'), (b'Asia/Qatar', b'(GMT+0300) Asia/Qatar'), (b'Asia/Qyzylorda', b'(GMT+0600) Asia/Qyzylorda'), (b'Asia/Rangoon', b'(GMT+0630) Asia/Rangoon'), (b'Asia/Riyadh', b'(GMT+0300) Asia/Riyadh'), (b'Asia/Sakhalin', b'(GMT+1100) Asia/Sakhalin'), (b'Asia/Samarkand', b'(GMT+0500) Asia/Samarkand'), (b'Asia/Seoul', b'(GMT+0900) Asia/Seoul'), (b'Asia/Shanghai', b'(GMT+0800) Asia/Shanghai'), (b'Asia/Singapore', b'(GMT+0800) Asia/Singapore'), (b'Asia/Taipei', b'(GMT+0800) Asia/Taipei'), (b'Asia/Tashkent', b'(GMT+0500) Asia/Tashkent'), (b'Asia/Tbilisi', b'(GMT+0400) Asia/Tbilisi'), (b'Asia/Tehran', b'(GMT+0430) Asia/Tehran'), (b'Asia/Thimphu', b'(GMT+0600) Asia/Thimphu'), (b'Asia/Tokyo', b'(GMT+0900) Asia/Tokyo'), (b'Asia/Ulaanbaatar', b'(GMT+0800) Asia/Ulaanbaatar'), (b'Asia/Urumqi', b'(GMT+0800) Asia/Urumqi'), (b'Asia/Ust-Nera', b'(GMT+1100) Asia/Ust-Nera'), (b'Asia/Vientiane', b'(GMT+0700) Asia/Vientiane'), (b'Asia/Vladivostok', b'(GMT+1100) Asia/Vladivostok'), (b'Asia/Yakutsk', b'(GMT+1000) Asia/Yakutsk'), (b'Asia/Yekaterinburg', b'(GMT+0600) Asia/Yekaterinburg'), (b'Asia/Yerevan', b'(GMT+0400) Asia/Yerevan'), (b'Atlantic/Azores', b'(GMT+0000) Atlantic/Azores'), (b'Atlantic/Bermuda', b'(GMT-0300) Atlantic/Bermuda'), (b'Atlantic/Canary', b'(GMT+0100) Atlantic/Canary'), (b'Atlantic/Cape_Verde', b'(GMT-0100) Atlantic/Cape_Verde'), (b'Atlantic/Faroe', b'(GMT+0100) Atlantic/Faroe'), (b'Atlantic/Madeira', b'(GMT+0100) Atlantic/Madeira'), (b'Atlantic/Reykjavik', b'(GMT+0000) Atlantic/Reykjavik'), (b'Atlantic/South_Georgia', b'(GMT-0200) Atlantic/South_Georgia'), (b'Atlantic/St_Helena', b'(GMT+0000) Atlantic/St_Helena'), (b'Atlantic/Stanley', b'(GMT-0300) Atlantic/Stanley'), (b'Australia/Adelaide', b'(GMT+1030) Australia/Adelaide'), (b'Australia/Brisbane', b'(GMT+1000) Australia/Brisbane'), (b'Australia/Broken_Hill', b'(GMT+1030) Australia/Broken_Hill'), (b'Australia/Currie', b'(GMT+1100) Australia/Currie'), (b'Australia/Darwin', b'(GMT+0930) Australia/Darwin'), (b'Australia/Eucla', b'(GMT+0845) Australia/Eucla'), (b'Australia/Hobart', b'(GMT+1100) Australia/Hobart'), (b'Australia/Lindeman', b'(GMT+1000) Australia/Lindeman'), (b'Australia/Lord_Howe', b'(GMT+1100) Australia/Lord_Howe'), (b'Australia/Melbourne', b'(GMT+1100) Australia/Melbourne'), (b'Australia/Perth', b'(GMT+0800) Australia/Perth'), (b'Australia/Sydney', b'(GMT+1100) Australia/Sydney'), (b'Canada/Atlantic', b'(GMT-0300) Canada/Atlantic'), (b'Canada/Central', b'(GMT-0500) Canada/Central'), (b'Canada/Eastern', b'(GMT-0400) Canada/Eastern'), (b'Canada/Mountain', b'(GMT-0600) Canada/Mountain'), (b'Canada/Newfoundland', b'(GMT-0230) Canada/Newfoundland'), (b'Canada/Pacific', b'(GMT-0700) Canada/Pacific'), (b'Europe/Amsterdam', b'(GMT+0200) Europe/Amsterdam'), (b'Europe/Andorra', b'(GMT+0200) Europe/Andorra'), (b'Europe/Athens', b'(GMT+0300) Europe/Athens'), (b'Europe/Belgrade', b'(GMT+0200) Europe/Belgrade'), (b'Europe/Berlin', b'(GMT+0200) Europe/Berlin'), (b'Europe/Bratislava', b'(GMT+0200) Europe/Bratislava'), (b'Europe/Brussels', b'(GMT+0200) Europe/Brussels'), (b'Europe/Bucharest', b'(GMT+0300) Europe/Bucharest'), (b'Europe/Budapest', b'(GMT+0200) Europe/Budapest'), (b'Europe/Busingen', b'(GMT+0200) Europe/Busingen'), (b'Europe/Chisinau', b'(GMT+0300) Europe/Chisinau'), (b'Europe/Copenhagen', b'(GMT+0200) Europe/Copenhagen'), (b'Europe/Dublin', b'(GMT+0100) Europe/Dublin'), (b'Europe/Gibraltar', b'(GMT+0200) Europe/Gibraltar'), (b'Europe/Guernsey', b'(GMT+0100) Europe/Guernsey'), (b'Europe/Helsinki', b'(GMT+0300) Europe/Helsinki'), (b'Europe/Isle_of_Man', b'(GMT+0100) Europe/Isle_of_Man'), (b'Europe/Istanbul', b'(GMT+0300) Europe/Istanbul'), (b'Europe/Jersey', b'(GMT+0100) Europe/Jersey'), (b'Europe/Kaliningrad', b'(GMT+0300) Europe/Kaliningrad'), (b'Europe/Kiev', b'(GMT+0300) Europe/Kiev'), (b'Europe/Lisbon', b'(GMT+0100) Europe/Lisbon'), (b'Europe/Ljubljana', b'(GMT+0200) Europe/Ljubljana'), (b'Europe/London', b'(GMT+0100) Europe/London'), (b'Europe/Luxembourg', b'(GMT+0200) Europe/Luxembourg'), (b'Europe/Madrid', b'(GMT+0200) Europe/Madrid'), (b'Europe/Malta', b'(GMT+0200) Europe/Malta'), (b'Europe/Mariehamn', b'(GMT+0300) Europe/Mariehamn'), (b'Europe/Minsk', b'(GMT+0300) Europe/Minsk'), (b'Europe/Monaco', b'(GMT+0200) Europe/Monaco'), (b'Europe/Moscow', b'(GMT+0400) Europe/Moscow'), (b'Europe/Oslo', b'(GMT+0200) Europe/Oslo'), (b'Europe/Paris', b'(GMT+0200) Europe/Paris'), (b'Europe/Podgorica', b'(GMT+0200) Europe/Podgorica'), (b'Europe/Prague', b'(GMT+0200) Europe/Prague'), (b'Europe/Riga', b'(GMT+0300) Europe/Riga'), (b'Europe/Rome', b'(GMT+0200) Europe/Rome'), (b'Europe/Samara', b'(GMT+0400) Europe/Samara'), (b'Europe/San_Marino', b'(GMT+0200) Europe/San_Marino'), (b'Europe/Sarajevo', b'(GMT+0200) Europe/Sarajevo'), (b'Europe/Simferopol', b'(GMT+0300) Europe/Simferopol'), (b'Europe/Skopje', b'(GMT+0200) Europe/Skopje'), (b'Europe/Sofia', b'(GMT+0300) Europe/Sofia'), (b'Europe/Stockholm', b'(GMT+0200) Europe/Stockholm'), (b'Europe/Tallinn', b'(GMT+0300) Europe/Tallinn'), (b'Europe/Tirane', b'(GMT+0200) Europe/Tirane'), (b'Europe/Uzhgorod', b'(GMT+0300) Europe/Uzhgorod'), (b'Europe/Vaduz', b'(GMT+0200) Europe/Vaduz'), (b'Europe/Vatican', b'(GMT+0200) Europe/Vatican'), (b'Europe/Vienna', b'(GMT+0200) Europe/Vienna'), (b'Europe/Vilnius', b'(GMT+0300) Europe/Vilnius'), (b'Europe/Volgograd', b'(GMT+0400) Europe/Volgograd'), (b'Europe/Warsaw', b'(GMT+0200) Europe/Warsaw'), (b'Europe/Zagreb', b'(GMT+0200) Europe/Zagreb'), (b'Europe/Zaporozhye', b'(GMT+0300) Europe/Zaporozhye'), (b'Europe/Zurich', b'(GMT+0200) Europe/Zurich'), (b'GMT', b'(GMT+0000) GMT'), (b'Indian/Antananarivo', b'(GMT+0300) Indian/Antananarivo'), (b'Indian/Chagos', b'(GMT+0600) Indian/Chagos'), (b'Indian/Christmas', b'(GMT+0700) Indian/Christmas'), (b'Indian/Cocos', b'(GMT+0630) Indian/Cocos'), (b'Indian/Comoro', b'(GMT+0300) Indian/Comoro'), (b'Indian/Kerguelen', b'(GMT+0500) Indian/Kerguelen'), (b'Indian/Mahe', b'(GMT+0400) Indian/Mahe'), (b'Indian/Maldives', b'(GMT+0500) Indian/Maldives'), (b'Indian/Mauritius', b'(GMT+0400) Indian/Mauritius'), (b'Indian/Mayotte', b'(GMT+0300) Indian/Mayotte'), (b'Indian/Reunion', b'(GMT+0400) Indian/Reunion'), (b'Pacific/Apia', b'(GMT+1400) Pacific/Apia'), (b'Pacific/Auckland', b'(GMT+1300) Pacific/Auckland'), (b'Pacific/Chatham', b'(GMT+1345) Pacific/Chatham'), (b'Pacific/Chuuk', b'(GMT+1000) Pacific/Chuuk'), (b'Pacific/Easter', b'(GMT-0500) Pacific/Easter'), (b'Pacific/Efate', b'(GMT+1100) Pacific/Efate'), (b'Pacific/Enderbury', b'(GMT+1300) Pacific/Enderbury'), (b'Pacific/Fakaofo', b'(GMT+1300) Pacific/Fakaofo'), (b'Pacific/Fiji', b'(GMT+1200) Pacific/Fiji'), (b'Pacific/Funafuti', b'(GMT+1200) Pacific/Funafuti'), (b'Pacific/Galapagos', b'(GMT-0600) Pacific/Galapagos'), (b'Pacific/Gambier', b'(GMT-0900) Pacific/Gambier'), (b'Pacific/Guadalcanal', b'(GMT+1100) Pacific/Guadalcanal'), (b'Pacific/Guam', b'(GMT+1000) Pacific/Guam'), (b'Pacific/Honolulu', b'(GMT-1000) Pacific/Honolulu'), (b'Pacific/Johnston', b'(GMT-1000) Pacific/Johnston'), (b'Pacific/Kiritimati', b'(GMT+1400) Pacific/Kiritimati'), (b'Pacific/Kosrae', b'(GMT+1100) Pacific/Kosrae'), (b'Pacific/Kwajalein', b'(GMT+1200) Pacific/Kwajalein'), (b'Pacific/Majuro', b'(GMT+1200) Pacific/Majuro'), (b'Pacific/Marquesas', b'(GMT-0930) Pacific/Marquesas'), (b'Pacific/Midway', b'(GMT-1100) Pacific/Midway'), (b'Pacific/Nauru', b'(GMT+1200) Pacific/Nauru'), (b'Pacific/Niue', b'(GMT-1100) Pacific/Niue'), (b'Pacific/Norfolk', b'(GMT+1130) Pacific/Norfolk'), (b'Pacific/Noumea', b'(GMT+1100) Pacific/Noumea'), (b'Pacific/Pago_Pago', b'(GMT-1100) Pacific/Pago_Pago'), (b'Pacific/Palau', b'(GMT+0900) Pacific/Palau'), (b'Pacific/Pitcairn', b'(GMT-0800) Pacific/Pitcairn'), (b'Pacific/Pohnpei', b'(GMT+1100) Pacific/Pohnpei'), (b'Pacific/Port_Moresby', b'(GMT+1000) Pacific/Port_Moresby'), (b'Pacific/Rarotonga', b'(GMT-1000) Pacific/Rarotonga'), (b'Pacific/Saipan', b'(GMT+1000) Pacific/Saipan'), (b'Pacific/Tahiti', b'(GMT-1000) Pacific/Tahiti'), (b'Pacific/Tarawa', b'(GMT+1200) Pacific/Tarawa'), (b'Pacific/Tongatapu', b'(GMT+1300) Pacific/Tongatapu'), (b'Pacific/Wake', b'(GMT+1200) Pacific/Wake'), (b'Pacific/Wallis', b'(GMT+1200) Pacific/Wallis'), (b'US/Alaska', b'(GMT-0800) US/Alaska'), (b'US/Arizona', b'(GMT-0700) US/Arizona'), (b'US/Central', b'(GMT-0500) US/Central'), (b'US/Eastern', b'(GMT-0400) US/Eastern'), (b'US/Hawaii', b'(GMT-1000) US/Hawaii'), (b'US/Mountain', b'(GMT-0600) US/Mountain'), (b'US/Pacific', b'(GMT-0700) US/Pacific'), (b'UTC', b'(GMT+0000) UTC')], max_length=100, blank=True, null=True, verbose_name='Timezone')),
                ('country', models.CharField(blank=True, max_length=2, null=True, verbose_name='Country', choices=[(b'AF', b'Afghanistan'), (b'AX', '\xc5land Islands'), (b'AL', b'Albania'), (b'DZ', b'Algeria'), (b'AS', b'American Samoa'), (b'AD', b'Andorra'), (b'AO', b'Angola'), (b'AI', b'Anguilla'), (b'AQ', b'Antarctica'), (b'AG', b'Antigua and Barbuda'), (b'AR', b'Argentina'), (b'AM', b'Armenia'), (b'AW', b'Aruba'), (b'AU', b'Australia'), (b'AT', b'Austria'), (b'AZ', b'Azerbaijan'), (b'BS', b'Bahamas'), (b'BH', b'Bahrain'), (b'BD', b'Bangladesh'), (b'BB', b'Barbados'), (b'BY', b'Belarus'), (b'BE', b'Belgium'), (b'BZ', b'Belize'), (b'BJ', b'Benin'), (b'BM', b'Bermuda'), (b'BT', b'Bhutan'), (b'BO', b'Bolivia, Plurinational State of'), (b'BA', b'Bosnia and Herzegovina'), (b'BW', b'Botswana'), (b'BV', b'Bouvet Island'), (b'BR', b'Brazil'), (b'IO', b'British Indian Ocean Territory'), (b'BN', b'Brunei Darussalam'), (b'BG', b'Bulgaria'), (b'BF', b'Burkina Faso'), (b'BI', b'Burundi'), (b'KH', b'Cambodia'), (b'CM', b'Cameroon'), (b'CA', b'Canada'), (b'CV', b'Cape Verde'), (b'KY', b'Cayman Islands'), (b'CF', b'Central African Republic'), (b'TD', b'Chad'), (b'CL', b'Chile'), (b'CN', b'China'), (b'CX', b'Christmas Island'), (b'CC', b'Cocos (Keeling) Islands'), (b'CO', b'Colombia'), (b'KM', b'Comoros'), (b'CG', b'Congo'), (b'CD', b'Congo, The Democratic Republic of the'), (b'CK', b'Cook Islands'), (b'CR', b'Costa Rica'), (b'CI', "C\xf4te d'Ivoire"), (b'HR', b'Croatia'), (b'CU', b'Cuba'), (b'CY', b'Cyprus'), (b'CZ', b'Czech Republic'), (b'DK', b'Denmark'), (b'DJ', b'Djibouti'), (b'DM', b'Dominica'), (b'DO', b'Dominican Republic'), (b'EC', b'Ecuador'), (b'EG', b'Egypt'), (b'SV', b'El Salvador'), (b'GQ', b'Equatorial Guinea'), (b'ER', b'Eritrea'), (b'EE', b'Estonia'), (b'ET', b'Ethiopia'), (b'FK', b'Falkland Islands (Malvinas)'), (b'FO', b'Faroe Islands'), (b'FJ', b'Fiji'), (b'FI', b'Finland'), (b'FR', b'France'), (b'GF', b'French Guiana'), (b'PF', b'French Polynesia'), (b'TF', b'French Southern Territories'), (b'GA', b'Gabon'), (b'GM', b'Gambia'), (b'GE', b'Georgia'), (b'DE', b'Germany'), (b'GH', b'Ghana'), (b'GI', b'Gibraltar'), (b'GR', b'Greece'), (b'GL', b'Greenland'), (b'GD', b'Grenada'), (b'GP', b'Guadeloupe'), (b'GU', b'Guam'), (b'GT', b'Guatemala'), (b'GG', b'Guernsey'), (b'GN', b'Guinea'), (b'GW', b'Guinea-Bissau'), (b'GY', b'Guyana'), (b'HT', b'Haiti'), (b'HM', b'Heard Island and McDonald Islands'), (b'VA', b'Holy See (Vatican City State)'), (b'HN', b'Honduras'), (b'HK', b'Hong Kong'), (b'HU', b'Hungary'), (b'IS', b'Iceland'), (b'IN', b'India'), (b'ID', b'Indonesia'), (b'IR', b'Iran, Islamic Republic of'), (b'IQ', b'Iraq'), (b'IE', b'Ireland'), (b'IM', b'Isle of Man'), (b'IL', b'Israel'), (b'IT', b'Italy'), (b'JM', b'Jamaica'), (b'JP', b'Japan'), (b'JE', b'Jersey'), (b'JO', b'Jordan'), (b'KZ', b'Kazakhstan'), (b'KE', b'Kenya'), (b'KI', b'Kiribati'), (b'KP', b"Korea, Democratic People's Republic of"), (b'KR', b'Korea, Republic of'), (b'KW', b'Kuwait'), (b'KG', b'Kyrgyzstan'), (b'LA', b"Lao People's Democratic Republic"), (b'LV', b'Latvia'), (b'LB', b'Lebanon'), (b'LS', b'Lesotho'), (b'LR', b'Liberia'), (b'LY', b'Libyan Arab Jamahiriya'), (b'LI', b'Liechtenstein'), (b'LT', b'Lithuania'), (b'LU', b'Luxembourg'), (b'MO', b'Macao'), (b'MK', b'Macedonia, The Former Yugoslav Republic of'), (b'MG', b'Madagascar'), (b'MW', b'Malawi'), (b'MY', b'Malaysia'), (b'MV', b'Maldives'), (b'ML', b'Mali'), (b'MT', b'Malta'), (b'MH', b'Marshall Islands'), (b'MQ', b'Martinique'), (b'MR', b'Mauritania'), (b'MU', b'Mauritius'), (b'YT', b'Mayotte'), (b'MX', b'Mexico'), (b'FM', b'Micronesia, Federated States of'), (b'MD', b'Moldova, Republic of'), (b'MC', b'Monaco'), (b'MN', b'Mongolia'), (b'ME', b'Montenegro'), (b'MS', b'Montserrat'), (b'MA', b'Morocco'), (b'MZ', b'Mozambique'), (b'MM', b'Myanmar'), (b'NA', b'Namibia'), (b'NR', b'Nauru'), (b'NP', b'Nepal'), (b'NL', b'Netherlands'), (b'AN', b'Netherlands Antilles'), (b'NC', b'New Caledonia'), (b'NZ', b'New Zealand'), (b'NI', b'Nicaragua'), (b'NE', b'Niger'), (b'NG', b'Nigeria'), (b'NU', b'Niue'), (b'NF', b'Norfolk Island'), (b'MP', b'Northern Mariana Islands'), (b'NO', b'Norway'), (b'OM', b'Oman'), (b'PK', b'Pakistan'), (b'PW', b'Palau'), (b'PS', b'Palestinian Territory, Occupied'), (b'PA', b'Panama'), (b'PG', b'Papua New Guinea'), (b'PY', b'Paraguay'), (b'PE', b'Peru'), (b'PH', b'Philippines'), (b'PN', b'Pitcairn'), (b'PL', b'Poland'), (b'PT', b'Portugal'), (b'PR', b'Puerto Rico'), (b'QA', b'Qatar'), (b'RE', 'R\xe9union'), (b'RO', b'Romania'), (b'RU', b'Russian Federation'), (b'RW', b'Rwanda'), (b'BL', 'Saint Barth\xe9lemy'), (b'SH', b'Saint Helena, Ascension and Tristan Da Cunha'), (b'KN', b'Saint Kitts and Nevis'), (b'LC', b'Saint Lucia'), (b'MF', b'Saint Martin'), (b'PM', b'Saint Pierre and Miquelon'), (b'VC', b'Saint Vincent and the Grenadines'), (b'WS', b'Samoa'), (b'SM', b'San Marino'), (b'ST', b'Sao Tome and Principe'), (b'SA', b'Saudi Arabia'), (b'SN', b'Senegal'), (b'RS', b'Serbia'), (b'SC', b'Seychelles'), (b'SL', b'Sierra Leone'), (b'SG', b'Singapore'), (b'SK', b'Slovakia'), (b'SI', b'Slovenia'), (b'SB', b'Solomon Islands'), (b'SO', b'Somalia'), (b'ZA', b'South Africa'), (b'GS', b'South Georgia and the South Sandwich Islands'), (b'ES', b'Spain'), (b'LK', b'Sri Lanka'), (b'SD', b'Sudan'), (b'SR', b'Suriname'), (b'SJ', b'Svalbard and Jan Mayen'), (b'SZ', b'Swaziland'), (b'SE', b'Sweden'), (b'CH', b'Switzerland'), (b'SY', b'Syrian Arab Republic'), (b'TW', b'Taiwan'), (b'TJ', b'Tajikistan'), (b'TZ', b'Tanzania, United Republic of'), (b'TH', b'Thailand'), (b'TL', b'Timor-Leste'), (b'TG', b'Togo'), (b'TK', b'Tokelau'), (b'TO', b'Tonga'), (b'TT', b'Trinidad and Tobago'), (b'TN', b'Tunisia'), (b'TR', b'Turkey'), (b'TM', b'Turkmenistan'), (b'TC', b'Turks and Caicos Islands'), (b'TV', b'Tuvalu'), (b'UG', b'Uganda'), (b'UA', b'Ukraine'), (b'AE', b'United Arab Emirates'), (b'GB', b'United Kingdom'), (b'US', b'United States'), (b'UM', b'United States Minor Outlying Islands'), (b'UY', b'Uruguay'), (b'UZ', b'Uzbekistan'), (b'VU', b'Vanuatu'), (b'VE', b'Venezuela, Bolivarian Republic of'), (b'VN', b'Viet Nam'), (b'VG', b'Virgin Islands, British'), (b'VI', b'Virgin Islands, U.S.'), (b'WF', b'Wallis and Futuna'), (b'EH', b'Western Sahara'), (b'YE', b'Yemen'), (b'ZM', b'Zambia'), (b'ZW', b'Zimbabwe')])),
                ('city', models.CharField(max_length=255, null=True, verbose_name='City', blank=True)),
                ('locale', kitsune.sumo.models.LocaleField(default=b'en-US', max_length=7, verbose_name='Preferred language', choices=[(b'af', 'Afrikaans'), (b'ar', '\u0639\u0631\u0628\u064a'), (b'az', 'Az\u0259rbaycanca'), (b'bg', '\u0411\u044a\u043b\u0433\u0430\u0440\u0441\u043a\u0438'), (b'bn-BD', '\u09ac\u09be\u0982\u09b2\u09be (\u09ac\u09be\u0982\u09b2\u09be\u09a6\u09c7\u09b6)'), (b'bn-IN', '\u09ac\u09be\u0982\u09b2\u09be (\u09ad\u09be\u09b0\u09a4)'), (b'bs', 'Bosanski'), (b'ca', 'catal\xe0'), (b'cs', '\u010ce\u0161tina'), (b'da', 'Dansk'), (b'de', 'Deutsch'), (b'ee', '\xc8\u028begbe'), (b'el', '\u0395\u03bb\u03bb\u03b7\u03bd\u03b9\u03ba\u03ac'), (b'en-US', 'English'), (b'es', 'Espa\xf1ol'), (b'et', 'eesti keel'), (b'eu', 'Euskara'), (b'fa', '\u0641\u0627\u0631\u0633\u06cc'), (b'fi', 'suomi'), (b'fr', 'Fran\xe7ais'), (b'fy-NL', 'Frysk'), (b'ga-IE', 'Gaeilge (\xc9ire)'), (b'gl', 'Galego'), (b'gu-IN', '\u0a97\u0ac1\u0a9c\u0ab0\u0abe\u0aa4\u0ac0'), (b'ha', '\u0647\u064e\u0631\u0652\u0634\u064e\u0646 \u0647\u064e\u0648\u0652\u0633\u064e'), (b'he', '\u05e2\u05d1\u05e8\u05d9\u05ea'), (b'hi-IN', '\u0939\u093f\u0928\u094d\u0926\u0940 (\u092d\u093e\u0930\u0924)'), (b'hr', 'Hrvatski'), (b'hu', 'Magyar'), (b'id', 'Bahasa Indonesia'), (b'ig', 'As\u1ee5s\u1ee5 Igbo'), (b'it', 'Italiano'), (b'ja', '\u65e5\u672c\u8a9e'), (b'km', '\u1781\u17d2\u1798\u17c2\u179a'), (b'ko', '\ud55c\uad6d\uc5b4'), (b'ln', 'Ling\xe1la'), (b'lt', 'lietuvi\u0173 kalba'), (b'ne-NP', '\u0928\u0947\u092a\u093e\u0932\u0940'), (b'nl', 'Nederlands'), (b'no', 'Norsk'), (b'pl', 'Polski'), (b'pt-BR', 'Portugu\xeas (do Brasil)'), (b'pt-PT', 'Portugu\xeas (Europeu)'), (b'ro', 'rom\xe2n\u0103'), (b'ru', '\u0420\u0443\u0441\u0441\u043a\u0438\u0439'), (b'si', '\u0dc3\u0dd2\u0d82\u0dc4\u0dbd'), (b'sk', 'sloven\u010dina'), (b'sl', 'sloven\u0161\u010dina'), (b'sq', 'Shqip'), (b'sr-Cyrl', '\u0421\u0440\u043f\u0441\u043a\u0438'), (b'sw', 'Kiswahili'), (b'sv', 'Svenska'), (b'ta', '\u0ba4\u0bae\u0bbf\u0bb4\u0bcd'), (b'ta-LK', '\u0ba4\u0bae\u0bbf\u0bb4\u0bcd (\u0b87\u0bb2\u0b99\u0bcd\u0b95\u0bc8)'), (b'te', '\u0c24\u0c46\u0c32\u0c41\u0c17\u0c41'), (b'th', '\u0e44\u0e17\u0e22'), (b'tr', 'T\xfcrk\xe7e'), (b'uk', '\u0423\u043a\u0440\u0430\u0457\u043d\u0441\u044c\u043a\u0430'), (b'ur', '\u0627\u064f\u0631\u062f\u0648'), (b'vi', 'Ti\u1ebfng Vi\u1ec7t'), (b'wo', 'Wolof'), (b'xh', 'isiXhosa'), (b'yo', '\xe8d\xe8 Yor\xf9b\xe1'), (b'zh-CN', '\u4e2d\u6587 (\u7b80\u4f53)'), (b'zh-TW', '\u6b63\u9ad4\u4e2d\u6587 (\u7e41\u9ad4)'), (b'zu', 'isiZulu')])),
            ],
            options={
                'permissions': (('view_karma_points', 'Can view karma points'), ('deactivate_users', 'Can deactivate users')),
            },
            bases=(models.Model, kitsune.search.models.SearchMixin),
        ),
        migrations.CreateModel(
            name='RegistrationProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activation_key', models.CharField(max_length=40, verbose_name='activation key')),
                ('user', models.ForeignKey(verbose_name='user', to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
                'verbose_name': 'registration profile',
                'verbose_name_plural': 'registration profiles',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=60, verbose_name='Value', blank=True)),
                ('user', models.ForeignKey(related_name='settings', verbose_name='User', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='setting',
            unique_together=set([('user', 'name')]),
        ),
        migrations.AddField(
            model_name='emailchange',
            name='user',
            field=models.ForeignKey(verbose_name='user', to=settings.AUTH_USER_MODEL, unique=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deactivation',
            name='moderator',
            field=models.ForeignKey(related_name='deactivations', verbose_name='moderator', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='deactivation',
            name='user',
            field=models.ForeignKey(related_name='+', verbose_name='user', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]