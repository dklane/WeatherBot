from aiohttp.http import SERVER_SOFTWARE
import discord
from discord.ext import commands
from discord.ext import tasks
import datetime
import random
from itertools import cycle
import json
import asyncio
import logging
from discord import Embed

client = commands.Bot(command_prefix = ',') 
client.remove_command('help')
status = cycle(['The Northern Atlantic', 'The Eastern Pacific', 'The Central Pacific', 'The Western Pacific', 'The Mediterranean Sea', 'The Southern Pacific', 'The Australian Region', 'The Arabian Sea', 'The Bay of Bengal', 'The Southwest Indian Ocean', 'The Southern Atlantic'])

#Bot presence
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd)
    change_status.start()
    print('Weather Bot (V1.6) is now active!')

#logging 

logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.CRITICAL)
logging.basicConfig(level=logging.ERROR)
logging.basicConfig(level=logging.WARNING)
logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


#Invalid command prompt
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Error: invalid command')
    else:
        await ctx.send('Error: invalid command')

@client.event
async def on_command_error_two(ctx, error):
    print('error')

#Gives ping number when user types =ping 
@client.command(aliases=['Ping'])
async def ping(ctx):
    embed = discord.Embed(
        colour = discord.Colour.green()
    )
    
    #Displays the ping number.
    embed.add_field(name='Pong!', value=(f'{round(client.latency * 1000)}ms'), inline=False)
    
    await ctx.send(embed=embed)

#Invite command
@client.command(aliases=['Invite'])
async def invite(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.blue()
    )

    embed.set_author(name='')
    embed.add_field(name='Weather Bot Invite', value='If you would like to invite Weather Bot to your own server, you can do so via this link: [Click Here](https://discord.com/api/oauth2/authorize?client_id=734979698983174235&permissions=8&scope=bot)', inline=False)
    await ctx.send(embed=embed)

#Command basically to test if the bot is online 
@client.command(aliases=['Hello'])
async def hello(ctx):
    await ctx.send('Im online!')

@client.command(aliases=['info', 'Info', 'Information'])
async def information(ctx):
    await ctx.send('```Have you ever received an alert on your mobile device or weather radio and wondered what the alert meant or what you should do during the alert? Weather Bot is pretty simple, it gives general information on what you should do if said alert is ever issued along with giving some tips on what to do when one is issued. Of course in the future this will not be the only thing Weather Bot does, but as of now that is its sole purpose currently.```')

@tasks.loop(minutes=30)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.command(aliases=['Tester', 'testers', 'Testers'])
async def tester(ctx):
    await ctx.send('Here is a link to the testing server for Weather Bot: https://discord.gg/GVzrs7mAqU')

@client.command(aliases=['Help'])
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.blue()
    )

    embed.set_author(name='Command Help Menu')
    embed.add_field(name='AlertHelp', value='Lists all weather-related alert commands.', inline=False)
    embed.add_field(name='Developers', value='Lists the amazing developers behind Weather Bot :3.', inline=False)
    embed.add_field(name='Help', value='Lists all the commands this bot has to offer.', inline=False)
    embed.add_field(name='Information', value='Gives a general description of what this bot is for.', inline=False)
    embed.add_field(name='Invite', value='Gives a link to invite Weather Bot to your server.', inline=False)
    embed.add_field(name='NHC', value='Gives information on NHC product release times.', inline=False)
    embed.add_field(name='Ping', value='Gives the bots ping.', inline=False)
    embed.add_field(name='Scales', value='Gives information on different scales for tornadoes, cyclones, etc...', inline=False)
    embed.add_field(name='Support', value='Get an invite for the Discord support server.', inline=False)
    embed.add_field(name='TCRs', value='Lists several links to Tropical Cyclone Report, Best Track Data, and many more data archives.', inline=False)
    embed.add_field(name='Tester', value='Gives a link to the Weater Bot Testing Server.', inline=False)
    await ctx.send(embed=embed)

@client.command(aliases=['Scales', 'scale', 'Scale'])
async def scales(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.dark_gold()
    )
    embed.set_author(name='Scales')
    embed.add_field(name='SSS', value='Defines the Saffir-Simpson Hurricane Wind Scale (SSHWS) in detail', inline=False)
    embed.add_field(name='EFS', value='Defines the Enhanced Fujita Scale (EF-Scale) in detail', inline=False)
    embed.add_field(name='AUS', value='Defines the Australian Cyclone Scale (AUS) in detail', inline=False)
    embed.add_field(name='IMD', value='Defines the Indian Meteorological Departments (IMD) cyclone scale in detail', inline=False)
    embed.add_field(name='PAGASA', value='Defines the PAGASA typhoon scale in detail', inline=False)
    embed.set_author(name='Alert Help')
    await ctx.send(embed=embed)
    
@client.command(aliases=['NHC'])
async def nhc(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.dark_gold()
    )
    embed.set_author(name='National Hurricane Center Information')
    embed.add_field(name='TWO', value='Gives the times for Tropical Weather Outlooks (TWOs)', inline=False)
    embed.add_field(name='TCA', value='Gives the times for Tropical Cyclone Advisories (TCAs)', inline=False)
    await ctx.send(embed=embed)

@client.command(aliases=['AlertHelp'])
async def alerthelp(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.dark_gold()
    )

    embed.set_author(name='Alert Help')
    embed.add_field(name='USAlerts', value='Lists commands that give information on United States alerts.', inline=False)
    embed.add_field(name='CAAlerts', value='Lists commands that give information on Canada alerts.', inline=False)
    embed.add_field(name='MXAlerts', value='(Coming Soon™) Lists commands that give information on Mexico alerts.', inline=False)
    await ctx.send(embed=embed)

@client.command(aliases=['USAlerts'])
async def usalerts(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.dark_gold()
    )

    embed.set_author(name='Alert Help')
    embed.add_field(name='TropicalAlerts (=TA)', value='Gives general information on tropical cyclone alerts', inline=False)
    embed.add_field(name='WinterAlerts (=WintA)', value='Gives general information on winter weather related alerts', inline=False)
    embed.add_field(name='SevereAlerts (=SA)', value='Gives general information on severe weather related alerts', inline=False)
    embed.add_field(name='WindAlerts (=WindA)', value='Gives general information on wind related alerts', inline=False)
    embed.add_field(name='MarineAlerts (=MA)', value='Gives general information on marine related alerts', inline=False)
    embed.add_field(name='FireAlerts (=FirA)', value='Gives general information on fire weather alerts', inline=False)
    embed.add_field(name='FloodAlerts (=FloA)', value='Gives general information on flooding alerts', inline=False)
    embed.add_field(name='HeatAlerts (=HA)', value='Gives general information on heat alerts', inline=False)
    await ctx.send(embed=embed)

@client.command(aliases=['Support'])
async def support(ctx):
    await ctx.send('Here is a permanent invite to the Weather Bot Support Server: https://discord.gg/8DXKEUgBeH')

@client.command(aliases=['TWO'])
async def two(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.blurple()
    )

    embed.set_author(name='Tropical Weather Outlook (TWO) Release Times')
    embed.add_field(name='IMPORTANT', value='The NHC releases TWOs regularly for both the Eastern/Central Pacific and Atlantic basins between the dates of May 15th to November 30th (Should be noted that the Atlantic Hurricane Season starts on June 1st). Outside of the seasons, Special Tropical Weather Outlooks (STWOs) will be issued if needed', inline=False)
    embed.add_field(name='06am UTC', value='(2am EDT, 1am EST)', inline=False)
    embed.add_field(name='12pm UTC', value='(8am EDT, 7am EST)', inline=False)
    embed.add_field(name='06pm UTC', value='(2pm EDT, 1pm EST)', inline=False)
    embed.add_field(name='12am UTC', value='(8pm EDT, 7pm EST)', inline=False)
    embed.add_field(name='NOTE', value='It is important to note that the NHC may issue TWOs earlier than stated here', inline=False)
    await ctx.send(embed=embed)

@client.command(aliases=['Advisory', 'StormAdvisories', 'advisories', 'Advisories', 'TCA', 'advisory'])
async def tca(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.red()
    )

    embed.set_author(name='Tropical Cyclone Advisories (TCA) Release Times')
    embed.add_field(name='IMPORTANT', value='The NHC releases TCAs when a tropical cyclone is active in the NATL, EPAC or CPAC. If a storm is not active, there will be no TCAs issued. In some cases or in the off-season, the NHC may issue Special Tropical Cyclone Advisories (STCAs) if needed. Typically, a tropical cyclone will only get a TCA every 6 hours however, if a tropical cyclone related alert is in effect, they will be issued every 3 hours. In cases such as a storm nearing landfall in the US, hourly position updates will be issued.', inline=False)
    embed.add_field(name='06am UTC (ONLY IF A TROPICAL CYCLONE ALERT IS IN EFFECT)', value='(2am EDT, 1am EST)', inline=False)
    embed.add_field(name='09am UTC', value='(5am EDT, 4am EST)', inline=False)
    embed.add_field(name='12pm UTC (ONLY IF A TROPICAL CYCLONE ALERT IS IN EFFECT)', value='(8am EDT, 7am EST)', inline=False)
    embed.add_field(name='03pm UTC', value='(11am EDT, 10am EST)', inline=False)
    embed.add_field(name='06pm UTC (ONLY IF A TROPICAL CYCLONE ALERT IS IN EFFECT)', value='(2pm EDT, 1pm EST)', inline=False)
    embed.add_field(name='09pm UTC', value='(5pm EDT, 4pm EST)', inline=False)
    embed.add_field(name='12am UTC (ONLY IF A TROPICAL CYCLONE ALERT IS IN EFFECT)', value='(8pm EDT, 7pm EST)', inline=False)
    embed.add_field(name='03am UTC', value='11pm EDT, 10pm EST)', inline=False)
    embed.add_field(name='NOTE', value='It is important to note that the NHC may issue TCAs earlier than stated here. To see more on tropical cyclone alerts, please type =TA', inline=False)
    await ctx.send(embed=embed)

#Gives general information on Tropical Cyclone Alerts
@client.command(aliases=['TropicalAlerts', 'TA', 'ta'])
async def tropicalalerts(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.red()
    )

    embed.set_author(name='Tropical Cyclone Alerts')
    embed.add_field(name='Tropical Storm Watch', value='A Tropical Storm Watch is issued when a tropical cyclone containing winds of 34 to 63 kt (39 to 73 mph) or higher poses a possible threat, generally within 48 hours. These winds may be accompanied by storm surge, coastal flooding, and/or river flooding.', inline=False)
    embed.add_field(name='Hurricane Watch', value='A Hurricane Watch is issued when a tropical cyclone containing winds of 64 kt (74 mph) or higher poses a possible threat, generally within 48 hours. These winds may be accompanied by storm surge, coastal flooding, and/or river flooding.', inline=False)
    embed.add_field(name='Storm Surge Watch', value='A storm surge watch is defined as the possibility of life-threatening inundation from rising water moving inland from the shoreline somwhere within the specified area, generally within 48 hours, in association with a tropical, subtropical, or post-tropical cyclone.', inline=False)
    embed.add_field(name='Tropical Storm Warning', value='A Tropical Storm Warning is issued when sustained winds of 34 to 63 kt (39 to 73 mph) or higher associated with a tropical cyclone are expected in 36 hours or less. These winds may be accompanied by storm surge, coastal flooding, and/or river flooding.', inline=False)
    embed.add_field(name='Hurricane Warning', value='A Hurricane Warning is issued when sustained winds of 64 kt (74 mph) or higher associated with a tropical cyclone are expected in 36 hours or less. These winds may be accompanied by storm surge, coastal flooding, and/or river flooding. A hurricane warning can remain in effect when dangerously high water or a combination of dangerously high water and exceptionally high waves continue, even though winds may be less than hurricane force. Preparations should be rushed to completion where one is issued as it is a very dangerous situation', inline=False)
    embed.add_field(name='Storm Surge Warning', value='A storm surge warning is defined as the danger of life-threatening inundation from rising water moving inland from the shoreline somewhere within the specified area, generally within 36 hours, in association with a tropical, subtropical, or post-tropical cyclone. This is a life-threatening situation and one should listen to local authorities and evacuate if told to do so', inline=False)
    embed.add_field(name='Extreme Wind Warning', value='An Extreme Wind Warning is issued for surface winds of 100 knots (115 MPH) or greater associated with non-convective, downslope, derecho (NOT associated with a tornado), or sustained hurricane winds are expected to occur within one hour. TAKE SHELTER IMMEDIATELY! This is an extremely dangerous and life-threatening situation', inline=False)
    embed.add_field(name='_ _', value='For a detailed look at the Saffir Simpson Hurricane Wind Scale, please type =SSS')
    embed.add_field(name='_ _', value='For more info, please visit https://www.weather.gov/lwx/WarningsDefined', inline=False)
    await ctx.send(embed=embed)

#Defines the SSHWS in detail
@client.command(aliases=['SSS', 'SaffirSimpsonScale', 'saffirsimpsonscale', 'sshws', 'SSHWS'])
async def sss(ctx):
    author = ctx.message.author
    
    embed = discord.Embed(
        colour = discord.Colour.dark_gold()
    )

    embed.set_author(name='Saffir Simpson Scale')
    embed.add_field(name='Tropical Depression', value='(<39mph) Breezy conditions and heavy rain can be expected from Tropical Depressions.')
    embed.add_field(name='Tropical Storm', value='(39-73mph) Gusty winds could cause damage to roof, shingles, vinyl siding and gutters. Small to Large branches could snap and shallow rooted trees could be topples. Power outages are possible and heavy rainfall is likely.', inline=False)
    embed.add_field(name='Category 1', value='(74-95mph) Well-constructed frame homes could have damage to roof, shingles, vinyl siding and gutters. Large branches of trees will snap and shallowly rooted trees may be toppled. Extensive damage to power lines and poles likely will result in power outages that could last a few to several days.', inline=False)
    embed.add_field(name='Category 2', value='(96-110mph) Well-constructed frame homes could sustain major roof and siding damage. Many shallowly rooted trees will be snapped or uprooted and block numerous roads. Near-total power loss is expected with outages that could last from several days to weeks.', inline=False)
    embed.add_field(name='Category 3', value='(111-129mph) Well-built framed homes may incur major damage or removal of roof decking and gable ends. Many trees will be snapped or uprooted, blocking numerous roads. Electricity and water will be unavailable for several days to weeks after the storm passes.', inline=False)
    embed.add_field(name='Category 4', value='(130-156mph) Well-built framed homes can sustain severe damage with loss of most of the roof structure and/or some exterior walls. Most trees will be snapped or uprooted and power poles downed. Fallen trees and power poles will isolate residential areas. Power outages will last weeks to possibly months. Most of the area will be uninhabitable for weeks or months.', inline=False)
    embed.add_field(name='Category 5', value='(157mph+) A high percentage of framed homes will be destroyed, with total roof failure and wall collapse. Fallen trees and power poles will isolate residential areas. Power outages will last for weeks to possibly months. Most of the area will be uninhabitable for weeks or months.', inline=False)
    embed.add_field(name='_ _', value='For more info, please visit https://www.nhc.noaa.gov/aboutsshws.php', inline=False)
    await ctx.send(embed=embed)


@client.command(aliases=['EFScale', 'EFS', 'efscale'])
async def efs(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.dark_orange()
    )

    embed.set_author(name='Enhanced Fujita Scale')
    embed.add_field(name='EF0', value='(65-85mph) Peels surface off some roofs; some damage to gutters or siding; branches broken off trees; shallow-rooted trees pushed over. Confirmed tornadoes with no reported damage (i.e., those that remain in open fields) have also been rated EF0. While permanent buildings generally suffer only minor damage, unprotected mobile homes or trailers may sustain moderate to serious damage.', inline=False)
    embed.add_field(name='EF1', value='(86-110mph) Roofs severely stripped; mobile homes overturned or badly damaged; loss of exterior doors; windows and other glass broken.', inline=False)
    embed.add_field(name='EF2', value='(111-135mph) Roofs torn off from well-constructed houses; foundations of frame homes shifted; mobile homes completely destroyed; large trees snapped or uprooted; light-object missiles generated; cars lifted off ground.', inline=False)
    embed.add_field(name='EF3', value='(136-165mph) Entire stories of well-constructed houses destroyed; severe damage to large buildings such as shopping malls; trains overturned; trees debarked; heavy cars lifted off the ground and thrown; structures with weak foundations are badly damaged.', inline=False)
    embed.add_field(name='EF4', value='(166-200mph) Well-constructed and whole frame houses completely leveled; some frame homes may be swept away; cars and other large objects thrown and small missiles generated.', inline=False)
    embed.add_field(name='EF5', value='(200mph+) Well-built frame houses destroyed with foundations swept clean of debris; steel-reinforced concrete structures are critically damaged; tall buildings collapse or have severe structural deformations; cars, trucks, and trains can be thrown approximately 1 mile (1.6 km).', inline=False)
    embed.add_field(name='_ _', value='For more info, please visit https://www.weather.gov/oun/efscale', inline=False)
    await ctx.send(embed=embed)

@client.command(aliases=['WinterAlerts', 'WintA', 'wintA', 'winta', 'Winta'])
async def winteralerts(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.blue()
    )

    embed.set_author(name='Winter Weather Alerts')
    embed.add_field(name='Winter Weather Advisory', value='A Winter Weather Advisory will be issued for any amount of freezing rain, or when 2 to 4 inches of snow (alone or in combination with sleet and freezing rain), is expected to cause a significant inconvenience, but not serious enough to warrant a warning.', inline=False)
    embed.add_field(name='Winter Storm Watch', value='A Winter Storm Watch is issued when there is the potential for significant and hazardous winter weather within 48 hours. It does not mean that significant and hazardous winter weather will occur...it only means it is possible.', inline=False)
    embed.add_field(name='Winter Storm Warning', value='A Winter Storm Warning is issued when a significant combination of hazardous winter weather is occurring or imminent.', inline=False)
    embed.add_field(name='Blizzard Warning', value='A Blizzard Warning means that the following conditions are occurring or expected within the next 12 to 18 hours. 1) 5 inches or more of snow/sleet within a 12-hour period or 7 inches of snow/sleet within a 24-hour period AND/OR Enough ice accumulation to cause damage to trees or powerlines. AND/OR a life threatening or damaging combination of snow and/or ice accumulation with wind.', inline=False)
    embed.add_field(name='Ice Storm Warning', value='¼ inch or more of ice accumulation.', inline=False)
    embed.add_field(name='Temperature Related Alerts', value='_ _', inline=False)
    embed.add_field(name='Frost Advisory', value='A Frost Advisory is issued when the minimum temperature is forecast to be 33 to 36 degrees on clear and calm nights during the growing season and this can be issued in Autumn near the end of the growing season.', inline=False)
    embed.add_field(name='Freeze Watch', value='A Freeze Watch is issued when there is a potential for significant, widespread freezing temperatures within the next 24-36 hour, typically issued during the growing season', inline=False)
    embed.add_field(name='Freeze Warning', value='A Freeze Warning is issued when significant, widespread freezing temperatures are expected. This is typically issued during the growing season', inline=False)
    embed.add_field(name='Wind Chill Advisory', value='A Wind Chill Advisory is issued when wind chills of -5F to -19F are expected east of the Blue Ridge Mountains, and when wind chills of -10 to -24F are expected along and west of the Blue Ridge Mountains and in Frederick and Carroll Counties in Maryland.', inline=False)
    embed.add_field(name='Wind Chill Warning', value='A Wind Chill Warning is issued when wind chills of -20F or lower are expected east of the Blue Ridge Mountains, and when wind chills of -25F or lower are expected along and west of the Blue Ridge Mountains and in Frederick and Carroll Counties in Maryland.', inline=False)
    embed.add_field(name='_ _', value='For more info, please visit https://www.weather.gov/lwx/WarningsDefined', inline=False)
    await ctx.send(embed=embed)

@client.command(aliases=['SevereAlerts', 'SA', 'sa'])
async def severealerts(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.red()
    )

    embed.set_author(name='Severe Weather Alerts')
    embed.add_field(name='Severe Thunderstorm Watch', value='A Severe Thunderstorm Watch is issued when severe thunderstorms are possible in and near the watch area. It does not mean that they will occur. It only means they are possible. Be prepared to take action if it ever is issued issued for your area.', inline=False)
    embed.add_field(name='Severe Thunderstorm Warning', value='A Severe Thunderstorm Warning is issued when severe thunderstorms are occurring or imminent in the warning area. If this is ever issued for your area, TAKE IMMEDIATE ACTION!', inline=False)
    embed.add_field(name='PDS Severe Thunderstorm Watch', value='PDS (Particularly Dangerous Situation) Severe Thunderstorm Watches are issued when there is a higher than normal risk of severe thunderstorm winds capable of major structural damage (in addition to large hail and perhaps a few isolated tornadoes), usually due to a strong and persistent derecho. Be prepared to take action if it ever is issued issued for your area.', inline=False)
    embed.add_field(name='PDS Severe Thunderstorm Warning', value='PDS Severe Thunderstorm Warnings are issued when a severe thunderstorm produces wind gusts >=80mph AND/OR the severe thunderstorm is producing >=2.75" hail (baseball size). If this is ever issued for your area, TAKE IMMEDIATE ACTION!', inline=False)
    embed.add_field(name='Tornado Watch', value='A Tornado Watch is issued when severe thunderstorms and tornadoes are possible in and near the watch area. It does not mean that they will occur. It only means they are possible. Be prepared to take action if it ever is issued issued for your area.', inline=False)
    embed.add_field(name='Tornado Warning', value='A Tornado Warning is issued when a tornado is imminent. When a tornado warning is issued, seek safe shelter immediately. If this is ever issued for your area, TAKE IMMEDIATE ACTION!', inline=False)
    embed.add_field(name='PDS Tornado Watch', value='PDS tornado wathces are issued when the forecaster has high confidence that multiple strong EF2-EF3 tornadoes or Violent tornadoes (EF4-EF5) will occur in the watch area. If this is issued, make sure to take extreme precaution. Be prepared to take action if it ever is issued issued for your area.', inline=False)
    embed.add_field(name='PDS Tornado Warning', value='The criteria for a PDS warning are when a tornado on the ground has been spotted or confirmed, or a significant tornado is expected based on radar signatures. PDS tornado warnings are structured as the second highest level of tornado warning within the impact based warning system. If this is ever issued for your area, TAKE IMMEDIATE ACTION!', inline=False)
    embed.add_field(name='TORNADO EMERGENCY', value='A tornado emergency is an enhanced version of a tornado warning, which is used by the National Weather Service (NWS) in the United States during imminent, significant tornado occurrences in highly populated areas. If this is ever issued for your area, TAKE IMMEDIATE ACTION without hesitation or delay!', inline=False)
    embed.add_field(name='_ _', value='For more info, please visit https://www.weather.gov/lwx/WarningsDefined', inline=False)
    embed.add_field(name='_ _', value='For information on the Enhanced Fujita Scale, Please type the command =EFS', inline=False)
    embed.add_field(name='_ _', value='For more info on PDS alerts, please visit https://www.spc.noaa.gov/publications/dean/pdswatch.pdf', inline=False)
    await ctx.send(embed=embed)

