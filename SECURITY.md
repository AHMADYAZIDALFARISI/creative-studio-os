# Security Policy

## Scope

This repository holds process documents, templates, and small scripts. It must never hold client secrets, credentials, contracts with real signatures, or personal data.

## Reporting

Report a leaked secret or a vulnerability in the scripts through GitHub private vulnerability reporting: open the repository's **Security** tab and choose **Report a vulnerability**. Do not open a public issue for it.

If you find client data or personal data in this repository, report it the same way. We remove it and rewrite history if needed.

## If a secret was committed

1. Revoke or rotate the secret at the provider first. Removing it from Git does not make it safe.
2. Remove it from the working tree and commit the fix.
3. Rewrite history only after rotation, and only with the repository owner.
4. Record the incident and the rotation date in the private incident log.

## Client project security

Client security guidance lives in [engineering/authentication-security/security-baseline.md](engineering/authentication-security/security-baseline.md). Never describe a client system as secure without reviewing its actual implementation.
