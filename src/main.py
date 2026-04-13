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

    profiles = [
        (
            "High-Energy Pop",
            {
                "favorite_genre": "pop",
                "favorite_mood": "happy",
                "target_energy": 0.90,
                "target_tempo_bpm": 128,
                "target_valence": 0.85,
                "target_danceability": 0.88,
                "target_acousticness": 0.12,
            },
        ),
        (
            "Chill Lofi",
            {
                "favorite_genre": "lofi",
                "favorite_mood": "calm",
                "target_energy": 0.25,
                "target_tempo_bpm": 78,
                "target_valence": 0.45,
                "target_danceability": 0.35,
                "target_acousticness": 0.78,
            },
        ),
        (
            "Deep Intense Rock",
            {
                "favorite_genre": "rock",
                "favorite_mood": "intense",
                "target_energy": 0.88,
                "target_tempo_bpm": 145,
                "target_valence": 0.30,
                "target_danceability": 0.48,
                "target_acousticness": 0.08,
            },
        ),
        # Adversarial/edge profiles probe contradictory preferences and out-of-band targets.
        (
            "Adversarial: High Energy + Sad",
            {
                "favorite_genre": "pop",
                "favorite_mood": "sad",
                "target_energy": 0.90,
                "target_tempo_bpm": 95,
                "target_valence": 0.10,
                "target_danceability": 0.82,
                "target_acousticness": 0.15,
            },
        ),
        (
            "Edge Case: Out-of-Range Targets",
            {
                "favorite_genre": "electronic",
                "favorite_mood": "happy",
                "target_energy": 1.20,
                "target_tempo_bpm": 220,
                "target_valence": -0.20,
                "target_danceability": 1.10,
                "target_acousticness": -0.30,
            },
        ),
    ]

    print("\nSystem Evaluation")
    print("Top 5 recommendations for each profile:\n")

    for profile_name, user_prefs in profiles:
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print(f"=== {profile_name} ===")
        print(
            f"genre={user_prefs['favorite_genre']}, "
            f"mood={user_prefs['favorite_mood']}, "
            f"target_energy={float(user_prefs['target_energy']):.2f}"
        )

        for idx, rec in enumerate(recommendations, start=1):
            song, score, explanation = rec
            print(f"{idx}. {song['title']} by {song['artist']}")
            print(f"   Score   : {score:.2f}")
            print(f"   Reasons : {explanation}")
            print()


if __name__ == "__main__":
    main()
