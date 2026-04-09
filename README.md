# QRT (Quick Response Team)

This project is a prototype of an emergency alert system that tries to simulate how real-world crisis alerts could be verified and delivered quickly.

The idea is simple:
Detect → Verify → Target → Dispatch

---

# QRT (Quick Response Team)

[![Live Demo](https://img.shields.io/badge/%20Live%20Demo-QRT%20Simulation-red?style=for-the-badge)](https://www.priyanshuchauhan.in/qrt)

---

## What this project does

* Takes an incoming alert signal
* Uses a basic ML model to check if it's real or not
* Finds users in the affected area using coordinates
* Sends alerts using a fast queue system
* Shows everything visually on a simple command center UI

---

## Project Structure

* `verification_engine.py` → handles AI verification + geo targeting
* `fast_queue.cpp` → dispatch system using queue
* `index.html` → frontend simulation UI

---

## How it works

1. A signal comes in (with credibility, urgency, etc.)
2. The ML model decides if it’s a real threat
3. If yes → system checks nearby users
4. Those users are added to a queue
5. Dispatcher sends alerts
6. Frontend shows the whole process

---

## Tech used

* Python (NumPy, sklearn)
* C++ (queue, basic threading)
* HTML, CSS, JavaScript

---

## Running the project

### Python

pip install numpy scikit-learn
python verification_engine.py

### C++

g++ fast_queue.cpp -o dispatcher
./dispatcher

### Frontend

Just open index.html in browser

---

## Notes

* This is just a simulation, not a production system
* Data is hardcoded for now
* No real networking is implemented

---

## Why I built this

I wanted to combine:

* machine learning
* system design
* frontend visualization

into one project that actually feels like a real-world system.

---

## Future improvements

* connect real APIs (weather / alerts)
* replace hardcoded users with database
* integrate backend (Node.js or FastAPI)
* real-time communication (WebSockets)

---

## Author

Priyanshu Chauhan


