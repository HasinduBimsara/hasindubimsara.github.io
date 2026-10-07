with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

replacements = {
    'ΓÇô': '–',
    'ΓÇó': '•',
    'ΓÇ¥': '"',
    'ΓÇ£': '"',
    'ΓÇÿ': "'",
    'ΓÇÖ': "'",
    'Γäó': '™',
}

for bad, good in replacements.items():
    content = content.replace(bad, good)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Cleaned encoding artifacts successfully.")
