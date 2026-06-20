import os

def save_svg(name, content):
    with open(f"assets/images/{name}.svg", "w") as f:
        f.write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">{content}</svg>')

os.makedirs("assets/images", exist_ok=True)

# 1. Coffee Cup
save_svg("coffee-cup", '<path d="M30 40h30v30c0 10-5 15-15 15s-15-5-15-15V40z" fill="#f0f0f0" stroke="#333" stroke-width="2"/><path d="M60 45h5c5 0 8 3 8 8s-3 8-8 8h-5" fill="none" stroke="#333" stroke-width="2"/><path d="M40 25c0-5 5-5 5 0s5 5 5 0" fill="none" stroke="#ccc" stroke-width="2"/>')

# 2. Open Book
save_svg("book", '<path d="M10 30c20-5 40 0 40 0s20-5 40 0v40c-20-5-40 0-40 0s-20-5-40 0V30z" fill="#fff" stroke="#333" stroke-width="2"/><line x1="50" y1="30" x2="50" y2="70" stroke="#333" stroke-width="2"/>')

# 3. Potted Plant
save_svg("plant", '<path d="M35 70h30l-5 20H40l-5-20z" fill="#8B4513"/><path d="M50 70V40" stroke="#228B22" stroke-width="3"/><circle cx="40" cy="45" r="10" fill="#32CD32"/><circle cx="60" cy="45" r="10" fill="#32CD32"/><circle cx="50" cy="30" r="10" fill="#32CD32"/>')

# 4. Cat Face
save_svg("cat", '<circle cx="50" cy="55" r="30" fill="#f9f9f9" stroke="#333" stroke-width="2"/><path d="M30 35l-5-15 15 10M70 35l5-15-15 10" fill="#f9f9f9" stroke="#333" stroke-width="2"/><circle cx="40" cy="50" r="3"/><circle cx="60" cy="50" r="3"/><path d="M45 65s5 5 10 0" fill="none" stroke="#333" stroke-width="2"/>')

# 5. Rabbit
save_svg("rabbit", '<ellipse cx="50" cy="65" rx="25" ry="20" fill="#fff" stroke="#333" stroke-width="2"/><path d="M40 45c-5-20 5-20 5 0M60 45c5-20-5-20-5 0" fill="#fff" stroke="#333" stroke-width="2"/><circle cx="45" cy="60" r="2"/><circle cx="55" cy="60" r="2"/><path d="M48 68l2 2 2-2" fill="none" stroke="#333" stroke-width="2"/>')

# 6. Bear
save_svg("bear", '<circle cx="50" cy="60" r="25" fill="#A52A2A" stroke="#333" stroke-width="2"/><circle cx="30" cy="40" r="8" fill="#A52A2A" stroke="#333" stroke-width="2"/><circle cx="70" cy="40" r="8" fill="#A52A2A" stroke="#333" stroke-width="2"/><circle cx="45" cy="55" r="2" fill="#000"/><circle cx="55" cy="55" r="2" fill="#000"/><ellipse cx="50" cy="65" rx="5" ry="3" fill="#000"/>')

# 7. Apple
save_svg("apple", '<path d="M50 85c-20 0-35-15-35-35s15-30 35-30 35 10 35 30-15 35-35 35z" fill="#ff4d4d" stroke="#333" stroke-width="2"/><path d="M50 20v-10" stroke="#8B4513" stroke-width="3"/><path d="M50 15c10-5 15 5 0 10" fill="#32CD32"/>')

# 8. Star
save_svg("star", '<path d="M50 10l12 25h28l-22 18 8 27-26-17-26 17 8-27-22-18h28z" fill="#FFD700" stroke="#333" stroke-width="2"/>')

# 9. Heart
save_svg("heart", '<path d="M50 80s-35-20-35-45c0-15 15-20 20-10 5-10 20-5 20 10 0 25-35 45-35 45z" fill="#ff69b4" stroke="#333" stroke-width="2"/>')

