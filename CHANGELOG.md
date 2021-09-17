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
> `reviews` feature improvement
- New property `replyContent`, `repliedAt` added. 
- Fix bug of `reivews` feature : Bug that occurs when the total number of reviews is less than the `count` argument.

## v0.0.2.3
> Added `continuation_token` as return value, argument of `reviews` feature
- New return value, argument `contination_token` added to `reviews` function. It will be helped to lazy pagination patterns.

## v0.0.2.4
> Added argument data to `continuation_token` of `reviews` feature
- Objectify `continuation_token` for saving arguments

## v.0.0.2.5
> `reviews` feature improvement 
- New property `reviewId` added to `reviews` function.

## v.0.0.2.6
> `detail` feature improvement
- New property `sale`, `saleText`, `saleTime`, `originalPrice` added to return of `detail` function

## v.0.0.2.7
> HotFix for data structure update of Google Play

## v.0.0.3.0
> Implement `reviews_all` feature

## v.0.0.3.1
> `reviews`, `reviews_all` feature improvement
- Resolve cases where errors occur when there are no reviews in the app.

## v.0.0.3.2
> `app` feature improvement
- Some calibration logic added to `app` function
- Added `inAppProductPrice` element to `app` function

## v.0.1
> Remove Python 2 support
- Python 2 is no longer supported since this version.

## v.0.1.1
> Sync Google Play data structure

## v.0.1.2
> Add `editorsChoice` property to `app` feature
- Added `editorsChoice` property to `app` feature.

## v.0.2
> Python 3.3, 3.4, 3.5 support stopped
- after this version, Python 3.6+ supports only.

## v.1.0.0
> Add `permissons` feature, some features improvement
- Added `permissions` feature for fetch permission info of specified app.
- `reviews` : the information of the `continuation_token` takes precedence over the specified arguments.
- Type hinting based on PEP 484 is supported.

## v.1.0.1
> features improvement - `app`, `reviews` feature
- Optimize `reviews` function : returns false value when `continuation_token.token` is `None`
- Fix `app` function : `comments` always `[]`

## v.1.0.2
> Patch element specs for a deal with play store data structure changes. features improvement - `app` feature
- Fix `app` function : all data always `None`
- Added `similarApps`, `moreByDeveloper` property to `app` feature
