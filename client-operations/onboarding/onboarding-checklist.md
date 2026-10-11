# Client Onboarding Checklist

**Purpose:** Start every engagement with the same setup, so nothing blocks discovery.
**Owner:** Project lead. **Timing:** Within two working days of a signed proposal or paid deposit.

## Checklist

- [ ] Client contact list: decision-maker, day-to-day contact, approvers, technical contact.
- [ ] Communication channel agreed (email, WhatsApp Business, Slack) and response time expectations.
- [ ] Working hours and timezone of both sides recorded.
- [ ] NDA signed if requested.
- [ ] Discovery questionnaire sent (EN or ID).
- [ ] Interview scheduled.
- [ ] Shared folder created (client drive). No client files in this public process repo.
- [ ] Access requests sent: domain registrar, hosting, analytics, social accounts, brand files. Use the client's password manager sharing or invite users. Never ask for passwords by chat.
- [ ] Project workspace created with `scripts/new_project.py`.
- [ ] Invoice for deposit issued per proposal terms.

## Welcome message: English

```
Hi {{CLIENT_FIRST_NAME}},

Thank you for choosing {{STUDIO_NAME}}. Here is how we start:

1. Discovery questionnaire: {{LINK}}. Please complete it by {{DATE}}.
2. Discovery interview: {{DATE}}, {{TIME}} {{TIMEZONE}}, {{DURATION}} minutes, {{MEETING_LINK}}.
3. Access: we will send invitation requests for {{SYSTEMS}}. Please do not send passwords by email or chat.

Your day-to-day contact is {{PM_NAME}}. We reply within {{RESPONSE_TIME}} on working days ({{WORKING_HOURS}} {{TIMEZONE}}).

Best regards,
{{SENDER}}
```

## Pesan sambutan: Bahasa Indonesia

```
Halo {{NAMA_KLIEN}},

Terima kasih telah memilih {{NAMA_STUDIO}}. Berikut langkah awal kita:

1. Kuesioner discovery: {{TAUTAN}}. Mohon diisi paling lambat {{TANGGAL}}.
2. Sesi wawancara discovery: {{TANGGAL}}, pukul {{JAM}} WIB, durasi {{DURASI}} menit, {{TAUTAN_MEETING}}.
3. Akses: kami akan mengirim permintaan undangan untuk {{SISTEM}}. Mohon tidak mengirim kata sandi melalui email atau chat.

Kontak harian Anda adalah {{NAMA_PM}}. Kami membalas dalam {{WAKTU_RESPONS}} pada hari kerja ({{JAM_KERJA}} WIB).

Salam,
{{PENGIRIM}}
```
