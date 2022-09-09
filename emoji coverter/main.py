message = input(">")
words = message.split(" ")
emojis = {
    ":)" : "😀",
    ":(" : "🙁",
    "umbrella" : "☔",
    "sunshine" : "🌞",
    "heart": "♥",
    "book" : "📚",
    "movie" :"🎬",
    "fire" : "🔥"
}
outcome  =""
for word in words:
    outcome += emojis.get(word, word) + " "
print(outcome)


 



