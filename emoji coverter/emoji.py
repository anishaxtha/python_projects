#   program by calling the fuction 

def emoji_coverter(message):
    words = message.split(" ")
    emojis = {
    ":)" : "😀",
    ":(" : "🙁",
    "umbrella" : "☔",
    "sunshine" : "🌞",
    "heart": "♥",
    "books" : "📚",
    "movie" :"🎬",
    "fire" : "🔥"
}
    outcome  = " "
    for word in words:
             outcome += emojis.get(word, word) + " "
    return outcome

 

message = input(">")
print(emoji_coverter(message))