# Data contracts

## Meta Ads CSV

The starter parser recognizes common labels for ad name, spend, impressions, clicks, purchases, and purchase conversion value. Meta export labels vary by currency, locale, selected columns, and report preset.

Ask the operator to export at ad level with:

- campaign, ad set, and ad names;
- delivery status;
- amount spent and impressions;
- link clicks or outbound clicks;
- purchases and purchase conversion value;
- reporting start and end dates;
- attribution setting when available.

Run `python tools/parse-meta-csv/parse.py data/<export>.csv`. If mappings are missing, patch the alias list or add a documented schema adapter. Never silently substitute a different metric.

## Customer research

Prefer anonymous source IDs. Keep raw transcripts and exports in `data/` or another access-controlled system. Only commit synthesized, non-identifying insights when the operator has confirmed that publication is appropriate.
