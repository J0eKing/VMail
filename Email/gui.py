import webview

def showUnread(u, sender, subject, body):
    html = '''<html>

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width = device-width, initial-scale = 1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Main</title>
    <style>
        @import url('https://fonts.googleapis.com/css?family=Arvo|Varela+Round');

        body {
            background-color: #6ed3cf;
            padding: 30px;
            margin: 30;
            text-align: left;
            font-family: "Arvo"
        }

        input{
            height: 27px;
            width: 500px;
            margin: 10px;
            
        }
        #ebody{
            background-color: white;
            height: 520px;
            margin-top: 20px;
            border-width: thin;
            border-style: groove;
            border-color: black;
            border-radius: 4px;
            padding: 5px;
        }
    </style>
</head>

<body>
    To: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type=text value="''' + u + '''">
    <br>
    From: &nbsp;&nbsp;&nbsp;&nbsp;<input type="text" value="''' + sender + '''">
    <br>
    Subject: <input type="text" value="''' + subject + '''">
    <div id="ebody">''' + str(body) + '''</div>

</body></html>'''

    webview.load_html(html)
