# Stand-in merchant logos for the walkthrough video

Data Enrichment and Settle In show the merchant logos that the Open Finance
enrichment API returns. Those images load from Mastercard's branding host
(`institution-branding-assets-cf.openbanking.mastercard.com`). When the machine
recording the video can't reach that host, `record.js` serves the same brand's
logo from this folder instead. When the host can be reached, the API's own
logo is always used.

`logos.json` maps the merchant id in each branding URL to a file here. A
merchant with no file (Whole Foods Market, for now) keeps the app's initials
badge.

| File | Source | Licence |
| --- | --- | --- |
| `amazon.svg`, `apple.svg`, `netflix.svg`, `uber.svg` | [super-tiny-icons](https://github.com/edent/SuperTinyIcons) 0.6.0, unchanged | MIT |
| `starbucks.svg`, `lyft.svg`, `target.svg` | [simple-icons](https://github.com/simple-icons/simple-icons) 16.35.0, set in the brand colour on a square tile | CC0-1.0 |

The logos are trademarks of their owners and appear here only to show what
enrichment returns.
