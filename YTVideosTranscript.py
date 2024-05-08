from youtube_transcript_api import YouTubeTranscriptApi, VideoUnavailable
'''
you get the video id by chesking link of video that you are using, the id is the characters that are in the link after "v="
for example if video liks is "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
then video id is "dQw4w9WgXcQ"
'''
video_id = "dQw4w9WgXcQ"


try:

    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    filename = input("enter file name")
    if transcript:
        transcript_text = " ".join([entry["text"] for entry in transcript])

        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"Video ID: {video_id}\n")
            f.write("Transcript:\n")
            f.write(transcript_text)


        print(f"Transcript for video {video_id} saved to {filename}.txt")
    else:
        print(f"No transcript available for video {video_id}")

except VideoUnavailable:
    print(f"Video {video_id} is unavailable or has no transcript")
except Exception as e:
    print(f"An error occurred: {e}")