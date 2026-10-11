# Deployment Checklist: {{PROJECT_NAME}} {{RELEASE}}

**How to use:** Complete before and during every production release. Guide: [deployment-rollback.md](../engineering/deployment/deployment-rollback.md).

**Date and time:** {{YYYY-MM-DD HH:MM TIMEZONE}} | **Release owner:** {{NAME}} | **Client contact on call:** {{NAME}}

## Before
- [ ] Test plan exit criteria met
- [ ] Client approval for go-live recorded
- [ ] Production environment variables set and checked (names listed in tech spec)
- [ ] Backup or snapshot taken at {{TIMESTAMP}}
- [ ] Rollback method written: {{METHOD}}
- [ ] Rollback triggers agreed: {{TRIGGERS}}
- [ ] DNS, SSL, redirects prepared
- [ ] Analytics and error tracking configured

## During
- [ ] Deploy started {{TIME}} / finished {{TIME}}
- [ ] Smoke tests: {{LIST}} passed

## After
- [ ] Monitoring checked for {{N}} minutes
- [ ] Search console sitemap submitted (if public site)
- [ ] Client notified with release notes
- [ ] Rollback used? Yes / No. If yes, reason:
