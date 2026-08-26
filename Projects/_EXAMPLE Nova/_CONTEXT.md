# Nova — Context

*Read at the start of any Nova-related work.*

> **This is a filled-in example** so you can see the shape of a real one.
> Delete this whole folder once your own projects are set up.

---

## What It Is

Nova is a client I build and maintain a booking system for — a small chain of physiotherapy clinics. They had three receptionists managing appointments across paper diaries and a shared inbox. The system replaced that with one scheduling app their staff actually uses.

## My Role

Sole developer and the only technical contact. I handle the build, the hosting, and anything that breaks. I'm not responsible for their business decisions, but I get asked about them.

## Key People

| Name | Role |
| :--- | :--- |
| Priya | Nova's operations manager — my main contact, decides scope |
| Daniel | Clinic owner — signs off on anything involving money |
| Mei | Front desk lead — the person who actually uses the thing daily; best source of real feedback |

## Current Status

Live since March, running on a single VPS. Two clinics migrated, the third is still on paper because Daniel wants to see a full quarter of clean data first. Roughly 400 bookings a week going through it. No serious incidents since the May timezone bug.

Currently mid-way through adding SMS reminders — the integration works in staging, waiting on Priya to confirm the message wording before it goes live.

## Open Items

- [ ] Get final SMS copy approved by Priya, then ship reminders to production
- [ ] Migrate clinic 3 once Daniel gives the go-ahead
- [ ] Set up automated database backups — currently manual, which is a real risk

## What I Don't Know Yet

- Whether Daniel wants to expand to the fourth location this year — affects whether I refactor the multi-clinic handling now or later
- What their actual budget is for ongoing maintenance beyond the current retainer

---
*Last updated: 2026-08-26*
