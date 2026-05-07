# 🏇 Horse Racer - A* Pathfinding & Flocking Simulation

A pygame-based horse racing simulation featuring autonomous AI horses that navigate a square race track using A* pathfinding and Boids flocking algorithms. Watch six uniquely named horses compete, learn from their mistakes, and race to the finish!

---

## 🎮 Quick Start

### Option 1: Standalone Executable (No Python Required)
1. Download `HorseRacer.exe` from the latest [GitHub Release](https://github.com/conno/Codes/releases)
2. Double-click to run — the game starts immediately!

### Option 2: Run from Source
```bash
pip install -r requirements.txt
python main.py
```

**Requirements:** Python 3.7+ | Pygame 2.0+

---

## 🕹️ Controls

| Input | Action |
|-------|--------|
| **Mouse Click** | Select a horse to view stats |
| **R Key** | Reset the race at any time |
| **Reset Button** | Click the on-screen button to restart |
| **Q Key** | Quit after race finishes (when prompted) |

---

## 🏁 How It Works

The race begins automatically. Six horses start staggered along the right side of a square track and must navigate **9 checkpoints** in clockwise order to complete one lap. Each horse is an independent AI agent that:

- Builds an **A* path** from its current position to the next checkpoint
- Uses **flocking behaviors** to avoid collisions with other horses
- **Remembers barriers** it hits to avoid them in future attempts
- **Auto-resets** if it gets stuck or goes the wrong way

The race ends when all horses finish. Results are displayed on screen and saved to `horse_rankings.json`.

---

## 🧠 AI Systems

### A* Pathfinding
Each horse uses the A* algorithm to find the most direct route along the track while avoiding walls and the invisible barrier that prevents counter-clockwise shortcuts.

- **Grid resolution:** 10 pixels per cell
- **Heuristic:** Euclidean (straight-line) distance
- **Optimizations:** Path caching, line-of-sight smoothing, barrier memory

### Flocking (Boids)
Inspired by Craig Reynolds' Boids algorithm, each horse balances five simultaneous steering forces:

| Force | Weight | Purpose |
|-------|--------|---------|
| Separation | 1.0 | Don't crowd other horses |
| Path Following | 3.0 | Stick to the A* waypoint path |
| Track Attraction | 3.0 | Stay on the brown track surface |
| Barrier Avoidance | 5.0 | Steer away from walls |
| Checkpoint Pull | 5.0 | Move toward the next checkpoint |
| Clockwise Force | 4.0 | Prevent wrong-direction shortcuts |

Forces are combined into a single steering vector each frame. Horses that hit too many barriers, stop moving, or go the wrong way too long will **automatically reset** to the starting line.

---

## 📊 Live Rankings

A ranking panel on the right side of the screen shows real-time standings:

- Finished horses sort by time
- Racing horses sort by checkpoints reached
- Reset count is tracked per horse

Click any horse to see its name, speed, current checkpoint, and reset count.

---

## 📁 Project Structure

```
HorseRacer/
├── main.py                     # Game entry point
├── config.py                   # Settings: FPS, track size, horse names
├── horse_rankings.json         # Persistent race results
├── requirements.txt            # Python dependencies
│
├── game/
│   └── horse_race_game.py      # Main loop, UI, event handling
│
├── models/
│   ├── horse.py                # AI agent with flocking + pathfinding
│   ├── grid.py                 # Grid system for A* pathfinding
│   ├── node.py                 # Node class (walkable/unwalkable states)
│   ├── vector2.py              # 2D vector math library
│   └── ranking.py              # Statistics tracking and persistence
│
├── pathfinding/
│   └── astar.py                # A* algorithm implementation
│
├── track/
│   └── race_track.py           # Square track, checkpoints, barriers
│
└── utils/
    └── colors.py               # RGB color definitions
```

---

## 🏇 The Horses

| Name | Color |
|------|-------|
| DASHER | Red |
| BOLTO | Blue |
| STORM | Yellow |
| FLASH | Purple |
| RACER | Orange |
| ZIPPY | White |

Each horse has the same AI but different starting positions, leading to emergent, unpredictable races every time.

---

## ⚙️ Configuration

Edit `config.py` to customize:

```python
WIDTH, HEIGHT = 1280, 720   # Window size
FPS = 60                     # Frame rate
NUM_HORSES = 6               # Number of racers
LAPS_TO_WIN = 1              # Laps required to finish
HORSE_NAMES = ["DASHER", "BOLTO", "STORM", "FLASH", "RACER", "ZIPPY"]
```

---

## ⚠️ Development Attribution

- **Code Generation:** Core game logic, pathfinding algorithms, and agent behaviors were generated with assistance from DeepSeek AI.
- **Documentation:** This README was written by Lumo (Proton's AI assistant).

*This project is an educational example of human-AI collaborative software development.*

---

## 📄 License

This project is for educational purposes. Feel free to modify, extend, and learn from it.

---

## 🙏 Credits

- **A* Algorithm:** Based on Unity pathfinding tutorial logic
- **Flocking Behavior:** Craig Reynolds' Boids algorithm (1986)
- **Graphics:** Pygame rendering library
- **AI Assistance:** DeepSeek (code generation), Lumo (documentation)

---

*Built for learning game AI and emergent behavior through human-AI collaboration*
- **Flocking:** Craig Reynolds' Boids algorithm
- **Graphics:** Pygame rendering library

---
*Built with ❤️ for learning game AI and pathfinding algorithms through human-AI collaboration*