@client.command(aliases=['WindAlerts', 'wind', 'Wind', 'WindA', 'windA', 'Winda', 'winda'])
async def windalerts(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.dark_green()
    )
    
    embed.set_author(name='Wind Alerts')
    embed.add_field(name='Special Weather Statement', value='If there is the possibility of gusty winds that dont quite reach the wind alerts criteria (<31mph), a special weather statement will be issued.', inline=False)
    embed.add_field(name='Wind Advisory', value='A Wind Advisory is issued when sustained winds of 31-39mph occur for an hour or more AND/OR wind gusts of 46-57mph occur for any duration.', inline=False)
    embed.add_field(name='High Wind Watch', value='A High Wind Watch is issued when the following conditions are possible: sustained winds >40mph occur for an hour or more OR wind gusts >=58mph occur for any duration', inline=False)
    embed.add_field(name='High Wind Warning', value='A High Wind Warning is issued when the following conditions are expected: sustained winds >40mph occur for an hour or more OR wind gusts >=58mph occur for any duration', inline=False)
    embed.add_field(name='_ _', value='For more info, please visit https://www.weather.gov/lwx/WarningsDefined', inline=False)
    await ctx.send(embed=embed)

@client.command(aliases=['MarineAlerts', 'Marine', 'marine', 'MA', 'ma'])
async def marinealerts(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.light_gray()
    )
    
    embed.set_author(name='Marine Alerts')
    embed.add_field(name='Small Craft Advisory', value='Small Craft Advisories are issued for the Tidal Potomac River and the Chesapeake Bay when one or both of the following conditions is expected to begin within 36 hours: sustained winds of 18 knots to 33 knots OR frequent gusts (duration of two or more hours) between 18 knots and 33 knots. OR waves of 4 feet or higher', inline=False)
    embed.add_field(name='Gale Warning', value='Gale Warnings are issued for the Tidal Potomac River and the Chesapeake Bay when one or both of the following conditions is expected to begin within 36 hours and not directly associated with a tropical cyclone: sustained winds of 34 knots to 47 knots OR frequent gusts (duration of two or more hours) between 34 knots and 47 knots.', inline=False)
    embed.add_field(name='Storm Warning', value='Storm Warnings are issued for the Tidal Potomac River and the Chesapeake Bay when one or both of the following conditions is expected to begin within 36 hours and not directly associated with a tropical cyclone: sustained winds of 48 knots to 63 knots OR frequent gusts (duration of two or more hours) of 48 knots to 63 knots', inline=False)
    embed.add_field(name='Hurricane Force Wind Warning', value='Hurricane Force Wind Warnings are issued for the Tidal Potomac River and the Chesapeake Bay when one or both of the following conditions is expected to begin within 36 hours and not directly associated with a tropical cyclone: sustained winds of 64 knots or greater OR frequent gusts (duration of two or more hours) of 64 knots or greater', inline=False)
    embed.add_field(name='Special Marine Warning', value='A warning of potentially hazardous weather conditions of short duration (up to 2 hours) affecting areas included in a CWF that are not adequately covered by existing marine warnings and producing one or more of the following: Sustained marine convective winds (showers/thunderstorms) or associated gusts of 34 knots or greater AND/OR Hail three quarters of an inch or more in diameter AND/OR Waterspouts', inline=False)
    embed.add_field(name='_ _', value='For more info, please visit https://www.weather.gov/lwx/WarningsDefined', inline=False)
    await ctx.send(embed=embed)

@client.command(aliases=['FireAlerts', 'FireWX', 'Firewx', 'FireWx', 'firewx', 'fireWx', 'firewX', 'fira', 'Fira', 'FirA', 'firA'])
async def firealerts(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.red()
    )
    
    embed.set_author(name='Fire Weather Alerts')
    embed.add_field(name='Fire Weather Watch', value='A Fire Weather Watch is issued to alert fire officials and firefighters of potentially dangerous fire weather conditions within the next 24 to 36 hours. They are issued when the following three criteria are met: Surface realative humidity less than 30% for VA and MD; relative humidity <=25% for WV AND Sustaned surface winds are >=20mph AND 10-hour fuel moisture less than 8% for VA; <=8% for MD and WV', inline=False)
    embed.add_field(name='Red Flag Warning', value='A Red Flag Warning is issued to alert fire officials and firefighters of potentially dangerous fire weather conditions within the next 12 to 24 hours. They are issued when the following three criteria are met: Surface relative humidity less than 30% for VA and MD; relative humidity <=25% for WV AND sustained surface winds >20mph AND 10-hour fuel moisture less than 8% for VA; <=8% for MD and WV', inline=False)
    embed.add_field(name='_ _', value='For more info, please visit https://www.weather.gov/lwx/WarningsDefined', inline=False)
    await ctx.send(embed=embed)

@client.command(aliases=['FloodAlerts', 'FloA', 'Floa', 'floA', 'floa'])
async def floodalerts(ctx):
    author = ctx.message.author
    
    embed = discord.Embed(
        colour = discord.Colour.green()
    )

    embed.set_author(name='Flooding Alerts')
    embed.add_field(name='Costal Flood Advisory', value='A Coastal Flood Advisory is issued when minor or nuisance coastal flooding is occurring or imminent.', inline=False)
    embed.add_field(name='Costal Flood Watch', value='A Coastal Flood Watch is issued when moderate to major coastal flooding is possible. Such flooding would potentially pose a serious risk to life and property.', inline=False)
    embed.add_field(name='Costal Flood Warning', value='A Coastal Flood Warning is issued when moderate to major coastal flooding is occurring or imminent. This flooding will pose a serious risk to life and property.', inline=False)
    embed.add_field(name='Flash Flood Watch', value='A Flash Flood Watch is issued when conditions are favorable for flash flooding usually in 24-36 hours. It does not mean that flash flooding will occur, but it is possible.', inline=False)
    embed.add_field(name='Flash Flood Warning', value='A Flash Flood Warning is issued when flash flooding is imminent or occurring. Heavy rain will cause or is causing a significant rise of water levels in urban areas and along small creeks and streams in 6 hours or less.', inline=False)
    embed.add_field(name='Flash Flood EMERGENCY', value='Extreme and life-threatening flash flooding is occurring or is imminent. Waters will rise very quickly and significant property damage is likely. MOVE TO HIGHER GROUND IMMEDIATELY!', inline=False)
    embed.add_field(name='Areal Flood Advisory', value='A gradual and minor flooding of low lying areas is expected to occur over the next few hours.', inline=False)
    embed.add_field(name='Flood Watch', value='A Flood Watch is issued when conditions are favorable for flooding. It does not mean flooding will occur, but it is possible.', inline=False)
    embed.add_field(name='Flood Warning', value='A Flood Warning is issued when flooding is imminent or occurring.', inline=False)
    embed.add_field(name='Hydrologic Outlook', value='Past, present or future persistent rains will bring an increased risk of small creek and streams flooding as well as well as river flooding.', inline=False)
    embed.add_field(name='River Flood Watch', value='A River Flood Watch is issued when river flooding is possible at one or more forecast points along a river.', inline=False)
    embed.add_field(name='River Flood Warning', value='A River Flood Warning is issued when river flooding is occurring or imminent at one or more forecast points along a river.', inline=False)
    embed.add_field(name='_ _', value='For more info, please visit https://www.weather.gov/lwx/WarningsDefined', inline=False)
    await ctx.send(embed=embed)

@client.command(aliases=['HeatAlerts', 'HA', 'ha'])
async def heatalerts(ctx):
    author = ctx.message.author
    
    embed = discord.Embed(
        colour = discord.Colour.orange()
    )

    embed.set_author(name='Heat Alerts')
    embed.add_field(name='Excessive Heat Watch', value='An Excessive Heat Watch is issued when there is a potential for the heat index value to reach or exceed 110 degrees (east of the Blue Ridge) or 105 degrees (west of the Blue Ridge) within the next 24 to 48 hours.', inline=False)
    embed.add_field(name='Excessive Heat Warning', value='An Excessive Heat Warning is issued when the heat index value is expected to reach or exceed 110 degrees (east of the Blue Ridge) or 105 degrees (west of the Blue Ridge) within the next 12 to 24 hours. An Excessive Heat Warning may be issued for lower criteria if it is early in the season or during a multi-day heat wave.', inline=False)
    embed.add_field(name='Heat Advisory', value='A Heat Advisory is issued when the heat index value is expected to reach 105 to 109 degrees (east of the Blue Ridge) or 100 to 104 degrees (west of the Blue Ridge) within the next 12 to 24 hours. A Heat Advisory may be issued for lower criteria if it is early in the season or during a multi-day heat wave.', inline=False)
    embed.add_field(name='_ _', value='For more info, please visit https://www.weather.gov/lwx/WarningsDefined', inline=False)
    await ctx.send(embed=embed)

#CANADA ALERTS

@client.command(aliases=['CAAlerts', 'Canada'])
async def caalerts(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.dark_gold()
    )

    embed.set_author(name='Alert Help')
    #Yukon Alerts Complete*
    embed.add_field(name='Yukon (Y)', value='Lists alerts that can be issued in Yukon, Canada', inline=False)
    #British Columbia Alerts Complete*
    embed.add_field(name='BritishColumbia (BC)', value='Lists alerts that can be issued in Bristish Columbia, Canada', inline=False)
    #Northwest Territories Alerts Complete*
    embed.add_field(name='NorthwestTerritories (NWT)', value='Lists alerts that can be issued in Northwest Territories, Canada', inline=False)
    #Alberta Alerts Complete*
    embed.add_field(name='Alberta (A)', value='Lists alerts that can be issued in Alberta, Canada', inline=False)
    #Nunavut Alerts Complete*
    embed.add_field(name='Nunavut (N)', value='Lists alerts that can be issued in Nunavut, Canada', inline=False)
    #Saskatchewan Alerts Complete*
    embed.add_field(name='Saskatchewan (S)', value='Lists alerts that can be issued in Saskatchewan, Canada', inline=False)
    #Manitoba Alerts Complete*
    embed.add_field(name='Manitoba (M)', value='Lists alerts that can be issued in Manitoba, Canada', inline=False)
    #Ontario Alerts Complete*
    embed.add_field(name='Ontario (O)', value='Lists alerts that can be issued in Ontario, Canada', inline=False)
    #Quebec Alerts Complete*
    embed.add_field(name='Quebec (Q)', value='Lists alerts that can be issued in Quebec, Canada', inline=False)
    #New Foundland and Labrador Alerts Complete*
    embed.add_field(name='NewfoundlandLabrador (NF)', value='Lists alerts that can be issued in Newfoundland and Labrador, Canada', inline=False)
    #New Brunswick Alerts Complete*
    embed.add_field(name='NewBrunswick (NB)', value='Lists alerts that can be issued in New Brunswick, Canada', inline=False)
    #Prince Edward Island Alerts Complete*
    embed.add_field(name='PrinceEdward (PE)', value='Lists alerts that can be issued in Prince Edward Island, Canada', inline=False)
    #Nova Scotia Alerts Complete*
    embed.add_field(name='NovaScotia (NS)', value='Lists alerts that can be issued in Nova Scotia, Canada', inline=False)
    #*Need to figure out multi-page embeds
    await ctx.send(embed=embed)

@client.command(aliases=['Yukon', 'Y', 'y'])
async def yukon(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.greyple()
    )
    embed.set_author(name='Yukon, Canada Alerts')
    embed.add_field(name='Blizzard Warning', value='When winds of 40 km/hr or greater are expected to cause widespread reductions in visibility to 400 metres or less, due to blowing snow, or blowing snow in combination with falling snow, for at least 4 hours. If North of the tree line, the conditions are expected to last for at least 6 hours.', inline=False)
    embed.add_field(name='Blowing Snow Advisory', value='When blowing snow, caused by winds of at least 30 km/h, is expected to reduce visibility to 800 metres or less for at least 3 hours. Cannot be issued North of the tree line.', inline=False)
    embed.add_field(name='Extreme Cold Warning', value='Issued when the temperature or wind chill is expected to reach minus 50°C for at least two hours.', inline=False)
    embed.add_field(name='Flash Freeze Warning', value='When significant ice is expected to form on roads, sidewalks or other surfaces over much of a region because of the freezing of residual water from either melted snow, or falling/fallen rain due to a rapid drop in temperatures.', inline=False)
    embed.add_field(name='Fog Advisory', value='When low visibilities in fog are expected for at least six hours.', inline=False)
    embed.add_field(name='Freezing Drizzle Advisory', value='When a period of freezing drizzle is expected for at least eight hours.', inline=False)
    embed.add_field(name='Freezing Rain Warning', value='When freezing rain is expected to pose a hazard to transportation or property; Or When freezing rain is expected for at least two hours.', inline=False)
    embed.add_field(name='Heat Warning', value='Issued when 2 or more consecutive days of daytime maximum temperatures are expected to reach 28°C or warmer and nighttime minimum temperatures are expected to fall to 13°C or warmer.', inline=False)
    embed.add_field(name='Hurricane Watch', value='When, within the following 36 hours, a hurricane or a developing hurricane is expected to pose a possible threat, with the risk of hurricane force winds (average sustained winds of 118 km/h or higher) threatening the area.', inline=False)
    embed.add_field(name='Hurricane Warning', value='When hurricane-force gales (average sustained winds of 118 km/h or higher) caused by a hurricane, or a strong tropical storm that may strengthen to hurricane force before making landfall, are expected to occur in 24 hours or less.  It may also include areas where storm surge or exceptionally high waves are expected, even though winds may be less than hurricane force.', inline=False)
    embed.add_field(name='Rainfall Warning (Alerting parameters for a Short Duration Rainfall (Heavy Downpour) Warning)', value='When 25mm or more of rain is expected within one hour.', inline=False)
    embed.add_field(name='Rainfall Warning (Alerting parameters Environment Canada uses for issuing a Long Duration Rainfall Warning in the Summer)', value='When 50mm or more of rain is expected within 24 hours; OR When 75mm or more of rain is expected within 48 hours.', inline=False)
    embed.add_field(name='Rainfall Warning (Alerting parameters Environment Canada uses for issuing a Long Duration Rainfall Warning in the Winter)', value='When 25 mm or more of rain is expected within 24 hours.', inline=False)
    embed.add_field(name='Rainfall Warning (Alerting parameters Environment Canada uses for issuing a Long Duration Rainfall Warning during a Thaw Only)', value='When 25mm or more of rain is expected within 24 hours.', inline=False)
    embed.add_field(name='Severe Thunderstorm Watch', value='When conditions are favourable for the development of severe thunderstorms with one or more of the following conditions: Wind gusts of 90km/h or greater, which could cause structural wind damage; hail greater than 2cm in diameter; or Heavy rainfall, as per rainfall criteria, excluding those for winter and during thaw')
    embed.add_field(name='Severe Thunderstorm Warning', value='When there is evidence based on radar, satellite pictures, or from a reliable spotter that any one or more of the following three weather conditions is imminent or occurring: Wind gusts of 90km/h or greater, which could cause structural wind damage; hail greater than 2cm in diameter; or Heavy rainfall, as per rainfall criteria, excluding those for winter and during thaw', inline=False)
    embed.add_field(name='Snowfall Warning', value='When 20 cm or more of snow falls within 24 hours or less OR When 10 cm or more of snow falls within 12 hours or less.', inline=False)
    embed.add_field(name='(Open-Water) Snow Squall Watch', value='When conditions are favourable for the development of open water snow squall down wind of large bodies of water, like the Great Lakes, with one or more of the following conditions: Localized, intense snowfall producing snowfall amounts of 15 cm or more in 12 hours or less. AND/OR Reduced visibility (less than 400 metres) caused by heavy snow with or without blowing snow for 3 hours or more.', inline=False)
    embed.add_field(name='(Frontal) Snow Squall Watch', value='When conditions are favourable for the development of brief periods of very poor visibilities caused by heavy snow and blowing snow.', inline=False)
    embed.add_field(name='(Open-Water) Snow Squall Warning', value='When, down wind of large bodies of water, like the Great Lakes, snow squalls are imminent or occurring with one or more of the following conditions being produced: Localized, intense snowfall producing snowfall amounts of 15 cm or more in 12 hours or less. AND/OR Reduced visibility (less than 400 metres) caused by heavy snow with or without blowing snow for 3 hours or more.', inline=False)
    embed.add_field(name='(Frontal) Snow Squall Warning', value='When there is a brief period (less than one hour) of very poor visibility (400 m or less), caused by heavy snow and blowing snow, and accompanied by strong, gusty winds of 45 km/h or greater, is expected to occur with the passage of a cold front.', inline=False)
    embed.add_field(name='Tornado Watch', value='When conditions are favourable for the development of severe thunderstorms with one or more tornadoes.', inline=False)
    embed.add_field(name='Tornado Warning', value='When a tornado has been reported; or when there is evidence based on radar, or from a reliable spotter that a tornado is imminent.', inline=False)
    embed.add_field(name='Tropical Storm Watch', value='When, within the following 36 hours, a tropical storm or a developing tropical storm is expected to pose a possible threat, with the risk of tropical-storm force winds (average sustained winds of 63-117 km/h) threatening the area. This watch could be issued for: A tropical storm; or A hurricane that might approach an area but be far enough away that it is expected to bring gales that are less than hurricane force (118 km/h or higher).', inline=False)
    embed.add_field(name='Tropical Storm Warning', value='When coastal and/or coastal winds of 63 to 117 km/h caused by a tropical cyclone are expected to occur.', inline=False)
    
    #Note - The above code is the max one can put into one embed
    #Will need to figure out how to create multi-page embeds for this update to release publicly
    '''
    embed.add_field(name='Weather Advisory', value=' generic weather advisory. One example might be on days when funnel clouds are expected, but a Tornado alert would not be appropriate.', inline=False)
    embed.add_field(name='Weather Warning', value='A generic weather warning may be issued for extreme weather events for which there is no suitable warning type, because they rarely occur. ', inline=False)
    embed.add_field(name='_ _', value='A generic weather warning may also be issued for other weather events during situations where the environment is vulnerable due to pre-existing conditions and any further weather could result in a significant hazard. For example: 50 km/h winds following an ice storm which could cause structural wind damage.', inline=False)
    embed.add_field(name='_ _', value='A generic weather warning may also be issued for situations where the event is not expected to reach warning criteria values, but there is a special reason for the warning. For example: the first event of the season, or an off-season event.', inline=False)
    #The two lines above this comment are extensions from the "Weather Warning" alert.
    embed.add_field(name='Wind Warning (Except Dempster)', value='80 km/h or more sustained wind; and/or Gusts to 100 km/h or more.', inline=False)
    embed.add_field(name='Winter Storm Watch', value='When conditions are favorable for the development of severe and potentially dangerous winter weather, including: A blizzard, A major snowfall (25cm or more within a 24 hour period); and significant snowfall (snowfall warning criteria amounts) combined with other winter weather hazard types such as: freezing rain, strong winds, blowing snow, and/or extreme wind chill. ', inline=False)
    embed.add_field(name='Winter Storm Warning', value='When severe and potentially dangerous winter weather conditions are expected, including: A major snowfall (25cm or more within a 24 hour period); and A significant snowfall (snowfall warning criteria amoubts) combined with other cold weather precipitation types such as: freezing rain, strong winds, blowing snow, and/or extreme cold. Blizzard conditions may be a part of an intense winter storm, in which case a Blizzard Warning is issued rather than a Winter Storm Warning.', inline=False)
    '''
    #Alerts here
    embed.add_field(name='_ _', value='For more information, please visit https://www.canada.ca/en.html')
    await ctx.send(embed=embed)

