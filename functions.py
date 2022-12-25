import json


def search_text(text):
    data = json.load(open("posts.json"))
    list_posts = []
    for post in data:
        if text.lower() in post["content"].lower():
            list_posts.append(post)
    return list_posts


def add_in_posts(picture, text):
    new_post = {
        "pic": "/uploads/images/" + picture,
        "content": text
    }
    data = json.load(open("posts.json"))
    data.append(new_post)
    with open("posts.json", "w") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)












   # <form action="post_by_tag.html" method="get">
   #      <p>По вхождению слова</p>
   #      <input type="text" name="s">
   #      <input type="submit" value="Найти" class="button">
   #  </form>