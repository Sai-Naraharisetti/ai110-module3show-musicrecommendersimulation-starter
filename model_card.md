# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

VibeMixer 1.0

---

## 2. Goal / Task

This recommender suggests songs that match a user's taste profile.
It tries to rank songs by how well they match genre, mood, and audio vibe.
The final output is the top 5 songs with a short reason for each.

---

## 3. Data Used

I used a small CSV catalog with 18 songs.
Each song has genre, mood, energy, tempo, valence, danceability, and acousticness.
The data covers multiple genres, but most genres only appear once.
Lofi appears 3 times and pop appears 2 times, so some styles are easier to match than others.
This is a toy dataset, so it cannot represent full real-world music taste.

---

## 4. Algorithm Summary

For each song, the model builds one score.
It adds points when genre and mood match the user profile.
It also adds points when numeric features are close to user targets.
Right now energy has strong weight, so songs with similar energy rise quickly.
Then all songs are sorted by score and the top 5 are returned.

---

## 5. Observed Behavior / Biases

The biggest pattern is that high-energy songs show up a lot.
After my weight experiment, energy started to overpower mood in some profiles.
For example, in a high-energy plus sad profile, upbeat songs still ranked high.
I also saw repeat songs across different users because the catalog is small.
So the system can create a mini filter bubble.

---

## 6. Evaluation Process

I tested five profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, Adversarial (High Energy + Sad), and an Edge profile with out-of-range targets.
I checked whether top songs felt right for the intended vibe.
I also ran a sensitivity experiment: halved genre weight and doubled energy weight.
The results became more consistent by energy, but not always better by mood.
So the changes made recommendations more different, not always more accurate.

---

## 7. Intended Use and Non-Intended Use

Intended use:
This project is for learning how recommendation logic works.
It is good for classroom demos and simple experiments.

Non-intended use:
It should not be used as a production music recommender.
It should not be used for high-stakes decisions about people.
It does not model context like lyrics, language, culture, or listening history.

---

## 8. Ideas for Improvement

1. Add input validation and clamp out-of-range user targets.
2. Rebalance weights so mood and genre are not drowned out by energy.
3. Add a diversity rule so one song does not keep appearing for very different users.

---

## 9. Personal Reflection

My biggest learning moment was seeing how one weight change can shift the whole personality of recommendations.
AI tools helped me move faster when writing profile tests and checking outputs, but I had to double-check every suggested logic tweak with actual runs.
What surprised me most is that even a simple scoring formula can feel "smart" to users when results are presented as ranked choices.
If I continue this project, I want to add user history and a diversity penalty so recommendations feel less repetitive and more personal.