@client.command(aliases=['BritishColumbia', 'BC', 'bc'])
async def britishcolumbia(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.greyple()
    )
    embed.set_author(name='British Columbia, Canada Alerts')
    embed.add_field(name='Arctic Outflow Warning', value='Any combination of wind speed and temperature giving a wind chill of -20 or lower for 6 hours or more. A separate Wind Warning is not required. Can only be issued for coastal British Columbia regions.', inline=False)
    embed.add_field(name='Blizzard Warning', value='When winds of 40 km/hr or greater are expected to cause widespread reductions in visibility to 400 metres or less, due to blowing snow, or blowing snow in combination with falling snow, for at least 4 hours. If North of the tree line, the conditions are expected to last for at least 6 hours.', inline=False)
    embed.add_field(name='Blowing Snow Advisory', value='When blowing snow, caused by winds of at least 30 km/h, is expected to reduce visibility to 800 metres or less for at least 3 hours. Cannot be issued North of the tree line.', inline=False)
    embed.add_field(name='Extreme Cold Warning (For Southern Interior and Coastal B.C.)', value='Issued when the temperature or wind chill is expected to reach minus 35°C for at least two hours.', inline=False)
    embed.add_field(name='Extreme Cold Warning (For Central Interior B.C.)', value='Issued when the temperature or wind chill is expected to reach minus 40°C for at least two hours.', inline=False)
    embed.add_field(name='Extreme Cold Warning (For Northern B.C.)', value='Issued when the temperature or wind chill is expected to reach minus 45°C for at least two hours.', inline=False)
    embed.add_field(name='Flash Freeze Warning', value='When significant ice is expected to form on roads, sidewalks or other surfaces over much of a region because of the freezing of residual water from either melted snow, or falling/fallen rain due to a rapid drop in temperatures.', inline=False)
    embed.add_field(name='Fog Advisory', value='When low visibilities in fog are expected for at least six hours.', inline=False)
    embed.add_field(name='Freezing Drizzle Advisory', value='When a period of freezing drizzle is expected for at least eight hours.', inline=False)
    embed.add_field(name='Freezing Rain Warning', value='When freezing rain is expected to pose a hazard to transportation or property; Or When freezing rain is expected for at least two hours.', inline=False)
    embed.add_field(name='Heat Warning (Northeast – Northern Interior, Central Interior, including Chilcotin, Cariboos, Prince George, North Thompson, and North Columbia, BC Peace, Bulkley Valley and the Lakes and Fort Nelson)', value='Issued when 2 or more consecutive days of daytime maximum temperatures are expected to reach 29°C or warmer and nighttime minimum temperatures are expected to fall to 14°C or warmer.', inline=False)
    embed.add_field(name='Heat Warning (Northwest – Central and Northern Coast (inland and coastal regions), Northern Vancouver Island, and northwestern BC)', value='Issued when 2 or more consecutive days of daytime maximum temperatures are expected to reach 28°C or warmer and nighttime minimum temperatures are expected to fall to 13°C or warmer.', inline=False)
    embed.add_field(name='Heat Warning (Southeast – Southern interior (including South Thompson and Okanagan), Kootenays, and Columbias (south))', value='Issued when 2 or more consecutive days of daytime maximum temperatures are expected to reach 35°C or warmer and nighttime minimum temperatures are expected to fall to 18°C or warmer.', inline=False)
    embed.add_field(name='Heat Warning (Southwest – Western Metro Vancouver including the North Shore, City of Vancouver and Richmond, Howe Sound, Whistler, Sunshine Coast, Vancouver Island (except northern sections))', value='Issued when 2 or more consecutive days of daytime maximum temperatures are expected to reach 29°C or warmer and nighttime minimum temperatures are expected to fall to 16°C or warmer.', inline=False)
    embed.add_field(name='Heat Warning (Southwest inland - Eastern Metro Vancouver including Coquitlam and Surrey, and the Fraser Valley)', value='Issued when 2 or more consecutive days of daytime maximum temperatures are expected to reach 33°C or warmer and nighttime minimum temperatures are expected to fall to 17°C or warmer.', inline=False)
    embed.add_field(name='Hurricane Watch', value='When, within the following 36 hours, a hurricane or a developing hurricane is expected to pose a possible threat, with the risk of hurricane force winds (average sustained winds of 118 km/h or higher) threatening the area.', inline=False)
    embed.add_field(name='Hurricane Warning', value='When hurricane-force gales (average sustained winds of 118 km/h or higher) caused by a hurricane, or a strong tropical storm that may strengthen to hurricane force before making landfall, are expected to occur in 24 hours or less.  It may also include areas where storm surge or exceptionally high waves are expected, even though winds may be less than hurricane force.', inline=False)
    embed.add_field(name='Rainfall Warning (Alerting parameters for a Short Duration Rainfall (Heavy Downpour) Warning (For interior dry sections of British Columbia))', value='When 15mm or more of rain is expected within one hour', inline=False)
    embed.add_field(name='Rainfall Warning (Alerting parameters for a Short Duration Rainfall (Heavy Downpour) Warning (For the remaining areas in British Columbia))', value='When 25mm or more of rain is expected within one hour', inline=False)
    embed.add_field(name='Rainfall Warning (Alerting parameters Environment Canada uses for issuing a Long Duration Rainfall Warning in the Summer (For interior dry sections of British Columbia))', value='When 25mm or more of rain is expected within 24 hours', inline=False)
    embed.add_field(name='Rainfall Warning (Alerting parameters Environment Canada uses for issuing a Long Duration Rainfall Warning in the Summer (locations listed below))', value='(For Inland Vancouver Island, West Vancouver Island, North Vancouver Island, Central Coast - coastal sections and north coast - coastal sections) When 50mm or more of rain is expected within 24 hours; or when 75mm or more of rain is expected within 48 hours', inline=False)
    embed.add_field(name='Rainfall Warning (Alerting parameters Environment Canada uses for issuing a Long Duration Rainfall Warning in the Winter (locations listed below))', value='(For British Columbia except Inland Vancouver Island, West Vancouver Island, North Vancouver Island, Central Coast - coastal sections and north coast - coastal sections) When 50mm or more of rain is expected within 24 hours; or when 75mm or more of rain is expected within 48 hours', inline=False)
    embed.add_field(name='Rainfall Warning (Alerting parameters Environment Canada uses for issuing a Long Duration Rainfall Warning in the Winter (locations listed below))', value='(For Inland Vancouver Island, West Vancouver Island, North Vancouver Island, Central Coast - coastal sections and north coast - coastal sections) When 100mm or more of rain is expected within 24 hours', inline=False)
    
    #Above is the limit for one embed!
    '''
    embed.add_field(name='Rainfall Warning (Alerting parameters Environment Canada uses for issuing a Long Duration Rainfall Warning during a Thaw Only (For Interior British Columbia))', value='When 25mm or more of rain is expected within 24 hours', inline=False)
    embed.add_field(name='Severe Thunderstorm Watch', value='When conditions are favorable for the development of severe thunderstorms with one or more of the following conditions: Wind gusts of 90km/h or greater, which could cause strutural wind damage; Hail of two centimeters (cm) or larger in diameter; or Heavy rainfall, as per rainfall criteria, excluding those for winter and during thaw', inline=False)
    embed.add_field(name='Severe Thunderstorm Warning', value='When there is evidence based on radar, satellite, pictures, or from a reliable spotter that any one or more of the following three weather conditions is imminent or occurring: Wind gusts of 90km/h or greater, which could cause strutural wind damage; Hail of two centimeters (cm) or larger in diameter; or Heavy rainfall, as per rainfall criteria, excluding those for winter and during thaw', inline=False)
    embed.add_field(name='Snowfall Warning (locations listed below)', value='(For Whistler, Howe Sound, Inland Vancouver Island, North Columbia, West Columbia, Kinbasket, Elk Valley, Yoho Park - Kootenay Park, North Coast - Inland Sections, West Kootenay, Arrow Slocan Lakes, Kootenay Lake, Cassiar Mountains in British Columbia) When 15cm or more of snow falls within 12 hours or less', inline=False)
    embed.add_field(name='Snowfall Warning (For Southern and Central coastal sections of British Columbia)', value='When 10cm or more of snow falls within 12 hours or less; or when 5 cm or more of snow falls within six hours or less', inline=False)
    embed.add_field(name='Snowfall Warning (For Haines Skagway roads in British Columbia)', value='When 20cm or more of snow falls within 24 hours or less', inline=False)
    embed.add_field(name='Snowfall Warning (For all remaining areas of British Columbia)', value='When 10cm or more of snow falls within 12 hours or less', inline=False)
    embed.add_field(name='(Open-Water) Snow Squall Watch', value='When conditions are favourable for the development of open water snow squall down wind of large bodies of water, like the Great Lakes, with one or more of the following conditions: Localized, intense snowfall producing snowfall amounts of 15 cm or more in 12 hours or less. AND/OR Reduced visibility (less than 400 metres) caused by heavy snow with or without blowing snow for 3 hours or more.', inline=False)
    embed.add_field(name='(Frontal) Snow Squall Watch', value='When conditions are favourable for the development of brief periods of very poor visibilities caused by heavy snow and blowing snow.', inline=False)
    embed.add_field(name='(Open-Water) Snow Squall Warning', value='When, down wind of large bodies of water, like the Great Lakes, snow squalls are imminent or occurring with one or more of the following conditions being produced: Localized, intense snowfall producing snowfall amounts of 15 cm or more in 12 hours or less. AND/OR Reduced visibility (less than 400 metres) caused by heavy snow with or without blowing snow for 3 hours or more.', inline=False)
    embed.add_field(name='(Frontal) Snow Squall Warning', value='When there is a brief period (less than one hour) of very poor visibility (400 m or less), caused by heavy snow and blowing snow, and accompanied by strong, gusty winds of 45 km/h or greater, is expected to occur with the passage of a cold front.', inline=False)
    embed.add_field(name='Tornado Watch', value='When conditions are favourable for the development of severe thunderstorms with one or more tornadoes.', inline=False)
    embed.add_field(name='Tornado Warning', value='When a tornado has been reported; or when there is evidence based on radar, or from a reliable spotter that a tornado is imminent.', inline=False)
    embed.add_field(name='Tropical Storm Watch', value='When, within the following 36 hours, a tropical storm or a developing tropical storm is expected to pose a possible threat, with the risk of tropical-storm force winds (average sustained winds of 63-117 km/h) threatening the area. This watch could be issued for: A tropical storm; or A hurricane that might approach an area but be far enough away that it is expected to bring gales that are less than hurricane force (118 km/h or higher).', inline=False)
    embed.add_field(name='Tropical Storm Warning', value='When coastal and/or coastal winds of 63 to 117 km/h caused by a tropical cyclone are expected to occur.', inline=False)
    embed.add_field(name='Tsunami Advisory (For coastal areas and inlets of British Columbia)', value='A tsunami advisory indicated a tsunami with the potential to produce strong currents or waves and is dangerous to those in or very near the water is imminent, expected, or occurring. Large inundations are not expected in areas under advisory status. If this alert is issued for you, make your way to higher ground immediately, this is a life threatening situation!', inline=False)
    embed.add_field(name='Tsunami Warning (For coastal areas and inlets of British Columbia)', value='A tsunami warning indicates that a tsunami is imminent, expected, or occurring and that coastal locations in the warned area should expect widespread flooding. If this alert is issued for you, make your way to higher ground immediately, this is a life threatening situation!', inline=False)
    embed.add_field(name='Tsunami Watch (For coastal areas and inlets of British Columbia)', value='A tsunami watch is an early alert issued to areas which may later be impacted by a tsunami. If this alert is issued for your area, make sure to stay tuned to local officials and your local weather office for the latest information on the potential tsunami.', inline=False)
    embed.add_field(name='_ _', value='To get the latest earthquake and tsunami alert information, please visit https://tsunami.gov/', inline=False)
    embed.add_field(name='Weather Advisory', value=' generic weather advisory. One example might be on days when funnel clouds are expected, but a Tornado alert would not be appropriate.', inline=False)
    embed.add_field(name='Weather Warning', value='A generic weather warning may be issued for extreme weather events for which there is no suitable warning type, because they rarely occur. ', inline=False)
    embed.add_field(name='_ _', value='A generic weather warning may also be issued for other weather events during situations where the environment is vulnerable due to pre-existing conditions and any further weather could result in a significant hazard. For example: 50 km/h winds following an ice storm which could cause structural wind damage.', inline=False)
    embed.add_field(name='_ _', value='A generic weather warning may also be issued for situations where the event is not expected to reach warning criteria values, but there is a special reason for the warning. For example: the first event of the season, or an off-season event.', inline=False)
    embed.add_field(name='Wind Warning (For Western Vancouver Island)', value='80 km/h or more sustained wind; and/or gusts to 100 km/h or more.', inline=False)
    embed.add_field(name='Wind Warning (Excluding North Vancouver Island, Central Coast - coastal sections, North Coast - coastal sections, and Haida Gwaii', value='90 km/h or more sustained wind; and/or gusts to 110 km/h or more.', inline=False)
    embed.add_field(name='Wind Warning (Remaining areas in British Columbia', value='70 km/h or more sustained wind; and/or gusts to 90 km/h or more.', inline=False)
    embed.add_field(name='Winter Storm Watch', value='When conditions are favorable for the development of severe and potentially dangerous winter weather, including: A blizzard, A major snowfall (25cm or more within a 24 hour period); and significant snowfall (snowfall warning criteria amounts) combined with other winter weather hazard types such as: freezing rain, strong winds, blowing snow, and/or extreme wind chill. ', inline=False)
    embed.add_field(name='Winter Storm Warning', value='When severe and potentially dangerous winter weather conditions are expected, including: A major snowfall (25cm or more within a 24 hour period); and A significant snowfall (snowfall warning criteria amoubts) combined with other cold weather precipitation types such as: freezing rain, strong winds, blowing snow, and/or extreme cold. Blizzard conditions may be a part of an intense winter storm, in which case a Blizzard Warning is issued rather than a Winter Storm Warning.', inline=False)
    '''
    #Alerts here
    embed.add_field(name='_ _', value='For more information, please visit https://www.canada.ca/en.html')
    await ctx.send(embed=embed)

@client.command(aliases=['NorthwestTerritories', 'NWT', 'nwt'])
async def northwestterritories(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.greyple()
    )
    embed.set_author(name='Northwest Territories, Canada Alerts')
    embed.add_field(name='Blizzard Warning', value='When winds of 40 km/hr or greater are expected to cause widespread reductions in visibility to 400 metres or less, due to blowing snow, or blowing snow in combination with falling snow, for at least 4 hours. If North of the tree line, the conditions are expected to last for at least 6 hours.', inline=False)
    embed.add_field(name='Blowing Snow Advisory', value='When blowing snow, caused by winds of at least 30 km/h, is expected to reduce visibility to 800 metres or less for at least 3 hours. Cannot be issued North of the tree line.', inline=False)
    embed.add_field(name='Extreme Cold Warning (For NWT (except Paulatuk, Sachs Harbour and Ulukhaktok), Baffin Island (except Igloolik and Hall Beach))', value='Issued when the temperature or wind chill is expected to reach minus 50°C for at least two hours.', inline=False)
    embed.add_field(name='Extreme Cold Warning (For NWT (Paulatuk, Sachs Harbour and Ulukhaktok only))', value='Issued when the temperature or wind chill is expected to reach minus 55°C for at least two hours.', inline=False)
    embed.add_field(name='Flash Freeze Warning', value='When significant ice is expected to form on roads, sidewalks or other surfaces over much of a region because of the freezing of residual water from either melted snow, or falling/fallen rain due to a rapid drop in temperatures.', inline=False)
    embed.add_field(name='Fog Advisory', value='When low visibilities in fog are expected for at least six hours.', inline=False)
    embed.add_field(name='Freezing Drizzle Advisory', value='When a period of freezing drizzle is expected for at least eight hours.', inline=False)
    embed.add_field(name='Freezing Rain Warning', value='When freezing rain is expected to pose a hazard to transportation or property; Or When freezing rain is expected for at least two hours.', inline=False)
    embed.add_field(name='Heat Warning', value='Issued when 2 or more consecutive days of daytime maximum temperatures are expected to reach 29°C or warmer and nighttime minimum temperatures are expected to fall to 14°C or warmer.', inline=False)
    embed.add_field(name='Hurricane Watch', value='When, within the following 36 hours, a hurricane or a developing hurricane is expected to pose a possible threat, with the risk of hurricane force winds (average sustained winds of 118 km/h or higher) threatening the area.', inline=False)
    embed.add_field(name='Hurricane Warning', value='When hurricane-force gales (average sustained winds of 118 km/h or higher) caused by a hurricane, or a strong tropical storm that may strengthen to hurricane force before making landfall, are expected to occur in 24 hours or less.  It may also include areas where storm surge or exceptionally high waves are expected, even though winds may be less than hurricane force.', inline=False)
    embed.add_field(name='_ _', value='For more information, please visit https://www.canada.ca/en.html')
    
    #Below code needs to be tested
    '''
    embed.add_field(name='Rainfall Warning (Alerting parameters for a Short Duration Rainfall (Heavy Downpour))', value='When 25mm or more of rain is expected within one hour.', inline=False)
    embed.add_field(name='Rainfall Warning (Alerting parameters Environment Canada uses for issuing a Long Duration Rainfall Warning in the Summer)', value='When 50mm or more of rain is expected within 24 hours; or when 75mm or more of rain is expected within 48 hours.', inline=False)
    embed.add_field(name='Rainfall Warning (Alerting parameters Environment Canada uses for issuing a Long Duration Rainfall Warning in the Winter)', value='When 25mm or more of rain is expected within 24 hours.', inline=False)
    embed.add_field(name='Severe Thunderstorm Watch', value='When conditions are favorable for the development of severe thunderstorms with one or more of the following conditions: Wind gusts of 90km/h or greater, which could cause strutural wind damage; Hail of two centimeters (cm) or larger in diameter; or Heavy rainfall, as per rainfall criteria, excluding those for winter and during thaw', inline=False)
    embed.add_field(name='Severe Thunderstorm Warning', value='When there is evidence based on radar, satellite, pictures, or from a reliable spotter that any one or more of the following three weather conditions is imminent or occurring: Wind gusts of 90km/h or greater, which could cause strutural wind damage; Hail of two centimeters (cm) or larger in diameter; or Heavy rainfall, as per rainfall criteria, excluding those for winter and during thaw', inline=False)
    embed.add_field(name='Snowfall Warning', value='When 10 cm or more of snow falls within 12 hours or less.', inline=False)
    embed.add_field(name='(Open-Water) Snow Squall Watch', value='When conditions are favourable for the development of open water snow squall down wind of large bodies of water, like the Great Lakes, with one or more of the following conditions: Localized, intense snowfall producing snowfall amounts of 15 cm or more in 12 hours or less. AND/OR Reduced visibility (less than 400 metres) caused by heavy snow with or without blowing snow for 3 hours or more.', inline=False)
    embed.add_field(name='(Frontal) Snow Squall Watch', value='When conditions are favourable for the development of brief periods of very poor visibilities caused by heavy snow and blowing snow.', inline=False)
    embed.add_field(name='(Open-Water) Snow Squall Warning', value='When, down wind of large bodies of water, like the Great Lakes, snow squalls are imminent or occurring with one or more of the following conditions being produced: Localized, intense snowfall producing snowfall amounts of 15 cm or more in 12 hours or less. AND/OR Reduced visibility (less than 400 metres) caused by heavy snow with or without blowing snow for 3 hours or more.', inline=False)
    embed.add_field(name='(Frontal) Snow Squall Warning', value='When there is a brief period (less than one hour) of very poor visibility (400 m or less), caused by heavy snow and blowing snow, and accompanied by strong, gusty winds of 45 km/h or greater, is expected to occur with the passage of a cold front.', inline=False)
    embed.add_field(name='Tornado Watch', value='When conditions are favourable for the development of severe thunderstorms with one or more tornadoes.', inline=False)
    embed.add_field(name='Tornado Warning', value='When a tornado has been reported; or when there is evidence based on radar, or from a reliable spotter that a tornado is imminent.', inline=False)
    embed.add_field(name='Tropical Storm Watch', value='When, within the following 36 hours, a tropical storm or a developing tropical storm is expected to pose a possible threat, with the risk of tropical-storm force winds (average sustained winds of 63-117 km/h) threatening the area. This watch could be issued for: A tropical storm; or A hurricane that might approach an area but be far enough away that it is expected to bring gales that are less than hurricane force (118 km/h or higher).', inline=False)
    embed.add_field(name='Tropical Storm Warning', value='When coastal and/or coastal winds of 63 to 117 km/h caused by a tropical cyclone are expected to occur.', inline=False)
    embed.add_field(name='Weather Advisory', value=' generic weather advisory. One example might be on days when funnel clouds are expected, but a Tornado alert would not be appropriate.', inline=False)
    embed.add_field(name='Weather Warning', value='A generic weather warning may be issued for extreme weather events for which there is no suitable warning type, because they rarely occur. ', inline=False)
    embed.add_field(name='_ _', value='A generic weather warning may also be issued for other weather events during situations where the environment is vulnerable due to pre-existing conditions and any further weather could result in a significant hazard. For example: 50 km/h winds following an ice storm which could cause structural wind damage.', inline=False)
    embed.add_field(name='_ _', value='A generic weather warning may also be issued for situations where the event is not expected to reach warning criteria values, but there is a special reason for the warning. For example: the first event of the season, or an off-season event.', inline=False)
    embed.add_field(name='Wind Warning', value='70 km/h or more sustained wind; and/or gusts to 90 km/h or more.', inline=False)
    embed.add_field(name='Winter Storm Watch', value='When conditions are favorable for the development of severe and potentially dangerous winter weather, including: A blizzard, A major snowfall (25cm or more within a 24 hour period); and significant snowfall (snowfall warning criteria amounts) combined with other winter weather hazard types such as: freezing rain, strong winds, blowing snow, and/or extreme wind chill. ', inline=False)
    embed.add_field(name='Winter Storm Warning', value='When severe and potentially dangerous winter weather conditions are expected, including: A major snowfall (25cm or more within a 24 hour period); and A significant snowfall (snowfall warning criteria amoubts) combined with other cold weather precipitation types such as: freezing rain, strong winds, blowing snow, and/or extreme cold. Blizzard conditions may be a part of an intense winter storm, in which case a Blizzard Warning is issued rather than a Winter Storm Warning.', inline=False)
    '''
    #Alerts here
    await ctx.send(embed=embed)

