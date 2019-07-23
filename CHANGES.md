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
