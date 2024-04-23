# payload_config.py

payload_data = {
    "methods": [
        "GET", "HEAD", "POST", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE", "PATCH"
    ],
    "custom_strings": [
        "http/ \n\n",
        "°#http/ \n\n/",
        "CONNECT [host]:[port] HTTP/1.1[crlf]GET /path HTTP/1.1[crlf]Host: [host][crlf][crlf]",
    ],
    "domains": [
        "wikipedia.org/about", 
        "youtube.com/about", 
        "google.com/", 
        "bing.com/search"
    ]
}
