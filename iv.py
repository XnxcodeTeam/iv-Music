#!/usr/bin/env python3
# Dibuat Sabtu, 25 Oktober 2025
# Coded by WahyuDin Ambia XD

import sys
import shutil
import subprocess
import os
import re
from colorama import Fore, Style, init

init(autoreset=True)
VERSI = "2.1.0"

# <!-- hapus warna ANSI -->
_ansi_re = re.compile(r'\x1b\[[0-9;]*m')
def hapus_ansi(teks: str) -> str:
    if not teks:
        return teks
    return _ansi_re.sub('', teks)

# <!-- auto update yt-dlp -->
def update_module():
    try:
        import yt_dlp
        from yt_dlp import version as yv
        print(f"{Fore.LIGHTBLACK_EX}🔎 yt-dlp versi: {yv.__version__}")
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-U", "yt-dlp"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
    except Exception:
        print(f"{Fore.YELLOW}⚠️ yt-dlp belum terinstal, lagi diinstal dulu...")
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-U", "yt-dlp"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
    finally:
        import yt_dlp
        return yt_dlp

yt_dlp = update_module()

# <!-- banner -->
def banner():
    logo = ''' _         .-..-.             _                               
:_;        : `' :            :_;                              
.-..-..-.  : .. :.-..-. .--. .-. .--.                         
: :: `; :  : :; :: :; :`._-.': :'  ..'                        
:_;`.__.'  :_;:_;`.__.'`.__.':_;`.__.'                      
.---.                      .-.                  .-.           
: .  :                     : :                  : :           
: :: : .--. .-..-..-.,-.,-.: :   .--.  .--.   .-' : .--. .--. 
: :; :' .; :: `; `; :: ,. :: :_ ' .; :' .; ; ' .; :' '_.': ..'
:___.'`.__.'`.__.__.':_;:_;`.__;`.__.'`.__,_;`.__.'`.__.':_;     '''
    print(logo)
    print(f"{Fore.LIGHTBLACK_EX}iv-downloader v{VERSI} | powered by yt-dlp\n")