# 10. Pencil
save_svg("pencil", '<path d="M30 20l40 40-10 10-40-40z" fill="#FFD700" stroke="#333" stroke-width="2"/><path d="M20 10l10 10-10 10z" fill="#000"/><path d="M70 60l5 5-10 10-5-5z" fill="#ffc0cb" stroke="#333" stroke-width="2"/>')

# 11. Camera
save_svg("camera", '<rect x="20" y="35" width="60" height="40" rx="5" fill="#ccc" stroke="#333" stroke-width="2"/><circle cx="50" cy="55" r="15" fill="#eee" stroke="#333" stroke-width="2"/><circle cx="50" cy="55" r="8" fill="#333"/><rect x="30" y="25" width="15" height="10" fill="#333"/>')

# 12. Cake
save_svg("cake", '<path d="M20 70h60v15H20z" fill="#f0e68c"/><path d="M20 50h60v20H20z" fill="#ffb6c1"/><path d="M20 50c0-10 10-15 30-15s30 5 30 15" fill="#fff"/><circle cx="50" cy="30" r="5" fill="#ff0000"/>')

# 13. Cloud
save_svg("cloud", '<path d="M25 70c-10 0-15-10-5-15 0-15 20-20 30-10 10-10 30-5 30 15 10 5 5 15-5 15H25z" fill="#f0f8ff" stroke="#333" stroke-width="2"/>')

# 14. Sun
save_svg("sun", '<circle cx="50" cy="50" r="20" fill="#FFFF00" stroke="#FFA500" stroke-width="2"/><path d="M50 10v10M50 80v10M10 50h10M80 50h10M22 22l7 7M71 71l7 7M22 78l7-7M71 29l7-7" stroke="#FFA500" stroke-width="3"/>')

# 15. Bird
save_svg("bird", '<path d="M30 50c0-15 20-25 40-10 10 10 5 25-10 25H30z" fill="#87CEEB" stroke="#333" stroke-width="2"/><path d="M70 45l10-5-5 10z" fill="#FFA500"/><circle cx="55" cy="45" r="2"/>')

# 16. Robot
save_svg("robot", '<rect x="30" y="40" width="40" height="40" fill="#bdc3c7" stroke="#333" stroke-width="2"/><rect x="35" y="25" width="30" height="15" fill="#bdc3c7" stroke="#333" stroke-width="2"/><circle cx="42" cy="32" r="2" fill="#e74c3c"/><circle cx="58" cy="32" r="2" fill="#e74c3c"/><path d="M45 15v10" stroke="#333" stroke-width="2"/>')

# 17. Rocket
save_svg("rocket", '<path d="M50 20c-10 20-10 40-10 50h20c0-10 0-30-10-50z" fill="#ecf0f1" stroke="#333" stroke-width="2"/><path d="M40 70l-10 10v-10zM60 70l10 10v-10z" fill="#e74c3c"/><circle cx="50" cy="45" r="5" fill="#3498db"/>')

# 18. Light Bulb
save_svg("idea", '<path d="M50 20c-15 0-20 10-20 20 0 10 5 15 10 20v10h20V60c5-5 10-10 10-20 0-10-5-20-20-20z" fill="#f1c40f" stroke="#333" stroke-width="2"/><path d="M40 75h20M42 80h16" stroke="#333" stroke-width="2"/>')

# 19. Paint Palette
save_svg("palette", '<path d="M20 50c0-20 20-35 45-30 15 5 20 20 15 35-5 15-20 25-40 20-10-2 20 20 20 20-30 0-40-25-40-45z" fill="#d2b48c" stroke="#333" stroke-width="2"/><circle cx="40" cy="35" r="5" fill="#e74c3c"/><circle cx="60" cy="40" r="5" fill="#2ecc71"/><circle cx="55" cy="60" r="5" fill="#3498db"/>')

# 20. House
save_svg("house", '<path d="M20 50v35h60V50L50 20 20 50z" fill="#fff" stroke="#333" stroke-width="2"/><rect x="40" y="65" width="20" height="20" fill="#8B4513"/><rect x="30" y="55" width="10" height="10" fill="#87CEEB"/>')

print("20 SVGs generated successfully.")