@client.command(aliases=['Alberta', 'A', 'a'])
async def alberta(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.greyple()
    )
    embed.set_author(name='Alberta, Canada Alerts')
    embed.add_field(name='Blizzard Warning', value='When winds of 40 km/hr or greater are expected to cause widespread reductions in visibility to 400 metres or less, due to blowing snow, or blowing snow in combination with falling snow, for at least 4 hours. If North of the tree line, the conditions are expected to last for at least 6 hours.', inline=False)
    embed.add_field(name='Blowing Snow Advisory', value='When blowing snow, caused by winds of at least 30 km/h, is expected to reduce visibility to 800 metres or less for at least 3 hours. Cannot be issued North of the tree line.', inline=False)
    embed.add_field(name='Dust Storm Warning', value='When blowing dust is expected to occur, reducing visibility to 800 metres or less for one hour or more. Can only be issued in Alberta, Saskatchewan, and Manitoba.', inline=False)
    embed.add_field(name='Extreme Cold Warning (For Prairies - Alberta)', value='Issued when the temperature or wind chill is expected to reach minus 40°C for at least two hours.', inline=False)
    embed.add_field(name='Flash Freeze Warning', value='When significant ice is expected to form on roads, sidewalks or other surfaces over much of a region because of the freezing of residual water from either melted snow, or falling/fallen rain due to a rapid drop in temperatures.', inline=False)
    embed.add_field(name='Fog Advisory', value='When low visibilities in fog are expected for at least six hours.', inline=False)
    embed.add_field(name='Freezing Drizzle Advisory', value='When a period of freezing drizzle is expected for at least eight hours.', inline=False)
    embed.add_field(name='Freezing Rain Warning', value='When freezing rain is expected to pose a hazard to transportation or property; Or When freezing rain is expected for at least two hours.', inline=False)
    embed.add_field(name='Frost Advisory', value='Issued during the growing season when widespread frost formation is expected over an extensive area. Surface temperatures are expected to fall near freezing in the overnight period.', inline=False)
    embed.add_field(name='Heat Warning (Extreme south (including Pincher Creek, Cardston, Lethbridge, and Medicine Hat))', value='Issued when 2 or more consecutive days of daytime maximum temperatures are expected to reach 32°C or warmer and nighttime minimum temperatures are expected to fall to 16°C or warmer.', inline=False)
    embed.add_field(name='Heat Warning (Extreme south (including Pincher Creek, Cardston, Lethbridge, and Medicine Hat))', value='Issued when 2 or more consecutive days of daytime maximum temperatures are expected to reach 29°C or warmer and nighttime minimum temperatures are expected to fall to 14°C or warmer.', inline=False)
    embed.add_field(name='Hurricane Watch', value='When, within the following 36 hours, a hurricane or a developing hurricane is expected to pose a possible threat, with the risk of hurricane force winds (average sustained winds of 118 km/h or higher) threatening the area.', inline=False)
    embed.add_field(name='Hurricane Warning', value='When hurricane-force gales (average sustained winds of 118 km/h or higher) caused by a hurricane, or a strong tropical storm that may strengthen to hurricane force before making landfall, are expected to occur in 24 hours or less.  It may also include areas where storm surge or exceptionally high waves are expected, even though winds may be less than hurricane force.', inline=False)
    
    #Below code needs to be tested
    '''
    embed.add_field(name='Rainfall Warning (Alerting parameters for a Short Duration Rainfall (Heavy Downpour))', value='When 25mm or more of rain is expected within one hour.', inline=False)
    embed.add_field(name='Rainfall Warning (Alerting parameters Environment Canada uses for issuing a Long Duration Rainfall Warning in the Summer)', value='When 50mm or more of rain is expected within 24 hours; or when 75mm or more of rain is expected within 48 hours.', inline=False)
    embed.add_field(name='Rainfall Warning (Alerting parameters Environment Canada uses for issuing a Long Duration Rainfall Warning in the Winter)', value='When 25mm or more of rain is expected within 24 hours.', inline=False)
    embed.add_field(name='Severe Thunderstorm Watch', value='When conditions are favorable for the development of severe thunderstorms with one or more of the following conditions: Wind gusts of 90km/h or greater, which could cause strutural wind damage; Hail of two centimeters (cm) or larger in diameter; or Heavy rainfall, as per rainfall criteria, excluding those for winter and during thaw', inline=False)
    embed.add_field(name='Severe Thunderstorm Warning', value='When there is evidence based on radar, satellite, pictures, or from a reliable spotter that any one or more of the following three weather conditions is imminent or occurring: Wind gusts of 90km/h or greater, which could cause strutural wind damage; Hail of two centimeters (cm) or larger in diameter; or Heavy rainfall, as per rainfall criteria, excluding those for winter and during thaw', inline=False)
    embed.add_field(name='Snowfall Warning', value='When 10 cm or more of snow falls within 12 hours or less.', inline=False)
    embed.add_field(name='(Open-Water) Snow Squall Watch', value='When conditions are favourable for the development of open water snow squall down wind of large bodies of water, like the Great Lakes, with one or more of the following conditions: Localized, intense snowfall producing snowfall amounts of 15 cm or more in 12 hours or less. AND/OR Reduced visibility (less than 400 metres) caused by heavy snow with or without blowing snow for 3 hours or more.', inline=False)
    embed.add_field(name='(Frontal) Snow Squall Watch', value='When conditions are favourable for the development of brief periods of very poor visibilities caused by heavy snow and blowing snow.', inline=False)
    embed.add_field(name='(Open-Water) Snow Squall Warning', value='When, down wind of large bodies of water, like the Great Lakes, snow squalls are imminent or occurring with one or more of the following conditions being produced: Localized, intense snowfall producing snowfall amounts of 15 cm or more in 12 hours or less. AND/OR Reduced visibility (less than 400 metres) caused by heavy snow with or without blowing snow for 3 hours or more.', inline=False)
    embed.add_field(name='(Frontal) Snow Squall Warning', value='When there is a brief period (less than one hour) of very poor visibility (400 m or less), caused by heavy snow and blowing snow, and accompanied by strong, gusty winds of 45 km/h or greater, is expected to occur with the passage of a cold front.', inline=False)
    embed.add_field(name='Tornado Watch', value='When conditions are favourable for the development of severe thunderstorms with one or more tornadoes.', inline=False)
    embed.add_field(name='Tornado Warning', value='When a tornado has been reported; or when there is evidence based on radar, or from a reliable spotter that a tornado is imminent.', inline=False)
    embed.add_field(name='Tropical Storm Watch', value='When, within the following 36 hours, a tropical storm or a developing tropical storm is expected to pose a possible threat, with the risk of tropical-storm force winds (average sustained winds of 63-117 km/h) threatening the area. This watch could be issued for: A tropical storm; or A hurricane that might approach an area but be far enough away that it is expected to bring gales that are less than hurricane force (118 km/h or higher).', inline=False)
    embed.add_field(name='Tropical Storm Warning', value='When coastal and/or coastal winds of 63 to 117 km/h caused by a tropical cyclone are expected to occur.', inline=False)
    embed.add_field(name='Weather Advisory', value=' generic weather advisory. One example might be on days when funnel clouds are expected, but a Tornado alert would not be appropriate.', inline=False)
    embed.add_field(name='Weather Warning', value='A generic weather warning may be issued for extreme weather events for which there is no suitable warning type, because they rarely occur. ', inline=False)
    embed.add_field(name='_ _', value='A generic weather warning may also be issued for other weather events during situations where the environment is vulnerable due to pre-existing conditions and any further weather could result in a significant hazard. For example: 50 km/h winds following an ice storm which could cause structural wind damage.', inline=False)
    embed.add_field(name='_ _', value='A generic weather warning may also be issued for situations where the event is not expected to reach warning criteria values, but there is a special reason for the warning. For example: the first event of the season, or an off-season event.', inline=False)
    embed.add_field(name='Wind Warning (Excluding Crowsnest Pass, Pincher Creek, Waterton Lakes Nat. Park, Cardston, Fort Macleod, Magrath City of Lethbridge.)', value='80 km/h or more sustained wind; and/or gusts to 100 km/h or more.', inline=False)
    embed.add_field(name='Wind Warning (For remaining areas in Alberta)', value='70 km/h or more sustained wind; and/or gusts to 90 km/h or more.', inline=False)
    embed.add_field(name='Winter Storm Watch', value='When conditions are favorable for the development of severe and potentially dangerous winter weather, including: A blizzard, A major snowfall (25cm or more within a 24 hour period); and significant snowfall (snowfall warning criteria amounts) combined with other winter weather hazard types such as: freezing rain, strong winds, blowing snow, and/or extreme wind chill. ', inline=False)
    embed.add_field(name='Winter Storm Warning', value='When severe and potentially dangerous winter weather conditions are expected, including: A major snowfall (25cm or more within a 24 hour period); and A significant snowfall (snowfall warning criteria amoubts) combined with other cold weather precipitation types such as: freezing rain, strong winds, blowing snow, and/or extreme cold. Blizzard conditions may be a part of an intense winter storm, in which case a Blizzard Warning is issued rather than a Winter Storm Warning.', inline=False)
    '''
    #Alerts here
    embed.add_field(name='_ _', value='For more information, please visit https://www.canada.ca/en.html')
    await ctx.send(embed=embed)

@client.command(aliases=['Nunavut', 'N', 'n'])
async def nunavut(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.greyple()
    )
    embed.set_author(name='Nunavut, Canada Alerts')
    #Should probably test this code
    embed.add_field(name='Blizzard Warning', value='When winds of 40 km/hr or greater are expected to cause widespread reductions in visibility to 400 metres or less, due to blowing snow, or blowing snow in combination with falling snow, for at least 4 hours. If North of the tree line, the conditions are expected to last for at least 6 hours.', inline=False)
    embed.add_field(name='Blowing Snow Advisory', value='When blowing snow, caused by winds of at least 30 km/h, is expected to reduce visibility to 800 metres or less for at least 3 hours. Cannot be issued North of the tree line.', inline=False)
    embed.add_field(name='Extreme Cold Warning (For Baffin Island (except Igloolik and Hall Beach))', value='Issued when the temperature or wind chill is expected to reach minus 50°C for at least two hours.', inline=False)
    embed.add_field(name='Extreme Cold Warning (For Nunavut)', value='Issued when the temperature or wind chill is expected to reach minus 52°C for at least two hours.', inline=False)
    embed.add_field(name='Extreme Cold Warning (For Baffin Island (Igloolik and Hall beach only) Western and Northern Nunavut)', value='Issued when the temperature or wind chill is expected to reach minus 55°C for at least two hours.', inline=False)
    embed.add_field(name='Flash Freeze Warning', value='When significant ice is expected to form on roads, sidewalks or other surfaces over much of a region because of the freezing of residual water from either melted snow, or falling/fallen rain due to a rapid drop in temperatures.', inline=False)
    embed.add_field(name='Fog Advisory', value='When low visibilities in fog are expected for at least six hours.', inline=False)
    embed.add_field(name='Freezing Drizzle Advisory', value='When a period of freezing drizzle is expected for at least eight hours.', inline=False)
    embed.add_field(name='Freezing Rain Warning', value='When freezing rain is expected to pose a hazard to transportation or property; Or When freezing rain is expected for at least two hours.', inline=False)
    embed.add_field(name='Heat Warning', value='No Heat Warning Program at this time.', inline=False)
    embed.add_field(name='Hurricane Watch', value='When, within the following 36 hours, a hurricane or a developing hurricane is expected to pose a possible threat, with the risk of hurricane force winds (average sustained winds of 118 km/h or higher) threatening the area.', inline=False)
    embed.add_field(name='Hurricane Warning', value='When hurricane-force gales (average sustained winds of 118 km/h or higher) caused by a hurricane, or a strong tropical storm that may strengthen to hurricane force before making landfall, are expected to occur in 24 hours or less.  It may also include areas where storm surge or exceptionally high waves are expected, even though winds may be less than hurricane force.', inline=False)
    #Code below needs to be tested
    '''
    embed.add_field(name='Rainfall Warning (Alerting parameters for a Short Duration Rainfall (Heavy Downpour))', value='When 25mm or more of rain is expected within one hour.', inline=False)
    embed.add_field(name='Rainfall Warning (Alerting parameters Environment Canada uses for issuing a Long Duration Rainfall Warning in the Summer)', value='When 50mm or more of rain is expected within 24 hours; or when 75mm or more of rain is expected within 48 hours.', inline=False)
    embed.add_field(name='Rainfall Warning (Alerting parameters Environment Canada uses for issuing a Long Duration Rainfall Warning in the Winter)', value='When 25mm or more of rain is expected within 24 hours.', inline=False)
    embed.add_field(name='Severe Thunderstorm Watch', value='When conditions are favorable for the development of severe thunderstorms with one or more of the following conditions: Wind gusts of 90km/h or greater, which could cause strutural wind damage; Hail of two centimeters (cm) or larger in diameter; or Heavy rainfall, as per rainfall criteria, excluding those for winter and during thaw', inline=False)
    embed.add_field(name='Severe Thunderstorm Warning', value='When there is evidence based on radar, satellite, pictures, or from a reliable spotter that any one or more of the following three weather conditions is imminent or occurring: Wind gusts of 90km/h or greater, which could cause strutural wind damage; Hail of two centimeters (cm) or larger in diameter; or Heavy rainfall, as per rainfall criteria, excluding those for winter and during thaw', inline=False)
    embed.add_field(name='Snowfall Warning', value='When 10 cm or more of snow falls within 12 hours or less.', inline=False)
    embed.add_field(name='(Open-Water) Snow Squall Watch', value='When conditions are favourable for the development of open water snow squall down wind of large bodies of water, like the Great Lakes, with one or more of the following conditions: Localized, intense snowfall producing snowfall amounts of 15 cm or more in 12 hours or less. AND/OR Reduced visibility (less than 400 metres) caused by heavy snow with or without blowing snow for 3 hours or more.', inline=False)
    embed.add_field(name='(Frontal) Snow Squall Watch', value='When conditions are favourable for the development of brief periods of very poor visibilities caused by heavy snow and blowing snow.', inline=False)
    embed.add_field(name='(Open-Water) Snow Squall Warning', value='When, down wind of large bodies of water, like the Great Lakes, snow squalls are imminent or occurring with one or more of the following conditions being produced: Localized, intense snowfall producing snowfall amounts of 15 cm or more in 12 hours or less. AND/OR Reduced visibility (less than 400 metres) caused by heavy snow with or without blowing snow for 3 hours or more.', inline=False)
    embed.add_field(name='(Frontal) Snow Squall Warning', value='When there is a brief period (less than one hour) of very poor visibility (400 m or less), caused by heavy snow and blowing snow, and accompanied by strong, gusty winds of 45 km/h or greater, is expected to occur with the passage of a cold front.', inline=False)
    embed.add_field(name='Tornado Watch', value='When conditions are favourable for the development of severe thunderstorms with one or more tornadoes.', inline=False)
    embed.add_field(name='Tornado Warning', value='When a tornado has been reported; or when there is evidence based on radar, or from a reliable spotter that a tornado is imminent.', inline=False)
    embed.add_field(name='Tropical Storm Watch', value='When, within the following 36 hours, a tropical storm or a developing tropical storm is expected to pose a possible threat, with the risk of tropical-storm force winds (average sustained winds of 63-117 km/h) threatening the area. This watch could be issued for: A tropical storm; or A hurricane that might approach an area but be far enough away that it is expected to bring gales that are less than hurricane force (118 km/h or higher).', inline=False)
    embed.add_field(name='Tropical Storm Warning', value='When coastal and/or coastal winds of 63 to 117 km/h caused by a tropical cyclone are expected to occur.', inline=False)
    embed.add_field(name='Weather Advisory', value=' generic weather advisory. One example might be on days when funnel clouds are expected, but a Tornado alert would not be appropriate.', inline=False)
    embed.add_field(name='Weather Warning', value='A generic weather warning may be issued for extreme weather events for which there is no suitable warning type, because they rarely occur. ', inline=False)
    embed.add_field(name='_ _', value='A generic weather warning may also be issued for other weather events during situations where the environment is vulnerable due to pre-existing conditions and any further weather could result in a significant hazard. For example: 50 km/h winds following an ice storm which could cause structural wind damage.', inline=False)
    embed.add_field(name='_ _', value='A generic weather warning may also be issued for situations where the event is not expected to reach warning criteria values, but there is a special reason for the warning. For example: the first event of the season, or an off-season event.', inline=False)
    embed.add_field(name='Wind Warning', value='70 km/h or more sustained wind; and/or gusts to 90 km/h or more.', inline=False)
    embed.add_field(name='Winter Storm Watch', value='When conditions are favorable for the development of severe and potentially dangerous winter weather, including: A blizzard, A major snowfall (25cm or more within a 24 hour period); and significant snowfall (snowfall warning criteria amounts) combined with other winter weather hazard types such as: freezing rain, strong winds, blowing snow, and/or extreme wind chill. ', inline=False)
    embed.add_field(name='Winter Storm Warning', value='When severe and potentially dangerous winter weather conditions are expected, including: A major snowfall (25cm or more within a 24 hour period); and A significant snowfall (snowfall warning criteria amoubts) combined with other cold weather precipitation types such as: freezing rain, strong winds, blowing snow, and/or extreme cold. Blizzard conditions may be a part of an intense winter storm, in which case a Blizzard Warning is issued rather than a Winter Storm Warning.', inline=False)
    '''
    #Alerts Here
    embed.add_field(name='_ _', value='For more information, please visit https://www.canada.ca/en.html')
    await ctx.send(embed=embed)

