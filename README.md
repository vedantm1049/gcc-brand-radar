# GCC Brand Radar

A ranked watchlist of homegrown GCC beauty, personal care and wellness brands, screened from public data. Single static page (`index.html`), deployed on Netlify from this repo.

## Weekly refresh
1. Run Apify `apify/instagram-profile-scraper` with `usernames` = contents of `handles.json`.
2. Save the results (fields `username`, `followersCount`, `postsCount`) as `scraped.json`.
3. `python3 refresh.py scraped.json YYYY-MM-DD` appends a snapshot to `history.json` and rebuilds `index.html`.
4. Commit and push. Netlify redeploys automatically.

Do not edit `index.html` by hand. Edit `template2.html` or the data files, then run `python3 build2.py`.
