

def habrExtend(link:str) -> str:
    return "https://freelance.habr.com/" + link

def create_text(data : tuple) -> str:
    return data[1] + '\n' + data[2]