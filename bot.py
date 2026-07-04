import discord
from discord.ext import commands
from logic import DB_Manager
from config import DATABASE, TOKEN

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)
manager = DB_Manager(DATABASE)

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

@bot.command(name='start')
async def start_command(ctx):
    await ctx.send("Halo! Selamat datang di CareerBot! Saya adalah bot yang membantu kamu mencari informasi seputar dunia kerja dan karir.")
    await info(ctx)

@bot.command(name='info')
async def info(ctx):
    await ctx.send("""
    disini sini kamu bisa:
    Mencari lowongan kerja
    Melihat informasi perusahaan
    Mencari pekerjaan sesuai jurusan
    Melihat info CPNS
    Mencari peluang kerja luar negeri
                   """)
    
@bot.command(name='perusahaan')
async def perusahaan_command(ctx):
    await ctx.send("""
    Daftar Perusahaan:
    1. PT Teknologi Indonesia
    Bidang: Teknologi
    2. PT Kreatif Digital
    Bidang: Design
    3. PT Nusantara Sejahtera
    Bidang: Bisnis
                   """)
    
@bot.command(name='biodata')
async def biodata_command(ctx):
    await ctx.send("""
    Silakan kirim data kamu:

    Nama:
    Pendidikan:
    Jurusan:
    Minat kerja:
    """)
    
@bot.command(name='lokerumum')
async def lokerumum_command(ctx):
    await ctx.send("""
    Lowongan Kerja Umum :

    1. Programmer
    PT Digital Indonesia
    Jakarta

    2. Admin Online
    PT Maju Bersama
    Bandung

    3. Customer Service
    PT Solusi Mandiri
    Surabaya
    """)
    
@bot.command(name='lokerjurusan')
async def lokerjurusan_command(ctx):
    await ctx.send("""
    Loker Berdasarkan Jurusan :

    RPL:
    Programmer
    Web Developer
    Software Engineer

    DKV:
    UI/UX Designer
    Graphic Designer

    Akuntansi:
    Staff Keuangan
    Admin
    """)
    
@bot.command(name='cpns')
async def cpns_command(ctx):
    await ctx.send("""
    Informasi CPNS

    Formasi:
    Pranata Komputer

    Pendidikan:
    D3/S1 IT

    Persyaratan:
    - Ijazah
    - Dokumen lengkap
    - Mengikuti seleksi
    """)
    
@bot.command(name='kerjakeLN')
async def kerjaLN_command(ctx):
    await ctx.send("""
    Kerja ke Luar Negeri

    Negara tersedia:

    Jepang
    Pekerjaan:
    IT Support

    Korea Selatan
    Pekerjaan:
    Teknisi

    Persyaratan:
    - Skill kerja
    - Bahasa
    - Dokumen lengkap
    """)


@bot.command(name='projects')
async def get_projects(ctx):
    user_id = ctx.author.id
    projects = manager.get_projects(user_id)
    if projects:
        text = "\n".join([f"Project name: {x[2]} \nLink: {x[4]}\n" for x in projects])
        await ctx.send(text)
    else:
        await ctx.send('Kamu belum memiliki proyek!\nKamu dapat menambahkannya menggunakan perintah !new_project')