@client.command(aliases=['Saskatchewan', 'S', 's'])
async def saskatchewan(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.greyple()
    )
    embed.set_author(name='Saskatchewan, Canada Alerts')
    embed.add_field(name='Blizzard Warning', value='When winds of 40 km/hr or greater are expected to cause widespread reductions in visibility to 400 metres or less, due to blowing snow, or blowing snow in combination with falling snow, for at least 4 hours. If North of the tree line, the conditions are expected to last for at least 6 hours.', inline=False)
    embed.add_field(name='Blowing Snow Advisory', value='When blowing snow, caused by winds of at least 30 km/h, is expected to reduce visibility to 800 metres or less for at least 3 hours. Cannot be issued North of the tree line.', inline=False)
    embed.add_field(name='Dust Storm Warning', value='When blowing dust is expected to occur, reducing visibility to 800 metres or less for one hour or more. Can only be issued in Alberta, Saskatchewan, and Manitoba.', inline=False)
    embed.add_field(name='Extreme Cold Warning (For Southern Saskatchewan)', value='Issued when the temperature or wind chill is expected to reach minus 40°C for at least two hours.', inline=False)
    embed.add_field(name='Extreme Cold Warning (For Northern Saskatchewan)', value='Issued when the temperature or wind chill is expected to reach minus 45°C for at least two hours.', inline=False)
    embed.add_field(name='Flash Freeze Warning', value='When significant ice is expected to form on roads, sidewalks or other surfaces over much of a region because of the freezing of residual water from either melted snow, or falling/fallen rain due to a rapid drop in temperatures.', inline=False)
    embed.add_field(name='Fog Advisory', value='When low visibilities in fog are expected for at least six hours.', inline=False)
    embed.add_field(name='Freezing Drizzle Advisory', value='When a period of freezing drizzle is expected for at least eight hours.', inline=False)
    embed.add_field(name='Freezing Rain Warning', value='When freezing rain is expected to pose a hazard to transportation or property; Or When freezing rain is expected for at least two hours.', inline=False)
    embed.add_field(name='Frost Advisory', value='Issued during the growing season when widespread frost formation is expected over an extensive area. Surface temperatures are expected to fall near freezing in the overnight period.', inline=False)
    embed.add_field(name='Heat Warning (North and Central (including Meadow Lake, The Battlefords, Prince Albert, and Hudson Bay))', value='Issued when 2 or more consecutive days of daytime maximum temperatures are expected to reach 29°C or warmer and nighttime minimum temperatures are expected to fall to 14°C or warmer. OR Issued when 2 or more consecutive days of humidex values are expected to reach 34 or higher.', inline=False)
    embed.add_field(name='Heat Warning (South)', value='Issued when 2 or more consecutive days of daytime maximum temperatures are expected to reach 32°C or warmer and nighttime minimum temperatures are expected to fall to 16°C or warmer. OR Issued when 2 or more consecutive days of humidex values are expected to reach 38 or higher.', inline=False)
    embed.add_field(name='Hurricane Watch', value='When, within the following 36 hours, a hurricane or a developing hurricane is expected to pose a possible threat, with the risk of hurricane force winds (average sustained winds of 118 km/h or higher) threatening the area.', inline=False)
    embed.add_field(name='Hurricane Warning', value='When hurricane-force gales (average sustained winds of 118 km/h or higher) caused by a hurricane, or a strong tropical storm that may strengthen to hurricane force before making landfall, are expected to occur in 24 hours or less.  It may also include areas where storm surge or exceptionally high waves are expected, even though winds may be less than hurricane force.', inline=False)
    
    #Code below needs to be tested
    '''
    embed.add_field(name='Rainfall Warning (Alerting parameters for a Short Duration Rainfall (Heavy Downpour))', value='When 50mm or more of rain is expected within one hour.', inline=False)
    embed.add_field(name='Rainfall Warning (Alerting parameters Environment Canada uses for issuing a Long Duration Rainfall Warning in the Summer)', value='When 50mm or more of rain is expected within 24 hours; or when 75mm or more of rain is expected within 48 hours.', inline=False)
    embed.add_field(name='Rainfall Warning (Alerting parameters Environment Canada uses for issuing a Long Duration Rainfall Warning in the Winter)', value='When 25mm or more of rain is expected within 24 hours.', inline=False)
    embed.add_field(name='Severe Thunderstorm Watch', value='When conditions are favorable for the development of severe thunderstorms with one or more of the following conditions: Wind gusts of 90km/h or greater, which could cause strutural wind damage; Hail of two centimeters (cm) or larger in diameter; or Heavy rainfall, as per rainfall criteria, excluding those for winter and during thaw', inline=False)
    embed.add_field(name='Severe Thunderstorm Warning', value='When there is evidence based on radar, satellite, pictures, or from a reliable spotter that any one or more of the following three weather conditions is imminent or occurring: Wind gusts of 90km/h or greater, which could cause strutural wind damage; Hail of two centimeters (cm) or larger in diameter; or Heavy rainfall, as per rainfall criteria, excluding those for winter and during thaw', inline=False)
    embed.add_field(name='Snowfall Warning', value='When 10 cm or more of snow falls within 12 hours or less.', inline=False)
    embed.add_field(name='(Open-Water) Snow Squall Watch', value='When conditions are favourable for the development of open water snow squall down wind of large bodies of water, like the Great Lakes, with one or more of the following conditions: Localized, intense snowfall producing snowfall amounts of 15 cm or more in 12 hours or less. AND/OR Reduced visibility (less than 400 metres) caused by heavy snow with or without blowing snow for 3 hours or more.', inline=False)
    embed.add_field(name='(Frontal) Snow Squall Watch', value='When conditions are favourable for the development of brief periods of very poor visibilities caused by heavy snow and blowing snow.', inline=False)
    embed.add_field(name='(Open-Water) Snow Squall Warning', value='When, down wind of large bodies of water, like the Great Lakes, snow squalls are imminent or occurring with one or more of the following conditions being produced: Localized, intense snowfall producing snowfall amounts of 15 cm or more in 12 hours or less. AND/OR Reduced visibility (less than 400 metres) caused by heavy snow with or without blowing snow for 3 hours or more.', inline=False)
    embed.add_field(name='(Frontal) Snow Squall Warning', value='When there is a brief period (less than one hour) of very poor visibility (400 m or less), caused by heavy snow and blowing snow, and accompanied by strong, gusty winds of 45 km/h or greater, is expected to occur with the passage of a cold front.', inline=False)
    embed.add_field(name='Tornado Watch', value='When conditions are favourable for the development of severe thunderstorms with one or more tornadoes.', inline=False)
    embed.add_field(name='Tornado Warning', value='When a tornado has been reported; or when there is evidence based on radar, or from a reliable spotter that a tornado is imminent.', inline=False)
    embed.add_field(name='Tropical Storm Watch', value='When, within the following 36 hours, a tropical storm or a developing tropical storm is expected to pose a possible threat, with the risk of tropical-storm force winds (average sustained winds of 63-117 km/h) threatening the area. This watch could be issued for: A tropical storm; or A hurricane that might approach an area but be far enough away that it is expected to bring gales that are less than hurricane force (118 km/h or higher).', inline=False)
    embed.add_field(name='Tropical Storm Warning', value='When coastal and/or coastal winds of 63 to 117 km/h caused by a tropical cyclone are expected to occur.', inline=False)
    embed.add_field(name='Weather Advisory', value=' generic weather advisory. One example might be on days when funnel clouds are expected, but a Tornado alert would not be appropriate.', inline=False)
    embed.add_field(name='Weather Warning', value='A generic weather warning may be issued for extreme weather events for which there is no suitable warning type, because they rarely occur. ', inline=False)
    embed.add_field(name='_ _', value='A generic weather warning may also be issued for other weather events during situations where the environment is vulnerable due to pre-existing conditions and any further weather could result in a significant hazard. For example: 50 km/h winds following an ice storm which could cause structural wind damage.', inline=False)
    embed.add_field(name='_ _', value='A generic weather warning may also be issued for situations where the event is not expected to reach warning criteria values, but there is a special reason for the warning. For example: the first event of the season, or an off-season event.', inline=False)
    embed.add_field(name='Wind Warning', value='70 km/h or more sustained wind; and/or gusts to 90 km/h or more.', inline=False)
    embed.add_field(name='Winter Storm Watch', value='When conditions are favorable for the development of severe and potentially dangerous winter weather, including: A blizzard, A major snowfall (25cm or more within a 24 hour period); and significant snowfall (snowfall warning criteria amounts) combined with other winter weather hazard types such as: freezing rain, strong winds, blowing snow, and/or extreme wind chill. ', inline=False)
    embed.add_field(name='Winter Storm Warning', value='When severe and potentially dangerous winter weather conditions are expected, including: A major snowfall (25cm or more within a 24 hour period); and A significant snowfall (snowfall warning criteria amoubts) combined with other cold weather precipitation types such as: freezing rain, strong winds, blowing snow, and/or extreme cold. Blizzard conditions may be a part of an intense winter storm, in which case a Blizzard Warning is issued rather than a Winter Storm Warning.', inline=False)
    '''
    #Alerts here
    embed.add_field(name='_ _', value='For more information, please visit https://www.canada.ca/en.html')
    await ctx.send(embed=embed)

@client.command(aliases=['Manitoba', 'M', 'm'])
async def manitoba(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.greyple()
    )
    embed.set_author(name='Manitoba, Canada Alerts')
    embed.add_field(name='Blizzard Warning', value='When winds of 40 km/hr or greater are expected to cause widespread reductions in visibility to 400 metres or less, due to blowing snow, or blowing snow in combination with falling snow, for at least 4 hours. If North of the tree line, the conditions are expected to last for at least 6 hours.', inline=False)
    embed.add_field(name='Blowing Snow Advisory', value='When blowing snow, caused by winds of at least 30 km/h, is expected to reduce visibility to 800 metres or less for at least 3 hours. Cannot be issued North of the tree line.', inline=False)
    embed.add_field(name='Dust Storm Warning', value='When blowing dust is expected to occur, reducing visibility to 800 metres or less for one hour or more. Can only be issued in Alberta, Saskatchewan, and Manitoba.', inline=False)
    embed.add_field(name='Extreme Cold Warning (For Southern Manitoba)', value='Issued when the temperature or wind chill is expected to reach minus 40°C for at least two hours.', inline=False)
    embed.add_field(name='Extreme Cold Warning (For Northern Manitoba)', value='Issued when the temperature or wind chill is expected to reach minus 45°C for at least two hours.', inline=False)
    embed.add_field(name='Extreme Cold Warning (For extreme Northeast Manitoba)', value='Issued when the temperature or wind chill is expected to reach minus 50°C for at least two hours.', inline=False)
    embed.add_field(name='Flash Freeze Warning', value='When significant ice is expected to form on roads, sidewalks or other surfaces over much of a region because of the freezing of residual water from either melted snow, or falling/fallen rain due to a rapid drop in temperatures.', inline=False)
    embed.add_field(name='Fog Advisory', value='When low visibilities in fog are expected for at least six hours.', inline=False)
    embed.add_field(name='Freezing Drizzle Advisory', value='When a period of freezing drizzle is expected for at least eight hours.', inline=False)
    embed.add_field(name='Freezing Rain Warning', value='When freezing rain is expected to pose a hazard to transportation or property; Or When freezing rain is expected for at least two hours.', inline=False)
    embed.add_field(name='Frost Advisory', value='Issued during the growing season when widespread frost formation is expected over an extensive area. Surface temperatures are expected to fall near freezing in the overnight period.', inline=False)
    embed.add_field(name='Heat Warning (North)', value='Issued when 2 or more consecutive days of daytime maximum temperatures are expected to reach 29°C or warmer and nighttime minimum temperatures are expected to fall to 16°C or warmer. OR Issued when 2 or more consecutive days of humidex values are expected to reach 34 or higher.', inline=False)
    embed.add_field(name='Heat Warning (South)', value='Issued when 2 or more consecutive days of daytime maximum temperatures are expected to reach 32°C or warmer and nighttime minimum temperatures are expected to fall to 16°C or warmer. OR Issued when 2 or more consecutive days of humidex values are expected to reach 38 or higher.', inline=False)
    embed.add_field(name='Hurricane Watch', value='When, within the following 36 hours, a hurricane or a developing hurricane is expected to pose a possible threat, with the risk of hurricane force winds (average sustained winds of 118 km/h or higher) threatening the area.', inline=False)
    embed.add_field(name='Hurricane Warning', value='When hurricane-force gales (average sustained winds of 118 km/h or higher) caused by a hurricane, or a strong tropical storm that may strengthen to hurricane force before making landfall, are expected to occur in 24 hours or less.  It may also include areas where storm surge or exceptionally high waves are expected, even though winds may be less than hurricane force.', inline=False)
    
    #Code below needs to be tested
    '''
    embed.add_field(name='Rainfall Warning (Alerting parameters for a Short Duration Rainfall (Heavy Downpour))', value='When 50mm or more of rain is expected within one hour.', inline=False)
    embed.add_field(name='Rainfall Warning (Alerting parameters Environment Canada uses for issuing a Long Duration Rainfall Warning in the Summer)', value='When 50mm or more of rain is expected within 24 hours; or when 75mm or more of rain is expected within 48 hours.', inline=False)
    embed.add_field(name='Rainfall Warning (Alerting parameters Environment Canada uses for issuing a Long Duration Rainfall Warning in the Winter)', value='When 25mm or more of rain is expected within 24 hours.', inline=False)
    embed.add_field(name='Severe Thunderstorm Watch', value='When conditions are favorable for the development of severe thunderstorms with one or more of the following conditions: Wind gusts of 90km/h or greater, which could cause strutural wind damage; Hail of two centimeters (cm) or larger in diameter; or Heavy rainfall, as per rainfall criteria, excluding those for winter and during thaw', inline=False)
    embed.add_field(name='Severe Thunderstorm Warning', value='When there is evidence based on radar, satellite, pictures, or from a reliable spotter that any one or more of the following three weather conditions is imminent or occurring: Wind gusts of 90km/h or greater, which could cause strutural wind damage; Hail of two centimeters (cm) or larger in diameter; or Heavy rainfall, as per rainfall criteria, excluding those for winter and during thaw', inline=False)
    embed.add_field(name='Snowfall Warning', value='When 10 cm or more of snow falls within 12 hours or less.', inline=False)
    embed.add_field(name='(Open-Water) Snow Squall Watch', value='When conditions are favourable for the development of open water snow squall down wind of large bodies of water, like the Great Lakes, with one or more of the following conditions: Localized, intense snowfall producing snowfall amounts of 15 cm or more in 12 hours or less. AND/OR Reduced visibility (less than 400 metres) caused by heavy snow with or without blowing snow for 3 hours or more.', inline=False)
    embed.add_field(name='(Frontal) Snow Squall Watch', value='When conditions are favourable for the development of brief periods of very poor visibilities caused by heavy snow and blowing snow.', inline=False)
    embed.add_field(name='(Open-Water) Snow Squall Warning', value='When, down wind of large bodies of water, like the Great Lakes, snow squalls are imminent or occurring with one or more of the following conditions being produced: Localized, intense snowfall producing snowfall amounts of 15 cm or more in 12 hours or less. AND/OR Reduced visibility (less than 400 metres) caused by heavy snow with or without blowing snow for 3 hours or more.', inline=False)
    embed.add_field(name='(Frontal) Snow Squall Warning', value='When there is a brief period (less than one hour) of very poor visibility (400 m or less), caused by heavy snow and blowing snow, and accompanied by strong, gusty winds of 45 km/h or greater, is expected to occur with the passage of a cold front.', inline=False)
    embed.add_field(name='Tornado Watch', value='When conditions are favourable for the development of severe thunderstorms with one or more tornadoes.', inline=False)
    embed.add_field(name='Tornado Warning', value='When a tornado has been reported; or when there is evidence based on radar, or from a reliable spotter that a tornado is imminent.', inline=False)
    embed.add_field(name='Tropical Storm Watch', value='When, within the following 36 hours, a tropical storm or a developing tropical storm is expected to pose a possible threat, with the risk of tropical-storm force winds (average sustained winds of 63-117 km/h) threatening the area. This watch could be issued for: A tropical storm; or A hurricane that might approach an area but be far enough away that it is expected to bring gales that are less than hurricane force (118 km/h or higher).', inline=False)
    embed.add_field(name='Tropical Storm Warning', value='When coastal and/or coastal winds of 63 to 117 km/h caused by a tropical cyclone are expected to occur.', inline=False)
    embed.add_field(name='Weather Advisory', value=' generic weather advisory. One example might be on days when funnel clouds are expected, but a Tornado alert would not be appropriate.', inline=False)
    embed.add_field(name='Weather Warning', value='A generic weather warning may be issued for extreme weather events for which there is no suitable warning type, because they rarely occur. ', inline=False)
    embed.add_field(name='_ _', value='A generic weather warning may also be issued for other weather events during situations where the environment is vulnerable due to pre-existing conditions and any further weather could result in a significant hazard. For example: 50 km/h winds following an ice storm which could cause structural wind damage.', inline=False)
    embed.add_field(name='_ _', value='A generic weather warning may also be issued for situations where the event is not expected to reach warning criteria values, but there is a special reason for the warning. For example: the first event of the season, or an off-season event.', inline=False)
    embed.add_field(name='Wind Warning', value='70 km/h or more sustained wind; and/or gusts to 90 km/h or more.', inline=False)
    embed.add_field(name='Winter Storm Watch', value='When conditions are favorable for the development of severe and potentially dangerous winter weather, including: A blizzard, A major snowfall (25cm or more within a 24 hour period); and significant snowfall (snowfall warning criteria amounts) combined with other winter weather hazard types such as: freezing rain, strong winds, blowing snow, and/or extreme wind chill. ', inline=False)
    embed.add_field(name='Winter Storm Warning', value='When severe and potentially dangerous winter weather conditions are expected, including: A major snowfall (25cm or more within a 24 hour period); and A significant snowfall (snowfall warning criteria amoubts) combined with other cold weather precipitation types such as: freezing rain, strong winds, blowing snow, and/or extreme cold. Blizzard conditions may be a part of an intense winter storm, in which case a Blizzard Warning is issued rather than a Winter Storm Warning.', inline=False)
    '''
    #Alerts here
    embed.add_field(name='_ _', value='For more information, please visit https://www.canada.ca/en.html')
    await ctx.send(embed=embed)

@client.command(aliases=['Ontario', 'O', 'o'])
async def ontario(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.greyple()
    )
    embed.set_author(name='Ontario, Canada Alerts')
    embed.add_field(name='Blizzard Warning', value='When winds of 40 km/hr or greater are expected to cause widespread reductions in visibility to 400 metres or less, due to blowing snow, or blowing snow in combination with falling snow, for at least 4 hours. If North of the tree line, the conditions are expected to last for at least 6 hours.', inline=False)
    embed.add_field(name='Blowing Snow Advisory', value='When blowing snow, caused by winds of at least 30 km/h, is expected to reduce visibility to 800 metres or less for at least 3 hours. Cannot be issued North of the tree line.', inline=False)
    embed.add_field(name='Extreme Cold Warning (For South-central and Southwestern Ontario)', value='Issued when the temperature or wind chill is expected to reach minus 30°C for at least two hours.', inline=False)
    embed.add_field(name='Extreme Cold Warning (For Southeastern Ontario)', value='Issued when the temperature or wind chill is expected to reach minus 35°C for at least two hours.', inline=False)
    embed.add_field(name='Extreme Cold Warning (For Northern Ontario)', value='Issued when the temperature or wind chill is expected to reach minus 40°C for at least two hours.', inline=False)
    embed.add_field(name='Extreme Cold Warning (For Far Northern Ontario)', value='Issued when the temperature or wind chill is expected to reach minus 45°C for at least two hours.', inline=False)
    embed.add_field(name='Flash Freeze Warning', value='When significant ice is expected to form on roads, sidewalks or other surfaces over much of a region because of the freezing of residual water from either melted snow, or falling/fallen rain due to a rapid drop in temperatures.', inline=False)
    embed.add_field(name='Fog Advisory', value='When low visibilities in fog are expected for at least six hours.', inline=False)
    embed.add_field(name='Freezing Drizzle Advisory', value='When a period of freezing drizzle is expected for at least eight hours.', inline=False)
    embed.add_field(name='Freezing Rain Warning', value='When freezing rain is expected to pose a hazard to transportation or property; Or When freezing rain is expected for at least two hours.', inline=False)
    embed.add_field(name='Frost Advisory', value='Issued during the growing season when widespread frost formation is expected over an extensive area. Surface temperatures are expected to fall near freezing in the overnight period.', inline=False)
    embed.add_field(name='Heat Warning (Extreme southwest (Essex and Chatham-Kent Counties))', value='Issued when 2 or more consecutive days of daytime maximum temperatures are expected to reach 31°C or warmer and nighttime minimum temperatures are expected to fall to 21°C or warmer. OR Issued when 2 or more consecutive days of humidex values are expected to reach 42 or higher.', inline=False)
    embed.add_field(name='Heat Warning (North)', value='Issued when 2 or more consecutive days of daytime maximum temperatures are expected to reach 29°C or warmer and nighttime minimum temperatures are expected to fall to 18°C or warmer. OR Issued when 2 or more consecutive days of humidex values are expected to reach 36 or higher.', inline=False)
    embed.add_field(name='Heat Warning (Remainder of southern Ontario (including the District of Parry Sound))', value='Issued when 2 or more consecutive days of daytime maximum temperatures are expected to reach 31°C or warmer and nighttime minimum temperatures are expected to fall to 20°C or warmer. OR Issued when 2 or more consecutive days of humidex values are expected to reach 40 or higher.', inline=False)
    embed.add_field(name='Hurricane Watch', value='When, within the following 36 hours, a hurricane or a developing hurricane is expected to pose a possible threat, with the risk of hurricane force winds (average sustained winds of 118 km/h or higher) threatening the area.', inline=False)
    embed.add_field(name='Hurricane Warning', value='When hurricane-force gales (average sustained winds of 118 km/h or higher) caused by a hurricane, or a strong tropical storm that may strengthen to hurricane force before making landfall, are expected to occur in 24 hours or less.  It may also include areas where storm surge or exceptionally high waves are expected, even though winds may be less than hurricane force.', inline=False)
    
    #Code below needs to be tested
    '''
    embed.add_field(name='Rainfall Warning (Alerting parameters for a Short Duration Rainfall (Heavy Downpour))', value='When 50mm or more of rain is expected within one hour.', inline=False)
    embed.add_field(name='Rainfall Warning (Alerting parameters Environment Canada uses for issuing a Long Duration Rainfall Warning in the Summer)', value='When 50mm or more of rain is expected within 24 hours; or when 75mm or more of rain is expected within 48 hours.', inline=False)
    embed.add_field(name='Rainfall Warning (Alerting parameters Environment Canada uses for issuing a Long Duration Rainfall Warning in the Winter)', value='When 25mm or more of rain is expected within 24 hours.', inline=False)
    embed.add_field(name='Severe Thunderstorm Watch', value='When conditions are favorable for the development of severe thunderstorms with one or more of the following conditions: Wind gusts of 90km/h or greater, which could cause strutural wind damage; Hail of two centimeters (cm) or larger in diameter; or Heavy rainfall, as per rainfall criteria, excluding those for winter and during thaw', inline=False)
    embed.add_field(name='Severe Thunderstorm Warning', value='When there is evidence based on radar, satellite, pictures, or from a reliable spotter that any one or more of the following three weather conditions is imminent or occurring: Wind gusts of 90km/h or greater, which could cause strutural wind damage; Hail of two centimeters (cm) or larger in diameter; or Heavy rainfall, as per rainfall criteria, excluding those for winter and during thaw', inline=False)
    embed.add_field(name='Snowfall Warning', value='When 15 cm or more more of snow falls within 12 hours or less', inline=False)
    embed.add_field(name='(Open-Water) Snow Squall Watch', value='When conditions are favourable for the development of open water snow squall down wind of large bodies of water, like the Great Lakes, with one or more of the following conditions: Localized, intense snowfall producing snowfall amounts of 15 cm or more in 12 hours or less. AND/OR Reduced visibility (less than 400 metres) caused by heavy snow with or without blowing snow for 3 hours or more.', inline=False)
    embed.add_field(name='(Frontal) Snow Squall Watch', value='When conditions are favourable for the development of brief periods of very poor visibilities caused by heavy snow and blowing snow.', inline=False)
    embed.add_field(name='(Open-Water) Snow Squall Warning', value='When, down wind of large bodies of water, like the Great Lakes, snow squalls are imminent or occurring with one or more of the following conditions being produced: Localized, intense snowfall producing snowfall amounts of 15 cm or more in 12 hours or less. AND/OR Reduced visibility (less than 400 metres) caused by heavy snow with or without blowing snow for 3 hours or more.', inline=False)
    embed.add_field(name='(Frontal) Snow Squall Warning', value='When there is a brief period (less than one hour) of very poor visibility (400 m or less), caused by heavy snow and blowing snow, and accompanied by strong, gusty winds of 45 km/h or greater, is expected to occur with the passage of a cold front.', inline=False)
    embed.add_field(name='Tornado Watch', value='When conditions are favourable for the development of severe thunderstorms with one or more tornadoes.', inline=False)
    embed.add_field(name='Tornado Warning', value='When a tornado has been reported; or when there is evidence based on radar, or from a reliable spotter that a tornado is imminent.', inline=False)
    embed.add_field(name='Tropical Storm Watch', value='When, within the following 36 hours, a tropical storm or a developing tropical storm is expected to pose a possible threat, with the risk of tropical-storm force winds (average sustained winds of 63-117 km/h) threatening the area. This watch could be issued for: A tropical storm; or A hurricane that might approach an area but be far enough away that it is expected to bring gales that are less than hurricane force (118 km/h or higher).', inline=False)
    embed.add_field(name='Tropical Storm Warning', value='When coastal and/or coastal winds of 63 to 117 km/h caused by a tropical cyclone are expected to occur.', inline=False)
    embed.add_field(name='Weather Advisory', value=' generic weather advisory. One example might be on days when funnel clouds are expected, but a Tornado alert would not be appropriate.', inline=False)
    embed.add_field(name='Weather Warning', value='A generic weather warning may be issued for extreme weather events for which there is no suitable warning type, because they rarely occur. ', inline=False)
    embed.add_field(name='_ _', value='A generic weather warning may also be issued for other weather events during situations where the environment is vulnerable due to pre-existing conditions and any further weather could result in a significant hazard. For example: 50 km/h winds following an ice storm which could cause structural wind damage.', inline=False)
    embed.add_field(name='_ _', value='A generic weather warning may also be issued for situations where the event is not expected to reach warning criteria values, but there is a special reason for the warning. For example: the first event of the season, or an off-season event.', inline=False)
    embed.add_field(name='Wind Warning', value='70 km/h or more sustained wind; and/or gusts to 90 km/h or more.', inline=False)
    embed.add_field(name='Winter Storm Watch', value='When conditions are favorable for the development of severe and potentially dangerous winter weather, including: A blizzard, A major snowfall (25cm or more within a 24 hour period); and significant snowfall (snowfall warning criteria amounts) combined with other winter weather hazard types such as: freezing rain, strong winds, blowing snow, and/or extreme wind chill. ', inline=False)
    embed.add_field(name='Winter Storm Warning', value='When severe and potentially dangerous winter weather conditions are expected, including: A major snowfall (25cm or more within a 24 hour period); and A significant snowfall (snowfall warning criteria amoubts) combined with other cold weather precipitation types such as: freezing rain, strong winds, blowing snow, and/or extreme cold. Blizzard conditions may be a part of an intense winter storm, in which case a Blizzard Warning is issued rather than a Winter Storm Warning.', inline=False)
    '''

    embed.add_field(name='_ _', value='For more information, please visit https://www.canada.ca/en.html')
    await ctx.send(embed=embed)

