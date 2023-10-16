from django.shortcuts import render

import os


def home_page(request):
    folder_path = 'mainapp/static/audio'
    files = os.listdir(folder_path)

    audio_files = []
    chars = []

    for i in files:
        audio_files.append(i)
        chars.append(i.split('.')[0])

    main_list = zip(audio_files, chars)

    print(main_list)

    return render(request, "mainapp/home_page.html", {
        'main_list': main_list,
    })
