print("=" * 45)
print(" EXERCÍCIO - A Playlist do Fudencio")
print("=" * 45)

playlist = ["Catedral", "Reginaldo Rossi", "Charlie Brown Junior", "Guns N' Roses", "Seu Jorge"]

playlist.append("Michael Jackson")
playlist.append("Fagner")

playlist.remove("Fagner")

playlist.sort()

print("Sua playlist final: ")
for musica in playlist:
    print(musica)