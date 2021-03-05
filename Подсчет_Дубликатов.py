# def duplicate_count(text):
#     namber=0
#     text=list(text.lower())
#     dicts={}
#     for i in text:
#         if dicts.get(i):
#             dicts[i]=dicts[i]+1
#         else:
#             dicts[i]=1
#     for i in dicts.values():
#         if i>1:
#             namber+=1
#     return namber

def duplicate_count(text):
    return len([c for c in set(text.lower()) if text.lower().count(c)>1])

print(duplicate_count(""))
print(duplicate_count("abcde"))
print(duplicate_count("abcdeaa"))
print(duplicate_count("abcdeaB"))
print(duplicate_count("Indivisibilities"))
