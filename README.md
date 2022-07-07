# Google-Play-Scraper

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)
[![PyPI](https://img.shields.io/pypi/v/google-play-scraper.svg)](https://pypi.org/project/google-play-scraper)
[![downloads](https://img.shields.io/pypi/dm/google-play-scraper.svg)](https://pypistats.org/packages/google-play-scraper)
[![versions](https://img.shields.io/pypi/pyversions/google-play-scraper.svg)](https://github.com/JoMingyu/google-play-scraper)
[![scheduled e2e test](https://github.com/JoMingyu/google-play-scraper/actions/workflows/scheduled_e2e_test.yml/badge.svg)](https://github.com/JoMingyu/google-play-scraper/actions/workflows/scheduled_e2e_test.yml)

Google-Play-Scraper provides APIs to easily crawl the Google Play Store for Python *without any external dependencies!*

## Related Projects
### [google-play-scraper](https://github.com/facundoolano/google-play-scraper)
> Node.js scraper to get data from Google Play

I have referred a lot to the API design of this library.

## Installation
```
pip install google-play-scraper
```

## Usage
The country and language codes that can be included in the `lang` and `country` parameters described below depend on the [ISO 3166](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes) and [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) standards, respectively. Therefore, we recommend using an ISO database library such as [pycountry](https://github.com/flyingcircusio/pycountry).

### App Detail
```python
from google_play_scraper import app

result = app(
    'com.nianticlabs.pokemongo',
    lang='en', # defaults to 'en'
    country='us' # defaults to 'us'
)
```

Result of `print(result)`:

```
{
    "title": "Pokémon GO",
    "description": "New! Now you can battle other Pokémon GO Trainers online! Try the GO Battle League today!\r\n\r\nJoin Trainers across the globe who are discovering Pokémon as they explore the world around them. Pokémon GO is the global gaming sensation that has been downloaded over 1 billion times and named “Best Mobile Game” by the Game Developers Choice Awards and “Best App of the Year” by TechCrunch.\r\n_______________\r\n\r\nUncover the world of Pokémon: Explore and discover Pokémon wherever you are!\r\n \r\nCatch more Pokémon to complete your Pokédex!\r\n \r\nJourney alongside your Buddy Pokémon to help make your Pokémon stronger and earn rewards!\r\n\r\nCompete in epic Gym battles and...\r\n\r\nTeam up with other Trainers to catch powerful Pokémon during Raid Battles!\r\n \r\nIt’s time to get moving—your real-life adventures await! Let’s GO!\r\n_______________\r\n\r\nNotes: \r\n- This app is free-to-play and offers in-game purchases. It is optimized for smartphones, not tablets.\r\n- Compatible with Android devices that have 2GB RAM or more and have Android Version 6.0–10.0+ installed.\r\n- Compatibility is not guaranteed for devices without GPS capabilities or devices that are connected only to Wi-Fi networks.\r\n- Application may not run on certain devices even if they have compatible OS versions installed.\r\n- It is recommended to play while connected to a network in order to obtain accurate location information.\r\n- Compatibility information may be changed at any time.\r\n- Please visit PokemonGO.com for additional compatibility information. \r\n- Information current as of October 20, 2020.",
    "descriptionHTML": "New! Now you can battle other Pokémon GO Trainers online! Try the GO Battle League today!<br><br>Join Trainers across the globe who are discovering Pokémon as they explore the world around them. Pokémon GO is the global gaming sensation that has been downloaded over 1 billion times and named “Best Mobile Game” by the Game Developers Choice Awards and “Best App of the Year” by TechCrunch.<br>_______________<br><br>Uncover the world of Pokémon: Explore and discover Pokémon wherever you are!<br> <br>Catch more Pokémon to complete your Pokédex!<br> <br>Journey alongside your Buddy Pokémon to help make your Pokémon stronger and earn rewards!<br><br>Compete in epic Gym battles and...<br><br>Team up with other Trainers to catch powerful Pokémon during Raid Battles!<br> <br>It’s time to get moving—your real-life adventures await! Let’s GO!<br>_______________<br><br>Notes: <br>- This app is free-to-play and offers in-game purchases. It is optimized for smartphones, not tablets.<br>- Compatible with Android devices that have 2GB RAM or more and have Android Version 6.0–10.0+ installed.<br>- Compatibility is not guaranteed for devices without GPS capabilities or devices that are connected only to Wi-Fi networks.<br>- Application may not run on certain devices even if they have compatible OS versions installed.<br>- It is recommended to play while connected to a network in order to obtain accurate location information.<br>- Compatibility information may be changed at any time.<br>- Please visit PokemonGO.com for additional compatibility information. <br>- Information current as of October 20, 2020.",
    "summary": "Discover Pokémon worldwide",
    "installs": "100,000,000+",
    "minInstalls": 100000000,
    "score": 4.28594,
    "ratings": 15214804,
    "reviews": 970851,
    "histogram": [1455041, 416355, 885302, 2024405, 10433680],
    "price": 0,
    "free": True,
    "currency": "USD",
    "sale": False,
    "saleTime": None,
    "originalPrice": None,
    "saleText": None,
    "offersIAP": True,
    "inAppProductPrice": "$0.99 - $99.99 per item",
    "developer": "Niantic, Inc.",
    "developerId": "Niantic,+Inc.",
    "developerEmail": "pokemon-go-support@nianticlabs.com",
    "developerWebsite": "https://niantic.helpshift.com/a/pokemon-go/?p=web",
    "developerAddress": "One Ferry Building, Suite 200\nSan Francisco, CA 94111",
    "privacyPolicy": "https://nianticlabs.com/privacy/pokemongo/en",
    "genre": "Adventure",
    "genreId": "GAME_ADVENTURE",
    "icon": "https://play-lh.googleusercontent.com/SVQIX_fYcu5mc4Pq-D7dgxXZdRMpNTAbRKeBJygAsIXKITHEcKckyhzLsIXMQLSRZw",
    "headerImage": "https://play-lh.googleusercontent.com/KgDQ-Kjb2B7_jDP-8KmQDNhAmP2lqAV_w3zArOCBL7YZnQ02Qqp4VTlgdocO-4MFk4s",
    "screenshots": [
        "https://play-lh.googleusercontent.com/O-OR6Mh0AoNyiaYYaa3OJ_VHGfLqWW2qNzUUZxRRodD3fqs2Pm04FatavdNbz-jsMZM",
        "https://play-lh.googleusercontent.com/HiLNXxmIpOl1jLBssHWcGqsQ58oUC5RvmS5tiX7L86mPHCG6wVEN-aX5OxTKAbDzh10",
        "https://play-lh.googleusercontent.com/Il9B11lqrHX_Kd3QzLCA6hA6O7EsT56ItiLWMf1JkwcdmRyR3CE2KW_vR9w1izanO-JM",
        "https://play-lh.googleusercontent.com/_84Pq9dJ0_iTKwx9-CkYFYoakSMKK_yfdrp1WSX-inE2XvCTr8ri2tKoISLHN_9PEvP5",
        "https://play-lh.googleusercontent.com/JjgLXR7CMiQfSbtICOa86_35f7Pf8IzJn78zWQslwJn56Qm2O7BOV7xzXXE8mz3Vhg",
        "https://play-lh.googleusercontent.com/iAYd9LdbFI7aajPU760XoNZ8b3woDQ58B0harYiUed2y7WQLU19fcj9I8yS-_K9BDQ",
        "https://play-lh.googleusercontent.com/lpw5tz7Onf_6Sx4Q3kGX1zKXcec4EWpRyr9I4w5d3TrQMoorPWVke6veB5qmqhfQZn4",
    ],
    "video": "https://www.youtube.com/embed/DFXbVBFPOOs?ps=play&vq=large&rel=0&autohide=1&showinfo=0",
    "videoImage": "https://play-lh.googleusercontent.com/KgDQ-Kjb2B7_jDP-8KmQDNhAmP2lqAV_w3zArOCBL7YZnQ02Qqp4VTlgdocO-4MFk4s",
    "contentRating": "Everyone",
    "contentRatingDescription": "Mild Fantasy Violence",
    "adSupported": False,
    "containsAds": False,
    "released": "Jul 6, 2016",
    "updated": 1654116395,
    "version": "0.239.1",
    "recentChanges": "Trainers, here’s what’s new in Pokémon GO!\r\n\r\n- Kick off the new Season with Pokémon GO Fest on June 4, 2022, and June 5, 2022. Tickets are available now!\r\n- You can also share the fun of Pokémon GO Fest by gifting tickets to your friends!",
    "recentChangesHTML": "Trainers, here’s what’s new in Pokémon GO!<br><br>- Kick off the new Season with Pokémon GO Fest on June 4, 2022, and June 5, 2022. Tickets are available now!<br>- You can also share the fun of Pokémon GO Fest by gifting tickets to your friends!",
    "comments": [
        "5/12: crashes when i switch between screens, fold 3. Restarts each time, VERY annoying. It's a really fun game and I enjoy the aspect of going out for more than just a breath of fresh air. However, I'm on a Galaxy fold 3 common I find this game crashes quite often. What I mean is that it doesn't fully load when I open it. I've tried for stopping it, clearing cache, and even then it's hit or miss.",
        "The game itself is a great concept, and executed well. The community is still quite active(what, 4, 5 years later?) and is updated frequently. The issue is that there are a few really bad bugs.(I'll only be able to talk about one bug due to text limit :) ) This has only happened during the last week or so, where 4/5 times that I attempt to log in it stops at the very end. Then I have to exit out of the app and retry. This sometimes has taken up to 25 MINUTES to finally get a time where it works.",
        "It's fun, however there are things that could be improved. Why are there not lure modules for every type, or atleast most? It feels unfinished. It would be awesome for other players or friends to show up on your map, maybe not all the time, but if they were currently playing and toggled an option for it on. The map feels lonely, and less fleshed out.",
        'I have enjoyed the game for years and still give the concept 5 stars. But the recent update highlights the long-term technical issues. I personally am unhappy about splitscreen no longer being supported as this makes coordinating raids with my friends impossible. Pvp is still full of bugs and cheaters. Lately while booting the app it will crash and log me out. (This still occurs after following troubleshooting instructions.) I would like to play a solid game, not just a "cool" one.',
        "I love this game, I've spent hundreds of dollars already over the past 5+ years... Unfortunately, I'm leaving this 1* review because the in the latest update, Niantic got rid of pop-up view/split screen. I used this mode to keep stats, infographics, and whatever else I needed up on the screen and out of the way. I'm very disappointed because of this, and I'm now dissuaded from playing this game. I don't have the motivation to play anymore. I'll delete this review if/when it ever gets fixed.",
        "I used to love this game, but the previous updates broke it and the developers refuse to fix it or acknowledge any problems. Instead they blame it on user error. UPDATE: I can now log in after 2 weeks, thanks to the latest update, but the server lag is AWFUL and makes it hard to do much. But at least I can play again, sort of. I wish I could be compensated for the loss of progress, but I doubt it. Updated rating to 3 stars.",
        "I really love this game, but since the latest update it's been impossible to play. Takes 2-4 tries to even get past the loading splash and freezes + crashes at the slightest provocation (attempting to open News, Special Research, Gyms, trainer profile etc.) I know I'm not the only one having these issues across a wide variety of device & OS, so I'm very disappointed that this update has been out for weeks and these problems haven't been addressed. I'll improve my review and rating when they are.",
        "The quality of this game has gone down a lot recently, like community day being shortened, as well as incense being drastically reduced. And to top it all off, there is a glitch I've been experiencing where when I click on a pokemon, the screen goes white, and the game refuses to respond, then things went from bad to worse when it just crashed when the white screen appeared after a few seconds.",
        "Shoutout to the dev team for making Incenses USELESS by lowering the standing spawn rate SEVENTY FREAKING PERCENT. Now I'm incensed. Congrats! Also the memory requirements for this game have become absurd. Some of the features have been de-bloated, but it isn't enough. Also also, AR at startup should be opt-in rather than opt-out. The popup doesn't do jack as far as turning it off. Fix that. I will continue to use this, but I'm not spending any (more) money until these issues are fixed.",
        "I've played this game for a long time off and on. Got into it a lot more through the pandemic and since the last update I can't play it anymore. Can't even get past the load screen. Intensely aggravating. I'm about to stop playing permanently because even when it was 'working' it was crashing when trying to load rewarded Pokemon. I'll update rating if you guys can update the app enough to work on my Motorola.",
        "5/25: I love this game, but as for the past two months it has become physically unplayable. Crashes gradually became more and more common until I can't exit the \"Beware of your surroundings\" warning on start-up without the game breaking down. My phone meets and exceeds the minimum requirements, but it literally doesn't work.",
        "Personally, I (usually) love this game. Until recently, I'd get on twice a day or so and use the game to it's fullest potential. However after the last update, I'm in the game but 10 seconds and it crashes, kicking me out of the app. The game has crashed before, but never so many times in a row. Maybe my phone is just bad, but this and several other bugs hinder the otherwise amazing experience.",
        "I really enjoy this game, but since the latest update, it takes 2-3 tries to actually get the app to start. Sometimes I have to reboot my phone just to get the app to fully open; otherwise it gets stuck on the loading screen. Additionally, if I start the app while connected to WiFi, then switch to data, it hangs (and the white Poke ball spins in the upper left corner). It's quite frustrating, especially since the previous version started up fairly quickly. Please fix!",
        "I played when the game first came out but it quickly grew boring. I set it aside for a couple years and came back when a friend asked me to join them. I've played for a few months only to grow bored again and disgusted at the money grab this game is. They implemented some good changes during covid but have decided to kill that off. Remote passes are often the only way I can raid each week and I have many friends with the same limitation. Not to mention the very limited hours for quests Saturdays",
        "Fix the hit box for throws. Numerous times I've landed straight in the middle with no excellent being triggered. Complete bs for a game that is this old. Fix the stuttering that happens every 15 seconds or so. Seriously, complete BS that these bugs are still in the game. Stop adding new things b4 fixing whats already broken. Hello? Where is your brain at??",
        "I love the game however recently the game hasn't been loading pass the watch out for object around you screen. The moment I touch the screen the game closes out. I tried to uninstall and reinstall hoping it would work but it hasn't. I don't know if it's a bug. Hopefully it will be fixed soon I don't want to stop playing a game I had for a long time. I love my Eevee and evolutions especially Vaporeon.",
        "Please add back the ability to split screen or multiscreen the app!! I'm used to playing two accounts at once, and I bought this new amazing gaming phone so it can handle two instances running at once!! Being limited to one screen per phone is such a downgrade. I'll update my review if it's patched.",
        "It's a fun game. It does use up quite a bit of battery on your phone~so plan accordingly. A suggestion I have~during battles a notice will pop up that an attack is coming and asks if you want to block it. The 'not now' button is in the same spot at the attack botton. And most times I accidentally push 'not now' and then my Pokemon dies :/. Can that be changed, please?",
        "I've been playing since this came out. I have never had so many force closings happen in ANY APP ever! Every single time I go to take a picture to finish a task it force closes. I've uninstalled and reinstalled 4 times now with no relief. What's the deal? I'm about to just quit the game all together if this keeps up",
        "The app has been pretty much broken for a while now. It takes several tries for me to get in and even then the app is slow, unresponsive, and sometimes freezes my whole phone and then crashes anyways. I can't even listen to music while I play anymore, it makes the game lag terribly. Usually it shuts off my music and then crashes itself. No amount of restarting my phone or refreshing the game data helps. I really did enjoy the game but it's been a nightmare lately and it's not worth the headache.",
        "I remember playing this game a bit when I was younger, and it was fine, no problems. Nowadays, I can't even play it without textures not loading in and it freezing and then crashing every minute or so. It still a relatively good game looking pass that, though. Edit: I don't know what you guys or I did, but it's acting better! Still lags a bit, but it's much better than before!",
        "The game is great! It's fun to play, the controls are easy, the graphics and sound are amazing, and there are no ads! That said, if it is your only exposure to the Pokémon franchise, please know that it is nothing like the canon games (that's right, I don't consider it canon- that's how different it is)! My only complaint is that it can be pretty laggy sometimes!",
        "The app is very stable and basically never crashes or has connection issues compared to when I first started playing. With the changes made since the pandemic it's now a lot easier to play whenever without needing to sit in an urban area near a ton of PokeStops, which is great. The main problem is they keep pushing AR mode and have completely ruined buddies by getting rid of the old mode that actually worked.",
        "So before this last update it was working fine, but now it crashes and when I log in it doesn't run for more than a minute. I love this game but it's starting to make me mad because of the constant crashing. The game should have a bigger interaction meter for the people who can't go out as much because of the pandemic. Im giving it a three star but it will go back up when it starts to work better.",
        "Game is a fun idea, poorly executed on anything other than apple. I want to play with my friends but the difference in quality is too great. Don't make the game for multiple platforms if it's only optimized for one. Used increased distances to help with COVID restrictions and pulled them back, regardless of the pandemic still raging. Unethical and unprofessional.",
        "I've been enjoying this game for almost 2 years now, however I have encountered a few issues 1. The game is unusually laggy right now, and freezes somewhat often. 2. On my phone, the game simply will not update, I have to delete it and reinstall it again in order to apply updates. Other than that, the game is very fun, however until there issues are fixed my rating will be lowered to 3 stars.",
        "Really glitchy.... The graphics are not good too .... It is really basic, same backgrounds and other designs are still the same. The Asian company doesn't even bother changing the designs after 6 years. The NEWS are saying, that they are using the game as a counter terrorism organization app. They are using locations, physical activity, different land mapping, Google maps, phone storage and more. As soon as you download the game, you are granting permission of the app into your phone. Beware!!",
        "First off, I really enjoy this game. Have been playing for almost 4 years. But it's turned into trash with every update, and the game is virtually unplayable due to constant crashes and failing to even start. I initially gave it 4 stars cause they couldn't get their server issues figured out. I'm lowering it to 1 star cause they haven't improved it, they've made it worse. Maybe they can put the millions a year of profits into making a game that can be played, I'll play again.",
        "Very good game, only 2 things I don't like, I don't live near pokestops (just delt a bad hand). And also I was wondering if there could be a switch that let you show up on other peoples screens, It can help friends find eachother and find a new person to battle. Edit: lots of the charechters fall apart, only a small graphical glitch",
        "I have the hardest time with this game. For the most part it's fun but the grind is really high especially if you play this more for a collector status vs. a someone who likes to battle, which cause an annoying pay to play senario. Not to mention it's a really buggy app, 9 out of 10 it has a very hard time launching. It crashes and it slows down all the time. I really hope they make this game better in the future but for now I guess I wait so much time grinding uselessly until then, I guess.",
        "Sometimes it works well, other times it constantly crashes. Also, when their game keeps messing up and you lose items that you had to pay for, they will only reimburse your items so many times. It doesn't matter if their game keeps crashing, they don't want you refunded. I stopped spending any money on coins because of this.",
        "Wish I could give zero stars. I'm getting sick of uninstalling and reinstalling after every little update just because the developers are apparently incompetent. Seems to be a recurring issue otherwise I'd be more understanding and forgiving. It would be nice to be able to open the app in less than 3 attempts every time... unfortunately Niantic doesn't seem to care about the players, just the money",
        "The latest update has caused a lot of issues for me. It's slow to start, and sometimes it stays on the start up screen for 5 minutes with no change. It'll take up to 4 tries to actually load the game. Not only that, incense being nerfed was the biggest mistake they can ever make. There's still a pandemic!",
        "A pretty good time killer every once in a while. My only real complaints are the slow player progression and poor loading times. Granted, I don't exactly have the best phone, so load times could be a me issue. The game can get pretty tiresome after a week or so, but never boring enough for me to consider uninstalling.",
        "I really don't want to hate this game, but it's extremely difficult. The battle league (or Battle Lag, as I like to call it), is infuriating and raids tend to be buggy as well. Furthermore, in recent months it seems as though it's become significantly more pay to win. Niantic has made some minor changes after the uproar, but it's still becoming a game that very much favors the fat wallet. It can be fun, at times, but the bad moments are starting to outnumber the good ones.",
        "Pokémon Go is a great premise and I have enjoyed playing it since it came out. When the pandemic hit and the distance to stops and Pokémon was increased to help allow more people to play safely, my game experience massively improved. Niantic has now reversed the spinning distance back from 80 m spinning distance to 40 m which greatly limits my ability to play the game effectively. Please put it back. Update: Niantic listened to the fan base and permanently changed to 80 m. Thank you!",
        "Fun enough to keep around on my phone. Been playing it since around the time it released, but there's been very little change in regards to gameplay over the years, and at a point you hit a severe wall with leveling and gaining items. At one point it just becomes a straight up grind and it's no longer the sort of game I go out of my way to play, I just turn it on when my friends play it.",
        "Used to be more of a tech demo.... But still fun to play with. Nowadays there's a real game here with the excellent pvp battle league - it's definitely got a learning curve, but it really does give me a reason to catch them all. Also there are often interesting events going on. Very entertaining, makes the game fresher. In app purchases aren't too pay to win. Time, location, and brains are the biggest factors. I hope they continue to put the work in to make the game great!",
        "Overall experience with the game personally has been much better recently compared to a few years ago. Definitely noticing more crashes with this update though. One crash cost me a raid and remote raid pass that I paid for. Obviously it's not the biggest issue, but if I'm willing to put money into a mobile game and I lose what I paid for in-game because of YOUR update, then I feel like the game should be able to replace what's lost during the crash. Just something to consider for your customers.",
        "Why half the interaction distance with health concerns still high? Doubling the distance was a great idea. It helped with several misplaced pokestops in my area that are an accessible due to misplacement or closed access. People do silly things sometimes to get to some of these stops. I did not see that happening in the last year. This decision should be reversed with a rise in the d variant. The interactive distance is too small.",
    ],
    "appId": "com.nianticlabs.pokemongo",
    "url": "https://play.google.com/store/apps/details?id=com.nianticlabs.pokemongo&hl=en&gl=us",
}
```

### App Reviews
`reviews` function returns `result` with `continuation token`.

- `result` : Crawling result of reviews. (list)
- `continuation_token` : Data containing how many items were loaded, what arguments used in the current result. If you pass this value to the `continuation_token` parameter of the `reviews` function, the next items are crawled. For example, if 1000 reviews are retrieved and the returned token 'eXamplE' is passed to the reviews function, the list of reviews is retrieved from 1000 or later items.

> :bulb: Setting `count` too high can cause problems. Because the maximum number of reviews per page supported by Google Play is 200, it is designed to pagination and recrawl by 200 until the number of results reaches count.

```python
from google_play_scraper import Sort, reviews

result, continuation_token = reviews(
    'com.fantome.penguinisle',
    lang='en', # defaults to 'en'
    country='us', # defaults to 'us'
    sort=Sort.NEWEST, # defaults to Sort.NEWEST
    count=3, # defaults to 100
    filter_score_with=5 # defaults to None(means all score)
)

# If you pass `continuation_token` as an argument to the reviews function at this point,
# it will crawl the items after 3 review items.

result, _ = reviews(
    'com.fantome.penguinisle',
    continuation_token=continuation_token # defaults to None(load from the beginning)
)
```

Result of `print(result)`:

```
[
    {
        "userName": "Alyssa Williams",
        "userImage": "https://lh3.googleusercontent.com/-cVEHKr7mzv8/AAAAAAAAAAI/AAAAAAAAAAA/AKF05nB2r3GUkji31m0tC4ylFNiVMpmNWA/photo.jpg",
        "content": "This is literally the best idle game I have ever played. The penguins waddle around and live their best lives in the cutest little outfits. I just unlocked the little penguins and I have been sobbing uncontrollably for ten minutes because they are so adorable. There are only two suggestions I have for this game: more of the penguin info ads. I love them. I have learned so much about all the teeny fellas. Secondly, I would like to be able to name my 'guins so I can tell them apart.",
        "score": 5,
        "thumbsUpCount": 54,
        "reviewCreatedVersion": "1.16",
        "at": datetime.datetime(2020, 2, 24, 17, 19, 34),
        "replyContent": "Hello, We will gradually improve the various systems in the game to enhance the player's game experience. We have recorded your suggestions and feedback to the planner. If you have any other suggestions and ideas, please feel free to contact us at penguinisle@habby.com.Thank you for playing!",
        "repliedAt": datetime.datetime(2020, 2, 24, 18, 30, 42),
        "reviewId": "gp:AOqpTOE0Iy5S9Je1F8W1BgCl6l_TCFP_QN4qGtRATX3PeB5VV9aZu6UHfMWdYFF1at4qZ59xxLNHFqYLql5SL-k"
    },
    {
        "userName": "EasyJet 123",
        "userImage": "https://lh3.googleusercontent.com/a-/AOh14GhE3-Fsq5KDs_kmCRGcifbNUQTOtK5DpZkJ2AiqyQ",
        "content": "Easily my favorite game. Relaxing, with easy controls, no purchase necessary to advance... I love it. 100% recommend. I love how you can get gems continually by completing missions, and the low price of boosts are great. But how about adding new buildings like an airport, an army base, and a train station? Would be great to see these. And the building purchase price might be lowered so it's a bit easier to progress after the Igloo. Maybe...",
        "score": 5,
        "thumbsUpCount": 79,
        "reviewCreatedVersion": "1.14",
        "at": datetime.datetime(2020, 2, 12, 8, 42, 41),
        "replyContent": None,
        "repliedAt": None,
        "reviewId": "gp:AOqpTOHyQo9QEPtxefmvjNuqR9VmFyBaj2FNXLvHsuH19de9bC0dT_voHWSKNGFcc10jv077wOdzBrkgLKX6pUc"
    },
    {
        "userName": "Lillemann",
        "userImage": "https://lh3.googleusercontent.com/a-/AOh14GjiVSIrx033k9HZ9Tu4BQ1iYZST0IRW8UlDCX3gdw",
        "content": "Really good looking. And it runs super super smooth. I love the camera options when clicking the camera button. And the penguins looks absolutely awesome and I really love the limited eddition ones. That sometimes the ads are replaced with penguin facts is just awesome. I suggest that you set up some kind of leaderboard it could probobly show the players that are earning the most money per sec or something. But overall this game is a strong 10/10",
        "score": 5,
        "thumbsUpCount": 2,
        "reviewCreatedVersion": "1.14",
        "at": datetime.datetime(2020, 2, 11, 18, 8, 11),
        "replyContent": "Thank you very much for your review concerning our game. We will try our best to do better,If you have any other feedback or suggestions, feel free to contact us at penguinisle@habby.com. Have a nice day!",
        "repliedAt": datetime.datetime(2020, 2, 11, 18, 53, 38),
        "reviewId": "gp:AOqpTOEGUPB6HA0DIPNp3K2yAHRK-GN96dVJ-zkhPgKpclevgt8q9nR6Pv4N_F4TIPCpMeaoTutNGOZ2CSs65Ws"
    },
]
```

### App All Reviews
`reviews_all` function returns all of reviews from app. If you want to set the count to infinity while using the `reviews` function, you can use the `reviews_all` function.

> :bulb: Because of the Google Play Store limit (up to 200 reviews can be fetched at a time), http requests are generated as long as the number of app reviews is divided by 200. For example, targeting an app like Pokémon GO makes tens of thousands of http requests.

```python
from google_play_scraper import Sort, reviews_all

result = reviews_all(
    'com.fantome.penguinisle',
    sleep_milliseconds=0, # defaults to 0
    lang='en', # defaults to 'en'
    country='us', # defaults to 'us'
    sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
    filter_score_with=5 # defaults to None(means all score)
)
```


### App Permissions
`permissions` function returns permissions of app.

```python
from google_play_scraper import permissions

result = permissions(
    'com.spotify.music',
    lang='en', # defaults to 'en'
    country='us', # defaults to 'us'
)
```

Result of `print(result)`:

```
{
    "Microphone": [
        "record audio"
    ],
    "Wi-Fi connection information": [
        "view Wi-Fi connections"
    ],
    "Camera": [
        "take pictures and videos"
    ],
    "Photos/Media/Files": [
        "modify or delete the contents of your USB storage",
        "read the contents of your USB storage"
    ],
    "Storage": [
        "modify or delete the contents of your USB storage",
        "read the contents of your USB storage"
    ],
    "Device ID & call information": [
        "read phone status and identity"
    ],
    "Contacts": [
        "find accounts on the device"
    ],
    "Phone": [
        "read phone status and identity"
    ],
    "Identity": [
        "add or remove accounts",
        "find accounts on the device"
    ],
    "Other": [
        "access Bluetooth settings",
        "allow Wi-Fi Multicast reception",
        "change network connectivity",
        "change your audio settings",
        "control Near Field Communication",
        "control vibration",
        "full network access",
        "install shortcuts",
        "pair with Bluetooth devices",
        "prevent device from sleeping",
        "run at startup",
        "send sticky broadcast",
        "use accounts on the device",
        "view network connections"
    ],
    "Uncategorized": [
        "receive data from Internet"
    ]
}
```
### App Search
```python
from google_play_scraper import search

result = search("best Pikachu game",
                lang="en",  # defaults to 'en'
                country="us",  # defaults to 'us'
                n_hits=3  # defaults to 30 (= Google's maximum)
)
result
```

Result of `print(result)`:

```
[{'appId': 'com.nianticlabs.pokemongo',
  'icon': 'https://play-lh.googleusercontent.com/SVQIX_fYcu5mc4Pq-D7dgxXZdRMpNTAbRKeBJygAsIXKITHEcKckyhzLsIXMQLSRZw',
  'screenshots': ['https://play-lh.googleusercontent.com/O-OR6Mh0AoNyiaYYaa3OJ_VHGfLqWW2qNzUUZxRRodD3fqs2Pm04FatavdNbz-jsMZM',
   'https://play-lh.googleusercontent.com/HiLNXxmIpOl1jLBssHWcGqsQ58oUC5RvmS5tiX7L86mPHCG6wVEN-aX5OxTKAbDzh10',
   'https://play-lh.googleusercontent.com/Il9B11lqrHX_Kd3QzLCA6hA6O7EsT56ItiLWMf1JkwcdmRyR3CE2KW_vR9w1izanO-JM',
   'https://play-lh.googleusercontent.com/_84Pq9dJ0_iTKwx9-CkYFYoakSMKK_yfdrp1WSX-inE2XvCTr8ri2tKoISLHN_9PEvP5',
   'https://play-lh.googleusercontent.com/JjgLXR7CMiQfSbtICOa86_35f7Pf8IzJn78zWQslwJn56Qm2O7BOV7xzXXE8mz3Vhg',
   'https://play-lh.googleusercontent.com/iAYd9LdbFI7aajPU760XoNZ8b3woDQ58B0harYiUed2y7WQLU19fcj9I8yS-_K9BDQ',
   'https://play-lh.googleusercontent.com/lpw5tz7Onf_6Sx4Q3kGX1zKXcec4EWpRyr9I4w5d3TrQMoorPWVke6veB5qmqhfQZn4',
   'https://play-lh.googleusercontent.com/KgDQ-Kjb2B7_jDP-8KmQDNhAmP2lqAV_w3zArOCBL7YZnQ02Qqp4VTlgdocO-4MFk4s'],
  'title': 'Pokémon GO',
  'score': 4.283571,
  'genre': 'Adventure',
  'price': 0,
  'free': True,
  'currency': 'USD',
  'video': 'https://www.youtube.com/embed/DFXbVBFPOOs?ps=play&vq=large&rel=0&autohide=1&showinfo=0',
  'videoImage': 'https://i.ytimg.com/vi/DFXbVBFPOOs/hqdefault.jpg',
  'description': 'New! Now you can battle other Pokémon GO Trainers online! Try the GO Battle League today!\r\n\r\nJoin Trainers across the globe who are discovering Pokémon as they explore the world around them. Pokémon GO is the global gaming sensation that has been downloaded over 1 billion times and named “Best Mobile Game” by the Game Developers Choice Awards and “Best App of the Year” by TechCrunch.\r\n_______________\r\n\r\nUncover the world of Pokémon: Explore and discover Pokémon wherever you are!\r\n \r\nCatch more Pokémon to complete your Pokédex!\r\n \r\nJourney alongside your Buddy Pokémon to help make your Pokémon stronger and earn rewards!\r\n\r\nCompete in epic Gym battles and...\r\n\r\nTeam up with other Trainers to catch powerful Pokémon during Raid Battles!\r\n \r\nIt’s time to get moving—your real-life adventures await! Let’s GO!\r\n_______________\r\n\r\nNotes: \r\n- This app is free-to-play and offers in-game purchases. It is optimized for smartphones, not tablets.\r\n- Compatible with Android devices that have 2GB RAM or more and have Android Version 6.0–10.0+ installed.\r\n- Compatibility is not guaranteed for devices without GPS capabilities or devices that are connected only to Wi-Fi networks.\r\n- Application may not run on certain devices even if they have compatible OS versions installed.\r\n- It is recommended to play while connected to a network in order to obtain accurate location information.\r\n- Compatibility information may be changed at any time.\r\n- Please visit PokemonGO.com for additional compatibility information. \r\n- Information current as of October 20, 2020.',
  'descriptionHTML': 'New! Now you can battle other Pokémon GO Trainers online! Try the GO Battle League today!<br><br>Join Trainers across the globe who are discovering Pokémon as they explore the world around them. Pokémon GO is the global gaming sensation that has been downloaded over 1 billion times and named “Best Mobile Game” by the Game Developers Choice Awards and “Best App of the Year” by TechCrunch.<br>_______________<br><br>Uncover the world of Pokémon: Explore and discover Pokémon wherever you are!<br> <br>Catch more Pokémon to complete your Pokédex!<br> <br>Journey alongside your Buddy Pokémon to help make your Pokémon stronger and earn rewards!<br><br>Compete in epic Gym battles and...<br><br>Team up with other Trainers to catch powerful Pokémon during Raid Battles!<br> <br>It’s time to get moving—your real-life adventures await! Let’s GO!<br>_______________<br><br>Notes: <br>- This app is free-to-play and offers in-game purchases. It is optimized for smartphones, not tablets.<br>- Compatible with Android devices that have 2GB RAM or more and have Android Version 6.0–10.0+ installed.<br>- Compatibility is not guaranteed for devices without GPS capabilities or devices that are connected only to Wi-Fi networks.<br>- Application may not run on certain devices even if they have compatible OS versions installed.<br>- It is recommended to play while connected to a network in order to obtain accurate location information.<br>- Compatibility information may be changed at any time.<br>- Please visit PokemonGO.com for additional compatibility information. <br>- Information current as of October 20, 2020.',
  'developer': 'Niantic, Inc.',
  'installs': '100,000,000+'},
 {'appId': 'jp.pokemon.pokemonunite',
  'icon': 'https://play-lh.googleusercontent.com/l6iBBhrah3mNhvcjZgZBwICAF5uu3KjorU4pq-eMOxYgT_L_TnpzT7a3TmmdxaMMgbUy',
  'screenshots': ['https://play-lh.googleusercontent.com/0BXdHWr_OWcqwc2egRCGa9el75tMO9VS7tj2K2oiHMulKpVZ7t7eKLYwdye7JnUhdxMj',
   'https://play-lh.googleusercontent.com/tReAAbW5OMk2tFwAWHuCCjdfUHTcx11tHPfmX8HF9ggTf4dJZ5A5AKfEoGYhg0ee9kU',
   'https://play-lh.googleusercontent.com/VVXVsn7QiICtyN7VI4IlFAhC4i5Vw-ezx3sLbywIG01HpKUlbVcDsnqM6Rc6TStHgQ',
   'https://play-lh.googleusercontent.com/qIdex-XxcS2Dl5Efq6DJF39VQuJShLoeLC0X40YiqeSV-ePG0N2CGKWbZI07sXPEDDo',
   'https://play-lh.googleusercontent.com/BQun4awXd5t-NapkXAI7-uyOl1PzWr80NWPKnSsDBrR8-FZLLBIz5KNg_pHK36EMoYYK',
   'https://play-lh.googleusercontent.com/57M-IQvvMsyRUULDZZ6cXGRaiVJMUY9ABf7R19sdmi8sS-hOzf7wp3v5JgOxrIMcag',
   'https://play-lh.googleusercontent.com/BOIBHIXkqZKDcUSvZUM88GiftsIxLoFU1qR2R0PiKRImWXOT4MG0GRdfRkIhESTlipoc',
   'https://play-lh.googleusercontent.com/F_kaX-tKz2KwQeozaB4emu8OaH422d3uSB9Ovhp3Rdycyh303Pukj-LLmsh4drid4Q2Y',
   'https://play-lh.googleusercontent.com/HuxwQsc_wqUeGgyeclWyiNYKIYbUhx4HL2evXauReksvdMwKazZ2Ze8oYysbPkTH7Do',
   'https://play-lh.googleusercontent.com/h_VR3XmUEbStoW4Kbkz48etOwc6I8AO7caEPmlG_s6QoFn_Hvy8cPGHZs8Ie8sIn4COD',
   'https://play-lh.googleusercontent.com/pXZIkNh6VGWAkL5kDDVUVxAjba1aRVootuQRfHmLRLnI3TC2AqMm5H19M8jIj2jzIQ',
   'https://play-lh.googleusercontent.com/zW64FFgL-bacNW851Z-veKZJEAFjt5G6iA_1DJjH5GGgoBrzOITYOSANSoZRvTrV91Dp',
   'https://play-lh.googleusercontent.com/LgY2r8NPH1SErkQ46Srhyzujxg3Po-ZBo7DYOUrqctIya-DeeTJRbOtC1lAtgdAE3w',
   'https://play-lh.googleusercontent.com/legf5ocJ02NksPSP__k5g7I-EXa9w34F1Xd5BBQ2p4ILvvGdkR2T-CXfqwhzLF4RJW8',
   'https://play-lh.googleusercontent.com/KRaCNowecDHdl1V7y1wkhlBf_qOiGddBNRORXOU5xfAQdjnJqK3RYD8dgCUFY29E_Uo',
   'https://play-lh.googleusercontent.com/Kx2V-5ybEv2m1K1f1v2bJHRO27WNIpb-2Gex6sMh63Fzr9T6Npwh3lDu2tG8oOnP7A',
   'https://play-lh.googleusercontent.com/_yL5mS4Iw65B0L9gfoz--xKbfijilqEA0kEVk5N3muLXBLsWly2BR-mpwJl5Ia2IoQ',
   'https://play-lh.googleusercontent.com/ULyQg55oKym85qsQMvKq0nVginG2gF0qw5g82knbjS15pMu-n_HxRYL86FyOEiRXboQ',
   'https://play-lh.googleusercontent.com/6LZs0vvZFta2dcFjKSglRx-ugeYzYYjM_ziEYv8_O14Hngr6rid2-qYuBsgri8GefQ',
   'https://play-lh.googleusercontent.com/Q5nklhiiZwY_tnUjUlvh9PkDS-H-OF7wBI_AblMUbpVVdVr1CEw1CuO791p_1bU0bkgE',
   'https://play-lh.googleusercontent.com/AVrvQmbm06_cta6VInNudHS0aqOQcZEkM-KRGU8IdN3HW3lHMEXwJsyWTivUK8juBQ',
   'https://play-lh.googleusercontent.com/MaFH8pnG9lT6m7XeaFC0r2ZsRprk9VkSTO22ornPlot9GGrimGl9iBoiy4emMtgOFg'],
  'title': 'Pokémon UNITE',
  'score': 4.5547147,
  'genre': 'Action',
  'price': 0,
  'free': True,
  'currency': 'USD',
  'video': 'https://www.youtube.com/embed/ZLBVuHDguvQ?ps=play&vq=large&rel=0&autohide=1&showinfo=0',
  'videoImage': 'https://i.ytimg.com/vi/ZLBVuHDguvQ/hqdefault.jpg',
  'description': 'Headline:\r\n\r\nPokémon UNITE:\r\nTeam up and take down the opposition in Pokémon’s first 5-on-5 strategic team battle game!  \r\n\r\nJoin Trainers from around the world as they head for Aeos Island to compete in Unite Battles! In Unite Battles, Trainers face off in 5-on-5 team battles to see who can score the most points within the allotted time. Teamwork is key as you and your teammates defeat wild Pokémon, level up, evolve your own Pokémon, and work to prevent the opposing team from scoring points. Put your teamwork to the test, and take home the win!  \r\n\r\nKey Features: \r\n•\tBATTLE IN STYLE: Take to the field while looking your best in Holowear! Thanks to a special technology developed using Aeos energy, Trainers can deck out their Pokémon in a variety of holographic outfits—with new styles arriving regularly! \r\n \r\n•\tUNITE MOVES: Unleash the true power of your Pokémon with Unite Moves! Leverage these all-new Pokémon moves, which are only possible while in Unite Battles, and turn the tide of even the direst situations. \r\n \r\n•\tRANK UP: Looking to prove how skilled you are? Participate in ranked matches, and earn points as you climb up the global leaderboard! \r\n \r\n•\tCOMMUNICATION IS KEY: Even the most skilled Trainers recognize how important communication is to their team’s success. Leverage signals, quick-chat messages, and—for the first time in a Pokémon title—voice chat to communicate and stay in sync with your team. \r\n \r\n•\tCROSS-PLATFORM PLAY: Challenge Trainers from around the world to Unite Battles on the Nintendo SwitchTM system or on a compatible mobile device thanks to cross-platform support. Trainers may use their Pokémon Trainer Club account or Nintendo Account on both Nintendo Switch and mobile to easily keep their progress synced between devices. \r\n\r\n\r\nCheck out the official website for more information, and follow Pokémon UNITE on Twitter for all the latest news. \r\n------------------------------------------------------------\r\nOfficial Website: http://PokemonUNITE.com/\r\nOfficial Twitter: https://twitter.com/PokemonUNITE/\r\n\r\nLegal:\r\n•\tThis is a free-to-start game; optional in-game purchases available. Data charges may apply.\r\n•\tAn internet connection is required to play the game.',
  'descriptionHTML': 'Headline:<br><br>Pokémon UNITE:<br>Team up and take down the opposition in Pokémon’s first 5-on-5 strategic team battle game!  <br><br>Join Trainers from around the world as they head for Aeos Island to compete in Unite Battles! In Unite Battles, Trainers face off in 5-on-5 team battles to see who can score the most points within the allotted time. Teamwork is key as you and your teammates defeat wild Pokémon, level up, evolve your own Pokémon, and work to prevent the opposing team from scoring points. Put your teamwork to the test, and take home the win!  <br><br>Key Features: <br>•\tBATTLE IN STYLE: Take to the field while looking your best in Holowear! Thanks to a special technology developed using Aeos energy, Trainers can deck out their Pokémon in a variety of holographic outfits—with new styles arriving regularly! <br> <br>•\tUNITE MOVES: Unleash the true power of your Pokémon with Unite Moves! Leverage these all-new Pokémon moves, which are only possible while in Unite Battles, and turn the tide of even the direst situations. <br> <br>•\tRANK UP: Looking to prove how skilled you are? Participate in ranked matches, and earn points as you climb up the global leaderboard! <br> <br>•\tCOMMUNICATION IS KEY: Even the most skilled Trainers recognize how important communication is to their team’s success. Leverage signals, quick-chat messages, and—for the first time in a Pokémon title—voice chat to communicate and stay in sync with your team. <br> <br>•\tCROSS-PLATFORM PLAY: Challenge Trainers from around the world to Unite Battles on the Nintendo SwitchTM system or on a compatible mobile device thanks to cross-platform support. Trainers may use their Pokémon Trainer Club account or Nintendo Account on both Nintendo Switch and mobile to easily keep their progress synced between devices. <br><br><br>Check out the official website for more information, and follow Pokémon UNITE on Twitter for all the latest news. <br>------------------------------------------------------------<br>Official Website: http://PokemonUNITE.com/<br>Official Twitter: https://twitter.com/PokemonUNITE/<br><br>Legal:<br>•\tThis is a free-to-start game; optional in-game purchases available. Data charges may apply.<br>•\tAn internet connection is required to play the game.',
  'developer': 'The Pokemon Company',
  'installs': '10,000,000+'},
 {'appId': 'com.dena.a12026418',
  'icon': 'https://play-lh.googleusercontent.com/h4dRm7zBF605F3rNY-KdMlTIGatw4csK1HSUEBit7-PtqPmYuXxzP-Wooy8hRI8YTA',
  'screenshots': ['https://play-lh.googleusercontent.com/82gD-bWWy0B9SHVaPqTnvCNo_SBk0ssGyI2ZrbgOvNQ6FK6guz20aKPKhLcCCUv_SP8',
   'https://play-lh.googleusercontent.com/ysrmlowWJCm5nF-i-nAezyDr_jHlfe0tCOLOSzsIVyGTMQnDxoO5h30uCk5DgYDY6A',
   'https://play-lh.googleusercontent.com/Xj85MdUloyyfLNjud73TBcJL3j9r97O3lEWjwnTyk4hF00gqQb58x64Bx2HoJlmBW5Oi',
   'https://play-lh.googleusercontent.com/J7tY8gJtd5pyiGe-To-Amfbc7aiWqzLqm3Msg0UnLSp0DCtX9mwxS4xAisliQw2OfA0',
   'https://play-lh.googleusercontent.com/u_od4LQquoRSoZF5hA9dAH0dB41illZ6ouYxIl49bH8yHoQulcUslwxy-b9nWxCiOJtM',
   'https://play-lh.googleusercontent.com/wIRwnAKtqBD6GL2Lxnz8K-1jZlZ9qbBUXD5tMToxF-sUyWNBxUD5m_rR8bwXR98oGls',
   'https://play-lh.googleusercontent.com/I-wGFjAD7ut2YGNze8xDVaiR89HCAxKPEOgfYcGpR3Ka5vKjQPH5M4BXti2xWJqEpA',
   'https://play-lh.googleusercontent.com/9cap7BX24s5T_RNPDIXN6rykD0J4LMOhaC1JCPjcRGhkcTO32JNX2GD88Hw5usFjbgo',
   'https://play-lh.googleusercontent.com/j3024cER2J5EIyNIWybWFDqfxuAkvJqrRxTKxAx55eWilRoY7aOF2JvK_yFNMm1CXAkU',
   'https://play-lh.googleusercontent.com/6zEEW5lScq4uIw-7B4w19dDVglcTBRHRG0pUdRHjLpULuUw9hKmLnu8mDonkmlYqTA'],
  'title': 'Pokémon Masters EX',
  'score': 4.3176017,
  'genre': 'Role Playing',
  'price': 0,
  'free': True,
  'currency': 'USD',
  'video': 'https://www.youtube.com/embed/tPN87sf7hyU?ps=play&vq=large&rel=0&autohide=1&showinfo=0',
  'videoImage': 'https://i.ytimg.com/vi/tPN87sf7hyU/hqdefault.jpg',
  'description': 'DYNAMAX! \r\nThe ability to Dynamax comes to Pokémon Masters EX! Now your Pokémon can drastically multiply in size once per battle to unleash a powerful max move on your opponents!\r\n\r\nTRAINERS DON SPECIAL OUTFITS!\r\nEnjoy special and seasonal Trainer outfits—exclusive to Pokémon Masters EX!\r\n\r\nHATCH EGGS & TEAM UP!\r\nHatch Eggs to get new Pokémon! Add hatched Pokémon to your team, and battle your way to the top!\r\n\r\nBUILD THE ULTIMATE TEAM FOR 3-ON-3 BATTLE!\r\nAssemble Trainers and Pokémon to take on battles! Create a team all your own, and aim for victory!\r\n\r\nTRAINERS FROM THE PAST COME TOGETHER!\r\nChampions, Elite Four members, and Gym Leaders from the past have come together! Team up with Trainers and their Pokémon, and go on adventures!\r\n\r\nNEW STORIES WITH YOUR FAVORITE CHARACTERS\r\nIn Pokémon Masters EX, experience an original story that crosses generations—along with familiar Trainers!\r\n\r\n\r\n・We recommend a device with at least 2GB of RAM.\r\n・Android OS 7.0 or higher is recommended.\r\n・Android OS 5.0 or above\r\nNote: \r\n・We do not guarantee functionality on all devices listed above.\r\n・There may be cases where the app does not function properly due to your device’s capabilities, specifications, or particular conditions for using apps.\r\n・It may take time to become compatible with the latest OS.',
  'descriptionHTML': 'DYNAMAX! <br>The ability to Dynamax comes to Pokémon Masters EX! Now your Pokémon can drastically multiply in size once per battle to unleash a powerful max move on your opponents!<br><br>TRAINERS DON SPECIAL OUTFITS!<br>Enjoy special and seasonal Trainer outfits—exclusive to Pokémon Masters EX!<br><br>HATCH EGGS &amp; TEAM UP!<br>Hatch Eggs to get new Pokémon! Add hatched Pokémon to your team, and battle your way to the top!<br><br>BUILD THE ULTIMATE TEAM FOR 3-ON-3 BATTLE!<br>Assemble Trainers and Pokémon to take on battles! Create a team all your own, and aim for victory!<br><br>TRAINERS FROM THE PAST COME TOGETHER!<br>Champions, Elite Four members, and Gym Leaders from the past have come together! Team up with Trainers and their Pokémon, and go on adventures!<br><br>NEW STORIES WITH YOUR FAVORITE CHARACTERS<br>In Pokémon Masters EX, experience an original story that crosses generations—along with familiar Trainers!<br><br><br>・We recommend a device with at least 2GB of RAM.<br>・Android OS 7.0 or higher is recommended.<br>・Android OS 5.0 or above<br>Note: <br>・We do not guarantee functionality on all devices listed above.<br>・There may be cases where the app does not function properly due to your device’s capabilities, specifications, or particular conditions for using apps.<br>・It may take time to become compatible with the latest OS.',
  'developer': 'DeNA Co., Ltd.',
  'installs': '10,000,000+'}]
```

## Changes
Change logs are here : [CHANGELOG.md](CHANGELOG.md)
