from pytubefix import YouTube
from pytubefix.exceptions import PytubeFixError
from pydub import AudioSegment
import os

def yt_to_mp3():
    try:
        url = input("Enter yt URL: ")
        yt = YouTube(url)

        stream = yt.streams.get_audio_only()

        output_dir = r'C:\Users\user\Documents\Rockstar Games\GTA V\User Music'

        print(f"At {output_dir}")
        print(f"Downloading {yt.title}...")

        dld_stream = stream.download(output_path=output_dir)

        mp3_file = os.path.splitext(dld_stream)[0] + '.mp3'
        audio = AudioSegment.from_file(dld_stream)
        audio.export(mp3_file, format='mp3')
        os.remove(dld_stream)

        print("Downloaded successfully!")
    except PytubeFixError:
        print(f"Incorrect URL!")
    except Exception:
        print(f"Download failed")

def mp3_to_wav():
    try:
        mp3_name = input("Name of mp3 to convert: ")
        mp3_dir = r'C:\Users\user\Documents\Rockstar Games\GTA V\User Music'
        mp3_file = os.path.join(mp3_dir, f'{mp3_name}.mp3')

        wav_dir = r'C:\Users\user\Desktop\songs'
        wav_file = os.path.join(wav_dir, f"{mp3_name}.wav")

        audio = AudioSegment.from_file(mp3_file)
        audio.export(wav_file, format='wav')
        print("Export complete!")
    except Exception:
        print("No such file!")

def wav_to_mp3():
    try:
        wav_name = input("Name of wav to convert: ")
        wav_dir = r'C:\Users\user\Desktop\songs'
        wav_file = os.path.join(wav_dir, f'{wav_name}.wav')

        mp3_dir = r'C:\Users\user\Desktop\songs'
        mp3_file = os.path.join(mp3_dir, f"{wav_name}.mp3")

        audio = AudioSegment.from_file(wav_file)
        audio.export(mp3_file, format='mp3')
        print("Export complete!")
    except Exception:
        print("No such file!")

def UI():
    print("AUDIO CONVERTER")
    while True:
        print("1. yt to mp3")
        print("2. mp3 to wav")
        print("3. wav to mp3")
        print("4. Exit")
        try:
            choice = int(input("Enter a choice 1-4: "))
            if choice == 1:
                yt_to_mp3()
                print("-" * 13)
            elif choice == 2:
                mp3_to_wav()
                print("-" * 13)
            elif choice == 3:
                wav_to_mp3()
                print("-" * 13)
            elif choice == 4:
                print("Exiting...")
                break
        except ValueError:
            print("Please enter only number!")


def main():
    UI()

if __name__ == "__main__":
    main()