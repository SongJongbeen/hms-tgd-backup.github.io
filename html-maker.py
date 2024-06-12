# html_path = f"{self.backup_folder}/html-{content_link.split('/')[-1]}.html"
tgd_csv = "tgd-crawler/tgd.csv"
content_html_path = "tgd-crawler/backup/html-73465473.html"
html_path = "tgd-crawler/html-73465473.html"

with open(content_html_path, "r", encoding="utf8") as file:
    content_html = file.read()

with open()

base_html = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>안녕</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            background-color: #f0f0f0;
        }
        .container {
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            padding: 20px;
            margin-top: 50px;
            width: 80%;
            max-width: 800px;
        }
        .header {
            text-align: center;
            margin-bottom: 20px;
        }
        .title {
            font-size: 2em;
            margin: 0;
        }
        .meta {
            font-size: 1.2em;
            color: #555;
        }
        .content {
            margin-top: 20px;
        }
        iframe {
            width: 100%;
            height: 360px;
            border: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1 class="title">안녕</h1>
            <p class="meta">작성자: 성경 | 작성 날짜: 06-08</p>
        </div>
        <div class="content">
            <p>
                <span class="fr-video fr-deletable fr-fvc fr-dvb fr-draggable">
                    <iframe allowfullscreen="allowfullscreen" src="https://www.youtube.com/embed/d4OTnN5brgY?autoplay=0&amp;mute=0&amp;enablejsapi=1&amp;origin=tgd.kr" id="630408456"></iframe>
                </span>
            </p>
        </div>
    </div>
</body>
</html>
"""