# <!-- tampilkan bantuan -->
def tampilkan_bantuan():
    banner()
    print(f"""{Fore.CYAN}📘 IV Downloader — Command Reference{Style.RESET_ALL}
{Fore.LIGHTBLACK_EX}────────────────────────────────────────────{Style.RESET_ALL}
Pemutar musik dan pengunduh interaktif modern yang dibuat untuk Termux,
dengan dukungan lengkap untuk daftar putar, ekstraksi audio, dan kontrol interaktif.
Platform yang didukung: {Fore.CYAN}YouTube, Instagram, TikTok, Facebook, dan lainnya.
{Fore.LIGHTBLACK_EX}────────────────────────────────────────────{Style.RESET_ALL}
{Fore.LIGHTWHITE_EX}USAGE:
  python3 iv.py {Fore.CYAN}[options] {Fore.YELLOW}<url / search query>

{Fore.LIGHTWHITE_EX}OPTIONS:
{Fore.CYAN}  -h,  --help{Style.RESET_ALL}            tampilkan bantuan ini
{Fore.CYAN}  -f,  --format{Style.RESET_ALL}          format output {Fore.YELLOW}(audio/video)
{Fore.CYAN}  -a,  --abr{Style.RESET_ALL}             kualitas audio {Fore.CYAN}[64,128,192 kbps] {Fore.YELLOW}(default: 128)
{Fore.CYAN}  -q,  --quality{Style.RESET_ALL}         kualitas video{Fore.CYAN} [144p–1080p]
{Fore.CYAN}  -p,  --play{Style.RESET_ALL}            putar audio langsung tanpa download
{Fore.CYAN}  -sr, --search{Style.RESET_ALL}          cari audio/video secara interaktif
{Fore.CYAN}  -l,  --list-formats{Style.RESET_ALL}    tampilkan semua format video
{Fore.CYAN}      --min-duration{Style.RESET_ALL}     filter durasi minimal {Fore.YELLOW}(detik)
{Fore.CYAN}      --max-duration{Style.RESET_ALL}     filter durasi maksimal {Fore.YELLOW}(detik)
{Fore.CYAN}      --max-results{Style.RESET_ALL}      jumlah hasil pencarian {Fore.YELLOW}[1–20] {Fore.CYAN}(default: 10)

{Fore.LIGHTWHITE_EX}INTERAKTIF MODE:
  • Saat menggunakan {Fore.CYAN}-sr {Style.RESET_ALL}/ {Fore.CYAN}--search{Style.RESET_ALL}, pilih hasil dari daftar:
      1 = Putar langsung
      2 = Download audio {Fore.CYAN}(.mp3){Style.RESET_ALL}
  • Saat membuka URL playlist, pilih opsi:
      1 = Putar semua audio
      2 = Download semua audio {Fore.CYAN}(.mp3){Style.RESET_ALL}
      3 = Download semua video {Fore.CYAN}(.mp4){Style.RESET_ALL}
      4 = Lihat daftar & pilih satu item
      5 = Keluar

{Fore.LIGHTWHITE_EX}EXAMPLES:{Style.RESET_ALL}
  iv {Fore.CYAN}-sr {Fore.YELLOW}"cigarettes after sex" {Fore.CYAN}--max-results 10 --min-duration 3600{Style.RESET_ALL}
  iv {Fore.CYAN}-f mp4 -q 240p {Fore.YELLOW}"url video"{Style.RESET_ALL}
  iv {Fore.CYAN}-a 64 {Fore.YELLOW}"url audio" {Fore.CYAN}-p{Style.RESET_ALL}
  iv {Fore.YELLOW}"link video/audio"        {Fore.CYAN}(default: mp3 128 kbps){Style.RESET_ALL}
  iv {Fore.CYAN}"https://www.youtube.com/playlist?list=..."  {Fore.YELLOW}(playlist mode){Style.RESET_ALL}
{Fore.LIGHTBLACK_EX}────────────────────────────────────────────{Style.RESET_ALL}
📁 Semua hasil disimpan otomatis ke: {Fore.CYAN}/sdcard/Download/iv-Download/{Style.RESET_ALL}
  (Playlist akan dibuatkan folder terpisah)

{Style.RESET_ALL}📦 Dibangun dengan: yt-dlp + ffmpeg + mpv
{Style.RESET_ALL}📜 Source: {Fore.CYAN}https://github.com/XnxcodeTeam/iv-Music{Style.RESET_ALL}
""")

# <!-- cek dependensi -->
def periksa_dependensi():
    if shutil.which("ffmpeg") is None:
        print(f"{Fore.RED}❌ ffmpeg gak ditemukan! Install dulu: pkg install ffmpeg -y")
        sys.exit(1)
    if shutil.which("mpv") is None:
        print(f"{Fore.RED}❌ mpv gak ditemukan! Install dulu: pkg install mpv -y")
        sys.exit(1)

# <!-- progress download -->
def progress_hook(d):
    status = d.get('status')
    if status == 'downloading':
        persen = hapus_ansi(d.get('_percent_str', '0%')).strip()
        speed = hapus_ansi(d.get('_speed_str', '0 KiB/s'))
        eta = hapus_ansi(d.get('_eta_str', '??:??'))
        print(f"{Fore.CYAN}⬇️ {persen} | {speed} | ETA {eta}   ", end="\r")
    elif status == 'finished':
        print(f"\n{Fore.GREEN}✅ Selesai: {d.get('filename')}")

# <!-- putar audio -->
def putar_audio(url, bitrate="128", dari_playlist=False):
    print(f"{Fore.LIGHTCYAN_EX}▶️ Muter audio langsung ({bitrate} kbps)...")
    cmd = ["mpv", "--no-video", "--no-cache", f"--ytdl-format=bestaudio[abr>={bitrate}]"]
    cmd.append(url)
    subprocess.run(cmd)

