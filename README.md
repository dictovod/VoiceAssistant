# VoiceAssistant http://138.124.35.201/vosk.7z to C:\
This is a simple voice echo application built in Python for Windows 11

# Simple Voice Echo Assistant

## Overview

This is a simple voice echo application built in Python for Windows 11 that listens to speech and repeats it back. The application uses Vosk for offline speech recognition (located at C:\vosk) and pyttsx3 for text-to-speech synthesis. It's designed to be straightforward - just listen to what you say and repeat it back.

**Recent Update (August 2025):** 
- Complete GUI redesign with compact interface (400x250) and professional menu system
- Implemented ultra-strict microphone filtering showing only 3 real microphones (vs 15+ virtual devices)
- Added configurable logging system in menu - users can choose what to show in logs
- Speech rate control moved to menu with presets (slow/normal/fast) and custom dialog
- Device management through menu with "Show all devices" diagnostic window
- Fixed critical TTS issue with full reinitialization for second+ pronunciations
- Cleaned up project by removing unused files
- Menu structure: Settings > Speed/Devices/Logging, Help > About

## User Preferences

Preferred communication style: Simple, everyday language.
Language preference: Russian.
Request: Simple voice assistant for Windows 11 that listens and repeats speech using Vosk from C:\vosk directory.

## System Architecture

### Core Design Pattern
The application follows a modular architecture with clear separation of concerns:

- **Main Coordinator**: `VoiceAssistant` class acts as the central orchestrator
- **Audio Processing**: `AudioHandler` manages all audio input/output operations
- **Command Processing**: `CommandProcessor` handles voice command interpretation and response generation
- **Configuration Management**: `Config` class centralizes all application settings

### Audio Architecture
The audio system is built on three main components:
- **PyAudio**: Low-level audio I/O operations
- **SpeechRecognition**: Converts speech to text using offline recognition
- **pyttsx3**: Text-to-speech synthesis for response output

The audio handler includes ambient noise adjustment and configurable speech recognition parameters to optimize performance in different environments.

### Command Processing System
Uses regex pattern matching to identify and route voice commands to appropriate handlers. The processor includes built-in responses for:
- Time and date queries
- Basic mathematical operations
- Identity and help requests
- Weather queries (basic offline responses)
- Greeting interactions

### Configuration Management
Centralized configuration system that supports:
- Environment variable overrides
- Audio device selection
- Speech recognition parameters
- TTS settings (rate, volume)
- Timeout and threshold configurations

### Error Handling and Logging
Comprehensive error handling with structured logging throughout all components. The system includes dependency checking and graceful failure modes.

## External Dependencies

### Core Audio Libraries
- **PyAudio**: Cross-platform audio I/O library for microphone and speaker access
- **SpeechRecognition**: Python library for performing speech recognition with offline capabilities
- **pyttsx3**: Text-to-speech conversion library with offline synthesis

### System Libraries
- **wave**: Python standard library for WAV file operations
- **threading**: For concurrent audio processing operations
- **io**: For in-memory audio buffer handling

### Development Dependencies
- **logging**: Python standard library for application logging
- **datetime**: For time and date functionality
- **re**: Regular expression matching for command processing
- **os/sys**: System interface and environment variable access

The application is designed to run completely offline with no external API dependencies or internet connectivity requirements.
