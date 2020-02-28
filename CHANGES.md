# Google-Play-Scraper Changelog
## v0.0.1
> Implemented app detail feature
- App Detail

## v0.0.1.1
> Improved app detail feature
- Removed unnecessary fields.
    - scoreText : because 'score' is more accurate. ex) scoreText: '4.7', score: 4.73642
    - priceText : because 'price' is more meaningful. ex) priceText: '$3.49', price: 3.49
- Applied post processing to complex data to provide meaningful data.
- Added `recentChangesHTML` field : original data of html unescaped 'recentChanges' field.
- Added `summaryHTML` field : original data of html unescaped `summary` field.

## v0.0.1.2
> Increased stability - app detail feature
- By defining default values for each crawled element, crashes in the crawling process are significantly reduced.
- Therefore, no crash occurs even for a DOM that has no contents at all.
- It makes it possible to produce more realistic crawl results.
- Special Thanks to [DestroyLee](https://github.com/DestroyLee)

## v0.0.1.3
> Responded to data structure changes in google play
- The comment information, which occupied `ds:15`, moved to `ds:16`.
- The review information, which occupied `ds:7`, moved to `ds:6`.

## v0.0.1.4
> Responded to data structure changes in google play
- The comment information, which occupied `ds:16`, moved to `ds:17`.

## v0.0.1.5
> Added `containsAds`
- Added `containsAds` field : equals to `adSupported`, but defaults to `False`, not `None`.

## v0.0.1.6
> Removed `familyGenre`, `familyGenreId`
- Removed `familyGenre`, `familyGenreId` field : these fields are no longer valid from play store.

## v0.0.1.7
> Fixed `comments`
- Fixed `comments` data fetch bug of `app` feature.

## v0.0.1.8
> Updated Python 2 support
- Fixed errors when using library in python2.

## v0.0.2.0
> Added `reviews` feature
- `reviews` feature released with dirty codes.

## v0.0.2.1
> Added `filter_score_with` parameter to `reviews` feature
- New feature `reviews filtering with score` released. 

## v0.0.2.2
> `reivews` feature improvement
- New property `reviews` Added. 
- Fix bug of `reivews` feature : Bug that occurs when the total number of reviews is less than the `count` argument.
