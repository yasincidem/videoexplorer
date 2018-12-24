import requests

# #Get tags from video

## Beğenme oranı
## görüntülenme sayısı
## Yorum sayısı
## abone sayısı

with requests.get("https://www.googleapis.com/youtube/v3/videos?key=AIzaSyAZGJ9zSpQuNzen5QYfuOS4mxOyrwT9hAM&part=snippet,statistics,topicDetails&id=WyprXhvGVYk") as url:
    data = url.json()
    tags = data['items'][0]['snippet']['tags']
    commentCount = data['items'][0]['statistics']['commentCount']
    dislikeCount = data['items'][0]['statistics']['dislikeCount']
    likeCount = data['items'][0]['statistics']['likeCount']
    viewCount = data['items'][0]['statistics']['viewCount']


print(tags)
print (100 * (float(likeCount)) / (float(likeCount) + float(dislikeCount)))
print(commentCount)
print(viewCount)

#
# Get subtitles from video
import xmltodict as xmltodict

map = {}
req = requests.get("https://www.youtube.com/api/timedtext?lang=en&v=WyprXhvGVYk")
# req2 = requests.get("https://www.googleapis.com/youtube/v3/videos?key=AIzaSyAZGJ9zSpQuNzen5QYfuOS4mxOyrwT9hAM&fields=items(snippet(title,description,tags))&part=snippet&id=WyprXhvGVYk")
#
# print(req2.json()['items'][0]['snippet']['tags'])

data = xmltodict.parse(req.content)
subtitle = ''
for item in data['transcript']['text']:
    subtitle += (item['#text'])
for item in subtitle.split(' '):
    if item in map:
        map.__setitem__(item, 1 + map[item])
    else:
        map.setdefault(item, 1)

# print('Words in subtitle: ', sorted(map, key=map.get, reverse=True))
# reqUclassify = requests.get("https://api.uclassify.com/v1/uClassify/topics/classify/?readKey=CMh5lX5QKHV4&text={}".format(subtitle))
# var = 'uClassify: ', sorted(reqUclassify.json(), key=reqUclassify.json().get, reverse=True)[0]
# print(var)

def findVideo(id, count):
    if count == 0:
        return
    else:
        req = requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&relatedToVideoId={id}&type=video&key=AIzaSyAZGJ9zSpQuNzen5QYfuOS4mxOyrwT9hAM".format(id= id))
        print(req.json()['items'][0]['id']['videoId'])

        return findVideo(req.json()['items'][0]['id']['videoId'], count - 1)

findVideo("WyprXhvGVYk", 5)


def youtube_search(options):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=options.q,
    part='id,snippet',
    maxResults=options.max_results
  ).execute()

  videos = []
  channels = []
  playlists = []

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get('items', []):
    if search_result['id']['kind'] == 'youtube#video':
      videos.append('%s (%s)' % (search_result['snippet']['title'],
                                 search_result['id']['videoId']))
    elif search_result['id']['kind'] == 'youtube#channel':
      channels.append('%s (%s)' % (search_result['snippet']['title'],
                                   search_result['id']['channelId']))
    elif search_result['id']['kind'] == 'youtube#playlist':
      playlists.append('%s (%s)' % (search_result['snippet']['title'],
                                    search_result['id']['playlistId']))

  print 'Videos:\n', '\n'.join(videos), '\n'
  print 'Channels:\n', '\n'.join(channels), '\n'
  print 'Playlists:\n', '\n'.join(playlists), '\n'


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--q', help='Search term', default='Google')
  parser.add_argument('--max-results', help='Max results', default=25)
  args = parser.parse_args()

  try:
    youtube_search(args)
  except HttpError, e:
    print 'An HTTP error %d occurred:\n%s' % (e.resp.status, e.content)