@client.command(aliases=['Quebec', 'Q', 'q'])
async def quebec(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.greyple()
    )
    embed.set_author(name='Quebec, Canada Alerts')
    #Test all the below code
    embed.add_field(name='Blizzard Warning', value='When winds of 40 km/hr or greater are expected to cause widespread reductions in visibility to 400 metres or less, due to blowing snow, or blowing snow in combination with falling snow, for at least 4 hours. If North of the tree line, the conditions are expected to last for at least 6 hours.', inline=False)
    embed.add_field(name='Blowing Snow Advisory', value='When blowing snow, caused by winds of at least 30 km/h, is expected to reduce visibility to 800 metres or less for at least 3 hours. Cannot be issued North of the tree line.', inline=False)
    embed.add_field(name='Extreme Cold Warning (For Western, Central and Eastern Quebec)', value='Issued when the temperature or wind chill is expected to reach minus 38°C for at least two hours.', inline=False)
    embed.add_field(name='Extreme Cold Warning (For Northern Quebec)', value='Issued when the temperature or wind chill is expected to reach minus 48°C for at least two hours.', inline=False)
    embed.add_field(name='Extreme Cold Warning (Nunavik)', value='Issued when the temperature or wind chill is expected to reach minus 52°C for at least 2 hours')
    embed.add_field(name='Flash Freeze Warning (Excluding Nunavik*)', value='When significant ice is expected to form on roads, sidewalks or other surfaces over much of a region because of the freezing of residual water from either melted snow, or falling/fallen rain due to a rapid drop in temperatures.', inline=False)
    embed.add_field(name='Fog Advisory (Excluding Nunavik*)', value='When low visibilities in fog are expected for at least six hours.', inline=False)
    embed.add_field(name='Freezing Drizzle Advisory (Excluding Nunavik*)', value='When a period of freezing drizzle is expected for at least eight hours.', inline=False)
    embed.add_field(name='Freezing Rain Warning (Excluding Nunavik*)', value='When freezing rain is expected to pose a hazard to transportation or property; Or When freezing rain is expected for at least two hours.', inline=False)
    embed.add_field(name='Frost Advisory', value='Issued during the growing season when widespread frost formation is expected over an extensive area. Surface temperatures are expected to fall near freezing in the overnight period.', inline=False)
    embed.add_field(name='Heat Warning (Excluding Nunavik*)', value='Issued when the humidex value is 40 or higher and when the temperature is 30°C or warmer, and both conditions persist for at least one hour. OR Issued when temperature is 40°C or warmer.', inline=False)
    embed.add_field(name='Hurricane Watch', value='When, within the following 36 hours, a hurricane or a developing hurricane is expected to pose a possible threat, with the risk of hurricane force winds (average sustained winds of 118 km/h or higher) threatening the area.', inline=False)
    embed.add_field(name='Hurricane Warning', value='When hurricane-force gales (average sustained winds of 118 km/h or higher) caused by a hurricane, or a strong tropical storm that may strengthen to hurricane force before making landfall, are expected to occur in 24 hours or less.  It may also include areas where storm surge or exceptionally high waves are expected, even though winds may be less than hurricane force.', inline=False)
    
    #Below code is new
    '''
    embed.add_field(name='Rainfall Warning (Excluding Nunavik* (Alerting parameters for a Short Duration Rainfall (Heavy Downpour)))', value='When 50mm or more of rain is expected within one hour.', inline=False)
    embed.add_field(name='Rainfall Warning (Excluding Nunavik* (Alerting parameters Environment Canada uses for issuing a Long Duration Rainfall Warning in the Summer)', value='When 50mm or more of rain is expected within 24 hours; or when 75mm or more of rain is expected within 48 hours.', inline=False)
    embed.add_field(name='Rainfall Warning (Excluding Nunavik* (Alerting parameters Environment Canada uses for issuing a Long Duration Rainfall Warning in the Winter)', value='When 25mm or more of rain is expected within 24 hours.', inline=False)
    embed.add_field(name='Severe Thunderstorm Watch (Excluding Nunavik*)', value='When conditions are favorable for the development of severe thunderstorms with one or more of the following conditions: Wind gusts of 90km/h or greater, which could cause strutural wind damage; Hail of two centimeters (cm) or larger in diameter; or Heavy rainfall, as per rainfall criteria, excluding those for winter and during thaw', inline=False)
    embed.add_field(name='Severe Thunderstorm Warning (Excluding Nunavik*)', value='When there is evidence based on radar, satellite, pictures, or from a reliable spotter that any one or more of the following three weather conditions is imminent or occurring: Wind gusts of 90km/h or greater, which could cause strutural wind damage; Hail of two centimeters (cm) or larger in diameter; or Heavy rainfall, as per rainfall criteria, excluding those for winter and during thaw', inline=False)
    embed.add_field(name='Snowfall Warning (Excluding Nunavik*)', value='When 15cm or more of snow falls within 12 hours or less.', inline=False)
    embed.add_field(name='(Open-Water) Snow Squall Watch (Excluding Nunavik*)', value='When conditions are favourable for the development of open water snow squall down wind of large bodies of water, like the Great Lakes, with one or more of the following conditions: Localized, intense snowfall producing snowfall amounts of 15 cm or more in 12 hours or less. AND/OR Reduced visibility (less than 400 metres) caused by heavy snow with or without blowing snow for 3 hours or more.', inline=False)
    embed.add_field(name='(Frontal) Snow Squall Watch (Excluding Nunavik*)', value='When conditions are favourable for the development of brief periods of very poor visibilities caused by heavy snow and blowing snow.', inline=False)
    embed.add_field(name='(Open-Water) Snow Squall Warning (Excluding Nunavik*)', value='When, down wind of large bodies of water, like the Great Lakes, snow squalls are imminent or occurring with one or more of the following conditions being produced: Localized, intense snowfall producing snowfall amounts of 15 cm or more in 12 hours or less. AND/OR Reduced visibility (less than 400 metres) caused by heavy snow with or without blowing snow for 3 hours or more.', inline=False)
    embed.add_field(name='(Frontal) Snow Squall Warning (Excluding Nunavik*)', value='When there is a brief period (less than one hour) of very poor visibility (400 m or less), caused by heavy snow and blowing snow, and accompanied by strong, gusty winds of 45 km/h or greater, is expected to occur with the passage of a cold front.', inline=False)
    embed.add_field(name='Tornado Watch (Excluding Nunavik*)', value='When conditions are favourable for the development of severe thunderstorms with one or more tornadoes.', inline=False)
    embed.add_field(name='Tornado Warning (Excluding Nunavik*)', value='When a tornado has been reported; or when there is evidence based on radar, or from a reliable spotter that a tornado is imminent.', inline=False)
    embed.add_field(name='Tropical Storm Watch', value='When, within the following 36 hours, a tropical storm or a developing tropical storm is expected to pose a possible threat, with the risk of tropical-storm force winds (average sustained winds of 63-117 km/h) threatening the area. This watch could be issued for: A tropical storm; or A hurricane that might approach an area but be far enough away that it is expected to bring gales that are less than hurricane force (118 km/h or higher).', inline=False)
    embed.add_field(name='Tropical Storm Warning', value='When coastal and/or coastal winds of 63 to 117 km/h caused by a tropical cyclone are expected to occur.', inline=False)
    embed.add_field(name='Weather Advisory (Excluding Nunavik*)', value=' generic weather advisory. One example might be on days when funnel clouds are expected, but a Tornado alert would not be appropriate.', inline=False)
    embed.add_field(name='Weather Warning (Excluding Nunavik*)', value='A generic weather warning may be issued for extreme weather events for which there is no suitable warning type, because they rarely occur. ', inline=False)
    embed.add_field(name='_ _', value='A generic weather warning may also be issued for other weather events during situations where the environment is vulnerable due to pre-existing conditions and any further weather could result in a significant hazard. For example: 50 km/h winds following an ice storm which could cause structural wind damage.', inline=False)
    embed.add_field(name='_ _', value='A generic weather warning may also be issued for situations where the event is not expected to reach warning criteria values, but there is a special reason for the warning. For example: the first event of the season, or an off-season event.', inline=False)
    embed.add_field(name='Wind Warning', value='70 km/h or more sustained wind; and/or gusts to 90 km/h or more.', inline=False)
    embed.add_field(name='Winter Storm Watch (Excluding Nunavik*)', value='When conditions are favorable for the development of severe and potentially dangerous winter weather, including: A blizzard, A major snowfall (25cm or more within a 24 hour period); and significant snowfall (snowfall warning criteria amounts) combined with other winter weather hazard types such as: freezing rain, strong winds, blowing snow, and/or extreme wind chill. ', inline=False)
    embed.add_field(name='Winter Storm Warning (Excluding Nunavik*)', value='When severe and potentially dangerous winter weather conditions are expected, including: A major snowfall (25cm or more within a 24 hour period); and A significant snowfall (snowfall warning criteria amoubts) combined with other cold weather precipitation types such as: freezing rain, strong winds, blowing snow, and/or extreme cold. Blizzard conditions may be a part of an intense winter storm, in which case a Blizzard Warning is issued rather than a Winter Storm Warning.', inline=False)
    embed.add_field(name='_ _', value='*No alert of this type exists for this region at this moment.', inline=False)
    '''
    embed.add_field(name='_ _', value='For more information, please visit https://www.canada.ca/en.html')
    await ctx.send(embed=embed)

@client.command(aliases=['NewFoundland', 'Newfoundland', 'NewFoundlandLabrador', 'NF', 'nf', 'NFL', 'nfl'])
async def newfoundland(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.greyple()
    )
    embed.set_author(name='NewFoundland and Labrador, Canada Alerts')
    embed.add_field(name='Blizzard Warning', value='When winds of 40 km/hr or greater are expected to cause widespread reductions in visibility to 400 metres or less, due to blowing snow, or blowing snow in combination with falling snow, for at least 4 hours. If North of the tree line, the conditions are expected to last for at least 6 hours.', inline=False)
    embed.add_field(name='Blowing Snow Advisory', value='When blowing snow, caused by winds of at least 30 km/h, is expected to reduce visibility to 800 metres or less for at least 3 hours. Cannot be issued North of the tree line.', inline=False)
    embed.add_field(name='Extreme Cold Warning (For Atlantic Canada except Labrador)', value='Issued when the temperature or wind chill is expected to reach minus 35°C for at least two hours.', inline=False)
    embed.add_field(name='Extreme Cold Warning (For Labrador)', value='Issued when the temperature or wind chill is expected to reach minus 45°C for at least two hours.', inline=False)
    embed.add_field(name='Flash Freeze Warning', value='When significant ice is expected to form on roads, sidewalks or other surfaces over much of a region because of the freezing of residual water from either melted snow, or falling/fallen rain due to a rapid drop in temperatures.', inline=False)
    embed.add_field(name='Fog Advisory', value='When low visibilities in fog are expected for at least 18 hours.', inline=False)
    embed.add_field(name='Freezing Drizzle Advisory', value='When a period of freezing drizzle is expected for at least eight hours.', inline=False)
    embed.add_field(name='Freezing Rain Warning', value='When freezing rain is expected to pose a hazard to transportation or property; Or When freezing rain is expected for at least four hours.', inline=False)
    embed.add_field(name='Heat Warning', value='Issued when 2 or more consecutive days of daytime maximum temperatures are expected to reach 28°C or warmer and nighttime minimum temperatures are expected to fall to 16°C or warmer. OR Issued when 2 or more consecutive days of humidex values are expected to reach 36 or higher.', inline=False)
    embed.add_field(name='Hurricane Watch', value='When, within the following 36 hours, a hurricane or a developing hurricane is expected to pose a possible threat, with the risk of hurricane force winds (average sustained winds of 118 km/h or higher) threatening the area.', inline=False)
    embed.add_field(name='Hurricane Warning', value='When hurricane-force gales (average sustained winds of 118 km/h or higher) caused by a hurricane, or a strong tropical storm that may strengthen to hurricane force before making landfall, are expected to occur in 24 hours or less.  It may also include areas where storm surge or exceptionally high waves are expected, even though winds may be less than hurricane force.', inline=False)
    
    #Below code needs to be tested (new code)
    '''
    embed.add_field(name='Rainfall Warning (Alerting parameters for a Short Duration Rainfall (Heavy Downpour))', value='When 25 mm or more of rain is expected within one hour.', inline=False)
    embed.add_field(name='Rainfall Warning (Alerting parameters Environment Canada uses for issuing a Long Duration Rainfall Warning in the Summer)', value='When 50mm or more of rain is expected within 24 hours; or when 75mm or more of rain is expected within 48 hours.', inline=False)
    embed.add_field(name='Rainfall Warning (Alerting parameters Environment Canada uses for issuing a Long Duration Rainfall Warning in the Winter)', value='When 25mm or more of rain is expected within 24 hours.', inline=False)
    embed.add_field(name='Severe Thunderstorm Watch', value='When conditions are favorable for the development of severe thunderstorms with one or more of the following conditions: Wind gusts of 90km/h or greater, which could cause strutural wind damage; Hail of two centimeters (cm) or larger in diameter; or Heavy rainfall, as per rainfall criteria, excluding those for winter and during thaw', inline=False)
    embed.add_field(name='Severe Thunderstorm Warning', value='When there is evidence based on radar, satellite, pictures, or from a reliable spotter that any one or more of the following three weather conditions is imminent or occurring: Wind gusts of 90km/h or greater, which could cause strutural wind damage; Hail of two centimeters (cm) or larger in diameter; or Heavy rainfall, as per rainfall criteria, excluding those for winter and during thaw', inline=False)
    embed.add_field(name='Snowfall Warning', value='When 15cm or more of snow falls within 12 hours or less.', inline=False)
    embed.add_field(name='(Open-Water) Snow Squall Watch', value='When conditions are favourable for the development of open water snow squall down wind of large bodies of water, like the Great Lakes, with one or more of the following conditions: Localized, intense snowfall producing snowfall amounts of 15 cm or more in 12 hours or less. AND/OR Reduced visibility (less than 400 metres) caused by heavy snow with or without blowing snow for 3 hours or more.', inline=False)
    embed.add_field(name='(Frontal) Snow Squall Watch', value='When conditions are favourable for the development of brief periods of very poor visibilities caused by heavy snow and blowing snow.', inline=False)
    embed.add_field(name='(Open-Water) Snow Squall Warning', value='When, down wind of large bodies of water, like the Great Lakes, snow squalls are imminent or occurring with one or more of the following conditions being produced: Localized, intense snowfall producing snowfall amounts of 15 cm or more in 12 hours or less. AND/OR Reduced visibility (less than 400 metres) caused by heavy snow with or without blowing snow for 3 hours or more.', inline=False)
    embed.add_field(name='(Frontal) Snow Squall Warning', value='When there is a brief period (less than one hour) of very poor visibility (400 m or less), caused by heavy snow and blowing snow, and accompanied by strong, gusty winds of 45 km/h or greater, is expected to occur with the passage of a cold front.', inline=False)
    embed.add_field(name='Tornado Watch)', value='When conditions are favourable for the development of severe thunderstorms with one or more tornadoes.', inline=False)
    embed.add_field(name='Tornado Warning', value='When a tornado has been reported; or when there is evidence based on radar, or from a reliable spotter that a tornado is imminent.', inline=False)
    embed.add_field(name='Tropical Storm Watch', value='When, within the following 36 hours, a tropical storm or a developing tropical storm is expected to pose a possible threat, with the risk of tropical-storm force winds (average sustained winds of 63-117 km/h) threatening the area. This watch could be issued for: A tropical storm; or A hurricane that might approach an area but be far enough away that it is expected to bring gales that are less than hurricane force (118 km/h or higher).', inline=False)
    embed.add_field(name='Tropical Storm Warning', value='When coastal and/or coastal winds of 63 to 117 km/h caused by a tropical cyclone are expected to occur.', inline=False)
    embed.add_field(name='Weather Advisory', value=' generic weather advisory. One example might be on days when funnel clouds are expected, but a Tornado alert would not be appropriate.', inline=False)
    embed.add_field(name='Weather Warning', value='A generic weather warning may be issued for extreme weather events for which there is no suitable warning type, because they rarely occur. ', inline=False)
    embed.add_field(name='_ _', value='A generic weather warning may also be issued for other weather events during situations where the environment is vulnerable due to pre-existing conditions and any further weather could result in a significant hazard. For example: 50 km/h winds following an ice storm which could cause structural wind damage.', inline=False)
    embed.add_field(name='_ _', value='A generic weather warning may also be issued for situations where the event is not expected to reach warning criteria values, but there is a special reason for the warning. For example: the first event of the season, or an off-season event.', inline=False)
    embed.add_field(name='Wind Warning (For Wreckhouse Winds)', value='80 km/h or more sustained wind; and/or gusts to 100 km/h or more.', inline=False)
    embed.add_field(name='Wind Warning (For remaining portions of New Foundland & Labrador)', value='70 km/h or more sustained wind; and/or gusts to 90 km/h or more.', inline=False)
    embed.add_field(name='Winter Storm Watch', value='When conditions are favorable for the development of severe and potentially dangerous winter weather, including: A blizzard, A major snowfall (25cm or more within a 24 hour period); and significant snowfall (snowfall warning criteria amounts) combined with other winter weather hazard types such as: freezing rain, strong winds, blowing snow, and/or extreme wind chill. ', inline=False)
    embed.add_field(name='Winter Storm Warning', value='When severe and potentially dangerous winter weather conditions are expected, including: A major snowfall (25cm or more within a 24 hour period); and A significant snowfall (snowfall warning criteria amoubts) combined with other cold weather precipitation types such as: freezing rain, strong winds, blowing snow, and/or extreme cold. Blizzard conditions may be a part of an intense winter storm, in which case a Blizzard Warning is issued rather than a Winter Storm Warning.', inline=False)
    '''
    embed.add_field(name='_ _', value='For more information, please visit https://www.canada.ca/en.html')
    await ctx.send(embed=embed)