# <!-- pilih format video -->
def pilih_format(info, kualitas):
    formatters = [f for f in info.get('formats', []) if f.get('height')]
    if not formatters:
        return None
    tersedia = sorted(set(int(f['height']) for f in formatters))
    try:
        target = int(kualitas)
    except Exception:
        target = max(tersedia)
    if target in tersedia:
        terpilih = max([f for f in formatters if int(f['height']) == target], key=lambda x: x.get('tbr') or 0)
        return terpilih['format_id']
    fallback = max(tersedia)
    print(f"{Fore.YELLOW}⚠️ {target}p ndak tersedia, fallback ke {fallback}p")
    terpilih = max([f for f in formatters if int(f['height']) == fallback], key=lambda x: x.get('tbr') or 0)
    return terpilih['format_id']

# <!-- download konten -->
def unduh_konten(url, ekstensi="mp3", kualitas="720", bitrate="128", dari_playlist=False, nama_playlist=None):
    import yt_dlp
    format_audio = ["mp3", "m4a", "opus", "aac", "wav"]
    base_path = "/sdcard/Download/iv-Download"
    if dari_playlist and nama_playlist:
        folder = re.sub(r'[\\/:"*?<>|]+', '_', nama_playlist).strip() or "playlist"
        output_dir = os.path.join(base_path, folder)
        os.makedirs(output_dir, exist_ok=True)
        outtmpl = os.path.join(output_dir, "%(playlist_index)03d - %(title)s.%(ext)s")
    else:
        output_dir = base_path
        os.makedirs(output_dir, exist_ok=True)
        outtmpl = os.path.join(output_dir, "%(title)s.%(ext)s")
    opsi = {
        "outtmpl": outtmpl,
        "noplaylist": not dari_playlist,
        "progress_hooks": [progress_hook],
        "continuedl": True,
        "retries": 10,
        "fragment_retries": 10,
        "socket_timeout": 60,
        "http_headers": {"User-Agent": "Mozilla/5.0"},
        "extractor_args": {"youtube": {"player_client": ["android", "web"]}},
    }
    try:
        with yt_dlp.YoutubeDL(opsi) as ydl:
            info = ydl.extract_info(url, download=False)
            if ekstensi in format_audio:
                opsi["format"] = "bestaudio/best"
                opsi["postprocessors"] = [{
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": ekstensi,
                    "preferredquality": bitrate,
                }]
            else:
                fmt = pilih_format(info, kualitas)
                if not fmt:
                    print(f"{Fore.RED}❌ Ga ada format video valid")
                    return
                opsi["format"] = f"{fmt}+bestaudio/best"
                opsi["merge_output_format"] = ekstensi
            with yt_dlp.YoutubeDL(opsi) as y:
                y.download([url])
        print(f"\n{Fore.GREEN}✅ Tersimpan di: {output_dir}")
    except Exception as e:
        print(f"{Fore.RED}❌ Error: {str(e)}")

# <!-- cek url -->
def cek_url_playlist(url: str) -> bool:
    if not url:
        return False
    u = url.lower()
    return ("playlist?list=" in u) or ("&list=" in u) or ("?list=" in u)

# <!-- mode playlist -->
def kelola_playlist(url):
    try:
        ydl_opts = {"quiet": True, "skip_download": True, "extract_flat": True,
                    "extractor_args": {"youtube": {"player_client": ["web", "android"]}}}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
        nama_pl = info.get("title", "playlist")
        entri = info.get("entries") or []
        if not entri:
            print(f"{Fore.RED}❌ Playlist kosong.")
            return
        print(f"🎶 Playlist Name: {Fore.LIGHTCYAN_EX}{nama_pl}")
        print(f"Jumlah item: {len(entri)}\n")
        print(f"{Fore.YELLOW}Mau yang mana?")
        print(" [1] Putar semua audio")
        print(" [2] Download semua audio (.mp3)")
        print(" [3] Download semua video (.mp4)")
        print(" [4] Lihat daftar isi playlist")
        print(" [5] Keluar")
        pilih = input("Pilih [1-5]: ").strip()
        if pilih == "1":
            b = input("Masukkan kualitas audio [64/128/192] (default 128): ").strip() or "128"
            putar_audio(url, bitrate=b, dari_playlist=True)
        elif pilih == "2":
            b = input("Masukkan kualitas audio [64/128/192] (default 128): ").strip() or "128"
            unduh_konten(url, "mp3", "720", b, True, nama_pl)
        elif pilih == "3":
            q = input("Masukkan Kualitas video [144/240/360/480/720/1080] (default 720): ").strip() or "720"
            unduh_konten(url, "mp4", q, "128", True, nama_pl)
        elif pilih == "4":
            for i, e in enumerate(entri, 1):
                judul = e.get("title", "Tanpa judul")
                dur = int(e.get("duration") or 0)
                durm, durs = divmod(dur, 60)
                print(f"[{i}] {judul} ({durm}:{durs:02d})")
        else:
            print(f"{Fore.YELLOW}Keluar dari playlist.")
    except Exception as e:
        print(f"{Fore.RED}❌ Error: {str(e)}")

