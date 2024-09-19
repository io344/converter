from pytubefix import YouTube
from pytubefix.exceptions import PytubeFixError
from pydub import AudioSegment
import os
import time

def wrapper(func):
    def meth_wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        diff_time = end_time - start_time
        print(f"Execution finished at {diff_time:.2f} s")
        print("-" * 13)
        return result
    return meth_wrapper

@wrapper
def yt_vid_dl(yt, output_dir):
    stream = yt.streams.get_highest_resolution()
    print(f"Downloading {stream.title}")
    stream.download(output_path=output_dir)
    print("Download complete!")

@wrapper
def mp3_dl(yt, output_dir):
    stream = yt.streams.get_audio_only()
    print(f"At {output_dir}")
    print(f"Downloading {yt.title}...")

    dld_stream = stream.download(output_path=output_dir)

    mp3_file = os.path.splitext(dld_stream)[0] + '.mp3'
    audio = AudioSegment.from_file(dld_stream)
    audio.export(mp3_file, format='mp3')
    os.remove(dld_stream)

    print("Downloaded successfully!")

@wrapper
def wav_exporter(mp3_file, wav_file):
    audio = AudioSegment.from_file(mp3_file)
    audio.export(wav_file, format='wav')
    print("Export complete!")

@wrapper
def mp3_exporter(wav_file, mp3_file):
    audio = AudioSegment.from_file(wav_file)
    audio.export(mp3_file, format='mp3')
    print("Export complete!")


def yt_downloader():
    print("* YT DOWNLOADER *")
    print("-" * 13)
    try:
        url = input("Enter yt URL: ")
        yt = YouTube(url)
        output_dir = r'C:\Users\user\Desktop\yt_vids'
        yt_vid_dl(yt, output_dir)
    except PytubeFixError:
        print("URL not found!")
    except Exception as e:
        print(f"Download failed! {e}")

def yt_to_mp3():
    print("* YT to MP3 *")
    print("-" * 13)
    try:
        url = input("Enter yt URL: ")
        yt = YouTube(url)
        output_dir = r'C:\Users\user\Documents\Rockstar Games\GTA V\\User Music'
        mp3_dl(yt, output_dir)
    except PytubeFixError:
        print(f"Incorrect URL!")
    except Exception:
        print(f"Download failed")

def mp3_to_wav():
    print("* MP3 TO WAV *")
    print("-" * 13)
    try:
        mp3_name = input("Name of mp3 to convert: ")
        mp3_dir = r'C:\Users\user\Documents\Rockstar Games\GTA V\\User Music'
        mp3_file = os.path.join(mp3_dir, f'{mp3_name}.mp3')

        wav_dir = r'C:\\Users\\user\Desktop\songs'
        wav_file = os.path.join(wav_dir, f"{mp3_name}.wav")
        wav_exporter(mp3_file, wav_file)
    except Exception:
        print("No such file!")

def wav_to_mp3():
    print("* WAV TO MP3 *")
    print("-" * 13)
    try:
        wav_name = input("Name of wav to convert: ")
        wav_dir = r'C:\Users\user\Desktop\songs'
        wav_file = os.path.join(wav_dir, f'{wav_name}.wav')

        mp3_dir = r'C:\Users\user\Desktop\songs'
        mp3_file = os.path.join(mp3_dir, f"{wav_name}.mp3")
        mp3_exporter(wav_file, mp3_file)
    except Exception as e:
        print(f"No such file! {e}")

def me_holding_func(func):
    func()
    print("-" * 12)

def UI():
    print("AUDIO CONVERTER")
    while True:
        print("1. yt video downloader")
        print("2. yt to mp3")
        print("3. mp3 to wav")
        print("4. wav to mp3")
        print("5. Exit")
        try:
            choice = int(input("Enter a choice 1-5: "))
            if choice == 1:
                yt_downloader()
            elif choice == 2:
                yt_to_mp3()
            elif choice == 3:
                mp3_to_wav()
            elif choice == 4:
                wav_to_mp3()
            elif choice == 5:
                print("Exiting...")
                break
            else:
                print("Choose only numbers 1-5!")
                print("-" * 13)
        except ValueError:
            print("Please enter only number!")

def main():
    UI()

if __name__ == "__main__":
    main()