@client.command(aliases=['NewBrunswick', 'NB', 'nb'])
async def newbrunswick(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.greyple()
    )
    embed.set_author(name='New Brunswick, Canada Alerts')
    embed.add_field(name='Blizzard Warning', value='When winds of 40 km/hr or greater are expected to cause widespread reductions in visibility to 400 metres or less, due to blowing snow, or blowing snow in combination with falling snow, for at least 4 hours. If North of the tree line, the conditions are expected to last for at least 6 hours.', inline=False)
    embed.add_field(name='Blowing Snow Advisory', value='When blowing snow, caused by winds of at least 30 km/h, is expected to reduce visibility to 800 metres or less for at least 3 hours. Cannot be issued North of the tree line.', inline=False)
    embed.add_field(name='Extreme Cold Warning (For Atlantic Canada except Labrador)', value='Issued when the temperature or wind chill is expected to reach minus 35°C for at least two hours.', inline=False)
    embed.add_field(name='Flash Freeze Warning', value='When significant ice is expected to form on roads, sidewalks or other surfaces over much of a region because of the freezing of residual water from either melted snow, or falling/fallen rain due to a rapid drop in temperatures.', inline=False)
    embed.add_field(name='Fog Advisory', value='When low visibilities in fog are expected for at least 18 hours.', inline=False)
    embed.add_field(name='Freezing Drizzle Advisory', value='When a period of freezing drizzle is expected for at least eight hours.', inline=False)
    embed.add_field(name='Freezing Rain Warning', value='When freezing rain is expected to pose a hazard to transportation or property; Or When freezing rain is expected for at least four hours.', inline=False)
    embed.add_field(name='Frost Advisory', value='Issued during the growing season when widespread frost formation is expected over an extensive area. Surface temperatures are expected to fall near freezing in the overnight period.', inline=False)
    embed.add_field(name='Heat Warning', value='Issued when 2 or more consecutive days of daytime maximum temperatures are expected to reach 30°C or warmer and nighttime minimum temperatures are expected to fall to 18°C or warmer. OR Issued when 2 or more consecutive days of humidex values are expected to reach 36 or higher.', inline=False)
    
    #Below code needs to be tested (new code)
    '''
    embed.add_field(name='Hurricane Watch', value='When, within the following 36 hours, a hurricane or a developing hurricane is expected to pose a possible threat, with the risk of hurricane force winds (average sustained winds of 118 km/h or higher) threatening the area.', inline=False)
    embed.add_field(name='Hurricane Warning', value='When hurricane-force gales (average sustained winds of 118 km/h or higher) caused by a hurricane, or a strong tropical storm that may strengthen to hurricane force before making landfall, are expected to occur in 24 hours or less.  It may also include areas where storm surge or exceptionally high waves are expected, even though winds may be less than hurricane force.', inline=False)
    embed.add_field(name='Rainfall Warning (Alerting parameters for a Short Duration Rainfall (Heavy Downpour))', value='When 25mm or more of rain is expected within one hour.', inline=False)
    embed.add_field(name='Rainfall Warning (Alerting parameters Environment Canada uses for issuing a Long Duration Rainfall Warning in the Summer)', value='When 50mm or more of rain is expected within 24 hours; or when 75mm or more of rain is expected within 48 hours.', inline=False)
    embed.add_field(name='Rainfall Warning (Alerting parameters Environment Canada uses for issuing a Long Duration Rainfall Warning in the Winter)', value='When 25mm or more of rain is expected within 24 hours.', inline=False)
    embed.add_field(name='Severe Thunderstorm Watch', value='When conditions are favorable for the development of severe thunderstorms with one or more of the following conditions: Wind gusts of 90km/h or greater, which could cause strutural wind damage; Hail of two centimeters (cm) or larger in diameter; or Heavy rainfall, as per rainfall criteria, excluding those for winter and during thaw', inline=False)
    embed.add_field(name='Severe Thunderstorm Warning', value='When there is evidence based on radar, satellite, pictures, or from a reliable spotter that any one or more of the following three weather conditions is imminent or occurring: Wind gusts of 90km/h or greater, which could cause strutural wind damage; Hail of two centimeters (cm) or larger in diameter; or Heavy rainfall, as per rainfall criteria, excluding those for winter and during thaw', inline=False)
    embed.add_field(name='Snowfall Warning', value='When 15cm or more of snow falls within 12 hours or less.', inline=False)
    embed.add_field(name='(Open-Water) Snow Squall Watch', value='When conditions are favourable for the development of open water snow squall down wind of large bodies of water, like the Great Lakes, with one or more of the following conditions: Localized, intense snowfall producing snowfall amounts of 15 cm or more in 12 hours or less. AND/OR Reduced visibility (less than 400 metres) caused by heavy snow with or without blowing snow for 3 hours or more.', inline=False)
    embed.add_field(name='(Frontal) Snow Squall Watch', value='When conditions are favourable for the development of brief periods of very poor visibilities caused by heavy snow and blowing snow.', inline=False)
    embed.add_field(name='(Open-Water) Snow Squall Warning', value='When, down wind of large bodies of water, like the Great Lakes, snow squalls are imminent or occurring with one or more of the following conditions being produced: Localized, intense snowfall producing snowfall amounts of 15 cm or more in 12 hours or less. AND/OR Reduced visibility (less than 400 metres) caused by heavy snow with or without blowing snow for 3 hours or more.', inline=False)
    embed.add_field(name='(Frontal) Snow Squall Warning', value='When there is a brief period (less than one hour) of very poor visibility (400 m or less), caused by heavy snow and blowing snow, and accompanied by strong, gusty winds of 45 km/h or greater, is expected to occur with the passage of a cold front.', inline=False)
    embed.add_field(name='Tornado Watch)', value='When conditions are favourable for the development of severe thunderstorms with one or more tornadoes.', inline=False)
    embed.add_field(name='Tornado Warning', value='When a tornado has been reported; or when there is evidence based on radar, or from a reliable spotter that a tornado is imminent.', inline=False)
    embed.add_field(name='Tropical Storm Watch', value='When, within the following 36 hours, a tropical storm or a developing tropical storm is expected to pose a possible threat, with the risk of tropical-storm force winds (average sustained winds of 63-117 km/h) threatening the area. This watch could be issued for: A tropical storm; or A hurricane that might approach an area but be far enough away that it is expected to bring gales that are less than hurricane force (118 km/h or higher).', inline=False)
    embed.add_field(name='Tropical Storm Warning', value='When coastal and/or coastal winds of 63 to 117 km/h caused by a tropical cyclone are expected to occur.', inline=False)
    embed.add_field(name='Tsunami Advisory (For coastal areas)', value='A tsunami advisory indicated a tsunami with the potential to produce strong currents or waves and is dangerous to those in or very near the water is imminent, expected, or occurring. Large inundations are not expected in areas under advisory status. If this alert is issued for you, make your way to higher ground immediately, this is a life threatening situation!', inline=False)
    embed.add_field(name='Tsunami Warning (For coastal areas)', value='A tsunami warning indicates that a tsunami is imminent, expected, or occurring and that coastal locations in the warned area should expect widespread flooding. If this alert is issued for you, make your way to higher ground immediately, this is a life threatening situation!', inline=False)
    embed.add_field(name='Tsunami Watch (For coastal areas)', value='A tsunami watch is an early alert issued to areas which may later be impacted by a tsunami. If this alert is issued for your area, make sure to stay tuned to local officials and your local weather office for the latest information on the potential tsunami.', inline=False)
    embed.add_field(name='_ _', value='To get the latest earthquake and tsunami alert information, please visit https://tsunami.gov/', inline=False)
    embed.add_field(name='Weather Advisory', value=' generic weather advisory. One example might be on days when funnel clouds are expected, but a Tornado alert would not be appropriate.', inline=False)
    embed.add_field(name='Weather Warning', value='A generic weather warning may be issued for extreme weather events for which there is no suitable warning type, because they rarely occur. ', inline=False)
    embed.add_field(name='_ _', value='A generic weather warning may also be issued for other weather events during situations where the environment is vulnerable due to pre-existing conditions and any further weather could result in a significant hazard. For example: 50 km/h winds following an ice storm which could cause structural wind damage.', inline=False)
    embed.add_field(name='_ _', value='A generic weather warning may also be issued for situations where the event is not expected to reach warning criteria values, but there is a special reason for the warning. For example: the first event of the season, or an off-season event.', inline=False)
    embed.add_field(name='Wind Warning', value='70 km/h or more sustained wind; and/or gusts to 90 km/h or more.', inline=False)
    embed.add_field(name='Winter Storm Watch', value='When conditions are favorable for the development of severe and potentially dangerous winter weather, including: A blizzard, A major snowfall (25cm or more within a 24 hour period); and significant snowfall (snowfall warning criteria amounts) combined with other winter weather hazard types such as: freezing rain, strong winds, blowing snow, and/or extreme wind chill. ', inline=False)
    embed.add_field(name='Winter Storm Warning', value='When severe and potentially dangerous winter weather conditions are expected, including: A major snowfall (25cm or more within a 24 hour period); and A significant snowfall (snowfall warning criteria amoubts) combined with other cold weather precipitation types such as: freezing rain, strong winds, blowing snow, and/or extreme cold. Blizzard conditions may be a part of an intense winter storm, in which case a Blizzard Warning is issued rather than a Winter Storm Warning.', inline=False)
    '''
    embed.add_field(name='_ _', value='For more information, please visit https://www.canada.ca/en.html')
    await ctx.send(embed=embed)

@client.command(aliases=['PrinceEdwardIsland', 'PrinceEdward', 'princeedward', 'PE', 'pe'])
async def princeedwardisland(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.greyple()
    )
    embed.set_author(name='Prince Edward Island, Canada Alerts')
    embed.add_field(name='Blizzard Warning', value='When winds of 40 km/hr or greater are expected to cause widespread reductions in visibility to 400 metres or less, due to blowing snow, or blowing snow in combination with falling snow, for at least 4 hours. If North of the tree line, the conditions are expected to last for at least 6 hours.', inline=False)
    embed.add_field(name='Blowing Snow Advisory', value='When blowing snow, caused by winds of at least 30 km/h, is expected to reduce visibility to 800 metres or less for at least 3 hours. Cannot be issued North of the tree line.', inline=False)
    embed.add_field(name='Extreme Cold Warning (For Atlantic Canada except Labrador)', value='Issued when the temperature or wind chill is expected to reach minus 35°C for at least two hours.', inline=False)
    embed.add_field(name='Flash Freeze Warning', value='When significant ice is expected to form on roads, sidewalks or other surfaces over much of a region because of the freezing of residual water from either melted snow, or falling/fallen rain due to a rapid drop in temperatures.', inline=False)
    embed.add_field(name='Fog Advisory', value='When low visibilities in fog are expected for at least 18 hours.', inline=False)
    embed.add_field(name='Freezing Drizzle Advisory', value='When a period of freezing drizzle is expected for at least eight hours.', inline=False)
    embed.add_field(name='Freezing Rain Warning', value='When freezing rain is expected to pose a hazard to transportation or property; Or When freezing rain is expected for at least four hours.', inline=False)
    embed.add_field(name='Frost Advisory', value='Issued during the growing season when widespread frost formation is expected over an extensive area. Surface temperatures are expected to fall near freezing in the overnight period.', inline=False)
    embed.add_field(name='Heat Warning', value='Issued when 2 or more consecutive days of daytime maximum temperatures are expected to reach 28°C or warmer and nighttime minimum temperatures are expected to fall to 18°C or warmer. OR Issued when 2 or more consecutive days of humidex values are expected to reach 36 or higher.', inline=False)
    
    #Code below needs to be tested (new code)
    '''
    embed.add_field(name='Hurricane Watch', value='When, within the following 36 hours, a hurricane or a developing hurricane is expected to pose a possible threat, with the risk of hurricane force winds (average sustained winds of 118 km/h or higher) threatening the area.', inline=False)
    embed.add_field(name='Hurricane Warning', value='When hurricane-force gales (average sustained winds of 118 km/h or higher) caused by a hurricane, or a strong tropical storm that may strengthen to hurricane force before making landfall, are expected to occur in 24 hours or less.  It may also include areas where storm surge or exceptionally high waves are expected, even though winds may be less than hurricane force.', inline=False)
    embed.add_field(name='Rainfall Warning (Alerting parameters for a Short Duration Rainfall (Heavy Downpour))', value='When 25mm or more of rain is expected within one hour.', inline=False)
    embed.add_field(name='Rainfall Warning (Alerting parameters Environment Canada uses for issuing a Long Duration Rainfall Warning in the Summer)', value='When 50mm or more of rain is expected within 24 hours; or when 75mm or more of rain is expected within 48 hours.', inline=False)
    embed.add_field(name='Rainfall Warning (Alerting parameters Environment Canada uses for issuing a Long Duration Rainfall Warning in the Winter)', value='When 25mm or more of rain is expected within 24 hours.', inline=False)
    embed.add_field(name='Severe Thunderstorm Watch', value='When conditions are favorable for the development of severe thunderstorms with one or more of the following conditions: Wind gusts of 90km/h or greater, which could cause strutural wind damage; Hail of two centimeters (cm) or larger in diameter; or Heavy rainfall, as per rainfall criteria, excluding those for winter and during thaw', inline=False)
    embed.add_field(name='Severe Thunderstorm Warning', value='When there is evidence based on radar, satellite, pictures, or from a reliable spotter that any one or more of the following three weather conditions is imminent or occurring: Wind gusts of 90km/h or greater, which could cause strutural wind damage; Hail of two centimeters (cm) or larger in diameter; or Heavy rainfall, as per rainfall criteria, excluding those for winter and during thaw', inline=False)
    embed.add_field(name='Snowfall Warning', value='When 15cm or more of snow falls within 12 hours or less.', inline=False)
    embed.add_field(name='(Open-Water) Snow Squall Watch', value='When conditions are favourable for the development of open water snow squall down wind of large bodies of water, like the Great Lakes, with one or more of the following conditions: Localized, intense snowfall producing snowfall amounts of 15 cm or more in 12 hours or less. AND/OR Reduced visibility (less than 400 metres) caused by heavy snow with or without blowing snow for 3 hours or more.', inline=False)
    embed.add_field(name='(Frontal) Snow Squall Watch', value='When conditions are favourable for the development of brief periods of very poor visibilities caused by heavy snow and blowing snow.', inline=False)
    embed.add_field(name='(Open-Water) Snow Squall Warning', value='When, down wind of large bodies of water, like the Great Lakes, snow squalls are imminent or occurring with one or more of the following conditions being produced: Localized, intense snowfall producing snowfall amounts of 15 cm or more in 12 hours or less. AND/OR Reduced visibility (less than 400 metres) caused by heavy snow with or without blowing snow for 3 hours or more.', inline=False)
    embed.add_field(name='(Frontal) Snow Squall Warning', value='When there is a brief period (less than one hour) of very poor visibility (400 m or less), caused by heavy snow and blowing snow, and accompanied by strong, gusty winds of 45 km/h or greater, is expected to occur with the passage of a cold front.', inline=False)
    embed.add_field(name='Tornado Watch)', value='When conditions are favourable for the development of severe thunderstorms with one or more tornadoes.', inline=False)
    embed.add_field(name='Tornado Warning', value='When a tornado has been reported; or when there is evidence based on radar, or from a reliable spotter that a tornado is imminent.', inline=False)
    embed.add_field(name='Tropical Storm Watch', value='When, within the following 36 hours, a tropical storm or a developing tropical storm is expected to pose a possible threat, with the risk of tropical-storm force winds (average sustained winds of 63-117 km/h) threatening the area. This watch could be issued for: A tropical storm; or A hurricane that might approach an area but be far enough away that it is expected to bring gales that are less than hurricane force (118 km/h or higher).', inline=False)
    embed.add_field(name='Tropical Storm Warning', value='When coastal and/or coastal winds of 63 to 117 km/h caused by a tropical cyclone are expected to occur.', inline=False)
    embed.add_field(name='Tsunami Advisory (For coastal areas)', value='A tsunami advisory indicated a tsunami with the potential to produce strong currents or waves and is dangerous to those in or very near the water is imminent, expected, or occurring. Large inundations are not expected in areas under advisory status. If this alert is issued for you, make your way to higher ground immediately, this is a life threatening situation!', inline=False)
    embed.add_field(name='Tsunami Warning (For coastal areas)', value='A tsunami warning indicates that a tsunami is imminent, expected, or occurring and that coastal locations in the warned area should expect widespread flooding. If this alert is issued for you, make your way to higher ground immediately, this is a life threatening situation!', inline=False)
    embed.add_field(name='Tsunami Watch (For coastal areas)', value='A tsunami watch is an early alert issued to areas which may later be impacted by a tsunami. If this alert is issued for your area, make sure to stay tuned to local officials and your local weather office for the latest information on the potential tsunami.', inline=False)
    embed.add_field(name='_ _', value='To get the latest earthquake and tsunami alert information, please visit https://tsunami.gov/', inline=False)
    embed.add_field(name='Weather Advisory', value=' generic weather advisory. One example might be on days when funnel clouds are expected, but a Tornado alert would not be appropriate.', inline=False)
    embed.add_field(name='Weather Warning', value='A generic weather warning may be issued for extreme weather events for which there is no suitable warning type, because they rarely occur. ', inline=False)
    embed.add_field(name='_ _', value='A generic weather warning may also be issued for other weather events during situations where the environment is vulnerable due to pre-existing conditions and any further weather could result in a significant hazard. For example: 50 km/h winds following an ice storm which could cause structural wind damage.', inline=False)
    embed.add_field(name='_ _', value='A generic weather warning may also be issued for situations where the event is not expected to reach warning criteria values, but there is a special reason for the warning. For example: the first event of the season, or an off-season event.', inline=False)
    embed.add_field(name='Wind Warning', value='70 km/h or more sustained wind; and/or gusts to 90 km/h or more.', inline=False)
    embed.add_field(name='Winter Storm Watch', value='When conditions are favorable for the development of severe and potentially dangerous winter weather, including: A blizzard, A major snowfall (25cm or more within a 24 hour period); and significant snowfall (snowfall warning criteria amounts) combined with other winter weather hazard types such as: freezing rain, strong winds, blowing snow, and/or extreme wind chill. ', inline=False)
    embed.add_field(name='Winter Storm Warning', value='When severe and potentially dangerous winter weather conditions are expected, including: A major snowfall (25cm or more within a 24 hour period); and A significant snowfall (snowfall warning criteria amoubts) combined with other cold weather precipitation types such as: freezing rain, strong winds, blowing snow, and/or extreme cold. Blizzard conditions may be a part of an intense winter storm, in which case a Blizzard Warning is issued rather than a Winter Storm Warning.', inline=False)
    '''
    embed.add_field(name='_ _', value='For more information, please visit https://www.canada.ca/en.html')
    await ctx.send(embed=embed)

