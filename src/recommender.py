import csv
from typing import List, Dict, Tuple
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        """Initialize the recommender with an in-memory song catalog."""
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top-k songs ranked by match score for a user profile."""
        scored = []
        for song in self.songs:
            score = 0.0
            if song.genre.lower() == user.favorite_genre.lower():
                score += 1.0
            if song.mood.lower() == user.favorite_mood.lower():
                score += 1.0

            energy_similarity = max(0.0, 1.0 - abs(song.energy - user.target_energy))
            score += 4.0 * energy_similarity

            if user.likes_acoustic:
                score += 1.0 * song.acousticness
            else:
                score += 1.0 * (1.0 - song.acousticness)

            scored.append((song, score))

        scored.sort(key=lambda row: row[1], reverse=True)
        return [song for song, _ in scored[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Build a short natural-language explanation for a recommended song."""
        reasons: List[str] = []
        if song.genre.lower() == user.favorite_genre.lower():
            reasons.append("genre matches")
        if song.mood.lower() == user.favorite_mood.lower():
            reasons.append("mood matches")

        energy_similarity = max(0.0, 1.0 - abs(song.energy - user.target_energy))
        if energy_similarity >= 0.8:
            reasons.append("energy is close to target")

        if user.likes_acoustic and song.acousticness >= 0.6:
            reasons.append("fits acoustic preference")
        if (not user.likes_acoustic) and song.acousticness <= 0.4:
            reasons.append("leans non-acoustic as preferred")

        if not reasons:
            return "Recommended as a balanced overall match across features."
        return "Recommended because " + ", ".join(reasons) + "."

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from CSV and parse numeric fields into Python numbers."""
    songs: List[Dict] = []
    with open(csv_path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["id"] = int(row["id"])
            row["energy"] = float(row["energy"])
            row["tempo_bpm"] = float(row["tempo_bpm"])
            row["valence"] = float(row["valence"])
            row["danceability"] = float(row["danceability"])
            row["acousticness"] = float(row["acousticness"])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Compute a weighted score and reason list for one song."""
    score = 0.0
    reasons: List[str] = []

    favorite_genre = user_prefs.get("favorite_genre", user_prefs.get("genre"))
    favorite_mood = user_prefs.get("favorite_mood", user_prefs.get("mood"))
    target_energy = user_prefs.get("target_energy", user_prefs.get("energy"))

    if favorite_genre and str(song.get("genre", "")).lower() == str(favorite_genre).lower():
        score += 1.0
        reasons.append("genre match (+1.0)")

    if favorite_mood and str(song.get("mood", "")).lower() == str(favorite_mood).lower():
        score += 1.0
        reasons.append("mood match (+1.0)")

    if target_energy is not None:
        energy_similarity = max(0.0, 1.0 - abs(float(song["energy"]) - float(target_energy)))
        energy_points = 4.0 * energy_similarity
        score += energy_points
        reasons.append(f"energy closeness (+{energy_points:.2f})")

    if "target_valence" in user_prefs:
        valence_similarity = max(0.0, 1.0 - abs(float(song["valence"]) - float(user_prefs["target_valence"])))
        valence_points = 0.75 * valence_similarity
        score += valence_points
        reasons.append(f"valence closeness (+{valence_points:.2f})")

    if "target_danceability" in user_prefs:
        dance_similarity = max(0.0, 1.0 - abs(float(song["danceability"]) - float(user_prefs["target_danceability"])))
        dance_points = 0.5 * dance_similarity
        score += dance_points
        reasons.append(f"danceability closeness (+{dance_points:.2f})")

    if "target_acousticness" in user_prefs:
        acoustic_similarity = max(0.0, 1.0 - abs(float(song["acousticness"]) - float(user_prefs["target_acousticness"])))
        acoustic_points = 0.5 * acoustic_similarity
        score += acoustic_points
        reasons.append(f"acousticness closeness (+{acoustic_points:.2f})")

    if "target_tempo_bpm" in user_prefs:
        tempo_gap = abs(float(song["tempo_bpm"]) - float(user_prefs["target_tempo_bpm"]))
        tempo_similarity = max(0.0, 1.0 - min(tempo_gap / 100.0, 1.0))
        tempo_points = 0.25 * tempo_similarity
        score += tempo_points
        reasons.append(f"tempo closeness (+{tempo_points:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score all songs, rank them, and return top-k recommendations with reasons."""
    # Score every song, then sort highest-to-lowest in one expression
    scored = sorted(
        [(song, *score_song(user_prefs, song)) for song in songs],
        key=lambda row: row[1],
        reverse=True,
    )

    # Flatten reasons list into a human-readable string for each top-k result
    return [
        (song, score, "; ".join(reasons) if reasons else "overall feature similarity")
        for song, score, reasons in scored[:k]
    ]
