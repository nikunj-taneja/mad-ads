# Safe Meta Ads uploader

This starter creates one link ad from an **image hash already present in Meta**. It is intentionally narrow: no media upload, video, carousel, catalog, targeting, campaign creation, or activation yet.

## Credential bootstrap

1. In Meta Business Settings, create or choose an app and a system user.
2. Give that system user access to the target ad account. For the checker, grant read access; for uploads, grant ad-management access. Meta's UI and permission names change, so verify against current official Meta documentation.
3. Generate a system-user access token for that app. Do not commit it.
4. Copy `.env.example` to `.env` and fill in:

```dotenv
META_ACCESS_TOKEN=replace_me
META_AD_ACCOUNT_ID=1234567890
```

The account ID may also start with `act_`; the client normalizes it. Validate access first:

```bash
python tools/meta-ads-auditor/audit.py
```

## Use

Obtain an existing image hash from Meta Ads Manager or the Graph API, then preview the exact payload:

```bash
python tools/meta-ads-uploader/upload.py \
  --name "Neutral test ad" --adset-id 123 --page-id 456 \
  --image-hash abc123 --url https://example.com/product \
  --primary-text "A clear product benefit." --headline "Learn more"
```

Dry-run is the default and makes no network request. A write needs both safety flags:

```bash
# Review the dry-run output first.
python tools/meta-ads-uploader/upload.py ... --execute --confirm-paused-upload
```

Every created ad is `PAUSED`; the tool has no activation option. Use a disposable paused ad set for initial validation. Review the result in Ads Manager before making any change there.

## Troubleshooting

- Missing variables: create `.env` at the repository root.
- OAuth or permission error: regenerate/inspect the token and confirm system-user access to the exact account.
- Invalid parameter: confirm the page, ad set, image hash, CTA, and destination belong to compatible business assets.
- API-version error: pass `--graph-version vNN.N` after checking Meta's current supported Marketing API version.
