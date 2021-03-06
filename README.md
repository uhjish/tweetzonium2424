Some notes on the twitter search API

## Search Operator Examples

|Operator                    |Finds tweets
|---|---
|watching now                |containing both “watching” and “now”. This is the default operator.
|“happy hour”                |containing the exact phrase “happy hour”.
|love OR hate                |containing either “love” or “hate” (or both).
|beer -root                  |containing “beer” but not “root”.
|#haiku                      |containing the hashtag “haiku”.
|from:alexiskold             |sent from person “alexiskold”.
|to:techcrunch               |sent to person “techcrunch”.
|@mashable                   |referencing person “mashable”.
|superhero since:2015-07-19  |containing “superhero” and sent since date “2015-07-19” (year-month-day).
|ftw until:2015-07-19        |containing “ftw” and sent before the date “2015-07-19”.
|movie -scary :)             |containing “movie”, but not “scary”, and with a positive attitude.
|flight :(                   |containing “flight” and with a negative attitude.
|traffic ?                   |containing “traffic” and asking a question.
|hilarious filter:links      |containing “hilarious” and linking to URL.
|news source:twitterfeed     |containing “news” and entered via TwitterFeed


##Example Tweet in Statuses returned

```
    {
      "coordinates": null,
      "favorited": false,
      "truncated": false,
      "created_at": "Mon Sep 24 03:35:21 +0000 2012",
      "id_str": "250075927172759552",
      "entities": {
          "urls": [
   
          ],
          "hashtags": [
            {
              "text": "freebandnames",
              "indices": [
                20,
                34
              ]
            }
          ],
          "user_mentions": [
   
          ]
      },
      "in_reply_to_user_id_str": null,
      "contributors": null,
      "text": "Aggressive Ponytail #freebandnames",
      "metadata": {
        "iso_language_code": "en",
        "result_type": "recent"
      },
      "retweet_count": 0,
      "in_reply_to_status_id_str": null,
      "id": 250075927172759552,
      "geo": null,
      "retweeted": false,
      "in_reply_to_user_id": null,
      "place": null,
      "in_reply_to_screen_name": null,
      "source": "<a>Twitter for Mac</a>",
      "in_reply_to_status_id": null
      "user": {
          "profile_sidebar_fill_color": "DDEEF6",
          "profile_sidebar_border_color": "C0DEED",
          "profile_background_tile": false,
          "name": "Sean Cummings",
          "profile_image_url": "http://a0.twimg.com/profile_images/2359746665/1v6zfgqo8g0d3mk7ii5s_normal.jpeg",
          "created_at": "Mon Apr 26 06:01:55 +0000 2010",
          "location": "LA, CA",
          "follow_request_sent": null,
          "profile_link_color": "0084B4",
          "is_translator": false,
          "id_str": "137238150",
          "entities": {
            "url": {
              "urls": [
                {
                  "expanded_url": null,
                  "url": "",
                  "indices": [
                    0,
                    0
                  ]
                }
              ]
            },
            "description": {
              "urls": [
   
              ]
            }
          },
          "default_profile": true,
          "contributors_enabled": false,
          "favourites_count": 0,
          "url": null,
          "profile_image_url_https": "https://si0.twimg.com/profile_images/2359746665/1v6zfgqo8g0d3mk7ii5s_normal.jpeg",
          "utc_offset": -28800,
          "id": 137238150,
          "profile_use_background_image": true,
          "listed_count": 2,
          "profile_text_color": "333333",
          "lang": "en",
          "followers_count": 70,
          "protected": false,
          "notifications": null,
          "profile_background_image_url_https": "https://si0.twimg.com/images/themes/theme1/bg.png",
          "profile_background_color": "C0DEED",
          "verified": false,
          "geo_enabled": true,
          "time_zone": "Pacific Time (US & Canada)",
          "description": "Born 330 Live 310",
          "default_profile_image": false,
          "profile_background_image_url": "http://a0.twimg.com/images/themes/theme1/bg.png",
          "statuses_count": 579,
          "friends_count": 110,
          "following": null,
          "show_all_inline_media": false,
          "screen_name": "sean_cummings"
      }
    }
```