@client.command(aliases=['NovaScotia', 'NS', 'ns'])
async def novascotia(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.greyple()
    )
    embed.set_author(name='Nova Scotia, Canada Alerts')
    embed.add_field(name='Blizzard Warning', value='When winds of 40 km/hr or greater are expected to cause widespread reductions in visibility to 400 metres or less, due to blowing snow, or blowing snow in combination with falling snow, for at least 4 hours. If North of the tree line, the conditions are expected to last for at least 6 hours.', inline=False)
    embed.add_field(name='Blowing Snow Advisory', value='When blowing snow, caused by winds of at least 30 km/h, is expected to reduce visibility to 800 metres or less for at least 3 hours. Cannot be issued North of the tree line.', inline=False)
    embed.add_field(name='Extreme Cold Warning (For Atlantic Canada except Labrador)', value='Issued when the temperature or wind chill is expected to reach minus 35°C for at least two hours.', inline=False)
    embed.add_field(name='Flash Freeze Warning', value='When significant ice is expected to form on roads, sidewalks or other surfaces over much of a region because of the freezing of residual water from either melted snow, or falling/fallen rain due to a rapid drop in temperatures.', inline=False)
    embed.add_field(name='Fog Advisory', value='When low visibilities in fog are expected for at least 18 hours.', inline=False)
    embed.add_field(name='Freezing Drizzle Advisory', value='When a period of freezing drizzle is expected for at least eight hours.', inline=False)
    embed.add_field(name='Freezing Rain Warning', value='When freezing rain is expected to pose a hazard to transportation or property; Or When freezing rain is expected for at least four hours.', inline=False)
    embed.add_field(name='Frost Advisory', value='Issued during the growing season when widespread frost formation is expected over an extensive area. Surface temperatures are expected to fall near freezing in the overnight period.', inline=False)
    embed.add_field(name='Heat Warning', value='Issued when 2 or more consecutive days of daytime maximum temperatures are expected to reach 29°C or warmer and nighttime minimum temperatures are expected to fall to 16°C or warmer. OR Issued when 2 or more consecutive days of humidex values are expected to reach 36 or higher.', inline=False)
    
    #Code below needs to be tested (new code)
    '''
    embed.add_field(name='Hurricane Watch', value='When, within the following 36 hours, a hurricane or a developing hurricane is expected to pose a possible threat, with the risk of hurricane force winds (average sustained winds of 118 km/h or higher) threatening the area.', inline=False)
    embed.add_field(name='Hurricane Warning', value='When hurricane-force gales (average sustained winds of 118 km/h or higher) caused by a hurricane, or a strong tropical storm that may strengthen to hurricane force before making landfall, are expected to occur in 24 hours or less.  It may also include areas where storm surge or exceptionally high waves are expected, even though winds may be less than hurricane force.', inline=False)
    embed.add_field(name='Rainfall Warning (Alerting parameters for a Short Duration Rainfall (Heavy Downpour))', value='When 25mm or more of rain is expected within one hour.', inline=False)
    embed.add_field(name='Rainfall Warning (Alerting parameters Environment Canada uses for issuing a Long Duration Rainfall Warning in the Summer)', value='When 50mm or more of rain is expected within 24 hours; or when 75mm or more of rain is expected within 48 hours.', inline=False)
    embed.add_field(name='Rainfall Warning (Alerting parameters Environment Canada uses for issuing a Long Duration Rainfall Warning in the Winter)', value='When 25mm or more of rain is expected within 24 hours.', inline=False)
    embed.add_field(name='Severe Thunderstorm Watch', value='When conditions are favorable for the development of severe thunderstorms with one or more of the following conditions: Wind gusts of 90km/h or greater, which could cause strutural wind damage; Hail of two centimeters (cm) or larger in diameter; or Heavy rainfall, as per rainfall criteria, excluding those for winter and during thaw', inline=False)
    embed.add_field(name='Severe Thunderstorm Warning', value='When there is evidence based on radar, satellite, pictures, or from a reliable spotter that any one or more of the following three weather conditions is imminent or occurring: Wind gusts of 90km/h or greater, which could cause strutural wind damage; Hail of two centimeters (cm) or larger in diameter; or Heavy rainfall, as per rainfall criteria, excluding those for winter and during thaw', inline=False)
    embed.add_field(name='Snowfall Warning', value='When 15cm or more of snow falls within 12 hours or less.', inline=False)
    embed.add_field(name='(Open-Water) Snow Squall Watch', value='When conditions are favourable for the development of open water snow squall down wind of large bodies of water, like the Great Lakes, with one or more of the following conditions: Localized, intense snowfall producing snowfall amounts of 15 cm or more in 12 hours or less. AND/OR Reduced visibility (less than 400 metres) caused by heavy snow with or without blowing snow for 3 hours or more.', inline=False)
    embed.add_field(name='(Frontal) Snow Squall Watch', value='When conditions are favourable for the development of brief periods of very poor visibilities caused by heavy snow and blowing snow.', inline=False)
    embed.add_field(name='(Open-Water) Snow Squall Warning', value='When, down wind of large bodies of water, like the Great Lakes, snow squalls are imminent or occurring with one or more of the following conditions being produced: Localized, intense snowfall producing snowfall amounts of 15 cm or more in 12 hours or less. AND/OR Reduced visibility (less than 400 metres) caused by heavy snow with or without blowing snow for 3 hours or more.', inline=False)
    embed.add_field(name='(Frontal) Snow Squall Warning', value='When there is a brief period (less than one hour) of very poor visibility (400 m or less), caused by heavy snow and blowing snow, and accompanied by strong, gusty winds of 45 km/h or greater, is expected to occur with the passage of a cold front.', inline=False)
    embed.add_field(name='Tornado Watch)', value='When conditions are favourable for the development of severe thunderstorms with one or more tornadoes.', inline=False)
    embed.add_field(name='Tornado Warning', value='When a tornado has been reported; or when there is evidence based on radar, or from a reliable spotter that a tornado is imminent.', inline=False)
    embed.add_field(name='Tropical Storm Watch', value='When, within the following 36 hours, a tropical storm or a developing tropical storm is expected to pose a possible threat, with the risk of tropical-storm force winds (average sustained winds of 63-117 km/h) threatening the area. This watch could be issued for: A tropical storm; or A hurricane that might approach an area but be far enough away that it is expected to bring gales that are less than hurricane force (118 km/h or higher).', inline=False)
    embed.add_field(name='Tropical Storm Warning', value='When coastal and/or coastal winds of 63 to 117 km/h caused by a tropical cyclone are expected to occur.', inline=False)
    embed.add_field(name='Tsunami Advisory (For coastal areas)', value='A tsunami advisory indicated a tsunami with the potential to produce strong currents or waves and is dangerous to those in or very near the water is imminent, expected, or occurring. Large inundations are not expected in areas under advisory status. If this alert is issued for you, make your way to higher ground immediately, this is a life threatening situation!', inline=False)
    embed.add_field(name='Tsunami Warning (For coastal areas)', value='A tsunami warning indicates that a tsunami is imminent, expected, or occurring and that coastal locations in the warned area should expect widespread flooding. If this alert is issued for you, make your way to higher ground immediately, this is a life threatening situation!', inline=False)
    embed.add_field(name='Tsunami Watch (For coastal areas)', value='A tsunami watch is an early alert issued to areas which may later be impacted by a tsunami. If this alert is issued for your area, make sure to stay tuned to local officials and your local weather office for the latest information on the potential tsunami.', inline=False)
    embed.add_field(name='_ _', value='To get the latest earthquake and tsunami alert information, please visit https://tsunami.gov/', inline=False)
    embed.add_field(name='Weather Advisory', value=' generic weather advisory. One example might be on days when funnel clouds are expected, but a Tornado alert would not be appropriate.', inline=False)
    embed.add_field(name='Weather Warning', value='A generic weather warning may be issued for extreme weather events for which there is no suitable warning type, because they rarely occur. ', inline=False)
    embed.add_field(name='_ _', value='A generic weather warning may also be issued for other weather events during situations where the environment is vulnerable due to pre-existing conditions and any further weather could result in a significant hazard. For example: 50 km/h winds following an ice storm which could cause structural wind damage.', inline=False)
    embed.add_field(name='_ _', value='A generic weather warning may also be issued for situations where the event is not expected to reach warning criteria values, but there is a special reason for the warning. For example: the first event of the season, or an off-season event.', inline=False)
    embed.add_field(name='Wind Warning', value='70 km/h or more sustained wind; and/or gusts to 90 km/h or more.', inline=False)
    embed.add_field(name='Winter Storm Watch', value='When conditions are favorable for the development of severe and potentially dangerous winter weather, including: A blizzard, A major snowfall (25cm or more within a 24 hour period); and significant snowfall (snowfall warning criteria amounts) combined with other winter weather hazard types such as: freezing rain, strong winds, blowing snow, and/or extreme wind chill. ', inline=False)
    embed.add_field(name='Winter Storm Warning', value='When severe and potentially dangerous winter weather conditions are expected, including: A major snowfall (25cm or more within a 24 hour period); and A significant snowfall (snowfall warning criteria amoubts) combined with other cold weather precipitation types such as: freezing rain, strong winds, blowing snow, and/or extreme cold. Blizzard conditions may be a part of an intense winter storm, in which case a Blizzard Warning is issued rather than a Winter Storm Warning.', inline=False)
    '''
    embed.add_field(name='_ _', value='For more information, please visit https://www.canada.ca/en.html')
    await ctx.send(embed=embed)

#Main meteorology glossary section
@client.command(aliases=['wxgl', 'WXGL', 'Weather_Glossary', 'weather_glossary', 'Meteorology Glossary', 'meteorology glossary', 'met_glossary'])
async def metglossary(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.red()
    )
    embed.set_author(name='Meteorology Glossary')
    embed.add_field(name='Canadas Meteorology Glossary (=ca_glossary)', value='Opens the full meteorology glossery, provided by the Canadian Weather Service.', inline=False)
    #code here
    await ctx.send(embed=embed)

#End Canada Alerts
#Canada's Weather and Meteorology glossary
@client.command(aliases=['Canada_Glossary', 'canada_glossary', 'ca_glossary', 'ca_wx'])
async def caglossary(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.purple()
    )
    embed.set_author(name='Canadas Weather and Meteorology Glossary')
    #Remove this!
    embed.add_field(name='Filler Text', value='Filler text (heres a link to the glossary https://www.canada.ca/en/environment-climate-change/services/weather-general-tools-resources/glossary.html#wsglossaryB)', inline=False)
    
    #Below code needs to be tested
    embed.add_field(name='_ _', value='Please look at all the commands below, the letters after "Weather Glossary" relate to the alphabetical order of the glossary.', inline=False)
    embed.add_field(name='Weather Glossary A (command is =WXG_A)', value='_ _', inline=False)
    embed.add_field(name='Weather Glossary B (command is =WXG_B)', value='_ _', inline=False)
    embed.add_field(name='Weather Glossary C (command is =WXG_C)', value='_ _', inline=False)
    embed.add_field(name='Weather Glossary D (command is =WXG_D)', value='_ _', inline=False)
    embed.add_field(name='Weather Glossary E (command is =WXG_E)', value='_ _', inline=False)
    embed.add_field(name='Weather Glossary F (command is =WXG_F)', value='_ _', inline=False)
    embed.add_field(name='Weather Glossary G (command is =WXG_G)', value='_ _', inline=False)
    embed.add_field(name='Weather Glossary H (command is =WXG_H)', value='_ _', inline=False)
    embed.add_field(name='Weather Glossary I (command is =WXG_I)', value='_ _', inline=False)
    embed.add_field(name='Weather Glossary J (command is =WXG_J)', value='_ _', inline=False)
    embed.add_field(name='Weather Glossary K (command is =WXG_K)', value='_ _', inline=False)
    embed.add_field(name='Weather Glossary L (command is =WXG_L)', value='_ _', inline=False)
    embed.add_field(name='Weather Glossary M (command is =WXG_M)', value='_ _', inline=False)
    embed.add_field(name='Weather Glossary N (command is =WXG_N)', value='_ _', inline=False)
    embed.add_field(name='Weather Glossary O (command is =WXG_O)', value='_ _', inline=False)
    embed.add_field(name='Weather Glossary P (command is =WXG_P)', value='_ _', inline=False)
    embed.add_field(name='Weather Glossary R (command is =WXG_R)', value='_ _', inline=False)
    embed.add_field(name='Weather Glossary S (command is =WXG_S)', value='_ _', inline=False)
    embed.add_field(name='Weather Glossary T (command is =WXG_T)', value='_ _', inline=False)
    embed.add_field(name='Weather Glossary U (command is =WXG_U)', value='_ _', inline=False)
    embed.add_field(name='Weather Glossary V (command is =WXG_V)', value='_ _', inline=False)
    embed.add_field(name='Weather Glossary W (command is =WXG_W)', value='_ _', inline=False)
    embed.add_field(name='Weather Glossary Y (command is =WXG_Y)', value='_ _', inline=False)
    await ctx.send(embed=embed)

@client.command(aliases=['Weather_Glossary_A', 'weather_glossary_a', 'WXG_A', 'wxg_a'])
async def glossarya(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.red()
    )
    embed.set_author(name='Weather Glossary (A)')
    embed.add_field(name='Ablation', value='Reduction of the water equivalent of snow cover by melting, evaporation, wind, and avalanches.', inline=False)
    embed.add_field(name='Acid rain', value='A generic term used for precipitation that contains an abnormally high concentration of sulphuric and nitric acid. These acids form in the atmosphere when industrial gas emissions combine with water, and have negative impacts on the environment and human health.', inline=False)
    embed.add_field(name='Advection Fog', value='Fog which forms when a relatively moist and warm air mass moves over a colder water or land surface.', inline=False)
    embed.add_field(name='Advisory', value='A type of alert from Environment and Climate Change Canada’s Meteorological Service (MSC), where a certain weather or environmental hazard (for example air quality and tsunami) is either occurring, imminent or is expected to occur.', inline=False)
    await ctx.send(embed=embed)

@client.command(aliases=['Weather_Glossary_B', 'weather_glossary_b', 'WXG_B', 'wxg_b'])
async def glossaryb(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.red()
    )
    embed.set_author(name='Weather Glossary (B)')
    #code here
    await ctx.send(embed=embed)

@client.command(aliases=['Weather_Glossary_C', 'weather_glossary_c', 'WXG_C', 'wxg_c'])
async def glossaryc(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.red()
    )
    embed.set_author(name='Weather Glossary (C)')
    #code here
    await ctx.send(embed=embed)

@client.command(aliases=['Weather_Glossary_D', 'weather_glossary_d', 'WXG_D', 'wxg_d'])
async def glossaryd(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.red()
    )
    embed.set_author(name='Weather Glossary (D)')
    #code here
    await ctx.send(embed=embed)

@client.command(aliases=['Weather_Glossary_E', 'weather_glossary_e', 'WXG_E', 'wxg_e'])
async def glossarye(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.red()
    )
    embed.set_author(name='Weather Glossary (E)')
    #code here
    await ctx.send(embed=embed)

@client.command(aliases=['Weather_Glossary_F', 'weather_glossary_f', 'WXG_F', 'wxg_f'])
async def glossaryf(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.red()
    )
    embed.set_author(name='Weather Glossary (F)')
    #code here
    await ctx.send(embed=embed)

@client.command(aliases=['Weather_Glossary_G', 'weather_glossary_g', 'WXG_G', 'wxg_g'])
async def glossaryg(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.red()
    )
    embed.set_author(name='Weather Glossary (G)')
    #code here
    await ctx.send(embed=embed)

@client.command(aliases=['Weather_Glossary_H', 'weather_glossary_h', 'WXG_H', 'wxg_h'])
async def glossaryh(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.red()
    )
    embed.set_author(name='Weather Glossary (H)')
    #code here
    await ctx.send(embed=embed)

@client.command(aliases=['Weather_Glossary_I', 'weather_glossary_i', 'WXG_I', 'wxg_i'])
async def glossaryi(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.red()
    )
    embed.set_author(name='Weather Glossary (I)')
    #code here
    await ctx.send(embed=embed)

@client.command(aliases=['Weather_Glossary_J', 'weather_glossary_j', 'WXG_J', 'wxg_j'])
async def glossaryj(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.red()
    )
    embed.set_author(name='Weather Glossary (J)')
    #code here
    await ctx.send(embed=embed)

@client.command(aliases=['Weather_Glossary_K', 'weather_glossary_k', 'WXG_K', 'wxg_k'])
async def glossaryk(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.red()
    )
    embed.set_author(name='Weather Glossary (k)')
    #code here
    await ctx.send(embed=embed)

@client.command(aliases=['Weather_Glossary_L', 'weather_glossary_l', 'WXG_L', 'wxg_l'])
async def glossaryl(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.red()
    )
    embed.set_author(name='Weather Glossary (L)')
    #code here
    await ctx.send(embed=embed)

@client.command(aliases=['Weather_Glossary_M', 'weather_glossary_m', 'WXG_M', 'wxg_m'])
async def glossarym(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.red()
    )
    embed.set_author(name='Weather Glossary (M)')
    #code here
    await ctx.send(embed=embed)

@client.command(aliases=['Weather_Glossary_N', 'weather_glossary_n', 'WXG_N', 'wxg_n'])
async def glossaryn(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.red()
    )
    embed.set_author(name='Weather Glossary (N)')
    #code here
    await ctx.send(embed=embed)

@client.command(aliases=['Weather_Glossary_O', 'weather_glossary_o', 'WXG_O', 'wxg_o'])
async def glossaryo(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.red()
    )
    embed.set_author(name='Weather Glossary (O)')
    #code here
    await ctx.send(embed=embed)

@client.command(aliases=['Weather_Glossary_P', 'weather_glossary_p', 'WXG_P', 'wxg_p'])
async def glossaryp(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.red()
    )
    embed.set_author(name='Weather Glossary (P)')
    #code here
    await ctx.send(embed=embed)

@client.command(aliases=['Weather_Glossary_R', 'weather_glossary_r', 'WXG_R', 'wxg_r'])
async def glossaryr(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.red()
    )
    embed.set_author(name='Weather Glossary (R)')
    #code here
    await ctx.send(embed=embed)

@client.command(aliases=['Weather_Glossary_S', 'weather_glossary_s', 'WXG_S', 'wxg_s'])
async def glossarys(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.red()
    )
    embed.set_author(name='Weather Glossary (S)')
    #code here
    await ctx.send(embed=embed)

@client.command(aliases=['Weather_Glossary_T', 'weather_glossary_t', 'WXG_T', 'wxg_t'])
async def glossaryt(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.red()
    )
    embed.set_author(name='Weather Glossary (T)')
    #code here
    await ctx.send(embed=embed)

@client.command(aliases=['Weather_Glossary_U', 'weather_glossary_u', 'WXG_U', 'wxg_u'])
async def glossaryu(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.red()
    )
    embed.set_author(name='Weather Glossary (U)')
    #code here
    await ctx.send(embed=embed)

@client.command(aliases=['Weather_Glossary_V', 'weather_glossary_v', 'WXG_V', 'wxg_v'])
async def glossaryv(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.red()
    )
    embed.set_author(name='Weather Glossary (V)')
    #code here
    await ctx.send(embed=embed)

@client.command(aliases=['Weather_Glossary_W', 'weather_glossary_w', 'WXG_W', 'wxg_w'])
async def glossaryw(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.red()
    )
    embed.set_author(name='Weather Glossary (W)')
    #code here
    await ctx.send(embed=embed)

@client.command(aliases=['Weather_Glossary_Y', 'weather_glossary_y', 'WXG_Y', 'wxg_y'])
async def glossaryy(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.red()
    )
    embed.set_author(name='Weather Glossary (Y)')
    #code here
    await ctx.send(embed=embed)

#End Meteorlogy Glossary

#Mexico Alerts

@client.command(aliases=['MXAlerts', 'Mexico'])
async def mxalerts(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.purple()
    )
    embed.set_author(name='Alert Help')
    embed.add_field(name='_ _', value='Coming Soon™', inline=False)
    #embed.add_field(name='_ _', value='For more information, please visit >Link Here<', inline=False)
    await ctx.send(embed=embed)

#End Mexico Alerts

#Tropical Cyclone Reports command (maybe this will come with the next update alongside Canadian alerts?)
@client.command(aliases=['TCRs', 'tcrs', 'Tcrs', 'TCR'])
async def tcr(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.red()
    )
    embed.set_author(name='') #Title here?
    embed.add_field(name='Tropical Cyclone Reports', value='Tropical Cyclone Reports are issued by official RSMCs well after the tropical cyclone has taken place. These reports often hold information such as windspeed data, pressure data, storm surge data, etc... These reports can be seen as the RSMCs reanalysis of said tropical cyclone.', inline=False)
    embed.add_field(name='National Hurricane Center/Central Pacific Hurricane Center TCRs', value='The National Hurricane Center and Central Pacific Hurricane Center Tropical Cyclone Reports can be found here: https://www.nhc.noaa.gov/data/tcr/. To find TCRs written by the National Hurricane Center prior to 1995, click on the following link: https://www.nhc.noaa.gov/archive/storm_wallets/, an XML file index of all TCRs can be found here: https://www.nhc.noaa.gov/TCR_StormReportsIndex.xml', inline=False)
    #embed.add_field(name='_ _', value='To find TCRs written by the National Hurricane Center prior to 1995, click on the following link: https://www.nhc.noaa.gov/archive/storm_wallets/, an XML file index of all TCRs can be found here: https://www.nhc.noaa.gov/TCR_StormReportsIndex.xml', inline=False)
    embed.add_field(name='Joint Typhoon Warning Center (JTWC) TCRs', value='The JTWC releases annual tropical cylone reports each year and have done so for many many years, those reports can be found here: https://www.metoc.navy.mil/jtwc/jtwc.html?cyclone. The JTWC best track data archive for each basin (This being Western Pacific, Northern Indian Ocean and Southern Hemisphere) can be found here: https://www.metoc.navy.mil/jtwc/jtwc.html?best-tracks', inline=False)
    embed.add_field(name='Indian Meteorological Department TCRs', value='While the development team could not find reports on past tropical cyclones from the IMD, the IMD does have a best-track map for past seasons currently dating back to 1990. The link to that can be found here: http://www.rsmcnewdelhi.imd.gov.in/report.php?internal_menu=MzM=. The IMD Bulletin archive can be found here: http://www.rsmcnewdelhi.imd.gov.in/report.php?internal_menu=MzQ=. And if you somehow still have Adobe Flash Player, the IMD does have a cyclone eAtlas which contains cyclones in the North Indian Ocean from 1891 to 2020. That link can be found here: http://14.139.191.203/login.aspx?ReturnUrl=%2f.', inline=False)
    embed.add_field(name='Bureau of Meteorology TCRs', value='The Bureau of Meteorologies Tropical Cyclone Reports can be found here: http://www.bom.gov.au/cyclone/tropical-cyclone-knowledge-centre/history/past-tropical-cyclones/', inline=False)
    embed.add_field(name='Meteo France TCRs', value='Meteo France TCR archive unknown', inline=False)
    embed.add_field(name='Fiji Meteorological Service TCRs', value='Fiji Meteorological Service TCR archive unknown', inline=False)
    embed.add_field(name='Other Links', value='At this time the only other interesting link the development team found is a Tropical Cyclone Portal for the Southern Hemisphere couresy of the Bureau of Meteorology. This portal contains tropical cyclone tracks from 1970 to 2018. The link to this portal can be found here: http://www.bom.gov.au/cyclone/tropical-cyclone-knowledge-centre/history/tracks/', inline=False)
    embed.add_field(name='_ _', value='If you know of more links to TCR archives, please contact <@571932650915495966> via DMs.', inline=False)
    await ctx.send(embed=embed)

@commands.Cog.listener()
async def on_message_delete(self, message):

    deleted = discord.Embed(
        description=f"Message deleted in {message.channel.mention}", color=0x4040EC
    ).set_author(name=message.author, url=discord.Embed.Empty, icon_url=message.author.avatar_url)

    deleted.add_field(name="Message", value=message.content)
    deleted.timestamp = message.created_at
    channel = bot.get_channel(channel_id)
    await channel.send(embed=deleted)

@client.command()
async def pages(ctx):
    contents = [novascotia(), princeedwardisland(), ontario(), alberta(), manitoba()]
    pages = 5
    cur_page = 1
    message = await ctx.send(f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}")
    # getting the message object for editing and reacting

    await message.add_reaction("◀️")
    await message.add_reaction("▶️")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]
        # This makes sure nobody except the command sender can interact with the "menu"

    while True:
        try:
            reaction, user = await client.wait_for("reaction_add", timeout=60, check=check)
            # waiting for a reaction to be added - times out after x seconds, 60 in this
            # example

            if str(reaction.emoji) == "▶️" and cur_page != pages:
                cur_page += 1
                await message.edit(content=f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}")
                await message.remove_reaction(reaction, user)

            elif str(reaction.emoji) == "◀️" and cur_page > 1:
                cur_page -= 1
                await message.edit(content=f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}")
                await message.remove_reaction(reaction, user)

            else:
                await message.remove_reaction(reaction, user)
                # removes reactions if the user tries to go forward on the last page or
                # backwards on the first page
        except asyncio.TimeoutError:
            #await message.delete()
            break

            # ending the loop if user doesn't react after x seconds
