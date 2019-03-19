from youtube_dl import YoutubeDL

# dl = YoutubeDL()

# SAMPLE 1 - Download one video

# dl.download(['https://www.youtube.com/watch?v=WHK5p7JL7g4'])

# -----------------------------------------------------------------------------------
# SAMPLE 2 - Download multiple videos

# dl.download(['https://www.youtube.com/watch?v=wNVIn-QS4DE', 'https://www.youtube.com/watch?v=JZjRrg2rpic'])

# -----------------------------------------------------------------------------------
# SAMPLE 3 - Only download audio

# options = {
#     'format': 'bestaudio/audio' # Tell the downloader to download only the best quality of audio
# }
# dl = YoutubeDL(options)
# dl.download(['https://www.youtube.com/watch?v=c3jHlYsnEe0'])

# -----------------------------------------------------------------------------------
# SAMPLE 4 - Search then donwload the first video

# options = {
#     'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
#     'max_downloads': 1 # Tell downloader to download only the first entry (video)
# }
# dl = YoutubeDL(options)
# dl.download(['con điên TAMKA PKL'])

# -----------------------------------------------------------------------------------
# SAMPLE 5 - Search then donwload the first audio

# options = {
#     'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
#     'max_downloads': 1, # Tell downloader to download only the first entry (audio)
#     'format': 'bestaudio/audio'
# }
# dl = YoutubeDL(options)
# dl.download(['Nhớ mưa sài gòn lam trường'])

