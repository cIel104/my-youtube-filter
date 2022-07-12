from django.shortcuts import render
from django.conf import settings
from apiclient.discovery import build
import re

api_key = getattr(settings, "YOUTUBE_API_KEY", None)

def home_screen(request):
    return render(request, 'youtube_filter/home_screen.html')

def result_screen(request):
    #入力結果から必要な情報をyoutubeから取得
    videos = serch_youtube(request = request)

    #フィルターを分解
    filter = re.split("([+-×÷])",request.POST.get('filter'))

    #フィルターを使って並び替え
    sorted_videos = sort_by_filter(filter = filter, videos = videos, order = request.POST.get('order'))

    #表示用のリストを作成
    display_videos = make_display_videos(sorted_videos = sorted_videos, display = int(request.POST.get('display')))

    filters = {
        'words' : request.POST.get('word'),
        'filter' : filter,
        'display' : request.POST.get('display'),
        'read' : request.POST.get('read'),
        'order' : request.POST.get('order'),
        'videos' : display_videos,
    }
    return render(request, 'youtube_filter/result_screen.html', filters)

def serch_youtube(request):
    if settings.DEBUG:
        password = settings.YOUTUBE_API_KEY
    
    API_KEY = password #自分のapiキー
    KEY_WORD = request.POST.get('word') #検索ワード
    MAX_RESULT = request.POST.get('read') #取得件数
    ORDER = "viewCount" #再生順
    youtube = build("youtube", "v3", developerKey=API_KEY)

    #動画情報の取得
    search_response = youtube.search().list(
      q=KEY_WORD, #検索する文字列
      part="id,snippet", #snippetはタイトルや説明文
      maxResults=MAX_RESULT, #取得するデータ件数
      order=ORDER #ソート順
    ).execute()

    
    videos = []
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            movie_info = {}
            movie_info = get_movie_info(id = search_result["id"]["videoId"], youtube = youtube) #動画の情報を取得
            movie_info['title'] = search_result["snippet"]["title"] #タイトルの取得
            movie_info['url'] = 'https://www.youtube.com/watch?v=' + search_result["id"]["videoId"] #urlの取得
            videos.append(movie_info)
            #bad_count = get_bad_count(id = search_result["id"]["videoId"], youtube = youtube) 低評価だけとれない
    
    return videos

def get_movie_info(id, youtube):
    #再生回数を取得
    try:
        view_count = youtube.videos().list(part = 'statistics', id = id).execute()['items'][0]['statistics']['viewCount']
    except(KeyError):
        view_count = '1'
    #高評価数を取得
    try:
        good_count = youtube.videos().list(part = 'statistics', id = id).execute()['items'][0]['statistics']['likeCount']
    except(KeyError):
        good_count = '1'
    #お気に入り登録数を取得
    favor_count = youtube.videos().list(part = 'statistics', id = id).execute()['items'][0]['statistics']['favoriteCount']
    #コメント数を取得
    try:
        comment_count = youtube.videos().list(part = 'statistics', id = id).execute()['items'][0]['statistics']['commentCount']
    except(KeyError):
        comment_count = '1'
    
    movie_info = {'再生回数':view_count, '高評価':good_count, 'お気に入り登録数':favor_count, 'コメント数': comment_count}
    return movie_info

#低評価数を取得
# def get_bad_count(id, youtube):
#     bad_count = youtube.videos().list(part = 'statistics', id = id).execute()['items'][0]['statistics']['dislikeCount']
#     return bad_count

def sort_by_filter(filter, videos, order):
    #取得した値を文字列から数値へ変換
    num_videos = []
    for video in videos:
        num_video = {}
        for k, v in video.items():
            try:
                num_video[k] = int(v)
            except(ValueError):
                num_video[k] = v
        num_videos.append(num_video)

    #フィルターの式から値を'sort'に代入
    for video in num_videos:
        video['sort'] = video[filter[0]]
        for i in range(2,len(filter), 2):
            if filter[i] == '':
                break
            if filter[i-1] == '+':
                video['sort'] = video['sort'] + video[filter[i]]
            elif filter[i-1] == '-':
                video['sort'] = video['sort'] - video[filter[i]]
            elif filter[i-1] == '×':
                video['sort'] = video['sort'] * video[filter[i]]
            else:
                video['sort'] = video['sort'] / video[filter[i]]

    #降順と昇順の識別
    if order == 'desc':
        sorted_videos = sorted(num_videos, key = lambda x : int(x['sort']), reverse = True)
    else:
        sorted_videos = sorted(num_videos, key = lambda x : int(x['sort']))
    return sorted_videos

#表示件数を指定
def make_display_videos(sorted_videos, display):
    display_videos = []
    for i in range(display):
        display_videos.append(sorted_videos[i])
    return display_videos 