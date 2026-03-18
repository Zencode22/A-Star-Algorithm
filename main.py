#!/usr/bin/env python3
# ============================================================================
# MAIN ENTRY POINT
# ============================================================================

import pygame
import sys

# Initialize pygame first
pygame.init()

# Import config
from config import WIDTH, HEIGHT, FULLSCREEN
from game.horse_race_game import HorseRaceGame


def main():
    """Main entry point - no terminal controls needed"""
    
    # Always use windowed mode to ensure borders are visible
    # Ignore FULLSCREEN flag to keep windowed mode
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    current_width, current_height = WIDTH, HEIGHT
    
    pygame.display.set_caption("🐎 Horse Race Simulator 🐎")
    
    # Show welcome message
    print("=" * 60)
    print("🐎 HORSE RACE SIMULATOR 🐎")
    print("=" * 60)
    print(f"\nScreen size: {current_width} x {current_height}")
    print("\nGame Controls:")
    print("  SPACE      - Pause/Resume race")
    print("  R          - Reset race")
    print("  D          - Toggle debug view")
    print("  Mouse Click - Select a horse")
    print("  ESC        - Deselect horse")
    print("  Q          - Quit game")
    print("\nThe race will start automatically!")
    print("Watch the horses flock together while following")
    print("optimal A* paths around the track!")
    print("-" * 60)
    
    # Create and run the game
    try:
        game = HorseRaceGame(screen, current_width, current_height)
        game.run()
    except Exception as e:
        print(f"\n[ERROR] {e}")
        import traceback
        traceback.print_exc()
    finally:
        pygame.quit()
        print("\n[SYSTEM] Race simulation ended. Thanks for watching! 🐎")


if __name__ == "__main__":
    main()