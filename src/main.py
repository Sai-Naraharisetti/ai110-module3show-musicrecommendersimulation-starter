"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    # Default profile for the starter simulation
    user_prefs = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.80,
        "target_tempo_bpm": 122,
        "target_valence": 0.82,
        "target_danceability": 0.84,
        "target_acousticness": 0.20,
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations for profile:")
    print(
        f"genre={user_prefs['favorite_genre']}, "
        f"mood={user_prefs['favorite_mood']}, "
        f"target_energy={user_prefs['target_energy']:.2f}\n"
    )

    for idx, rec in enumerate(recommendations, start=1):
        song, score, explanation = rec
        print(f"{idx}. {song['title']} by {song['artist']}")
        print(f"   Score   : {score:.2f}")
        print(f"   Reasons : {explanation}")
        print()


if __name__ == "__main__":
    main()
