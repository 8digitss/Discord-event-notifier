# 🎉 Discord Event Notifier Bot

Hey there! This is a simple little Discord bot that lets you schedule events and sends out reminders before they start.

It's perfect for small servers, friend groups, or anyone who wants to stay on top of events.

---

## ✨ What Can It Do?
- Add events with a title, time, and description.
- List all upcoming events.
- Automatically remind people shortly before events start.
- Super easy commands!

---

## 📝 Bot Commands:

| Command        | Usage                                    | What It Does                    |
|----------------|------------------------------------------|--------------------------------|
| `!addevent`    | `!addevent "Event Title" "YYYY-MM-DDTHH:MM" Description` | Adds a new event with title, ISO-format time, and description. Example: `!addevent "Game Night" "2025-07-15T20:00" Let's play some games!` |
| `!listevents`  | `!listevents`                            | Shows all scheduled upcoming events in a neat list. |

The bot also automatically reminds you about events 10 minutes before they happen!

---

## 🧰 What You Need:
- Python 3.8 or newer.
- A Discord Bot Token (you can get one from the [Discord Developer Portal](https://discord.com/developers/applications)).
- The `discord.py` Python package.

---

## 🚀 How To Get Started:

1. **Install the Needed Packages:**
```bash
pip install -r requirements.txt
