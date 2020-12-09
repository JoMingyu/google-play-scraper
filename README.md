# Google-Play-Scraper

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)
[![PyPI](https://img.shields.io/pypi/v/google-play-scraper.svg)](https://pypi.org/project/google-play-scraper)
[![downloads](https://img.shields.io/pypi/dm/google-play-scraper.svg)](https://pypistats.org/packages/google-play-scraper)
[![versions](https://img.shields.io/pypi/pyversions/google-play-scraper.svg)](https://github.com/JoMingyu/google-play-scraper)

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
    "appId": "com.nianticlabs.pokemongo",
    "url": "https://play.google.com/store/apps/details?id=com.nianticlabs.pokemongo&hl=en&gl=us",
    "description": "NEW! It’s time to interact with your Pokémon like never before—Pokémon GO has recently introduced GO Snapshot! Taking AR photos is a snap with this easy-to-use update. You’re now able to take photos of any Pokémon you have in your collection. Document your adventures by taking photos of your favorite Pokémon to share with friends or as a memento of your epic journey. \r\n \r\nJoin Trainers across the globe who are discovering Pokémon as they explore the world around them. Pokémon GO is the global gaming sensation that has been downloaded over 850 million times and named \"Best Mobile Game\" by The Game Developers Choice Awards and \"Best App of the Year\" by TechCrunch.\r\n\r\nVenusaur, Charizard, Blastoise, Pikachu, and many other Pokémon have been discovered!\r\nPokémon are out there, and you need to find them. As you walk around a neighborhood, your smartphone will vibrate when there’s a Pokémon nearby. Take aim and throw a Poké Ball… You’ll have to stay alert, or it might get away!\r\n \r\nSearch far and wide for Pokémon and items\r\nCertain Pokémon appear near their native environment—look for Water-type Pokémon by lakes and oceans. Visit PokéStops and Gyms—found at interesting places like museums, art installations, historical markers, and monuments—to stock up on Poké Balls and helpful items.\r\n \r\nCatching, hatching, evolving, and more\r\nAs you level up, you’ll be able to catch more-powerful Pokémon to complete your Pokédex. You can add to your collection by hatching Pokémon Eggs based on the distances you walk. Help your Pokémon evolve by catching many of the same kind. Choose a Buddy Pokémon to walk with and earn Candy that will help you make your Pokémon stronger.\r\n \r\nCompete in epic Gym battles\r\nYou’ll join one of three teams and battle for the ownership of Gyms with your Pokémon at your side. As your Charmander evolves to Charmeleon and then Charizard, you can battle together to defeat a Gym and assign your Pokémon to defend it against all comers. \r\n\r\nTeam up to defeat powerful Raid Bosses\r\nA Raid Battle is a cooperative gameplay experience that encourages you to work with up to 20 other Trainers to defeat an extremely powerful Pokémon known as the Raid Boss. If you succeed in defeating it in battle, you’ll have the chance to catch an extra powerful Pokémon of your own!\r\n \r\nIt’s time to get moving—your real-life adventures await!\r\n\r\nNotes: \r\n\r\n- This app is free-to-play and offers in-game purchases. It is optimized for smartphones, not tablets.\r\n- Compatible with Android devices that have 2GB RAM or more and have Android Version 4.4–7.0+ installed.\r\n- Compatibility is not guaranteed for devices without GPS capabilities or devices that are connected only to Wi-Fi networks.\r\n- Compatibility with tablet devices is not guaranteed.\r\n- Application may not run on certain devices even if they have compatible OS versions installed.\r\n- It is recommended to play while connected to a network in order to obtain accurate location information.\r\n- Compatibility information may be changed at any time.\r\n- Please visit www.PokemonGO.com for additional compatibility information. \r\n- Information current as of February 18, 2019",
    "descriptionHTML": "NEW! It’s time to interact with your Pokémon like never before—Pokémon GO has recently introduced GO Snapshot! Taking AR photos is a snap with this easy-to-use update. You’re now able to take photos of any Pokémon you have in your collection. Document your adventures by taking photos of your favorite Pokémon to share with friends or as a memento of your epic journey. <br> <br>Join Trainers across the globe who are discovering Pokémon as they explore the world around them. Pokémon GO is the global gaming sensation that has been downloaded over 850 million times and named &quot;Best Mobile Game&quot; by The Game Developers Choice Awards and &quot;Best App of the Year&quot; by TechCrunch.<br><br>Venusaur, Charizard, Blastoise, Pikachu, and many other Pokémon have been discovered!<br>Pokémon are out there, and you need to find them. As you walk around a neighborhood, your smartphone will vibrate when there’s a Pokémon nearby. Take aim and throw a Poké Ball… You’ll have to stay alert, or it might get away!<br> <br>Search far and wide for Pokémon and items<br>Certain Pokémon appear near their native environment—look for Water-type Pokémon by lakes and oceans. Visit PokéStops and Gyms—found at interesting places like museums, art installations, historical markers, and monuments—to stock up on Poké Balls and helpful items.<br> <br>Catching, hatching, evolving, and more<br>As you level up, you’ll be able to catch more-powerful Pokémon to complete your Pokédex. You can add to your collection by hatching Pokémon Eggs based on the distances you walk. Help your Pokémon evolve by catching many of the same kind. Choose a Buddy Pokémon to walk with and earn Candy that will help you make your Pokémon stronger.<br> <br>Compete in epic Gym battles<br>You’ll join one of three teams and battle for the ownership of Gyms with your Pokémon at your side. As your Charmander evolves to Charmeleon and then Charizard, you can battle together to defeat a Gym and assign your Pokémon to defend it against all comers. <br><br>Team up to defeat powerful Raid Bosses<br>A Raid Battle is a cooperative gameplay experience that encourages you to work with up to 20 other Trainers to defeat an extremely powerful Pokémon known as the Raid Boss. If you succeed in defeating it in battle, you’ll have the chance to catch an extra powerful Pokémon of your own!<br> <br>It’s time to get moving—your real-life adventures await!<br><br>Notes: <br><br>- This app is free-to-play and offers in-game purchases. It is optimized for smartphones, not tablets.<br>- Compatible with Android devices that have 2GB RAM or more and have Android Version 4.4–7.0+ installed.<br>- Compatibility is not guaranteed for devices without GPS capabilities or devices that are connected only to Wi-Fi networks.<br>- Compatibility with tablet devices is not guaranteed.<br>- Application may not run on certain devices even if they have compatible OS versions installed.<br>- It is recommended to play while connected to a network in order to obtain accurate location information.<br>- Compatibility information may be changed at any time.<br>- Please visit www.PokemonGO.com for additional compatibility information. <br>- Information current as of February 18, 2019",
    "summary": "Step outside and catch Pokémon in the real world! Collect & battle with others.",
    "summaryHTML": "Step outside and catch Pokémon in the real world! Collect &amp; battle with others.",
    "installs": "100,000,000+",
    "minInstalls": 100000000,
    "score": 4.126332,
    "ratings": 12001843,
    "reviews": 4772986,
    "originalPrice": None,
    "sale": False,
    "saleText": None,
    "saleTime": None,
    "histogram": [
        1535599,
        406833,
        842775,
        1437189,
        7779447
    ],
    "price": 0,
    "free": True,
    "currency": "USD",
    "offersIAP": True,
    "editorsChoice": False,
    "size": "94M",
    "androidVersion": "5.0",
    "androidVersionText": "5.0 and up",
    "developer": "Niantic, Inc.",
    "developerId": "Niantic,+Inc.",
    "developerEmail": "pokemon-go-support@nianticlabs.com",
    "developerWebsite": "http://pokemongo.nianticlabs.com",
    "developerAddress": "One Ferry Building, Suite 200\nSan Francisco, CA 94111",
    "privacyPolicy": "https://nianticlabs.com/privacy/pokemongo/en",
    "developerInternalID": "7632469272431224129",
    "genre": "Adventure",
    "genreId": "GAME_ADVENTURE",
    "familyGenre": None,
    "familyGenreId": None,
    "icon": "https://lh3.googleusercontent.com/wPfLmWBJwsPdBhsFXc8X4QZOOvePWjoOBLFXXCwyegjRwYOuabmG5cynthlW0HDgy9s",
    "headerImage": "https://lh3.googleusercontent.com/KgDQ-Kjb2B7_jDP-8KmQDNhAmP2lqAV_w3zArOCBL7YZnQ02Qqp4VTlgdocO-4MFk4s",
    "screenshots": [
        "https://lh3.googleusercontent.com/K3IEjo1_LQWSpiD99xAbcfJNXcTG7W7wf3zUkYzQVj5k7OqSkdsoO-SmcZmxvF4CWIo",
        "https://lh3.googleusercontent.com/WeqKYk-_b4GyvkKAhp_AOwoQeP0X3VdiznoVaNE5Qc8Q1lh8uamv-iYWc50_FYsUDg",
        "https://lh3.googleusercontent.com/WCohW4co4ql2e6QwT1KhMos-6z0yH5z7kQMr-GLdC9s1bzMI8W5Yj8hU9BWDKLCguHw",
        "https://lh3.googleusercontent.com/1iRwgEuQSoT4AsSiPhFou-5eCwyLSzfnJ6A5YdW--N_EjDMTTW61bCgc9RaR9ZfcHqQ",
        "https://lh3.googleusercontent.com/hUU4GGw6zTmG_5zyDvdpMeK62tqxUPbrACwsl21hJPNgzOW-WAkvNRkRMv2Hv8pAXw",
        "https://lh3.googleusercontent.com/d9hOdTf9EMqQFb6NxX7vP8Hu41jul7uF_24uXgMJjNE2Vbs4uliwfUM_LDjwj7mSec0",
        "https://lh3.googleusercontent.com/DB42-AV-hedxobwSeruqvBc6knupZjjBqsdPxhT9kgpsCTHtW6xpaKO1jIKB3a8PUg",
        "https://lh3.googleusercontent.com/tmfbe4RhZOFGdQfXCvdQApmJRmjTBCtmabJ3nRE0zuc7FxYo97n4IxAhBYx2s13k2ZA",
        "https://lh3.googleusercontent.com/-8F-a-NXGkOMoej-FIQXV5LPePWFbyj2Ql7z_xCM4MkszVfKDXYmhYmNOfJNQY0Z_w",
        "https://lh3.googleusercontent.com/RVItTUG-T4r4fU3oJTae9-40VgkCCsbaBtjSDu50VzIxN4rGEkPK08FEEiLTcvBaE8yx",
        "https://lh3.googleusercontent.com/mbxUU-1nEpv5HnF5OKzlFAePPQBLZtpyUEU_XqyuFmwleBit6Gsn_YEyXiPUenEwSxa6",
        "https://lh3.googleusercontent.com/09qBoXVvzGazKqyJ1SPoAcbMDaYXEQLJwHwnFD__BS1-FJ8jS0pzdXN3-pEoEYTfgQ",
        "https://lh3.googleusercontent.com/l1FdglZMSppao9cjUw8P5QJdF-Sb6UfAHIxGN4iJk6Mtzz7RKME5boHiEN5b3BIX7A",
        "https://lh3.googleusercontent.com/bhpXUBwqKhyDSoPIdm-CLhMxsM3FWgjjnA4DzDheUea-8UvukHRZxLzbJCr7tlbIhA"
    ],
    "video": None,
    "videoImage": None,
    "contentRating": "Everyone",
    "contentRatingDescription": "Mild Fantasy Violence",
    "adSupported": False,
    "released": "Jul 6, 2016",
    "updated": 1563814423,
    "version": "0.149.0",
    "recentChanges": "Trainers—we need your help! Team GO Rocket is invading the world of Pokémon GO!\r\n\r\nHere’s what can you expect in this release.\r\n\r\n- New Challenges: Take on Team GO Rocket Grunts in battle!\r\n- Shadow Pokémon: Catch the mysterious Shadow Pokémon Team GO Rocket Grunts leave behind! Is there a way to help these Pokémon?\r\n- New Appraisal Tool: You can now learn even more about your Pokémon when appraising them.\r\n- Battle Minigames: Charged Attack gameplay includes new minigames.",
    "recentChangesHTML": "Trainers—we need your help! Team GO Rocket is invading the world of Pokémon GO!<br><br>Here’s what can you expect in this release.<br><br>- New Challenges: Take on Team GO Rocket Grunts in battle!<br>- Shadow Pokémon: Catch the mysterious Shadow Pokémon Team GO Rocket Grunts leave behind! Is there a way to help these Pokémon?<br>- New Appraisal Tool: You can now learn even more about your Pokémon when appraising them.<br>- Battle Minigames: Charged Attack gameplay includes new minigames.",
    "comments": [
        "*revised. This game is horrible after this last update. I do not like the appraisal filter. There are more bugs then ever. '' *This game is getting worse and worse. I am unable to update my app. There is never a new update for me. Everyone around me has had 2- 3 updates but I have not. I've gone to their customer service for help, nothing. Their customer service is awful. Automated useless replies. Now my game is freezing. I'm dropping in raids, losing raid bosses.",
        "I love the game but I'm having issues with the friends list. Error keeps saying, \"Failed to get friends list. Try again later.\" I've already uninstalled and installed the game four times. The error keeps popping up. I also can't walk my eggs. They are all in incubators and I've walked for an hour straight and it still reads 0/2.0, 0/5.0, and 0/10.0... very frustrating!",
        "This game is an amazing game except for one mechanic, the 50 pokecoin per day limit. This limits you from receiving more than 50 pokecoins (The in-game secondary currency that costs real money) per day from gyms. This is a cheap tactic to manipulate you to purchase more pokecoins, I get that they have developers and animators and artists. I understand they need to pay people and make a profit on top of that, but I strongly believe the previous limit of 100 was much more reasonable.",
        "For the past week, it takes about 5 minutes for the game to load up & open. Half the time it doesn't load at all for me then when I do finally get on, it freezes up constantly or closes the app all together...often when I'm in the middle of trying to catch something. There was one day where I couldn't get the game to open at all & lost my streaks! I've tried restarting my phone, uninstalling then reinstalling...nothing has helped the issues. Not too happy with this game right now 👎",
        "The latest update has made it near impossible to catch the pokemon with excellent throws. I can barely make out the little circle anymore. It's like the game was catered for large screen devices like tablets. I use a S7 edge and the catch screen is a nightmare. please revert! The game is still as glitchy as ever and nothing positive has come out of it. I can live without the quick catch for android, but the extreme downsize to the catch sequence leaves a lot to be desired. Wish i can go on",
        "I've been playing pokemon go for about a year now, and I gotta say, with the new update that just happened, I can not stand the new appraisal system. it just says when and where the pokemon was caught and gives you a little picture with a 3 star rating on its attack, defense, and hp. it basically rendered the add on PokeGenie useless. and even if you dont use apps like pokegenie and Calcy IV, it still doesn't tell if the pokemon will be good in battle or not",
        "Great game! My only issue with pokemon go is the step count. I have attempted several times to fix this through settings and such. I have a galaxy s10 so performance isn't an issue. I've been trying to hatch a 2 meter egg for two weeks now. not sure what's up but I'd really appreciate it if my issue was fixed.",
        "love the game, but I have 1 point of criticism if you want to even suggest an edit, you need to find someone who played Scanner [REDACTED] before new signups were redirected to Ingress Prime. I asked around for weeks on ingress and nobody responded, because noone plays it here.. There are stops incorrectly placed in my area and no way to even suggest a change. give players over level 30 the ability to suggest edits, and level 40 the ability to suggest new landmarks/curiousities as stops. PLEASE!",
        "I don't know what happen with this game. I can't view my friends list even though I don't have any friends yet and I try to add friends in my friends list. I'm not even can view my step progress. I put on pokemon as my buddy still not counting any steps. Can you tell me what should I do.?",
        "adventuer sync keeps getting turned off. any time there is an update or the game forces me to relog in. i do a lot of walking to find out half the time it doesnt count becaused they keep changing my settings. it gets aggrevating that every time i go to play have to check the settings to make sure they are how i left them. itis extremly annoying.",
        "While I love the game, there are some things I wish was better. Like having a power meter to help you gage how far you will throw the pokeballs, or a way to grow and farm the berries. The bag limits are particularly frustrating for me, as I can go from \"You can't use this pokestop, your bag is full!\" to \"I can\"t catch any more pokemon I ran out of balls!\" In a matter of five minuets or less.",
        "As someone who grew up with Pokemon, I really love this game, it'sso addictingand fun! and I love that I can play with others. Every update is more and more exciting! but I can't give it 5 stars, because 99% of my map vanished. I still have the pokestops and gyms which is a major relief lol, but except for a very small portion near my original log in point everything is just green.I've tried everything I can think of to fix it and I've never downloaded cheats, so I'm at a loss.",
        "I absolutely love this game, but I think it can be better. Please make it so you can withdraw your pokemon from gyms manually, there are rarely any people that come to the gyms in my area and my pokemon are basically imprisoned in the gyms. I just want to be able to take out my pokemon from the gym, not even for the coins, just so I can switch pokemon or power up that one, is that to much to ask? Other than that, I really enjoy the game and I'll keep playing it. But please, free my pokemon.",
        "After the recent update, the game is forcing me to play in AR mode. Even if I have it turned off. it will just show the pokemon in a white area. i tried reinstalling the app, it persists. AR is quite annoying and at this point its unplayable for me",
        "Ok well Pokemon Go has Aided in my physical recovery from spinal surgery, my kids got me into the game,as a means to getting me out of the house and making me walk as my therapy,and it worked. I just made level 33, I'm having fun,and getting Exercise. I've done a couple of community days, and it's really neat to go out and see people of all ages out there playing and being together and having Fun,so keep it up there's a lot of Pokemon for me to still catch, and I look forward to doing it. Go 💛!",
        "Love the game with all its little unexplained mysteries. It will make you spend, however. There's a suggestion I'd like to make. Could you make it possible to send friend requests through name instead of through trainer code? I've been playing this game for a week now, and although I've seen plenty of action and teamwork at Gyms and raids, I've got no friends yet. If friend requests are easier to send, you can add a block feature too, and I'm sure the game will be much more fun. Cheers!",
        "I love this game, and yet I can't enjoy it right now. I am getting an error message 'friends list is unavailable' and 'field metrics are currently unavailable'. This means I cannot track my steps, hatch eggs, add friends and many other things. My girlfriend is not having issues and I am sad that I can't join in with her and have as much fun. This only started yesterday, else would have 5 stars as I really enjoy this game.",
        "I love the game, but adventure sync no longer works after the last upgrade. All other game play is ok. I log a lot of km's a week and used to hatch eggs all the time and get km rewards. Now taking weeks of time with game on just to earn my distance. Otherwise would be a 5 star game.",
        "As someone who never really got into Pokemon, this game is actually quit amazing. Got into it when it first came out as a way to get out and walk while staying entertained. Three years later the game has underwent many changes that have kept it fun and engaging. Really brings people tohther. If youre not already pary of the online sensation..download it.. Youll have a blast-oise!",
        "This app is really cool! But if you are looking for problems then I got a few. First, is that you CAN NOT put LEGENDARY Pokemon in a gym. Second, when your Pokemon comes back from a gym and you get mony the max limet for each day is 50, which is not even enough money to buy something in the PokeStore! Third, in the clothes store the money to buy things is too expensive it costs 500 money and yes some items are FREE but seriously. Make sure to read the other comments to find more! Please fix.",
        "This is a very nice game with nice graphics and system, however to me the only concern is about spoofing. I understand the point of blocking spoofing but it is sometimes unachievable for some people like me to walk all over the place to catch pokemon. I really hope that Niantic itself could support with joystick feature in a limited area for us to walk around. For example, we are able to use joystick feature to walk 3~5km around our location. That will be great!!!",
        "What is going on with the GPS? It keeps asking me if driving when I'm walking. I'm a fast walker but not that fast. Also it seems to have a lot of trouble pinpointing my location. It'll have me in one spot then zoom me to another and then back again. It's also super hard to throw the balls. I'll hit the Pokemon with the ball but somehow still seem to miss. And what is up with not being able to catch a 300 cp Pokemon with a ultra ball? Really? Fix these issues and I'll give it 5 stars.",
        "I like the game, but for what ever reason the game decided to not load all the way so i signed out and now i can no longer sign back in, and the game won't let me make a new account either. I have forced stop the game, cleared catch, and I even uninstalled and reinstalled the game nothing has fixed my problem. So I literally can't play the game anymore.",
        "A lot better than before. not buggy like it used to be and more things to do in the game. Principal weak point of that game is there is never an event for parents after 7:30. Me or my wife love to take a walk after putting the kid to bed. When we do it, nothing happens in the game. Events and raids finish early. I think young parents would like an event once a month or 2. Forget raid hours early in the evening for us. It is not an option.",
        "Disappointed. The concept is fun, and it makes finding adventures with the family easy. The issue comes with the battle style and the pokemon power levels. Battles and raids are 15 sec bursts of tapping as fast as you can, I find it kind of lame. That coupled with power levels that range from 1 to the thousands, I think even tens of thousands, really separates people who want to have fun occasionally from people who make the game their life.",
        "Come on Niantic, I can't load the friends list, can't battle anyone, walking distance isnt being measured whatsoever, apparently i did 0km all of last week. Please sort these problems out, i love this game but ima have to leave it until these game-breaking bugs get fixed. If it helps, these issues are happening on my Huawei Mate 10 Pro",
        "New update doesnt track distance traveled. I have lost out on 20+ km worth of my walking distance because the game simple does not work. I went about a year without playing because many features did not work. Finally returned to the game in May 2019 and the first update after my return and it seems that the same problems still persist, a lot of features/ideas yet none of them work properly.",
        "I found the game of my dreams. As well as the people thatI dreamed of playing with. Its much more enjoyable with people who plays with you. But I do hope that the pokestop nomination update should be released quickly because there are a lot of places where there are only 1 gym and 1 pokestops, especially in the areas that are far from cities. I hope that this review reaches in the hearts of the game devs. Forever in support and in love with pokemons.",
        "Its really fun. One thing that kind of bothers me is that you can't put legendary Pokemon in gyms that you take over. I know they are legendary but it i have noticed most of the time is that legendary pokemon, once caught, that they about as strong as any other Pokemon. it would be hilarious and awesome to see a gym full of legendary pokemon.",
        "I love playing the game. Graphics are amazing, gameplay is amazing. I know it's being worked on, but I can't wait to be able to request new pokestops since I visit places that don't have any for miles. Also, the places with no stops wouldn't produce pokemon either. Being able to trade with long distance friends would be beneficial also for people with social anxiety who can't just walk up to someone and start talking to them. The way this game has grown since it started is unbelievably amazing!",
        "It is such a GREAT game, but since the new update, pokemon in the wild are pretty much are all silhouettes, when you tap on them they are sometimes black squares, when you go into the pokedex half of them are also black squares and when you tap into your profile or into a pokemon that you have caught, the top part of the screen is just black. All that and it also crashed, ALOT!!! It is just unbearable.",
        "I installed the game at first to get closer to my kids and exercise. I grew to love it and play it everyday. easy for all ages! the only thing I wish would be more pokestops and gyms but it's the only game that actually forces you to get up and move AND to make new friends. since starting this game I have made new friends from all over the world. we belong to different groups and we all meet up to raid. as an adult it is hard to make new friends, pokemon Go has given us a new life. come and play!",
        "The screen stays on when eggs are ready to hatch, even when the phone's been upside down the entire time. I haven't had any battery issues with this new phone but I know some people aren't that fortunate. Edit: After playing for another day, I can see why people say the catch circle is too small. To those complaining about the new appraisal system, it's basically the same thing they just did the IV calculation for you. Plus you can swipe to compare pokemon side by side.",
        "Just rejoined after deleting it two years ago and there have been a lot of upgrades! More Poke Stops and gyms, which is nice. However, the two-star rating is for the distance tracker and Adventure Sync. If the main point of this game is motivate people moving, then the trackers shouldn't be as off as they are. We walked at least a mile last night with the Adventure Sync on and full battery use, yet nothing was tracked in the game. Even checked this morning to see no progress added.",
        "One of the best games you can get for free. The game has online currency, but is not pay to win as it is very easy for any free to play person to get currency. The game releases new updates, and pokémon so you are never board. Pokémon Go is fun to play and keeps you active at the same time. You can progress faster in the game by hatching eggs. whitch you aquire for free, and hatch by keeping active. You can play with friends and family to boost your progress all free! Pokémon Go deserves 5 stars",
        "Not enough pokestops in rural areas!!! Not enough poke balls, or pokestops to get any! I live in a city with a mall and everything and still see nothing for miles! Only one poke stop and one gym at the churches, that's it! And I'm sitting in a neighborhood with a school and big park! Wizards unite has games at the park and objects popping up all over, so I've made my switch!",
        "Good game but poke stops should be a little more plentiful with items and we should be able to do more things(battle, trade) with our friends even if they are not in our vicinity. Also statistically we should know more about our Pokemon instead of only relying on the CP and the uplifting words of an appraiser. Also there should be more clear cut meaning of the size of the Pokemon (XL and XS) and what it does to the Pokemon.",
        "I've been playing this game for so long, I can't believe I haven't rated it yet. This is the very same game that blew up in 2016, but it's grown and refined a lot since then. The basic idea is to capture Pokémon while you're out, but you can also battle them in gyms and with other players. They also hold special events regularly for capturing special Pokémon. The game is best played with friends, but it's a fine \"fitness\" app, too. I give it a \"good enough to play for 3+ years\" out of 10.",
        "Kinda lame tbh. I downloaded it for a Pokemon experience, which I do get, but time a degree. MAKE SURE you find out which teams typically operate in your area (which is extremely hard unless you know someone who uses the app), because you can end up on a bad team and never be able to experience the full fun of the game.",
        "great game, but I'm really sad because when the game first came out, I had a dragonite and other good pokemon, and when I updated the game, they were ALL deleted. I was super sad to find all my good pokemon missing. plz fix that so it doesn't happen to others :(. it's still a great game though and I would reccomend getting it."
    ]
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
    sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
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

## Changes
Change logs are here : [CHANGELOG.md](CHANGELOG.md)