# <!-- pencarian -->
def cari_youtube(query, hasil=10):
    print(f"{Fore.CYAN}🔍 Nyari: {query} ...")
    ydl_opts = {"quiet": True, "skip_download": True, "extract_flat": True, "default_search": "ytsearch"}
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch{hasil}:{query}", download=False)
        entri = info.get("entries", [])
        if not entri:
            print(f"{Fore.RED}❌ Ga nemu hasil buat '{query}'")
            return
        print(f"{Fore.LIGHTCYAN_EX}🔎 Ketemu {len(entri)} hasil:\n")
        for i, e in enumerate(entri, 1):
            dur = int(e.get("duration") or 0)
            durm, durs = divmod(dur, 60)
            print(f"[{i}] {e.get('title')} ({durm}:{durs:02d})")
        pilih = input(f"\nPilih nomor [1-{len(entri)}]: ").strip()
        if not pilih.isdigit(): return
        idx = int(pilih) - 1
        if idx < 0 or idx >= len(entri): return
        url = entri[idx].get("url") or ""
        if not url.startswith("http"):
            url = f"https://www.youtube.com/watch?v={url}"
        aksi = input("1. Putar / 2. Download [1/2]: ").strip()
        if aksi == "1":
            putar_audio(url)
        elif aksi == "2":
            unduh_konten(url)
    except Exception as e:
        print(f"{Fore.RED}❌ Error: {str(e)}")

# <!-- CLI -->
if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 0 or "-h" in args or "--help" in args:
        tampilkan_bantuan()
        sys.exit(0)
    os.system("cls" if os.name == "nt" else "clear")
    banner()
    periksa_dependensi()
    # parsing argumen dasar
    ext, kualitas, bitrate = "mp3", "720", "128"
    if "-f" in args or "--format" in args:
        try:
            idx = args.index("-f") if "-f" in args else args.index("--format")
            ext = args[idx + 1].replace(".", "").lower()
        except: pass
    if "-q" in args or "--quality" in args:
        try:
            idx = args.index("-q") if "-q" in args else args.index("--quality")
            kualitas = args[idx + 1].replace("p", "")
        except: pass
    if "-a" in args or "--abr" in args:
        try:
            idx = args.index("-a") if "-a" in args else args.index("--abr")
            bitrate = args[idx + 1]
        except: pass
    # mode search
    if "-sr" in args or "--search" in args:
        try:
            idx = args.index("-sr") if "-sr" in args else args.index("--search")
            query = args[idx + 1]
        except:
            print(f"{Fore.RED}❌ Gunakan: -sr \"kata kunci\"")
            sys.exit(1)
        cari_youtube(query)
        sys.exit(0)
    # ambil url terakhir
    url = args[-1]
    # playlist
    if cek_url_playlist(url):
        kelola_playlist(url)
        sys.exit(0)
    # mode play tunggal
    if "-p" in args or "--play" in args:
        putar_audio(url, bitrate)
        sys.exit(0)
    # download tunggal
    unduh_konten(url, ext, kualitas, bitrate)
