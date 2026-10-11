# Deployment Checklist: Kopi Laras v1.0 (Fictional)

**Date and time:** 2026-10-14 10:00 WIB | **Release owner:** studio developer | **Client on call:** owner

- [x] Test plan exit criteria met (T-09 not run, accepted by client in writing)
- [x] Client approval for go-live recorded 2026-10-13
- [x] Environment variables set in hosting dashboard
- [x] Rollback method: redeploy previous build from hosting dashboard; domain still points to old link page until DNS switch
- [x] Rollback trigger: inquiry form fails in production
- [x] DNS TTL lowered on 2026-10-13; SSL issued; old link page redirected
- [x] Smoke tests: home, origins, wholesale form, language switch
- [x] Monitored 60 minutes; no form errors
- [x] Client notified with release notes
- Rollback used: No
