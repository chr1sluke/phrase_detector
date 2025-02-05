# Speech Command Detector

This Python script listens for a stealthly specific target phrase and triggers a macOS notification when the phrase is detected.

## Features
- Listens for a user-defined phrase in real-time using the `speech_recognition` library.
- When the phrase is detected, it triggers a macOS system notification with a custom alert.
- Adjustable listening duration (`DURATION`).
- Continues to listen and rechecks the phrase in a loop until interrupted.

## Installation

To get started with the Speech Command Detector, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/YOUR_USERNAME/speech-command-detector.git
   cd speech-command-detector
