# Authentication Logic Abuse Lab

## Overview
This lab demonstrates an authentication logic vulnerability involving OTP brute-force attacks,
followed by proper defensive hardening and validation.

The goal is to simulate real-world red team methodology:
identify → exploit → mitigate → re-test.

## Attack Scenario
- Application issues a 6-digit OTP after login
- OTP verification endpoint lacked rate limiting
- Attacker could brute-force OTPs via automation

## Exploitation
A Python script was used to automate OTP attempts against the verification endpoint.
Without protection, the OTP could be enumerated successfully.

## Mitigation
The following defenses were implemented:
- OTP bound to user identity
- Single-use OTP enforcement
- Rate limiting on verification endpoint

## Validation
After mitigation, the original brute-force attack was re-run.
The attack was blocked via HTTP 429 responses before enumeration completed.

## Skills Demonstrated
- Authentication logic testing
- Python attack automation
- Defensive validation
- Red team methodology
## Tech Stack
- Python (Flask)
- REST API authentication flows
- Rate limiting and abuse prevention
- Linux (Kali)
- curl for API interaction

