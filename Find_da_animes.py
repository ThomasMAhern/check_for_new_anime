!pip3 install playwright
import playwright
from playwright.async_api import async_playwright



animes = ['kimetsu no yaiba', 'ranking', 'strongest sage']

    
async def animeplanet_ep_num(name_of_anime):
    '''given anime name, go to anime-planet and extract episode value'''
    print(f'Attempting to get: {name_of_anime}')
    page = await context.new_page()
    await page.goto('https://www.anime-planet.com/')
    await page.fill('#siteSearch-input', name_of_anime) # enter anime text in search field
    await page.keyboard.press('Enter')
    episodes = page.inner_html('#siteContainer > ul > li:nth-child(2) > a > div.statusArea') #the episode item
    print(episodes())
#     value = episodes.('value') # get the actual number value
#     print(f'    Latest episode: {value}')
#     return value

async def nyaa_mag_link(name_of_anime, episode_2_get):
    '''given anime name and episode number, click on magnet link to open in transmission'''
    page = await context.new_page()
    await page.goto(f'https://nyaa.si/?f=0&c=0_0&q={name_of_anime}&o=desc&s=seeders')
    await page.pause()
    await page.click(f'{episode_2_get}') #contains the text with episode number?
    await page.click('id=magnet')

    

async with async_playwright() as p:
    browser = await p.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
#     await page.pause()
    
    for name in animes:
        latest_episode = await animeplanet_ep_num(name)
#         await nyaa_mag_link(name, latest_episode)
    


