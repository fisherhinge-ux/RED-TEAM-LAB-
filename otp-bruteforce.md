# OTP Brute Force & Replay

## Assumption
OTP verification endpoint enforces rate limiting and single-use constraints.

## Flaw
The OTP value is:
- Global
- Static
- Reusable
- Not bound to a user or session
- Not rate limited

## Observation
Automated requests allow enumeration of the full OTP space.
A valid OTP remains usable indefinitely.

## Impact
An attacker can bypass authentication controls and verify OTPs without user interaction.

## Risk
Account takeover through authentication logic failure.

## Mitigation
- Bind OTP to user and session
- Enforce rate limiting
- Expire OTP after use or time
- Use constant-time comparisons
