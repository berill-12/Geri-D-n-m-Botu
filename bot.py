import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event

async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def plastik_el_isi(ctx):
    fikirler = [
        "Pet şişe gibi plastik atıkları plastik geri dönüşüm kutusuna atabilirsin.",
        "Atıkları geri dönüşüm kutularına atarsan, çevreye zarar vermeyi engelleyebilirsin.",
        "Karton,defter gibi kağıt atıkları kağıt geri dönüşüm kutusuna atabilirsin.",
        "Unutma,atıkları doğru sınıflandırmayı bilmen çok önemli!"
    ]
    await ctx.send(f"Atıkları sınıflandırarak geri dönüştürmek:\n- " + "\n- ".join(fikirler))
    
@bot.command()
async def karton_kapakli_kitap(ctx):
    await ctx.send(f"Karton kapaklı kitap kağıt atıklar sınıfına girer! Kağıt geri dönüşüm kutusuna atabilirsin.")
    
@bot.command()
async def bardak(ctx):
    await ctx.send(f"Bardak cam atıklar sınıfına giriyor :). Cam geri döüşüm kutusuna atabilirsin.")

@bot.command()
async def pet_sise(ctx):
    await ctx.send(f"Pet şişeler plastikten üretilir. Plastik atık geri dönüşüm kutusuna atabilirsin")

@bot.command()
async def geri_donusumun_onemi(ctx):
     fikirler = [ 
         "Eğer atıkları geri dönüştürmezsek ve doğaya bırakırsak doğaya pek çok zararları olur."
         "Fakat atıklar geri dönüştürülürse tekrar tekrar kullanılabilir ve daha tasarruflu olabilir."
         "Bunun dışında atıklaın sınıflarını doğru bilmemiz gerekli."
         "Geri dönüşüme biraz daha önem verirsek, daha temiz bir çevreye sahip olabiliriz."
     ]
     await ctx.send(f"Geri dönüşümün önemi hakkında temel bilgiler:\n- " + "\n- ".join(fikirler))
    
