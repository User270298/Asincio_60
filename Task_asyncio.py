import asyncio
import aiohttp
import os
import time
import pickle
import ast


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def get_html(my_num):
    url1 = 'https://api.thecatapi.com/v1/images/search'
    url2 = 'https://random.dog/woof.json'
    tasks = []
    for i in range(my_num):

        tasks.append(fetch(url1))
        tasks.append(fetch(url2))
    res = await asyncio.gather(*tasks)
    count = 0
    for i in res:
        if my_num == count:
            break
        dictionary = ast.literal_eval(i)
        count += 1
        if isinstance(dictionary, list):
            print(dictionary[0]['url'])
        else:
            print(dictionary['url'])


async def get_dog_or_cat(change):
    if change == '1':
        url = 'https://random.dog/woof.json'
    elif change == '2':
        url = 'https://api.thecatapi.com/v1/images/search'
    task = []
    count = int(input('Enter count imagines: '))
    for _ in range(count):
        task.append(fetch(url))
    res = await asyncio.gather(*task)
    for i in res:
        dictionary = ast.literal_eval(i)
        if change == '1':
            print(dictionary['url'])
        elif change == '2':
            print(dictionary[0]['url'])


def save_images(images, pat):
    with open(images, 'rb') as image:
        file=image.read()
    print(os.path(pat))
    # with open(os.path(pat), 'bw') as f:
    #     f.write(file)



def main():
    change = input('Change have dogs or cats or animals: '
                   '1-Dogs;\n2-Cats;\n3-Animals\n')
    if change == '1':
        f=asyncio.run(get_dog_or_cat(change))
        save_images(f, 'DZ_60_asyncio')
    elif change == '2':
        asyncio.run(get_dog_or_cat(change))
    elif change == '3':
        asyncio.run(get_html(int(input('Enter count imagines: '))))

main()
# results= await asyncio.gather(*tasks)
# for result in results:
#     print(result)


# asyncio.run(get_html())
