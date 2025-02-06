# Phrase Detector

This Python script listens for a stealthily specific target phrase and triggers a macOS notification when the phrase is detected.

## Features
- Listens for a user-defined phrase in real-time using the `speech_recognition` library.
- When the phrase is detected, it triggers a macOS system notification with a custom alert.
- Adjustable listening duration (`DURATION`).
- Continues to listen and rechecks the phrase in a loop until interrupted.

## Prospective Application
- Home security system that is triggered when the target phrase is heard, and automatically calls Emergency Services
