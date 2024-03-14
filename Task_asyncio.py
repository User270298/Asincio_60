import asyncio
import aiohttp
import ast
import aiofiles

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def get_html(my_num):
    url1 = 'https://api.thecatapi.com/v1/images/search'
    url2 = 'https://random.dog/woof.json'
    tasks = []
    for _ in range(my_num):
        tasks.append(fetch(url1))
        tasks.append(fetch(url2))
    res = await asyncio.gather(*tasks)
    count = 0
    tasks.clear()

    for i in res:
        if my_num == count:
            break
        dictionary = ast.literal_eval(i)
        count += 1
        if isinstance(dictionary, list):
            tasks.append(dictionary[0]['url'])
        else:
            tasks.append(dictionary['url'])
    return tasks


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
    task.clear()
    for i in res:
        dictionary = ast.literal_eval(i)
        if change == '1':
            task.append(dictionary['url'])
        elif change == '2':
            task.append(dictionary[0]['url'])
    return task


async def save_images(images):
    for image in images:
        async with aiohttp.ClientSession() as session:
            async with session.get(image) as resp:
                if resp.status == 200:
                    f=await aiofiles.open(f'{image}'.rsplit('/', 1)[1], 'wb')
                    await f.write(await resp.read())
                    await f.close()

def main():
    change = input('Change have dogs or cats or animals: '
                   '1-Dogs;\n2-Cats;\n3-Animals\n')
    if change == '1':
        f = asyncio.run(get_dog_or_cat(change))
    elif change == '2':
        f = asyncio.run(get_dog_or_cat(change))
    elif change == '3':
        f = asyncio.run(get_html(int(input('Enter count imagines: '))))
    asyncio.run(save_images(f))


main()
