# Profile Comparison Reflection

I compared outputs from all profile pairs to understand what each preference setup is really testing.

1. High-Energy Pop vs Chill Lofi: High-Energy Pop pushes fast, punchy songs, while Chill Lofi shifts toward softer, lower-energy tracks. This makes sense because their target energy is almost opposite.
2. High-Energy Pop vs Deep Intense Rock: Both profiles share high energy, so some overlap appears, but Rock pulls in heavier songs while Pop keeps brighter songs near the top. Same intensity, different style direction.
3. High-Energy Pop vs Adversarial (High Energy + Sad): Both want high energy, so energetic songs still dominate. The "sad" mood request does not fully take over, which is why Gym Hero can still show up high.
4. High-Energy Pop vs Edge Case Out-of-Range: The edge profile gives strange target values, so scores are lower and less stable. It still surfaces energetic tracks because energy is weighted strongly.
5. Chill Lofi vs Deep Intense Rock: These lists separate clearly. Lofi prefers calm, acoustic-leaning songs, while Rock prefers high-energy and intense tracks.
6. Chill Lofi vs Adversarial (High Energy + Sad): Lofi and adversarial profiles diverge sharply because one wants low energy and the other wants very high energy. This confirms energy is a major driver.
7. Chill Lofi vs Edge Case Out-of-Range: Chill Lofi gives coherent calm recommendations, while the edge profile behaves more erratically due to invalid preference ranges. That difference suggests we should validate inputs.
8. Deep Intense Rock vs Adversarial (High Energy + Sad): These two overlap more than expected because both reward high energy. Mood differences matter less once energy dominates.
9. Deep Intense Rock vs Edge Case Out-of-Range: Rock remains focused and interpretable, while edge-case output looks like "best available energy match" rather than a clear mood/genre match.
10. Adversarial (High Energy + Sad) vs Edge Case Out-of-Range: Both are stress tests, but the adversarial profile still has meaningful preferences, while out-of-range inputs produce weaker, more arbitrary-feeling rankings.

Plain-language takeaway: Gym Hero keeps showing up because it is one of the highest-energy songs in a small dataset, and energy now has a very large weight. So even when a user asks for "happy pop" or another vibe, that one strong feature can pull the song up the list repeatedly.
